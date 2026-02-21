# Phase 2: Planning

## Why This Phase Matters

Before drafting prose, you need a paragraph-by-paragraph plan that specifies what each paragraph will accomplish, how it will open, and what citations it will deploy. This planning prevents the common problem of aimless literature cataloging and ensures each paragraph drives the argument forward.

---

## Your Tasks

### 1. Assign Paragraph Functions

For each paragraph in the outline, assign a function from `techniques/paragraph-functions.md`:

| Function | Purpose |
|----------|---------|
| **DESCRIBE_THEORY** | Explicate framework or concept |
| **SYNTHESIZE** | Summarize patterns across studies |
| **PROVIDE_CONTEXT** | Ground a subsection in new empirical terrain |
| **CONTRAST** | Present competing positions |
| **CRITIQUE** | Identify limitations |
| **IDENTIFY_GAP** | Mark what's unknown (the turn) |
| **BRIDGE** | Connect literatures or show framework fit |
| **BRIDGE_TO_METHODS** | Transition to data/methods section |
| **STATE_HYPOTHESES** | Articulate formal directional predictions |
| **STATE_QUESTIONS** | Articulate open-ended research questions |
| **THEORETICAL_SYNTHESIS** | Restate the core argument in summary form |
| **PREVIEW** | Summarize coming findings (rare; ~4% of articles) |

**Opening function**: Default to DESCRIBE_THEORY or SYNTHESIZE. The introduction already established the phenomenon — the theory section should open with the scholarly conversation. Use PROVIDE_CONTEXT only when a subsection shifts to empirical terrain the introduction did not cover.

**Closing function**: Choose based on the article's design:
- Quantitative/experimental → STATE_HYPOTHESES or BRIDGE_TO_METHODS
- Qualitative/interpretive → STATE_QUESTIONS, THEORETICAL_SYNTHESIS, or BRIDGE_TO_METHODS
- When unsure → BRIDGE_TO_METHODS (the most common move at ~34%)

### 2. Draft Topic Sentences

For each paragraph, write a topic sentence that:
- Signals the paragraph's function
- Uses appropriate opening type (from `techniques/sentence-toolbox.md`)
- Sets up the paragraph's work

**Example topic sentences by function**:

| Function | Topic Sentence |
|----------|----------------|
| DESCRIBE_THEORY | "The concept of 'recognition' draws on several conceptual traditions." |
| SYNTHESIZE | "A growing body of research examines how residents of high-crime neighborhoods interact with police." |
| PROVIDE_CONTEXT | "Congress passed the WWII Serviceman's Readjustment Act of 1944, better known as the GI Bill, to ease veterans' transition to civilian life." |
| CONTRAST | "Others, however, argue that secondary labor market entry traps immigrants in dead-end jobs." |
| IDENTIFY_GAP | "Yet we know little about how guest mothers maintain maternal identity when authority is constrained." |
| STATE_QUESTIONS | "This study examines how mothers in doubled-up households negotiate identity and dignity." |
| STATE_HYPOTHESES | "This reasoning leads to our first hypothesis:" |
| BRIDGE_TO_METHODS | "To test these expectations, we draw on linked administrative records from the Swedish population registers." |

### 3. Plan Citation Deployment

For each paragraph, specify:
- How many citations (target 2.4-5.0 per paragraph)
- Citation pattern (parenthetical, author-subject, string, quote)
- Key sources to include

Use this template:

```markdown
## Paragraph 3: SYNTHESIZE

**Topic sentence**: "Research on legal cynicism demonstrates that distrust is patterned by neighborhood context and prior police contact."

**Citations (5)**:
- Kirk and Papachristos 2011 (author-subject for definition)
- Sampson and Bartusch 1998 (parenthetical)
- Desmond et al. 2016 (parenthetical)
- Gau and Brunson 2010 (parenthetical)
- Tyler 2006 (parenthetical in string)

**Pattern**: Mix of author-subject for foundational work + parenthetical string for synthesis
```

### 4. Sequence for Flow

Review the paragraph sequence to ensure:

**Logical progression**:
- Theory → Synthesis → Gap → Closing move
- Each paragraph builds on what precedes

**Smooth transitions**:
- What transition marker will open each paragraph?
- How does each paragraph connect to the previous?

**Turn positioning**:
- Is the turn in the right place?
- Does adequate synthesis precede it?
- Does the closing move follow naturally?

### 5. Check Cluster Alignment

Verify the paragraph sequence matches cluster expectations:

