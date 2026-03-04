#!/usr/bin/env python3
# /// script
# requires-python = ">=3.10"
# dependencies = [
#     "sentence-transformers",
#     "chromadb",
# ]
# ///
"""Local RAG for library/markdown/ files.

Indexes markdown files from the local library into a ChromaDB vector store
using sentence-transformers embeddings, enabling semantic search across
your paper collection.

Usage:
    uv run rag.py index                    # Index all markdown files
    uv run rag.py index --keys key1 key2   # Index specific citation keys
    uv run rag.py search "query text"      # Semantic search
    uv run rag.py similar <chunk_id>       # Find similar passages
    uv run rag.py context <chunk_id>       # Show expanded context
    uv run rag.py status                   # Index statistics
    uv run rag.py list                     # List indexed documents
    uv run rag.py remove <citation_key>    # Remove a document
"""

import argparse
import hashlib
import json
import os
import re
import sys
import time

import chromadb
from sentence_transformers import SentenceTransformer


# ---------------------------------------------------------------------------
# Constants
# ---------------------------------------------------------------------------

LIBRARY_DIR = os.path.join(".", "library", "markdown")
INDEX_DIR = os.path.join(".", "library", ".rag-index")
BIB_PATH = os.path.join(".", "references.bib")
COLLECTION_NAME = "library"
EMBEDDING_MODEL = "all-MiniLM-L6-v2"
CHUNK_TOKEN_LIMIT = 512


# ---------------------------------------------------------------------------
# BibTeX parsing (lightweight, mirrors ingest.py)
# ---------------------------------------------------------------------------

def parse_bib_entries(bib_path):
    """Parse references.bib into a dict of citation_key -> metadata."""
    if not os.path.isfile(bib_path):
        return {}

    text = open(bib_path, "r", encoding="utf-8", errors="replace").read()
    entries = {}

    # Match each @type{key, ... } block
    pattern = re.compile(
        r"@(\w+)\{([^,]+),\s*(.*?)\n\}",
        re.DOTALL,
    )
    for m in pattern.finditer(text):
        entry_type = m.group(1).lower()
        citekey = m.group(2).strip()
        body = m.group(3)

        fields = {}
        for fm in re.finditer(r"(\w+)\s*=\s*\{(.*?)\}", body, re.DOTALL):
            fields[fm.group(1).lower()] = fm.group(2).strip()

        entries[citekey] = {
            "type": entry_type,
            "title": fields.get("title", ""),
            "author": fields.get("author", ""),
            "year": fields.get("year", ""),
            "md_path": fields.get("md_path", ""),
        }

    return entries


# ---------------------------------------------------------------------------
# Chunking
# ---------------------------------------------------------------------------

def _content_hash(text):
    """SHA-256 hash of text content."""
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def chunk_markdown(text, citation_key, source_file):
    """Split markdown into chunks by ## headers, with fallback to fixed-size."""
    chunks = []

    # Try splitting by ## headers
    sections = re.split(r"(?=^## )", text, flags=re.MULTILINE)

    if len(sections) > 1:
        for section in sections:
            section = section.strip()
            if not section:
                continue
            # Extract section title
            title_match = re.match(r"^## (.+)$", section, re.MULTILINE)
            title = title_match.group(1).strip() if title_match else ""
            chunks.append({
                "text": section,
                "section_title": title,
                "citation_key": citation_key,
                "source_file": source_file,
            })
    else:
        # Fallback: fixed-size chunks (~512 tokens ≈ ~2048 chars)
        chunk_size = 2048
        overlap = 200
        for i in range(0, len(text), chunk_size - overlap):
            chunk_text = text[i : i + chunk_size]
            if not chunk_text.strip():
                continue
            chunks.append({
                "text": chunk_text,
                "section_title": f"chunk-{i}",
                "citation_key": citation_key,
                "source_file": source_file,
            })

    return chunks


# ---------------------------------------------------------------------------
# ChromaDB helpers
# ---------------------------------------------------------------------------

