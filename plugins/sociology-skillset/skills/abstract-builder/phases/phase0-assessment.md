# Phase 0: Assessment

## Why This Phase Matters

The single most important decision in abstract writing is **archetype selection**. The archetype determines your opening move, sentence sequence, and closing strategy. Getting this wrong means writing an abstract that doesn't match your contribution—confusing readers about what kind of study this is.

This phase ensures you make a deliberate, informed choice about which style fits your project.

---

## Your Tasks

### 0. Check for Contribution Profile

Before doing your own archetype selection, check whether the user has a contribution profile from **contribution-framer** (`drafts/contribution-profile.md` or specified in `progress.yaml`).

If a contribution profile exists:
- Read it for the contribution type, threading vocabulary, and abstract template
- Use the profile's contribution type to inform archetype selection (the contribution type suggests which opening move and sentence sequence will work best)
- Use the profile's threading vocabulary to select key terms for the abstract
- The profile does not override archetype selection entirely (opening move is a separate dimension from contribution type), but it strongly constrains the options
- Still complete Steps 1-2 below, using the profile to pre-populate answers

If no contribution profile exists, proceed with all steps below.

### 1. Gather Project Information

Collect from the user:

**Required**:
- Research question(s)
- Main argument or contribution claim
- Data description (number of interviews, population, location)
- Key findings (2-3 main results)

**Helpful**:
- Target journal (if known)
- Existing draft (if revising)
- Contribution profile from contribution-framer (if available)
- How they want to position the research (phenomenon-led, gap-filling, etc.)

### 2. Apply the Archetype Decision Tree

Work through this diagnostic to recommend an archetype:

```
What should your FIRST SENTENCE do?

├── Describe an observable social phenomenon?
│   └── The phenomenon is compelling, surprising, or dramatic?
│   └── Readers don't need literature context?
│       └── ARCHETYPE 1: Empirical-Showcase
│
├── Position within scholarly conversation?
│   └── Literature, prior research, or "This study..." opener?
│   └── Gap-filling contribution?
│       └── ARCHETYPE 2: Research-Report
│
├── Establish why the topic matters?
│   └── Importance, urgency, change, or disruption?
│   └── Policy-relevant implications?
│       └── ARCHETYPE 3: Stakes-Driven
│
└── Ask a question?
    └── Explicit "How...?" or "What...?" question?
    └── Study definitively answers the puzzle?
        └── ARCHETYPE 4: Puzzle-Solver
```

### 3. Review Archetype Profile

Once you have a candidate archetype, read the detailed profile:
- `clusters/empirical-showcase.md`
- `clusters/research-report.md`
- `clusters/stakes-driven.md`
- `clusters/puzzle-solver.md`

Verify the profile matches the user's project.

### 4. Consider Secondary Factors

If the decision tree isn't definitive, consider:

| Factor | Empirical-Showcase | Research-Report | Stakes-Driven | Puzzle-Solver |
|--------|-------------------|-----------------|---------------|---------------|
| **Audience** | Broad readership | Subfield specialists | Policy-oriented | Theory-curious |
| **Contribution** | Empirical discovery | Gap-filling | Policy implications | Puzzle resolution |
| **Findings** | Surprising/dramatic | Extends literature | Has implications | Answers question |
| **Length need** | Standard (6.5 sent) | Flexible (6.4 sent) | Longer (7 sent) | Standard (6.6 sent) |

### 5. Present Assessment

Present in the conversation:

```markdown
# Abstract Assessment

## Project Summary
- Research question: [summarize]
- Main argument: [summarize]
- Data: [N] interviews with [population] in [location]
- Key findings: [list 2-3]

## Archetype Analysis

### Decision Tree Path
[Walk through the logic of the decision tree]

### Primary Recommendation: [Archetype Name]

**Why this fits**:
[2-3 sentences explaining the match between project and archetype]

**What this means**:
- Opening move: [description]
- Typical length: [X] sentences, [Y] words
- Closing strategy: [contribution/implications/findings]

---

### Alternative Considered: [Archetype Name]

**Why this might fit**: [1-2 sentences]

**What would make this preferable**: [specific conditions]

**Trade-off**: [what you gain vs. lose]

---

## Archetype Implications

| Feature | Recommendation |
|---------|---------------|
| Opening move | [specific move type] |
| Sentence count | [target] |
| Word count | [target range] |
| Closing move | [type] |

## Questions for User
- [Any clarifying questions before proceeding]
```

### 6. Present Recommendation

Present to user with clear structure:

1. **Your primary recommendation** with rationale
2. **One alternative** with what would make it preferable
3. **Decision factors** that could shift your recommendation
4. **Questions** you have before proceeding

**Important**: Let the user choose—don't assume they'll take the primary. Some users know their project better and may prefer the alternative.

---

## Guiding Principles

### When in Doubt, Choose Research-Report
It's the most common archetype overall (43% at SP/SF, 71% at ASR, 79% at AJS) and the safest approach. Clear, efficient, professional. **At ASR/AJS, Research-Report is the strong default.**

### Empirical-Showcase Requires Compelling Phenomena
Don't use this archetype unless your phenomenon is genuinely compelling or dramatic. Less common at ASR (15%) and AJS (12%) than at SP/SF (39%).

### Stakes-Driven Requires Genuine Significance — and the Right Venue
Only choose Stakes-Driven if you can articulate why the topic is important without it sounding like throat-clearing. **Near-absent at ASR/AJS (~3%)** — these journals prefer scholarly framing over urgency appeals.

### Puzzle-Solver is Rare for a Reason
Only ~5% of abstracts use this form across all venues. It requires a genuine, answerable question—not a rhetorical one.

### Venue Matters for Archetype Selection
If the user is targeting ASR or AJS, the default recommendation should be **Research-Report** unless there's a strong reason to deviate. At SP/SF, the archetype choice is more open.

### Archetype Can Shift
If you realize during sequencing that a different archetype fits better, you can adjust. But starting with the right archetype prevents rewrites.

---

## Field Identification

Determine whether a field-specific profile applies. Ask the user about their target venue or subfield, then check the `fields/` directory for available profiles.

If a field profile exists for the user's target field, read the corresponding `fields/{field}.md` file. This file contains all field-specific benchmarks, structural patterns, and writing guidance. It will be the single reference for field-specific guidance throughout all remaining phases.

Field profiles are additive — they adjust benchmarks on top of the archetype. Both dimensions apply simultaneously.

## Output

Present the full assessment and recommendation in the conversation. Do not create output files.

---

## When You're Done

Report to the orchestrator:
- Recommended archetype
- Key rationale (2-3 sentences)
- Any outstanding questions
- Readiness assessment for Phase 1

Example summary:
> "I recommend **Archetype 2: Research-Report** for this project. The user is studying how unaccompanied immigrant youth navigate work—a gap-filling contribution that positions within existing literature on immigrant incorporation. The user has 54 interviews and clear findings about institutional context and ethnic networks. Ready for Phase 1: Sequencing."
