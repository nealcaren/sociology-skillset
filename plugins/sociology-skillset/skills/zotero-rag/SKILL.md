---
name: zotero-rag
description: Semantic search for Zotero libraries using RAG. Use when users want to search their Zotero library by meaning (not keywords), find relevant passages across PDFs, discover thematic connections between sources, get expanded context around quotes, or find similar passages across documents. Triggers on queries like "find passages about X in my library", "search my Zotero for themes of Y", "what do my sources say about Z", "find similar discussions", or "get more context around this quote".
---

# Zotero RAG: Semantic Search

Search your Zotero library by meaning using the `mcp-zotero` MCP server's RAG tools. These 8 tools are available when the server is installed with `mcp-zotero[rag]`.

## First-Run Check

**Before doing anything else**, verify RAG tools are available:

1. **Check if zotero tools exist**: Try calling `health_check()`. If the tool is not found (no `zotero` MCP server configured), proceed to step 2. If it succeeds, check the response for `rag_available` and skip to step 3.

2. **Install mcp-zotero with RAG**: Run `uv tool list | grep mcp-zotero` in the terminal.
   - If **not installed**, tell the user:
     > "The Zotero MCP server with semantic search isn't installed yet. I can install it for you. Shall I run `uv tool install 'mcp-zotero[rag]'`?"
   - If **installed without RAG** (base only), tell the user:
     > "mcp-zotero is installed but without semantic search. I can upgrade it. Shall I run `uv tool install 'mcp-zotero[rag]'`?"
   - If the user agrees, run: `uv tool install "mcp-zotero[rag]"`
   - Then check if `.mcp.json` is configured. If not, ask the user for their Zotero Library ID (found at https://www.zotero.org/settings/keys) and write the config:
     ```json
     {
       "mcpServers": {
         "zotero": {
           "command": "mcp-zotero",
           "env": {
             "ZOTERO_LIBRARY_ID": "THEIR_ID",
             "ZOTERO_LOCAL": "true",
             "ZOTERO_LOCAL_KEY": "THEIR_KEY",
             "ZOTERO_ATTACHMENTS_DIR": "~/Zotero/storage"
           }
         }
       }
     }
     ```
   - Tell the user: "MCP server configured. Please restart Claude Code to load the new server, then invoke this skill again."

3. **Check RAG availability**: If `health_check()` returns `rag_available: false`:
   - Tell the user: "The Zotero server is running but semantic search isn't enabled. Shall I upgrade with `uv tool install 'mcp-zotero[rag]'`?"
   - After upgrading, the user must restart Claude Code to reload the MCP server.

4. **Verify RAG is working**: If `health_check()` returns `rag_available: true`, proceed to the user's task.

**Important**: `ZOTERO_ATTACHMENTS_DIR` must be set (typically `~/Zotero/storage`) — RAG needs this to find PDF files for indexing.

---

## Setup Reference

RAG tools are part of the consolidated `mcp-zotero` package:

```bash
# With semantic search
uv tool install "mcp-zotero[rag]"

# With semantic search + OCR for scanned PDFs
uv tool install "mcp-zotero[rag,ocr]"
```

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