def get_collection(client, model):
    """Get or create the library collection."""
    return client.get_or_create_collection(
        name=COLLECTION_NAME,
        metadata={"hnsw:space": "cosine"},
    )


def make_chunk_id(citation_key, section_title, idx):
    """Create a deterministic chunk ID."""
    raw = f"{citation_key}::{section_title}::{idx}"
    return hashlib.md5(raw.encode()).hexdigest()[:12]


# ---------------------------------------------------------------------------
# Subcommands
# ---------------------------------------------------------------------------

def cmd_index(args):
    """Index markdown files into ChromaDB."""
    bib_entries = parse_bib_entries(BIB_PATH)

    if not bib_entries:
        print(f"Error: No references.bib found at {BIB_PATH}")
        print("  Run `uv run plugins/sociology-skillset/scripts/ingest.py --file <pdf>` to add papers.")
        return

    # Determine which files to index — only files with a references.bib entry
    if args.keys:
        files_to_index = {}
        for key in args.keys:
            if key not in bib_entries:
                print(f"Warning: Citation key '{key}' not found in references.bib")
                continue
            md_path = bib_entries[key].get("md_path", "")
            if not md_path:
                print(f"Warning: No md_path for '{key}' in references.bib")
                continue
            if os.path.isfile(md_path):
                files_to_index[key] = md_path
            else:
                print(f"Warning: File not found for '{key}': {md_path}")
    else:
        files_to_index = {}
        for key, entry in bib_entries.items():
            if entry["md_path"] and os.path.isfile(entry["md_path"]):
                files_to_index[key] = entry["md_path"]
            elif entry["md_path"]:
                print(f"Warning: File missing for '{key}': {entry['md_path']}")

    # Report unlinked markdown files (in library/markdown/ but not in references.bib)
    bib_md_paths = {os.path.abspath(e["md_path"]) for e in bib_entries.values() if e["md_path"]}
    if os.path.isdir(LIBRARY_DIR):
        for fname in sorted(os.listdir(LIBRARY_DIR)):
            if not fname.endswith(".md"):
                continue
            fpath = os.path.abspath(os.path.join(LIBRARY_DIR, fname))
            if fpath not in bib_md_paths:
                print(f"Unlinked: {fname} (not in references.bib — run ingest.py to register it)")

    if not files_to_index:
        print("No markdown files found to index.")
        print(f"  Checked: {BIB_PATH} and {LIBRARY_DIR}")
        return

    # Initialize model and ChromaDB
    print(f"Loading embedding model: {EMBEDDING_MODEL}")
    model = SentenceTransformer(EMBEDDING_MODEL)
    os.makedirs(INDEX_DIR, exist_ok=True)
    client = chromadb.PersistentClient(path=INDEX_DIR)
    collection = get_collection(client, model)

    # Get existing content hashes to skip unchanged files
    existing_meta = {}
    try:
        existing = collection.get(include=["metadatas"])
        for meta in existing["metadatas"]:
            if meta and "citation_key" in meta and "content_hash" in meta:
                existing_meta[meta["citation_key"]] = meta["content_hash"]
    except Exception:
        pass

    indexed = 0
    skipped = 0
    total_chunks = 0

    for key, fpath in sorted(files_to_index.items()):
        text = open(fpath, "r", encoding="utf-8", errors="replace").read()
        content_hash = _content_hash(text)

        # Skip if unchanged
        if key in existing_meta and existing_meta[key] == content_hash:
            skipped += 1
            continue

        # Remove old chunks for this key if re-indexing
        if key in existing_meta:
            old_ids = collection.get(
                where={"citation_key": key},
            )
            if old_ids["ids"]:
                collection.delete(ids=old_ids["ids"])

        # Chunk and embed
        chunks = chunk_markdown(text, key, fpath)
        if not chunks:
            continue

        bib_meta = bib_entries.get(key, {})

        ids = []
        documents = []
        metadatas = []
        for i, chunk in enumerate(chunks):
            chunk_id = make_chunk_id(key, chunk["section_title"], i)
            ids.append(chunk_id)
            documents.append(chunk["text"])
            metadatas.append({
                "citation_key": key,
                "section_title": chunk["section_title"],
                "source_file": chunk["source_file"],
                "content_hash": content_hash,
                "chunk_index": i,
                "title": bib_meta.get("title", ""),
                "author": bib_meta.get("author", ""),
                "year": bib_meta.get("year", ""),
            })

        # Embed and add
        embeddings = model.encode(documents, show_progress_bar=False).tolist()
        collection.add(
            ids=ids,
            documents=documents,
            metadatas=metadatas,
            embeddings=embeddings,
        )

        indexed += 1
        total_chunks += len(chunks)
        print(f"  Indexed: {key} ({len(chunks)} chunks)")

    print(f"\nDone. Indexed {indexed} documents ({total_chunks} chunks), skipped {skipped} unchanged.")


