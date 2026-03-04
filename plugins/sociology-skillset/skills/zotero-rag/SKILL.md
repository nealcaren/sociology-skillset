---
name: zotero-rag
description: Semantic search across your project's local library (library/markdown/). Index papers, search by meaning, find similar passages, and get expanded context. Replaces the deprecated Zotero RAG integration.
---

# Library RAG: Semantic Search

Semantic search over your local library of markdown-converted papers using sentence-transformers embeddings and ChromaDB.

## Prerequisites

- **uv** installed (standard in this project)
- Papers ingested via `ingest.py` (which converts to markdown, organizes files, and adds metadata to `references.bib`)
- `references.bib` with `md_path` fields linking citation keys to markdown files

**Important**: Only files registered in `references.bib` are indexed. Loose markdown files in `library/markdown/` without a bib entry will be flagged as "unlinked" during indexing. Run `ingest.py` to register them.

## Quick Start

```bash
# Index your library (first time or after adding papers)
uv run plugins/sociology-skillset/scripts/rag.py index

# Search by meaning
uv run plugins/sociology-skillset/scripts/rag.py search "cultural capital and educational attainment"
```

## Script Location

All commands use:
```
uv run plugins/sociology-skillset/scripts/rag.py <command>
```

Dependencies (`sentence-transformers`, `chromadb`) are auto-installed by `uv` on first run via PEP 723 inline metadata. No manual installation needed.

## Commands

### Index

Build or update the vector index from `library/markdown/` files.

```bash
# Index all markdown files (incremental — skips unchanged files)
uv run plugins/sociology-skillset/scripts/rag.py index

# Index specific citation keys only
uv run plugins/sociology-skillset/scripts/rag.py index --keys Smith2020_Cultural Jones2019_Institutional
```

The index is stored at `library/.rag-index/`. First run downloads the `all-MiniLM-L6-v2` embedding model (~80MB, cached by sentence-transformers).

**Run this after adding new papers** to keep the index current.

### Search

Semantic search across all indexed documents. Returns JSON lines ranked by similarity.

```bash
uv run plugins/sociology-skillset/scripts/rag.py search "social movements and collective identity"
uv run plugins/sociology-skillset/scripts/rag.py search "interview methodology" --top-k 5
uv run plugins/sociology-skillset/scripts/rag.py search "Bourdieu field theory" --min-score 0.3
```

Each result includes: `chunk_id`, `citation_key`, `section_title`, `score`, `text` (truncated), plus `title`, `author`, `year` from `references.bib`.

### Similar

Find passages similar to a given chunk (from search results).

```bash
uv run plugins/sociology-skillset/scripts/rag.py similar <chunk_id>
uv run plugins/sociology-skillset/scripts/rag.py similar abc123def456 --top-k 5
```

Use this to explore thematic connections: find a relevant passage via `search`, then use `similar` to discover related content across other papers.

### Context

Show the full context around a chunk — the target chunk plus surrounding chunks from the same document.

```bash
uv run plugins/sociology-skillset/scripts/rag.py context <chunk_id>
uv run plugins/sociology-skillset/scripts/rag.py context abc123def456 --window 3
```

Returns the target chunk and neighboring chunks (default: 2 on each side), so you can read the passage in its original context.

### Status

Show index statistics: number of documents, chunks, and last modified time.

```bash
uv run plugins/sociology-skillset/scripts/rag.py status
```

### List

List all indexed documents with chunk counts.

```bash
uv run plugins/sociology-skillset/scripts/rag.py list
```

### Remove

Remove a document from the index by citation key.

```bash
uv run plugins/sociology-skillset/scripts/rag.py remove Smith2020_Cultural
```

## Typical Workflows

### First-time setup
1. Ensure papers are in `library/markdown/` (run `ingest.py` for each PDF/EPUB)
2. Run `uv run rag.py index` to build the index
3. Search with `uv run rag.py search "your topic"`

### Adding new papers
1. Ingest the paper: `uv run plugins/sociology-skillset/scripts/ingest.py --file paper.pdf`
2. Update the index: `uv run plugins/sociology-skillset/scripts/rag.py index`

### Adding a PDF for a paper already in references.bib
1. Ingest with update: `uv run plugins/sociology-skillset/scripts/ingest.py --file paper.pdf --citekey ExistingKey2022 --update`
2. Update the index: `uv run plugins/sociology-skillset/scripts/rag.py index`

### Deep exploration
1. **Search** for a topic: `search "concept or question"`
2. **Read context** of a promising hit: `context <chunk_id>`
3. **Find similar** passages across other papers: `similar <chunk_id>`
4. **Read the full paper** if needed: open the `source_file` path from results

## When to Use RAG vs. Grep

| Need | Tool |
|------|------|
| **Conceptual/semantic search** (find passages about a concept even if they don't use the exact words) | `rag.py search` |
| **Exact keyword/phrase search** (find specific terms, author names, method names) | `grep library/markdown/` |
| **Metadata search** (by author, year, journal) | `grep references.bib` |

Both approaches complement each other. Use semantic search for exploratory discovery and grep for precise retrieval.

## Technical Details

- **Embedding model**: `all-MiniLM-L6-v2` (384 dimensions, same as old Zotero RAG)
- **Vector store**: ChromaDB with file-based persistence at `library/.rag-index/`
- **Chunking**: Split by `##` headers (section-level); fallback to ~512-token fixed chunks for headerless documents
- **Incremental indexing**: Content hashes stored in metadata; unchanged files are skipped on re-index
- **Output format**: JSON lines for easy parsing by Claude or other tools
