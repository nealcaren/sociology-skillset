---
name: zotero-rag
description: "(DEPRECATED) Semantic search for Zotero libraries using RAG. Replaced by local BibTeX pipeline — use references.bib + library/markdown/ for full-text search."
---

# Zotero RAG: Semantic Search (DEPRECATED)

> **This skill is deprecated.** The Zotero RAG integration has been replaced by a local library pipeline where full-text search operates directly on markdown files.

## Migration Guide

### What Changed

- **Before**: `mcp-zotero[rag]` indexed PDFs in Zotero's storage and provided semantic search via embeddings
- **After**: PDFs and EPUBs are stored in `library/pdfs/`, converted to markdown in `library/markdown/`, and searched directly using grep or file reading

### New Workflow

1. **Ingest papers** into your local library:
   ```bash
   python plugins/sociology-skillset/scripts/ingest.py --file paper.pdf
   ```

2. **Search by content**: Read or grep the markdown files in `library/markdown/`

3. **Search by metadata**: Search `references.bib` for author, title, year, keywords

### What Replaces What

| Before (Zotero RAG) | After (Local Library) |
|---|---|
| `semantic_search(query=...)` | Grep `library/markdown/*.md` for relevant passages |
| `get_chunk_context(chunk_id=...)` | Read the full markdown file from `library/markdown/` |
| `find_similar_chunks(...)` | Search across markdown files for related content |
| `index_library(...)` | No indexing needed — markdown files are always current |

### Advantages

- No database locking or sync conflicts
- No separate indexing step required
- Works with EPUBs as well as PDFs
- Full text always available without embedding model dependencies