def cmd_search(args):
    """Semantic search across indexed documents."""
    if not os.path.isdir(INDEX_DIR):
        print("Error: No index found. Run `uv run rag.py index` first.")
        sys.exit(1)

    model = SentenceTransformer(EMBEDDING_MODEL)
    client = chromadb.PersistentClient(path=INDEX_DIR)
    collection = get_collection(client, model)

    query_embedding = model.encode([args.query]).tolist()
    results = collection.query(
        query_embeddings=query_embedding,
        n_results=args.top_k,
        include=["documents", "metadatas", "distances"],
    )

    if not results["ids"][0]:
        print("No results found.")
        return

    for i, (chunk_id, doc, meta, dist) in enumerate(zip(
        results["ids"][0],
        results["documents"][0],
        results["metadatas"][0],
        results["distances"][0],
    )):
        # ChromaDB cosine distance: 0 = identical, 2 = opposite
        # Convert to similarity score: 1 - (distance / 2)
        score = 1.0 - (dist / 2.0)

        if score < args.min_score:
            continue

        # Truncate text for display
        text = doc[:500].replace("\n", " ").strip()
        if len(doc) > 500:
            text += "..."

        result = {
            "rank": i + 1,
            "chunk_id": chunk_id,
            "citation_key": meta.get("citation_key", ""),
            "section_title": meta.get("section_title", ""),
            "score": round(score, 4),
            "title": meta.get("title", ""),
            "author": meta.get("author", ""),
            "year": meta.get("year", ""),
            "text": text,
        }
        print(json.dumps(result))


def cmd_similar(args):
    """Find passages similar to a given chunk."""
    if not os.path.isdir(INDEX_DIR):
        print("Error: No index found. Run `uv run rag.py index` first.")
        sys.exit(1)

    model = SentenceTransformer(EMBEDDING_MODEL)
    client = chromadb.PersistentClient(path=INDEX_DIR)
    collection = get_collection(client, model)

    # Get the target chunk
    try:
        target = collection.get(ids=[args.chunk_id], include=["documents", "embeddings"])
    except Exception:
        print(f"Error: Chunk ID '{args.chunk_id}' not found.")
        sys.exit(1)

    if not target["ids"]:
        print(f"Error: Chunk ID '{args.chunk_id}' not found.")
        sys.exit(1)

    # Query with the chunk's embedding
    results = collection.query(
        query_embeddings=target["embeddings"],
        n_results=args.top_k + 1,  # +1 to exclude self
        include=["documents", "metadatas", "distances"],
    )

    printed = 0
    for chunk_id, doc, meta, dist in zip(
        results["ids"][0],
        results["documents"][0],
        results["metadatas"][0],
        results["distances"][0],
    ):
        if chunk_id == args.chunk_id:
            continue  # skip self
        if printed >= args.top_k:
            break

        score = 1.0 - (dist / 2.0)
        if score < args.min_score:
            continue

        text = doc[:500].replace("\n", " ").strip()
        if len(doc) > 500:
            text += "..."

        result = {
            "chunk_id": chunk_id,
            "citation_key": meta.get("citation_key", ""),
            "section_title": meta.get("section_title", ""),
            "score": round(score, 4),
            "title": meta.get("title", ""),
            "author": meta.get("author", ""),
            "year": meta.get("year", ""),
            "text": text,
        }
        print(json.dumps(result))
        printed += 1


