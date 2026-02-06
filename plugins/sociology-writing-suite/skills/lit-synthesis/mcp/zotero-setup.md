# Zotero Integration Setup

This skill uses the **mcp-zotero** MCP server for library access and semantic search.

## Prerequisites

1. **Zotero 7+** installed and running on your machine
2. **mcp-zotero** MCP server configured in Claude
3. Papers imported into Zotero (from lit-search BibTeX or manually)

## MCP Server Setup

```bash
# Base install (38 Zotero API tools)
uv tool install mcp-zotero

# With semantic search (+ 8 RAG tools)
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

Enable Zotero's local API: **Zotero → Settings → Advanced → General → Allow other applications to communicate with Zotero**.

## Two Ways to Access Your Library

### 1. Base Tools (38 MCP Tools)

For structured library operations:
- `search_items` — keyword search across your library
- `get_item` — full metadata for a specific item
- `collection_items` — list items in a collection
- `download_attachments` — get PDF content

### 2. RAG Tools (8 MCP Tools, requires `[rag]` install)

For meaning-based search across PDF content:
- `semantic_search` — find passages by conceptual similarity
- `get_chunk_context` — expand results with surrounding text
- `find_similar_chunks` — discover related passages across documents

**Workflow**: Use base tools for metadata and structure, RAG tools for discovering passages by meaning.

## Semantic Search Setup

1. **Index your collection**:
   ```
   index_library collection_key="YOUR_COLLECTION"
   ```
   Check `warnings` in the response for scanned PDFs or extraction issues.

2. **Search by meaning**:
   ```
   semantic_search query="how organizations maintain legitimacy under pressure"
   ```

3. **Expand context**:
   ```
   get_chunk_context chunk_id="ABC123_5" context_lines=20
   ```

See `skills/zotero-rag/SKILL.md` for full documentation.

## Workflow Integration

### From lit-search

1. Export BibTeX from lit-search's `references.bib`
2. In Zotero: **File → Import** → select the BibTeX file
3. Papers appear in your library (create a collection for the project)
4. Use **"Find Available PDF"** to auto-download open access versions
5. Manually acquire remaining PDFs via institutional access

### Index for Semantic Search

After importing:
1. Note your collection key from Zotero
2. Run `index_library collection_key="YOUR_KEY"`
3. Wait for PDF extraction and embedding (may take a few minutes)
4. Use `semantic_search` to find passages by meaning

### Organizing for Analysis

Create a Zotero collection for your project:
1. Right-click **My Library** → **New Collection**
2. Name it (e.g., "housing-instability-lit-review")
3. Drag papers into the collection
4. Use tags for additional organization (e.g., "priority-read", "theoretical", "empirical")

### Annotating PDFs

As you read in Zotero's PDF viewer:
- **Highlight** key passages (yellow for findings, blue for theory, green for methods)
- **Add notes** to highlights for your interpretation
- These annotations are accessible via the zotero skill's annotation tools

## Troubleshooting

### "Zotero not found" Error

- Ensure Zotero is running
- Check that "Allow other applications" is enabled
- Restart both Zotero and Claude

### Semantic Search Returns No Results

- Verify the collection has been indexed: `index_status`
- Check that PDFs are attached (not just linked)
- Try `list_indexed_items` to see what's indexed

### Annotations Not Appearing

- Annotations must be made in Zotero's built-in PDF viewer
- External annotations (from Preview, Acrobat) won't sync
- Ensure the PDF is attached to the Zotero item (not just linked)

## Resources

- **zotero Skill**: `skills/zotero/SKILL.md` (43 MCP tools reference)
- **zotero-rag Skill**: `skills/zotero-rag/SKILL.md` (semantic search)
- **Zotero Documentation**: https://www.zotero.org/support/
