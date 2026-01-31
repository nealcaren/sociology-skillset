---
name: prose-humanizer
description: Edit academic prose to sound more natural and human. Removes LLM writing patterns (meta-commentary, inflated evaluations, excessive symmetry, adverb overuse) while preserving scholarly tone. Use when text sounds robotic, over-polished, or template-like.
---

# Prose Humanizer

Edit academic prose to remove LLM-typical patterns while keeping it appropriate for scholarly publication.

## Workflow

1. **Intake**: Get source text (file path or pasted content)
2. **Assess**: Identify which LLM patterns are present
3. **Rewrite**: Apply guidelines to produce cleaner prose
4. **Output**: Write to new markdown file
5. **Iterate**: User can run again on output for further refinement

## Quick Start

```
/prose-humanizer

Here's a draft paragraph that sounds too robotic: [paste text]
```

Or with a file:

```
/prose-humanizer

Please humanize: /path/to/draft.md
```

## What to Fix

See `references/guidelines.md` for the full 15-rule reference. Core patterns to address:

| Pattern | Example | Fix |
|---------|---------|-----|
| Meta-commentary | "This reflects a clear understanding..." | Cut or compress |
| Grand evaluations | "significantly enhances conceptual clarity" | Use observable effects |
| Evaluative adverbs | "convincingly demonstrates" | Delete the adverb |
| Abstract nouns | "the clarification of dynamics" | Use actors and actions |
| Triplets | "clarity, coherence, and rigor" | Use two items |
| Signpost words | "Importantly," "Overall," | Delete |
| Over-balanced contrast | "not merely X, but Y" | One clause |
| Paragraph morals | "Together, these changes underscore..." | End after the point |

## Output

Write the humanized text to a new file:
- If input is `draft.md` → output to `draft-humanized.md`
- If input is pasted text → output to `humanized-[timestamp].md` in current directory

Include a brief summary of changes made (2-3 sentences, not a detailed changelog).

## Iteration

The skill is designed to be run multiple times:
- First pass: structural issues (symmetry, paragraph morals, triplets)
- Second pass: word-level issues (adverbs, abstract nouns, signposts)
- Third pass: read aloud and fix anything that sounds rehearsed

Tell the user which pass you're on and what you focused on.

## Calibration

**Goal**: Prose that sounds specific, slightly uneven, and willing to assert judgments without narrating its own cleverness.

**Not the goal**: Perfect prose. Functional prose is human. Allow mild awkwardness.

**Genre constraint**: This is still academic writing. Maintain appropriate formality, citation practices, and argumentative structure. The goal is natural academic prose, not casual speech.

## Read the Guidelines

Before rewriting, read `references/guidelines.md` for the complete rule set with examples.
