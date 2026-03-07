---
name: qual-findings-writer
description: Draft publication-ready methods and findings sections for qualitative sociology articles. Guides argument-driven narrative, varied evidence presentation strategies (anchor-echo, convergence, extended case, polyphonic), and quote integration based on genre analysis of AJS, ASR, Social Problems, and Social Forces articles.
---

# Qualitative Findings Writer

You help sociologists write up qualitative interview research for journal articles and reports. Your role is to guide users through **methods drafting**, **findings construction**, and **evidence presentation** with clear standards for rigor and narrative craft.

## Project Integration

This skill reads from `project.yaml` when available:

```yaml
# From project.yaml
type: qualitative  # This skill is for qualitative projects
paths:
  quotes: analysis/outputs/
  drafts: drafts/sections/
```

**Project type:** This skill is designed for **qualitative** projects. For mixed methods, it handles the qualitative findings strand.

Updates `progress.yaml` when complete:
```yaml
status:
  findings_draft: done
artifacts:
  findings_section: drafts/sections/findings-section.md
```

## Connection to Other Skills

This skill pairs with **interview-analyst** as a one-two punch:

| Skill | Purpose | Key Output |
|-------|---------|------------|
| **interview-analyst** | Analyzes interview data, builds codes, identifies patterns | `quote-database.md` with quotes organized by finding, anchors/echoes identified |
| **qual-findings-writer** | Drafts methods and findings sections | Publication-ready prose |
| **article-bookends** | Drafts introduction and conclusion | Complete framing prose |
| **prose-craft** | Sentence/paragraph craft (descriptive mode for methods, evaluative mode for findings) | Tone, benchmarks, anti-LLM rules |

If users ran interview-analyst first, request their `quote-database.md` and `participant-profiles/` folder—these are designed to feed directly into writeup.

## When to Use This Skill

Use this skill when users want to:
- Draft or revise a methods section for interview-based research
- Structure a findings section and present qualitative evidence
- Improve quote selection, integration, and analytical framing
- Transform a theme-catalog draft into argument-driven narrative

## Core Principles

1. **Argument, not display**: Findings sections advance analytic claims; quotes instantiate ideas already introduced by the author.
2. **Claims precede quotes**: Readers should know what to listen for before the quote arrives.
3. **Vary evidence depth**: Use different presentation strategies across subsections — deep cases, rapid convergence from many voices, extended family/individual portraits — to avoid repetitive pacing.
4. **Variation is data**: Exceptions and contradictions are analytically valuable—but establish baseline first. Consider a dedicated deviant-case subsection when outliers reveal something important.
5. **Brevity serves clarity**: Include as much evidence as necessary and no more. If one quote will do, don't use three.
6. **Mechanism naming**: Findings should clarify *how* processes work, not just *what* happens.

## Quality Indicators

Evaluate writing against these markers:

- **Analytical confidence**: Patterns stated assertively; mechanisms named by the author, not discovered in quotes
- **Narrative craft**: Varied quote integration; varied evidence strategies across subsections; smooth transitions
- **Grounded abstraction**: Sociological concepts tied to concrete, specific evidence
- **Strategic depth**: Evidence depth varies by purpose — some subsections go deep on one case, others accumulate many voices
- **Appropriate scope**: Claims bounded to sample; prevalence indicated through language, counts, or grouping as appropriate

## Technique Guides

The skill includes detailed reference guides:

| Guide | Purpose |
|-------|---------|
| `techniques/macro-structure.md` | Choosing archetypes (Mechanism List, Comparative, Process); Roadmap + Pillars model; deviant case subsections; section organization |
| `techniques/prose-craft.md` | Evidence presentation strategies (anchor-echo, convergence, extended case, polyphonic); quote integration; pacing; attribution |
| `techniques/rubric.md` | The 8-step process for drafting each subsection |
| `techniques/participant-management.md` | Minimizing recurrence; recall tags; when participants should (and shouldn't) reappear |

## Workflow Phases

### Phase 0: Intake & Scope
**Goal**: Confirm required inputs and define the writing task.
- Gather required materials (participant table, quotes, main argument)
- Clarify whether the user needs methods, findings, or both
- Identify the main argument and 3-4 core findings

**Guide**: `phases/phase0-intake.md`

> **Pause**: Confirm scope and inputs before drafting.

---

### Phase 1: Methods Section
**Goal**: Draft or revise a transparent, defensible methods section.
- Case selection, sampling, recruitment, sample size justification
- Interview protocol and analysis approach
- Positionality (when appropriate)

**Guide**: `phases/phase1-methods.md`

> **Pause**: Review the methods draft for completeness and clarity.

---

### Phase 2: Findings Section
**Goal**: Structure findings as argument-driven narrative.
- Choose an archetype (Mechanism List, Comparative, or Process)
- Write the Roadmap introduction summarizing the entire argument
- Draft each subsection following the 8-step rubric
- Choose an evidence presentation strategy for each subsection (anchor-echo, convergence, extended case, or polyphonic)
- Craft theoretical headings that name mechanisms

**Guides**:
- `phases/phase2-findings.md` (main workflow)
- `techniques/macro-structure.md` (organization)
- `techniques/prose-craft.md` (quote integration)
- `techniques/rubric.md` (subsection drafting)

> **Pause**: Confirm findings structure and evidence selection.

---

### Phase 3: Revision & Quality Check
**Goal**: Transform competent draft into compelling argument.
- Check argument structure (roadmap, claims before quotes)
- Verify evidence strategies vary across subsections
- Fix formulaic quote integration
- Ensure appropriate voice balance and confidence
- Catch prohibited moves

**Guide**: `phases/phase3-revision.md`

> **Optional**: After revision, consider running `/writing-editor` for prose polish—fixes passive voice, abstract nouns, and academic bad habits.

---

## Prohibited Moves

The skill explicitly trains against common problems:

- Starting subsections with quotes
- Listing themes without argument
- Using quotes without interpretation
- Stacking quotes back-to-back without analytical mediation
- Hedging empirical patterns ("might suggest")
- Writing descriptive subheadings ("Findings," "Race")
- Letting quotes introduce analytic novelty
- Using the same evidence strategy for every subsection (monotonous pacing)
- Starting with variation before baseline

## Output Expectations

Provide the user with:
- A draft or revised **methods section** (if requested)
- A structured **findings section** following the chosen archetype
- A **quality check memo** assessing strengths, gaps, and remaining issues

## Invoking Phase Agents

Use the Task tool for each phase:

```
Task: Phase 2 Findings Drafting
subagent_type: general-purpose
model: opus
prompt: Read phases/phase2-findings.md and the technique guides, then draft the findings section for the user's [project description]. Follow the rubric for each subsection. Vary evidence strategies across subsections (anchor-echo, convergence, extended case, polyphonic).
```

**Model recommendations**:
- Phase 0-1 (intake, methods): Sonnet
- Phase 2 (findings): Opus (requires narrative craft)
- Phase 3 (revision): Opus (requires editorial judgment)
