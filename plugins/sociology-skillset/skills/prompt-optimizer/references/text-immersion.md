# Text Immersion

Reading texts carefully before writing or revising classification prompts. This reference covers three modes: exploratory immersion (Phase 1, Step 0 — when categories need to be developed), initial immersion (Phase 1, Step 1 — when categories exist but need grounding), and focused re-immersion (Phase 3, when optimization stalls).

All three modes apply the same core idea: sit with the actual texts before making definitional decisions. Label definitions written from codebook abstractions miss how categories actually manifest. Definitions revised from metric dashboards miss why the confusion exists. Categories invented without reading the data miss what is actually there. Reading the texts — attentively, with specific questions — closes these gaps.

---

## Exploratory Immersion (Phase 1, Step 0 — Path B)

**When:** The user has a research question ("what emotions are in these texts?") but no classification scheme. Categories need to be discovered, not just operationalized.

**Purpose:** Develop a classification scheme grounded in what actually appears in the texts, then propose it to the user for refinement.

### Sample

Read 40-50 texts. This is more than standard immersion because you are mapping unknown territory.

Request a **diverse** sample — texts from different authors, time periods, contexts, or whatever dimensions of variation exist in the corpus. You need to see the range, not just the center. If the user can identify texts they consider "typical" and texts they consider "unusual," include both.

### Reading Stance

