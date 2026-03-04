---
name: mcp-zotero
description: "(DEPRECATED) Operate Zotero libraries through the MCP server. Replaced by local BibTeX pipeline — use references.bib + library/ instead."
metadata:
  short-description: "Zotero library operations (DEPRECATED)"
---

# MCP Zotero (DEPRECATED)

> **This skill is deprecated.** The Zotero MCP integration has been replaced by a local BibTeX pipeline that avoids database locking and sync conflicts.

## Migration Guide

### What Changed

- **Before**: Zotero MCP server (`mcp-zotero`) interfaced with Zotero's local SQLite database
- **After**: `references.bib` is the canonical metadata store; PDFs/EPUBs live in `library/pdfs/`, converted markdown in `library/markdown/`

### How to Migrate

1. **Export your Zotero library** as BibTeX (File → Export Library → BibTeX)
2. **Run the migration script**:
   ```bash
   python plugins/sociology-skillset/scripts/migrate-zotero.py \
     --bib exported.bib \
     --files ~/Zotero/storage \
     --output-dir .
   ```
   This copies your PDFs/EPUBs to `library/pdfs/`, converts them to markdown, and creates `references.bib` with `pdf_path` and `md_path` fields.

3. **For new papers**, use the ingest script instead of Zotero:
   ```bash
   python plugins/sociology-skillset/scripts/ingest.py --file paper.pdf
   python plugins/sociology-skillset/scripts/ingest.py --file book.epub --doi 10.xxxx/xxxxx
   ```

### What Replaces What

| Before (Zotero MCP) | After (Local Library) |
|---|---|
| `search_items(query=...)` | Search `references.bib` by author/title/year |
| `get_item(item_key=...)` | Look up entry in `references.bib` by citation key |
| `download_attachments(...)` | Read from `library/pdfs/` directly |
| Zotero RAG semantic search | Read from `library/markdown/` + grep |
| `add_item(...)` | `python ingest.py --file paper.pdf` |

### Skills That Use the New Pipeline

All downstream skills (`lit-synthesis`, `reading-agent`, `bibliography-builder`, `peer-reviewer`, `argument-builder`) now read from `references.bib` and `library/` instead of calling Zotero MCP tools.

### Legacy Files

The `guides/` and `references/` subdirectories in this skill are preserved for reference but are no longer maintained.
