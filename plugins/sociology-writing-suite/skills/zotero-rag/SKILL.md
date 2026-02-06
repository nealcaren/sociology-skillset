---
name: zotero-rag
description: Semantic search for Zotero libraries using RAG. Use when users want to search their Zotero library by meaning (not keywords), find relevant passages across PDFs, discover thematic connections between sources, get expanded context around quotes, or find similar passages across documents. Triggers on queries like "find passages about X in my library", "search my Zotero for themes of Y", "what do my sources say about Z", "find similar discussions", or "get more context around this quote".
---

# Zotero RAG: Semantic Search

Search your Zotero library by meaning using the `mcp-zotero` MCP server's RAG tools. These 8 tools are available when the server is installed with `mcp-zotero[rag]`.

## Setup

RAG tools are part of the consolidated `mcp-zotero` package. Install with:

```bash
uv tool install "mcp-zotero[rag]"
```

Configure in `.mcp.json`:

```json
{
  "mcpServers": {
    "zotero": {
      "command": "mcp-zotero",
      "env": {
        "ZOTERO_LIBRARY_ID": "YOUR_LIBRARY_ID",
        "ZOTERO_LOCAL": "true",
        "ZOTERO_LOCAL_KEY": "YOUR_LOCAL_KEY",
        "ZOTERO_ATTACHMENTS_DIR": "~/Zotero/storage"
      }
    }
  }
}
```

`ZOTERO_ATTACHMENTS_DIR` is required for RAG — it tells the indexer where to find the PDF files.

Verify with `health_check` — look for `rag_available: true` in the response. If it shows `false`, the `[rag]` extras aren't installed.

## RAG Tools (8)

| Tool | Purpose |
|------|---------|
| `index_library` | Index all items or a specific collection |
| `index_items` | Index specific items by key |
| `semantic_search` | Find passages by meaning |
| `get_chunk_context` | Expand result with surrounding text |
| `find_similar_chunks` | Find related passages across documents |
| `index_status` | Check index statistics |
| `list_indexed_items` | See what's indexed |
| `remove_from_index` | Remove items from index |

These are in addition to the 38 base Zotero tools (search, collections, tags, items, etc.) which are always available.

## Workflows

### First Use: Index a Collection

1. `health_check` — verify connection and `rag_available: true`
2. Use `list_collections_top` to find your collection key
3. `index_library` with `collection_key` — index the whole collection

```
index_library collection_key="7MPS99AN"
```

Returns `indexed`, `skipped`, `errors`, and **`warnings`** — check warnings for scanned PDFs or extraction problems.

### Search → Explore → Connect

```
semantic_search query="how organizations maintain legitimacy under pressure"
```

Returns ranked passages with score, chunk_id, item_key, section_title, text.

```
get_chunk_context chunk_id="ABC123_5" context_lines=20
```

Expands the result with surrounding lines from the source.

```
find_similar_chunks chunk_id="ABC123_5" limit=5
```

Finds related discussions across other documents.

## Search Tips

**Conceptual queries work best:**
- "how organizations maintain legitimacy under pressure"
- "role of media framing in shaping public opinion about protesters"
- NOT just keywords like "legitimacy organization"

**Filter options:**
- `item_keys` — limit to specific items
- `chunk_types` — "abstract", "body", "chapter"
- `min_score` — similarity threshold (0-1, default 0.0)

## Extraction Quality Warnings

When indexing, the response includes a `warnings` field for items with extraction issues:

- **`low_density`** — Few chars per page; likely a scanned PDF that needs OCR
- **`very_short`** — Under 500 chars total; may be supplementary material (figures only)
- **`mostly_blank`** — Over 80% blank lines; extraction likely failed

If you see warnings, consider:
- **Scanned PDFs**: Install `mcp-zotero[rag,ocr]` and set `RAG_ENABLE_OCR=true`
- **Supplements**: Use `remove_from_index` to drop them — they pollute search results
- **Re-index**: Use `force_reindex=true` after enabling OCR

## Notes

- Indexing extracts text from PDFs and creates embeddings using `all-MiniLM-L6-v2`
- Re-running `index_library` skips unchanged documents (by content hash)
- Use `force_reindex=true` to re-process everything
- Index persists at `~/.zotero-rag` (configurable via `RAG_INDEX_DIR`)
- The base `mcp-zotero` install (without `[rag]`) provides 38 Zotero API tools but no semantic search