The question is open: **What is happening in these texts?** (Scoped to the user's research interest — emotion, framing, argumentation, etc.)

For each text, attend to:

**What is present:**
- What [emotions / frames / rhetorical moves / etc.] does this text contain?
- Is there one dominant signal or multiple?
- How intense or prominent is it?

**Variation across texts:**
- How is this text similar to others you have read?
- How is it different?
- Are you starting to see types or clusters? What are they?

**Dimensionality:**
- Is the phenomenon you are observing one-dimensional (e.g., emotion type) or multi-dimensional (e.g., emotion type + intensity + direction)?
- Are there aspects the user did not ask about but that vary in analytically interesting ways?

**Granularity:**
- How many natural groupings do you see? 3? 5? 10?
- Are some groupings common and others rare?
- Could rare groupings be merged, or are they analytically important despite being infrequent?

**Structure:**
- Are the categories mutually exclusive, or do texts frequently belong to multiple categories?
- Is the phenomenon categorical (discrete types) or continuous (a spectrum)?
- If continuous, where would natural cut points fall?

### Process

Read in two passes:

**Pass 1: Open reading.** Read all 40-50 texts without trying to categorize. Take notes on what you observe. Let patterns emerge. Do not commit to categories yet.

**Pass 2: Tentative grouping.** Read again, this time sorting texts into tentative groups. Notice:
- Which texts group together easily (these define your core categories)
- Which texts resist grouping (these are boundary cases — valuable for defining what categories are NOT)
- Which groups are large enough to be useful categories
- Which are too small or too heterogeneous

### Output

Present a proposed classification scheme to the user:

```
## Proposed Classification Scheme

### Research question: [the user's question]

### Proposed dimensions

Based on reading [N] texts, I see [N] dimensions that vary in analytically
interesting ways:

**Dimension 1: [Name]**
What it captures: [brief description]
Why it matters: [what it would tell the user]

**Dimension 2: [Name]** (if applicable)
...

### Proposed categories for [Dimension 1]

**[Category A]**: [Description grounded in observed texts]. Texts in this
category typically [observable features]. Appeared in roughly [N] of [N] texts.

**[Category B]**: [Description]. Typically [features]. Appeared in ~[N] texts.

...

### Boundary cases
- [Text X] sits between [A] and [B] because [reason]
- [Text Y] doesn't fit any proposed category cleanly

### Open questions for you (the researcher)
- Should [X] be its own category or a subtype of [Y]?
- Is [dimension 2] analytically useful for your project, or is it a distraction?
- The data contains [rare pattern] — is it worth capturing as a category, or
  should it be folded into [adjacent category]?
```

**The user decides.** The proposed scheme is a starting point for discussion. The user may accept it, revise categories, merge or split groups, add dimensions you did not propose, or reject dimensions you suggested. Iterate until the user is satisfied. Then proceed to standard immersion (Step 1) to ground the confirmed categories, and on to prompt construction (Step 2).

---

## Initial Immersion (Phase 1, Step 1)

**When:** Before writing any label definitions or seed prompt. After the user has described the task and categories (or after exploratory immersion has produced a scheme) but before you have committed anything to a prompt.

**Purpose:** Ground your understanding of the categories in the real texture of the texts, not just the user's abstract descriptions. If you just completed exploratory immersion, this step may be brief — a quick confirmation that the new categories map cleanly onto additional texts.

### Sample

Read 20-30 texts from the corpus. If the user has labeled data, request a stratified sample:
- 4-6 labeled examples per category
- Plus 5-10 texts the user considers borderline or difficult
- If fewer than 30 texts are available, read all of them

If the user does not have labeled data yet, request 20-30 representative texts and read them without labels.

### Reading Stance

For each text, attend to:

**Surface features:**
- What words, phrases, or patterns immediately signal a category?
- What is the text's tone, register, and style?
- How long is it? How much context does it carry?

**Category signals:**
- What makes this text "feel like" its category?
- Could a reasonable person assign it to a different category? Which one, and why?
- What feature would you point to if you had to justify the label?

**Boundary awareness:**
- Where does your own intuition hesitate?
- What would make this text tip into an adjacent category?
- Is the boundary between categories sharp or gradual in practice?

**Surprises:**
- Does any text not match your expectation of what its category looks like?
- Are there text types or styles you did not anticipate?
- Do any categories look different in practice than they sound in definition?

### Output

Present your observations to the user organized by category:

```
## Immersion Observations

### [Category A]
What texts in this category actually look like: [description grounded in examples]
Distinctive features: [what signals this category]
Potential confusion with: [adjacent category and why]

### [Category B]
...

### Boundary Cases
Texts that sit between categories: [list with notes on what makes them hard]

### Surprises
Things I noticed that the codebook definitions do not capture: [list]
```

These observations directly inform the label definitions in the seed prompt. Definitions should describe categories as they actually appear in the texts, not as they exist in theory.

---

## Focused Re-immersion (Phase 3)

**When:** Optimization has stalled. A specific category pair remains persistently confused after 2+ iterations of prompt editing. Metric-driven fixes are not working. The problem appears to be substantive — about what the categories actually mean — not technical.

**Purpose:** Understand the real boundary between two confused categories by reading texts from both sides. The goal is not a prompt tweak but a revised understanding of the distinction itself.

### Identifying the Trigger

Focused re-immersion is appropriate when:
- Macro-F1 improvement is < 2 points across 2 consecutive iterations
- The confusion matrix shows a persistent hot spot between a specific pair
- Prompt edits targeting that pair (sharper definitions, added exclusions, different framing) have not resolved it
- The model's reasoning (if available) suggests it understands the task but draws the boundary differently than intended

It is NOT appropriate when:
- Errors are spread across many category pairs (try Phase 4 diversity instead)
- The prompt has only been through 1 iteration (give metric-driven optimization a fair chance first)
- The issue is clearly a format or parsing problem

### Sampling

This requires a real sample — large enough to see the pattern, not just individual errors.

**Collect 15-20 texts from each side of the confused boundary**, stratified across four quadrants:

| | **Gold label = A** | **Gold label = B** |
|---|---|---|
| **Model predicted A** | Clear A (correctly classified) | Misclassified B→A |
| **Model predicted B** | Misclassified A→B | Clear B (correctly classified) |

Aim for roughly equal representation from each quadrant. If one quadrant has fewer than 5 texts (e.g., very few B→A errors), include all available and supplement the others.

**Total: 30-40 texts.** This is enough to see patterns without overwhelming the reading.

### Reading Stance

The question is focused: **What actually distinguishes A from B in these texts?**

Read through each quadrant in order:

**1. Clear A cases (correctly classified as A).**
- What do these texts have in common?
- What features make them unambiguously A?
- Is there a prototypical A text? What does it look like?

**2. Clear B cases (correctly classified as B).**
- Same questions. What makes B clearly B?
- How does the "feel" of B differ from A?
- What features are present in B but absent in A (or vice versa)?

**3. Misclassified A→B (A texts the model called B).**
- What do these have in common with each other?
- What feature of these texts makes them look like B to the model?
- Are they atypical A texts, or is the model responding to a real signal that the definition does not account for?

**4. Misclassified B→A (B texts the model called A).**
- Same questions in reverse.
- What makes these B texts look like A?
- Is there a subtype of B that resembles A?

### Across all four quadrants, ask:

- **Is the boundary where the codebook puts it, or is there a more natural split?** Sometimes the confusion exists because the "real" boundary runs in a different place than the defined one.
- **Is one category actually two things?** If misclassified A texts share a feature that correctly classified A texts lack, category A may contain a subtype that behaves differently.
- **Is the distinction gradient rather than categorical?** Some boundaries are genuinely fuzzy. Texts near the boundary may not have a single correct answer. If so, this is a ceiling on performance — not a prompt problem.
- **What feature, if you could point to it, would correctly sort the misclassified texts?** This is the diagnostic question. If you can name the feature, it can go into the prompt definition. If you cannot, the distinction may be inherently ambiguous.

### Output

The output of focused re-immersion is a diagnosis, not a prompt edit. Present it to the user:

```
## Re-immersion: [Category A] vs. [Category B]

### What I found
[Summary of the key distinction as it actually appears in the texts]

### Why the current definitions fail
[What the current definitions say vs. what the texts actually show]

### Recommendation
[One of the following:]

Option 1 — Revised definitions:
  [New definition for A]
  [New definition for B]
  [What changed and why]

Option 2 — Boundary shift:
  [The split should be drawn differently because...]
  [Proposed new boundary]

Option 3 — Category split:
  [Category X is actually two things: X1 and X2]
  [How they differ]

Option 4 — Ambiguity acknowledgment:
  [This distinction is genuinely fuzzy for texts like...]
  [Current performance (~X.XX F1 on this pair) is likely near the ceiling]
  [Consider: merging categories, adding an "uncertain" label, or accepting current performance]
```

**The user decides.** Re-immersion produces a finding about the coding scheme. The user — as the domain expert — decides whether to revise definitions, restructure categories, or accept the limitation.

After the user decides, rebuild the affected prompt section and re-enter the optimization loop in Phase 3.

---

## Principles for Both Modes

1. **Read, do not scan.** The goal is to understand what makes each text what it is, not to confirm a hypothesis about what keywords to look for.

2. **The texts are the ground truth.** If the codebook says A and B are distinct but the texts blur together, the problem is in the definitions, not the texts.

3. **Surprises are the most valuable signal.** A text that does not look like you expected it to is telling you something the current definitions miss.

4. **Boundary cases are data, not noise.** Texts that sit between categories reveal where the definitions need work. Do not dismiss them as outliers.

5. **The user is the domain expert.** You bring careful reading and pattern recognition. They bring substantive knowledge about why categories exist and what they mean. Immersion observations should be presented as findings for discussion, not as unilateral definitional changes.