| Cluster | Expected Sequence |
|---------|------------------|
| **Gap-Filler** | SYNTHESIZE → SYNTHESIZE → GAP → BRIDGE_TO_METHODS *or* HYPOTHESES |
| **Theory-Extender** | DESCRIBE → SYNTHESIZE → GAP → BRIDGE → BRIDGE_TO_METHODS *or* HYPOTHESES |
| **Concept-Builder** | DESCRIBE → CRITIQUE → DESCRIBE → SYNTHESIZE+INTRO → DESCRIBE (new) → BRIDGE_TO_METHODS *or* SYNTHESIS |
| **Synthesis** | DESCRIBE(A) → SYNTHESIZE(A) → DESCRIBE(B) → SYNTHESIZE(B) → BRIDGE → BRIDGE_TO_METHODS *or* QUESTIONS |
| **Problem-Driven** | DESCRIBE(1) → CONTRAST(2) → CRITIQUE → QUESTIONS *or* HYPOTHESES |

### 6. Write Paragraph Map

Append a `## Phase 2: Citation Plan` section to `theory-memo.md`, including the full paragraph map and citation deployment plan:

```markdown
## Phase 2: Citation Plan

# Paragraph Map

## Overview
- Total paragraphs: [N]
- Total target citations: [N]
- Turn location: Paragraph [N]
- Closing function: [BRIDGE_TO_METHODS / STATE_HYPOTHESES / STATE_QUESTIONS / THEORETICAL_SYNTHESIS]

---

## Paragraph 1
**Function**: DESCRIBE_THEORY
**Subsection**: [if applicable]
**Topic sentence**: "[Draft opening]"
**Content notes**: [What this paragraph covers]
**Citations (N)**:
- [Source 1] (pattern)
- [Source 2] (pattern)
**Transition to next**: [How it connects to P2]

---

## Paragraph 2
**Function**: [...]
...

[Continue for all paragraphs]

---

## Paragraph [N]: THE TURN
**Function**: IDENTIFY_GAP
**Topic sentence**: "[Draft turn sentence]"
**Turn structure**:
1. Acknowledge: [what we know]
2. Pivot: [contrastive marker]
3. Gap: [specific gap claim]
4. Connect: [link to your study]
**Citations (N)**:
- [Sources supporting the gap claim]

---

## Summary Table

| P# | Function | Subsection | Citations | Key Sources |
|----|----------|------------|-----------|-------------|
| 1 | DESCRIBE_THEORY | — | 3 | [list] |
| 2 | SYNTHESIZE | — | 5 | [list] |
...
```

### 7. Pre-Draft Checklist

Before moving to drafting, verify:

- [ ] Every paragraph has an assigned function
- [ ] Topic sentences drafted for all paragraphs
- [ ] Citations planned (2.4-5.0 per paragraph)
- [ ] Total citations in target range for cluster
- [ ] Turn sentence drafted
- [ ] Sequence flows logically
- [ ] Transitions planned
- [ ] Cluster sequence alignment checked
- [ ] Opening function is DESCRIBE_THEORY or SYNTHESIZE (not PROVIDE_CONTEXT, unless justified)
- [ ] Closing function matches article design (quant → hypotheses/bridge; qual → questions/synthesis/bridge)

---

## Guiding Principles

### Topic Sentences Do the Heavy Lifting
A reader should be able to understand the section by reading only the topic sentences. If they can't, your structure isn't clear.

### Citation Deployment is Strategic
Don't just sprinkle citations randomly. Plan which sources do which work.

### The Paragraph Map is Your Drafting Guide
In Phase 3, you'll draft one paragraph at a time following this map. The better the map, the smoother the drafting.

### Don't Duplicate the Introduction
The theory section is not a second introduction. If you find yourself writing about phenomena, statistics, or stakes that the introduction already established, you're drifting into "mini paper" territory. Start with the scholarly conversation.

### Leave Room for Discovery
You may discover during drafting that a paragraph needs to split, or two should merge. That's fine—the map is a guide, not a prison.

---

## Field-Specific Adjustments

When a field profile was identified in Phase 0, apply the field-specific
guidance from `fields/{field}.md`. Field profiles override generalist
defaults where they conflict. Key areas that field profiles may adjust:

- Target word count and paragraph count
- Opening move distribution and structural patterns
- Citation timing and density
- Audience assumptions and vocabulary
- Prohibited moves specific to the field

Refer to the field profile's benchmarks table and writing checklist for
this section.

## Output Files to Create

1. **theory-memo.md** - Append a `## Phase 2: Citation Plan` section containing the full paragraph-by-paragraph plan and citation deployment strategy.

---

## When You're Done

Report to the orchestrator:
- Number of planned paragraphs
- Turn placement (paragraph number)
- Total planned citations
- Closing function selected
- Any concerns about coverage or sequence

Example summary:
> "Paragraph map complete. **10 paragraphs** planned: 3 framework, 2 synthesis, 1 gap (turn at P6), 1 bridge, 1 bridge-to-methods. **38 citations** distributed across paragraphs (avg 3.8/paragraph). Closing with BRIDGE_TO_METHODS. Turn drafts specific gap about guest mother identity in doubled-up households. Ready for Phase 3: Drafting."
