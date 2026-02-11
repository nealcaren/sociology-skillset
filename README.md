# Sociology Writing Suite

A set of skills for [Claude Code](https://docs.anthropic.com/en/docs/claude-code) to assist with sociology research projects—qualitative, quantitative, and mixed methods. Covers the full research-to-publication workflow: literature review, data analysis (interviews, R, Stata), and academic writing.

**This project is actively under development.** Skills and workflows may change.

## Installation

Requires [Claude Code](https://docs.anthropic.com/en/docs/claude-code):

```bash
npm install -g @anthropic-ai/claude-code
```

Then install the plugin:

```
/plugin marketplace add nealcaren/sociology-writing-suite
/plugin install sociology-writing-suite@sociology-writing-suite
```

Or clone manually:

```bash
git clone https://github.com/nealcaren/sociology-writing-suite.git
```

And add to your Claude Code settings (`~/.claude/settings.json` or project `.claude/settings.json`):

```json
{
  "projects": {
    "/path/to/your/project": {
      "mcpServers": {},
      "skills": [
        "/path/to/sociology-writing-suite/plugins/sociology-writing-suite"
      ]
    }
  }
}
```

### Verify Installation

Restart Claude Code and type `/help`. You should see skills like `/interview-analyst`, `/r-analyst`, `/lit-search`, `/argument-builder`, etc.

## Quick Start

### The Research Coordinator

Start with `/research-coordinator` for full workflow orchestration. It drives the process proactively, maintains project state, and dispatches to specialized skills as needed:

```
/research-coordinator

I'm studying how journalists cover protests. I have 30 interviews with reporters.
```

The coordinator guides you through literature search, synthesis, data analysis, and writing.

### Invoke Skills Directly

Or invoke any skill directly:

```
/argument-builder
```

Claude loads the skill and guides you through its workflow.

### Provide Context

Include context when invoking:

```
/interview-analyst

I have 30 interviews with activists about why they left social movements.
My theoretical interest is in disengagement processes.
```

## The Skills

### Qualitative Research Chain

Go from raw interviews to written manuscript sections:

| Skill | What It Does |
|-------|--------------|
| `/interview-analyst` | Qualitative coding and pattern identification |
| `/qual-findings-writer` | Draft Methods and Findings sections for qualitative papers |
| `/article-bookends` | Draft Introduction, Discussion, and Conclusion |

### Quantitative Research Chain

Go from data to written manuscript sections:

| Skill | What It Does |
|-------|--------------|
| `/r-analyst` | Statistical analysis in R (DiD, IV, matching, panel methods, etc.) |
| `/stata-analyst` | Statistical analysis in Stata (same methods as r-analyst) |
| `/quant-findings-writer` | Draft Results sections for quantitative papers |
| `/article-bookends` | Draft Introduction, Discussion, and Conclusion |

### Mixed Methods Research Chain

| Skill | What It Does |
|-------|--------------|
| `/interview-analyst` | Qualitative strand analysis |
| `/r-analyst` or `/stata-analyst` | Quantitative strand analysis |
| `/mixed-methods-findings-writer` | Draft integrated Findings sections |
| `/article-bookends` | Draft Introduction, Discussion, and Conclusion |

### Literature Review Chain

Use in sequence to go from search to written Theory section:

| Skill | What It Does |
|-------|--------------|
| `/lit-search` | Build literature database using OpenAlex API |
| `/reading-agent` | Create structured reading notes for papers |
| `/lit-synthesis` | Deep reading, theoretical mapping, debate identification |
| `/argument-builder` | Draft publication-ready Theory section |

### Manuscript Section Skills

| Skill | What It Does |
|-------|--------------|
| `/abstract-builder` | Write publication-ready abstracts (4 archetype options) |
| `/methods-writer` | Write Methods sections (3 pathway options) |
| `/case-justification` | Write case selection rationale |

### Revision Support

| Skill | What It Does |
|-------|--------------|
| `/revision-coordinator` | Parse reviewer feedback, route to specialized skills |
| `/peer-reviewer` | Simulate peer review before submission |
| `/verifier` | Verify quotes and claims against source materials (transcripts, literature) |
| `/bibliography-builder` | Extract citations, match to Zotero, generate bibliography |
| `/writing-editor` | Edit prose to sound natural; fixes LLM patterns and academic bad habits |

### Meta-Skills

| Skill | What It Does |
|-------|--------------|
| `/project-scaffold` | Initialize project structure with standardized directories and progress tracking |
| `/genre-skill-builder` | Create new writing skills from corpus analysis |

### Zotero Integration

| Skill | What It Does |
|-------|--------------|
| `/zotero` | 38 MCP tools for Zotero library operations (search, metadata, collections, annotations) |
| `/zotero-rag` | Semantic search across PDF content using RAG embeddings |

These require the `mcp-zotero` server — see [Zotero Setup](#zotero-setup-optional) below.

## Common Workflows

### Writing a Qualitative Paper from Interview Data

1. `/interview-analyst` — Analyze interviews
2. `/methods-writer` — Write methods
3. `/qual-findings-writer` — Write findings
4. `/lit-search` → `/reading-agent` → `/lit-synthesis` → `/argument-builder` — Build literature review
5. `/article-bookends` — Write intro and conclusion
6. `/verifier` — Verify all quotes match source transcripts
7. `/peer-reviewer` — Pre-submission review
8. `/bibliography-builder` — Finalize references

### Writing a Quantitative Paper

1. `/r-analyst` or `/stata-analyst` — Run analysis (design → data → models → robustness → output)
2. `/methods-writer` — Write methods
3. `/quant-findings-writer` — Draft Results section from statistical output
4. `/lit-search` → `/reading-agent` → `/lit-synthesis` → `/argument-builder` — Build literature review
5. `/article-bookends` — Write intro and conclusion
6. `/peer-reviewer` — Pre-submission review
7. `/bibliography-builder` — Finalize references

### Writing a Mixed Methods Paper

1. `/interview-analyst` — Qualitative strand
2. `/r-analyst` or `/stata-analyst` — Quantitative strand
3. `/methods-writer` — Write methods (both approaches)
4. `/mixed-methods-findings-writer` — Draft integrated findings
5. `/lit-search` → `/reading-agent` → `/lit-synthesis` → `/argument-builder` — Build literature review
6. `/article-bookends` — Write intro and conclusion
7. `/peer-reviewer` — Pre-submission review

### Using Semantic Search for Literature

1. Index your Zotero collection: `index_library collection_key="YOUR_COLLECTION"`
2. Search by meaning: `semantic_search query="how organizations maintain legitimacy"`
3. Expand context: `get_chunk_context chunk_id="..." context_lines=20`
4. Find related passages: `find_similar_chunks chunk_id="..."`

### Revising After Peer Review

1. `/revision-coordinator` — Parse and route feedback
2. Skills dispatched by coordinator for specific sections
3. `/article-bookends` Phase 4 — Check coherence
4. `/peer-reviewer` — Validate before resubmission

## Skill Features

### Cluster-Based Writing

Several skills use empirically-derived styles based on analysis of 80 articles from *Social Problems* and *Social Forces*:

- **argument-builder**: Gap-Filler, Theory-Extender, Concept-Builder, Synthesis, Problem-Driven
- **article-bookends**: Same 5 clusters for intros/conclusions
- **quant-findings-writer**: 7 clusters (Progressive Model Builder, Hypothesis Tester, Decomposition Analyst, etc.)
- **mixed-methods-findings-writer**: 5 clusters (Thematic Integrator, Quant-Anchored Elaborator, etc.)
- **case-justification**: Minimal, Standard, Deep Historical, Comparative, Policy-Driven
- **methods-writer**: Efficient (600-900w), Standard (900-1200w), Detailed (1200-1800w)

### Calibration Benchmarks

All skills include empirically-derived benchmarks: word counts, citation density (~24 per 1,000 words for Theory sections), structural patterns, and cluster-specific norms.

### Phase-Based Workflows

Each skill follows a structured workflow with pause points for user review.

## Zotero Setup (Optional)

Several skills can connect to your [Zotero](https://www.zotero.org/) library for full-text PDF access, annotations, and semantic search. The skills will detect if Zotero isn't configured and offer to help you set it up. You can also set it up manually:

```bash
# Base install (38 Zotero API tools)
uv tool install mcp-zotero

# With semantic search (+ 8 RAG tools)
uv tool install "mcp-zotero[rag]"

# With OCR fallback for scanned PDFs
uv tool install "mcp-zotero[rag,ocr]"
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

See `plugins/sociology-writing-suite/skills/zotero/guides/setup.md` for details.

**Skills that use Zotero:** `zotero`, `zotero-rag`, `lit-synthesis`, `peer-reviewer`, `reading-agent`, `bibliography-builder`

## File Structure

```
sociology-writing-suite/
├── .claude-plugin/
│   └── marketplace.json        # Marketplace catalog
├── plugins/
│   └── sociology-writing-suite/
│       ├── plugin.json         # Plugin manifest
│       └── skills/
│           ├── abstract-builder/
│           ├── argument-builder/
│           ├── bibliography-builder/
│           ├── case-justification/
│           ├── genre-skill-builder/
│           ├── article-bookends/
│           ├── interview-analyst/
│           ├── lit-search/
│           ├── lit-synthesis/
│           ├── methods-writer/
│           ├── mixed-methods-findings-writer/
│           ├── peer-reviewer/
│           ├── project-scaffold/
│           ├── qual-findings-writer/
│           ├── quant-findings-writer/
│           ├── r-analyst/
│           ├── reading-agent/
│           ├── research-coordinator/
│           ├── revision-coordinator/
│           ├── stata-analyst/
│           ├── verifier/
│           ├── writing-editor/
│           ├── zotero/
│           └── zotero-rag/
└── README.md
```

Each skill folder contains:
- `SKILL.md` — Main skill definition
- `phases/` — Phase guides
- `clusters/` or `pathways/` — Style-specific guidance
- `techniques/` — Craft reference guides
- `guides/` — Setup and usage guides (for zotero skills)
- `references/` — Tool references and error patterns

## License

MIT

## Author

Neal Caren