def cmd_context(args):
    """Show expanded context around a chunk."""
    if not os.path.isdir(INDEX_DIR):
        print("Error: No index found. Run `uv run rag.py index` first.")
        sys.exit(1)

    client = chromadb.PersistentClient(path=INDEX_DIR)
    collection = client.get_collection(name=COLLECTION_NAME)

    # Get the target chunk
    try:
        target = collection.get(ids=[args.chunk_id], include=["documents", "metadatas"])
    except Exception:
        print(f"Error: Chunk ID '{args.chunk_id}' not found.")
        sys.exit(1)

    if not target["ids"]:
        print(f"Error: Chunk ID '{args.chunk_id}' not found.")
        sys.exit(1)

    meta = target["metadatas"][0]
    citation_key = meta.get("citation_key", "")
    chunk_index = meta.get("chunk_index", 0)

    # Get neighboring chunks from the same document
    neighbors = collection.get(
        where={"citation_key": citation_key},
        include=["documents", "metadatas"],
    )

    # Sort by chunk_index and find neighbors
    indexed_chunks = []
    for cid, doc, m in zip(neighbors["ids"], neighbors["documents"], neighbors["metadatas"]):
        indexed_chunks.append((m.get("chunk_index", 0), cid, doc, m))
    indexed_chunks.sort(key=lambda x: x[0])

    # Find the target and include surrounding chunks
    context_window = args.window
    target_pos = None
    for i, (idx, cid, doc, m) in enumerate(indexed_chunks):
        if cid == args.chunk_id:
            target_pos = i
            break

    if target_pos is None:
        # Fallback: just show the chunk itself
        print(json.dumps({
            "chunk_id": args.chunk_id,
            "citation_key": citation_key,
            "text": target["documents"][0],
        }))
        return

    start = max(0, target_pos - context_window)
    end = min(len(indexed_chunks), target_pos + context_window + 1)

    context_parts = []
    for i in range(start, end):
        idx, cid, doc, m = indexed_chunks[i]
        marker = " <<< TARGET" if cid == args.chunk_id else ""
        context_parts.append({
            "chunk_id": cid,
            "chunk_index": idx,
            "section_title": m.get("section_title", ""),
            "is_target": cid == args.chunk_id,
            "text": doc,
        })

    result = {
        "citation_key": citation_key,
        "title": meta.get("title", ""),
        "author": meta.get("author", ""),
        "year": meta.get("year", ""),
        "source_file": meta.get("source_file", ""),
        "chunks": context_parts,
    }
    print(json.dumps(result))


def cmd_status(args):
    """Show index statistics."""
    if not os.path.isdir(INDEX_DIR):
        print(json.dumps({"indexed": False, "message": "No index found. Run `uv run rag.py index` first."}))
        return

    client = chromadb.PersistentClient(path=INDEX_DIR)
    try:
        collection = client.get_collection(name=COLLECTION_NAME)
    except Exception:
        print(json.dumps({"indexed": False, "message": "No collection found."}))
        return

    count = collection.count()

    # Get unique documents
    all_meta = collection.get(include=["metadatas"])
    doc_keys = set()
    for meta in all_meta["metadatas"]:
        if meta and "citation_key" in meta:
            doc_keys.add(meta["citation_key"])

    # Index directory mod time
    index_mtime = os.path.getmtime(INDEX_DIR)
    last_indexed = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(index_mtime))

    result = {
        "indexed": True,
        "documents": len(doc_keys),
        "chunks": count,
        "last_modified": last_indexed,
        "index_path": os.path.abspath(INDEX_DIR),
    }
    print(json.dumps(result))


