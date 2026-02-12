# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What This Is

A Claude Code plugin marketplace containing the `sociology-skillset` plugin — more than two dozen markdown-based skills for academic sociology research covering qualitative, quantitative, and mixed methods workflows. No build system, no compiled code; skills are structured markdown files that Claude Code loads as instructions.

## Repository Layout

```
.claude-plugin/marketplace.json          # Marketplace catalog (version + plugin list)
plugins/sociology-skillset/
  plugin.json                            # Plugin manifest (version must match marketplace.json)
  skills/[skill-name]/
    SKILL.md                             # Skill definition (YAML frontmatter + instructions)
    phases/                              # Phase-specific guides (phase0-intake.md, etc.)
    clusters/ or pathways/               # Empirically-derived style variants
    techniques/                          # Craft reference guides
```

## Skill Anatomy

Each skill has a `SKILL.md` with YAML frontmatter:
```yaml
---
name: skill-name
description: One-line description shown in /help
---
```

Skills follow a **phase-based workflow** pattern: numbered phases with pause points for user review. Writing skills use **cluster-based guidance** derived from corpus analysis of Social Problems and Social Forces articles.

## Key Architectural Patterns

**Project coordination**: Skills read/write `project.yaml` (canonical paths, metadata) and `progress.yaml` (workflow state, artifact registry) in the user's research project directory. The `project-scaffold` skill creates these files; `research-coordinator` orchestrates the full workflow across skills.

**Skill composition**: Skills chain together with documented inputs/outputs. Example chains:
- Qualitative: `lit-search` → `lit-synthesis` → `argument-builder` → `interview-analyst` → `qual-findings-writer` → `article-bookends`
- Quantitative: `lit-search` → `lit-synthesis` → `argument-builder` → `r-analyst`/`stata-analyst` → `quant-findings-writer` → `article-bookends`
- Mixed: Both qualitative and quantitative strands → `mixed-methods-findings-writer` → `article-bookends`

**Three project types**: qualitative, quantitative, and mixed methods. Skills check project type from `project.yaml` and adapt their workflows accordingly.

**Zotero integration**: `zotero` and `zotero-rag` skills wrap the `mcp-zotero` MCP server (separate package at `nealcaren/mcp-zotero`). Both include first-run checks that detect whether the server is installed.

## Publishing Updates

See `PUBLISHING.md` for the full process. The critical rule: **versions must match** in both `plugin.json` and `marketplace.json`. After pushing, update the local marketplace with `/plugin marketplace update sociology-skillset`.

## Version Sync Checklist

When bumping versions or adding/removing skills, update these **three things** in **both** files:
1. `plugins/sociology-skillset/plugin.json` — `version` and `description`
2. `.claude-plugin/marketplace.json` — `plugins[0].version` and `plugins[0].description`

The `description` field is duplicated verbatim between the two files. It must list the current skill count and all skill names grouped by category. Keep the descriptions identical.

Also update the "Current Skills" section below and the skill count in this file's opening paragraph.

## Adding a New Skill

1. Create `plugins/sociology-skillset/skills/<skill-name>/SKILL.md` with YAML frontmatter (`name`, `description`)
2. Add phase files in `phases/` subdirectory if the skill uses phased workflows
3. Add cluster/pathway files if the skill offers style variants
4. Update skill count and skill list in: this file (CLAUDE.md), `plugin.json`, and `marketplace.json`
5. Bump the version in both `plugin.json` and `marketplace.json`
6. Use `genre-skill-builder` to create new writing skills from corpus analysis

## Current Skills (26)

**Zotero**: zotero, zotero-rag
**Literature**: lit-search, lit-synthesis, reading-agent, argument-builder
**Qualitative analysis**: interview-analyst
**Quantitative analysis**: r-analyst, stata-analyst
**Computational text analysis**: text-analyst
**Text classification**: prompt-optimizer
**Findings writing**: qual-findings-writer, quant-findings-writer, mixed-methods-findings-writer
**Manuscript sections**: methods-writer, case-justification, article-bookends, abstract-builder
**Revision**: verifier, peer-reviewer, revision-coordinator, writing-editor, bibliography-builder
**Meta**: genre-skill-builder, project-scaffold, research-coordinator
