---
name: writing-editor
description: Edit prose to sound more natural, direct, and engaging. Works top-down through four levels (Document → Paragraph → Sentence → Word) with human checkpoints at each stage. Fixes LLM patterns, writerly bad habits, and style deficits. Works for academic papers, reports, memos, essays, blog posts, proposals, and other nonfiction. Use when prose sounds robotic, dull, or inaccessible.
---

# Writing Editor

Edit prose using a top-down workflow with human review at each level. Works for any nonfiction genre — academic papers, reports, memos, essays, blog posts, proposals.

## Project Integration

This skill reads from `project.yaml` when available:

```yaml
# From project.yaml
paths:
  drafts: drafts/sections/
```

**Project type:** This skill works for **all project types**. Prose editing improves writing regardless of methodology.

## File Management

This skill uses git to track progress across phases. Before modifying any output file at a new phase:
1. Stage and commit current state: `git add [files] && git commit -m "writing-editor: Pre-editing snapshot"`
2. Then proceed with modifications.

Do NOT create version-suffixed copies (e.g., `-v2`, `-final`, `-working`). The git history serves as the version trail.

## Workflow: Four Levels with Checkpoints

Work through each level, presenting proposed changes for user approval before moving to the next.

### Step 0: Document Protection

**Before making any edits**:
- Check if the file is in a git repo; if not, offer to `git init`
- Commit the original state before any edits: `git add [file] && git commit -m "writing-editor: Pre-editing snapshot"`
- After each level's approved changes, commit with a message like: `"Writing editor: Level 1 (Document) complete"`

This creates a full revision history the user can diff or revert. The input file IS the output — edit it in place. Do not create a working copy or a separate output file.

### Levels with Checkpoints

| Level | What to Fix | Checkpoint |
|-------|-------------|------------|
| **1. Document** | Structure, hooks, titles, abstracts, citations | User approves before continuing |
| **2. Paragraph** | Symmetry, triplets, endings, contrast patterns | User approves before continuing |
| **3. Sentence** | Passive voice, agents, abstract nouns, meta-commentary, em/en dashes | User approves before continuing |
| **4. Word** | Adverbs, signposts, throat-clearing, fancy-talk | User approves final version |

This ensures the user stays in control and can accept/reject changes at each stage.

## Quick Start

```
/writing-editor

Please edit: /path/to/draft.md
```

Or with pasted text:

```
/writing-editor

Here's a draft that sounds too formal: [paste text]
```

## Primary Reference

Use `references/merged-guidelines.md` as the main editing guide. It consolidates all rules organized by level:

- **Level 1: Document** (6 rules) - hooks, titles, structure, abstracts, citations, concrete examples
- **Level 2: Paragraph** (5 rules) - endings, symmetry, triplets, contrast, syntax-logic match
- **Level 3: Sentence** (13 rules) - passive voice, first person, abstract nouns, placeholders, agents
- **Level 4: Word** (7 rules) - throat-clearing, signposts, adverbs, intensifiers, fancy-talk

## Additional References

For deeper context or source-specific guidance:

| File | Source |
|------|--------|
| `references/guidelines.md` | LLM-specific patterns (15 rules) |
| `references/becker-guidelines.md` | Becker's *Writing for Social Scientists* (12 rules) |
| `references/sword-guidelines.md` | Sword's *Stylish Academic Writing* (14 rules) |
| `references/phrase-transformations.md` | Common phrase before/after examples |

## Core Method: Deletion Test

At every level, apply Becker's test: Remove each word or phrase. If meaning doesn't change, delete it.

## Level 1: Document

Before touching sentences, fix:

- **Opening hook**: Does it grab attention or start with a bland formula?
- **Title**: Short and unified, or bloated with variables and colons?
- **Structure**: Do section headings match what the opening promises?
- **Abstract/summary**: Active voice with humans and claims, or passive hedging? (Skip if genre has no abstract.)
- **Citations/references**: Do they advance the argument or just signal allegiance? (Adjust for genre — academic papers cite; memos and blog posts may not.)
- **Concrete examples**: Is each major concept grounded in specifics?

Present document-level changes. Wait for user approval.

## Level 2: Paragraph

After document structure is sound:

- **Paragraph endings**: Do they moralize ("Together, these underscore...") or just stop?
- **Symmetry**: Do three paragraphs start the same way?
- **Triplets**: Ornamental lists of three that could be two? (Keep conceptual triplets like "race, class, and gender")
- **Over-balanced contrast**: "Not X, but Y" that could be one clause?
- **Syntax-logic match**: Does grammar show which ideas are subordinate?

Present paragraph-level changes. Wait for user approval.

## Level 3: Sentence

After paragraphs are structured:

- **Passive voice**: "Data were collected" → "We collected data"
- **First person**: Use I/we for methods and claims
- **Abstract nouns**: "The investigation of" → "We investigated"
- **Placeholders**: "complex relation" → specify the actual relation
- **Deictic pronouns**: "This shows" → "This finding shows"
- **There is/are**: "There is evidence" → "Evidence shows"
- **Subject-verb distance**: Keep within 12 words
- **Vivid verbs**: Replace weak verbs with specific action
- **Dead metaphors**: Cut "cutting edge," "shed light on"
- **Meta-commentary**: Cut sentences about process/intent
- **Grand evaluations**: Replace abstract praise with observable effects
- **Over-justification**: Allow judgment without explaining every reason
- **Em/en dashes**: Rewrite the sentence—don't just swap for commas. Split into two sentences, fold the aside into the main clause, use a colon, reposition the aside, or drop it. Offer multiple options.

Present sentence-level changes. Wait for user approval.

## Level 4: Word

Final polish:

- **Throat-clearing**: "It is important to..." → [delete]
- **Signposts**: "Importantly," "Overall," → [delete]
- **Evaluative adverbs**: "convincingly demonstrates" → "demonstrates"
- **Empty intensifiers**: "reasonably comprehensive" → "comprehensive"
- **Ability phrases**: "managed to maintain" → "kept"
- **Fancy-talk**: "predicated upon" → "depends on"
- **Excessive praise**: "thoughtful, rigorous, and sophisticated" → "careful"

Present word-level changes. Wait for user approval.

## Output

After all levels approved, the edited file IS the output — it was edited in place. Commit the final state: `git add [file] && git commit -m "writing-editor: Level 4 (Word) complete"`.

For pasted text (no file), write the final edited text to `edited-[timestamp].md`.

Include a brief summary of changes at each level in the conversation.

## Calibration

**Goal**: Prose that sounds specific, slightly uneven, and willing to assert judgments without narrating its own cleverness.

**Not the goal**: Perfect prose. Functional prose is human. Allow mild awkwardness.

**Genre awareness**: Detect the genre from the input and respect its conventions. Academic papers keep citations and hedging where warranted. Memos stay short. Blog posts can be conversational. Reports keep structure tight. Don't flatten genre differences — adapt the rules to the context.

**Final test**: Read aloud. If it sounds like a report when it should be an essay, or a template when it should be a memo — keep editing.