def cmd_list(args):
    """List all indexed documents."""
    if not os.path.isdir(INDEX_DIR):
        print("Error: No index found. Run `uv run rag.py index` first.")
        sys.exit(1)

    client = chromadb.PersistentClient(path=INDEX_DIR)
    try:
        collection = client.get_collection(name=COLLECTION_NAME)
    except Exception:
        print("Error: No collection found.")
        sys.exit(1)

    all_meta = collection.get(include=["metadatas"])

    # Aggregate by citation_key
    docs = {}
    for meta in all_meta["metadatas"]:
        if not meta or "citation_key" not in meta:
            continue
        key = meta["citation_key"]
        if key not in docs:
            docs[key] = {
                "citation_key": key,
                "title": meta.get("title", ""),
                "author": meta.get("author", ""),
                "year": meta.get("year", ""),
                "chunks": 0,
            }
        docs[key]["chunks"] += 1

    for doc in sorted(docs.values(), key=lambda d: d["citation_key"]):
        print(json.dumps(doc))


def cmd_remove(args):
    """Remove a document from the index."""
    if not os.path.isdir(INDEX_DIR):
        print("Error: No index found.")
        sys.exit(1)

    client = chromadb.PersistentClient(path=INDEX_DIR)
    try:
        collection = client.get_collection(name=COLLECTION_NAME)
    except Exception:
        print("Error: No collection found.")
        sys.exit(1)

    # Find chunks for this citation key
    results = collection.get(
        where={"citation_key": args.citation_key},
    )

    if not results["ids"]:
        print(f"No chunks found for citation key: {args.citation_key}")
        return

    collection.delete(ids=results["ids"])
    print(f"Removed {len(results['ids'])} chunks for: {args.citation_key}")


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(
        description="Local RAG for library/markdown/ files.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  uv run rag.py index                    Index all library markdown files
  uv run rag.py index --keys Smith2020   Index specific citation keys
  uv run rag.py search "social movements" Search for related passages
  uv run rag.py similar abc123          Find similar passages to a chunk
  uv run rag.py context abc123          Show expanded context for a chunk
  uv run rag.py status                  Show index statistics
  uv run rag.py list                    List all indexed documents
  uv run rag.py remove Smith2020        Remove a document from the index
""",
    )
    subparsers = parser.add_subparsers(dest="command", required=True)

    # index
    p_index = subparsers.add_parser("index", help="Index markdown files into the vector store")
    p_index.add_argument("--keys", nargs="+", help="Specific citation keys to index")

    # search
    p_search = subparsers.add_parser("search", help="Semantic search across indexed documents")
    p_search.add_argument("query", help="Search query text")
    p_search.add_argument("--top-k", type=int, default=10, help="Number of results (default: 10)")
    p_search.add_argument("--min-score", type=float, default=0.0, help="Minimum similarity score (default: 0.0)")

    # similar
    p_similar = subparsers.add_parser("similar", help="Find passages similar to a given chunk")
    p_similar.add_argument("chunk_id", help="Chunk ID to find similar passages for")
    p_similar.add_argument("--top-k", type=int, default=10, help="Number of results (default: 10)")
    p_similar.add_argument("--min-score", type=float, default=0.0, help="Minimum similarity score (default: 0.0)")

    # context
    p_context = subparsers.add_parser("context", help="Show expanded context around a chunk")
    p_context.add_argument("chunk_id", help="Chunk ID to expand context for")
    p_context.add_argument("--window", type=int, default=2, help="Number of surrounding chunks (default: 2)")

    # status
    subparsers.add_parser("status", help="Show index statistics")

    # list
    subparsers.add_parser("list", help="List all indexed documents")

    # remove
    p_remove = subparsers.add_parser("remove", help="Remove a document from the index")
    p_remove.add_argument("citation_key", help="Citation key of the document to remove")

    args = parser.parse_args()

    commands = {
        "index": cmd_index,
        "search": cmd_search,
        "similar": cmd_similar,
        "context": cmd_context,
        "status": cmd_status,
        "list": cmd_list,
        "remove": cmd_remove,
    }

    commands[args.command](args)


if __name__ == "__main__":
    main()
