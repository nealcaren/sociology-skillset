---
name: book-continuity
description: Audit the connections between chapters in an academic monograph — bridge-opening alignment, evidence reuse, vocabulary consistency, argument arc, theory callbacks, escalating complexity, and evidence balance. Produces a structured continuity report with findings and resolution recommendations.
---

# Book Continuity

You help researchers **audit the connections between chapters** in an academic monograph. Given a full or near-complete manuscript, you systematically check whether chapters talk to each other — whether bridges match openings, evidence is reused, framework vocabulary drifts, verdicts accumulate, theory dimensions are covered, complexity escalates, and evidence is distributed proportionally.

## When to Use This Skill

Use this skill when the researcher has:
- A complete or near-complete manuscript (all chapters drafted, even if rough)
- Individual chapter editorial reports (from `book-editor`) that flag cross-chapter issues
- A sense that chapters may not cohere as a book — that they read as standalone essays rather than a cumulative argument

This skill does NOT evaluate individual chapters. It evaluates the *seams* between chapters. For individual chapter diagnostics, use `book-editor`. For book-level architecture decisions (chapter count, sequencing, theory placement), use `book-architecture`.

## What This Skill Does

The continuity auditor performs seven diagnostic passes across the full manuscript, each targeting a different dimension of inter-chapter connection:

| Pass | What It Tests |
|------|--------------|
| 1. Bridge-opening alignment | Does each chapter's bridge match the next chapter's opening? Does the preview create demand that the opening fulfills? |
| 2. Quote and evidence reuse | Do any block quotes, extended vignettes, or data points appear in multiple chapters? |
| 3. Framework vocabulary consistency | Are the book's key theoretical terms used consistently across chapters, or do synonyms and ad hoc terms drift in? |
| 4. Argument arc and verdict coherence | Do chapter verdicts accumulate toward the book's thesis, or do they repeat the same finding or reach incompatible conclusions? |
| 5. Theory callbacks | Does each empirical chapter invoke the framework's variables? Are all dimensions covered across the book, or are some orphaned? |
| 6. Escalating complexity | Does each chapter add something new, or do multiple chapters reach essentially identical findings? |
| 7. Evidence balance across the book | Are cases, cities, respondent types, or data sources distributed proportionally, or do 2-3 dominate while others are thin? |

The output is a **continuity report** with a chapter inventory, pass-by-pass findings, and resolution recommendations.

---

## Workflow

### Phase 1: Inventory

**Goal:** Build a chapter-by-chapter inventory that serves as the raw material for all subsequent passes.

**Implementation:** Dispatch parallel subagents (one per chapter) to build the inventory. Loading the full manuscript into a single context risks exceeding memory and losing detail. Each subagent reads one chapter file and returns its inventory row. The orchestrator collects and assembles the rows into the inventory table.

```
For each chapter file:
  Spawn a subagent (sonnet) with:
    - The chapter file path
    - The master framework term list (from the theory chapter)
    - Instructions to return: chapter type, cluster, word count,
      verdict sentence, bridge sentence, opening sentence,
      framework terms used, cases featured, block quotes
```

Run all chapter agents in parallel using the Agent tool with multiple calls in a single message. Once all agents return, assemble the inventory table.

**For each chapter, record:**

| Field | What to Capture |
|-------|----------------|
| **Chapter number and title** | As labeled in the manuscript |
| **Chapter type** | Introduction, theory, context, parallel case, cross-issue, quant, conclusion |
| **Cluster** | The cluster within the chapter type (from the relevant writing skill) |
| **Word count** | Approximate |
| **Verdict sentence** | The 1-2 sentence finding stated in the chapter's conclusion section |
| **Bridge sentence** | The final forward-pointing sentence(s) of the chapter |
| **Opening sentence** | The first sentence of the next chapter |
| **Key framework terms used** | Which of the book's core theoretical concepts appear in this chapter |
| **Cases/cities/units featured** | Which empirical units receive substantial treatment |
| **Block quotes used** | Notable direct quotations (first few words + source) |

**Output:** A compact inventory table. This table is Part 1 of the final report.

**Tips:**
- If editorial reports exist for individual chapters, extract verdict, bridge, and opening sentences from them rather than re-reading entire chapters.
- The inventory need not be exhaustive for block quotes — focus on extended quotes (3+ sentences) and quotes that carry analytical weight.
- For framework terms, use the theory chapter as the master list. Record which terms from that list appear in each empirical chapter.

---

### Phase 2: Connection Audit (Passes 1-3)

**Goal:** Run the three mechanical checks that can be assessed by comparing adjacent entries in the inventory.

#### Pass 1: Bridge-Opening Alignment

For each chapter transition (Ch. N bridge to Ch. N+1 opening), test:

1. **Does the bridge create demand?** A bridge that says "The next chapter examines X" creates demand for X. A bridge that merely summarizes creates no demand.
2. **Does the opening fulfill that demand?** If the bridge promises X, the opening must deliver X within the first 2-3 paragraphs.
3. **Is there a tonal match?** If the bridge raises a question, the opening should answer or engage it — not start from an unrelated angle.
4. **Is there a gap?** If 500+ words of the opening pass before the bridge's promise is addressed, the connection is broken.

**Severity ratings:**
- **Aligned:** Bridge creates demand, opening fulfills it within 2-3 paragraphs
- **Loose:** Bridge creates demand, but the opening takes 4+ paragraphs to address it
- **Mismatched:** Bridge promises X, opening delivers Y
- **Missing:** No bridge exists, or the bridge is purely summative with no forward reference

#### Pass 2: Quote and Evidence Reuse

Scan the inventory for:

1. **Repeated block quotes:** The same direct quotation appearing in two or more chapters. This is almost always an error — the quote should live in one chapter and be referenced (not repeated) elsewhere.
2. **Repeated vignettes:** The same extended example or anecdote used in multiple chapters. Unlike quotes, a brief callback to a vignette can be effective, but extended retelling signals the vignette has not been assigned a home.
3. **Repeated data points:** The same statistic, table row, or empirical finding presented as if new in multiple chapters. Data can be referenced across chapters, but should be presented in full only once.

**Severity ratings:**
- **Duplicate:** Identical or near-identical passage appears in 2+ chapters
- **Redundant callback:** The same material is re-presented at length when a brief cross-reference would suffice
- **Acceptable reference:** A brief callback (1-2 sentences) to material fully presented elsewhere

#### Pass 3: Framework Vocabulary Consistency

1. **Build the master term list** from the theory chapter (or introduction, if no standalone theory chapter exists). These are the book's defined concepts — the variables, mechanisms, categories, and typological labels.
2. **For each empirical chapter**, check whether it uses the master terms or substitutes synonyms, abbreviations, or ad hoc alternatives.
3. **Flag vocabulary drift:** places where a chapter uses a term not in the master list to refer to a concept that has a defined name.

**Severity ratings:**
- **Consistent:** The chapter uses the master terms throughout
- **Minor drift:** 1-2 instances of synonym substitution; the meaning is clear but the vocabulary is imprecise
- **Significant drift:** The chapter uses a different vocabulary to describe the framework's concepts, making it unclear whether the same constructs are being invoked

---

### Phase 3: Arc Audit (Passes 4-6)

**Goal:** Run the three analytical checks that require judgment about the book's argument as a whole.

#### Pass 4: Argument Arc and Verdict Coherence

1. **List all chapter verdicts** in sequence.
2. **Test for accumulation:** Does each verdict add something new to the book's thesis? The ideal arc is additive — each chapter contributes a distinct piece of the argument that could not be derived from the others.
3. **Test for repetition:** Do two or more verdicts say essentially the same thing in different empirical contexts? Some repetition is expected in parallel case designs (confirming the theory works across cases), but the verdicts should still vary in emphasis, mechanism, or scope.
4. **Test for coherence:** Are any verdicts in tension with each other? Tension is not always a problem — a well-managed anomalous case can strengthen the argument — but unacknowledged tension is a problem.
5. **Test for thesis convergence:** Do the verdicts, taken together, add up to the book's stated thesis? If the thesis claims X and the verdicts collectively demonstrate Y, there is a gap.

**Severity ratings:**
- **Accumulating:** Each verdict adds a distinct contribution; the arc builds
- **Partially repetitive:** 2+ verdicts overlap substantially, though context differs
- **Repetitive:** 3+ verdicts make essentially the same finding
- **Incoherent:** Verdicts contradict each other without acknowledgment
- **Thesis gap:** Verdicts do not add up to the stated thesis

#### Pass 5: Theory Callbacks

1. **List the framework's dimensions** (variables, mechanisms, categories) from the theory chapter.
2. **For each empirical chapter**, record which dimensions are invoked.
3. **Build a coverage matrix:** dimensions as rows, chapters as columns.
4. **Flag orphaned dimensions:** framework elements that are defined in the theory chapter but never tested, illustrated, or invoked in any empirical chapter.
5. **Flag over-concentrated dimensions:** framework elements that appear in every chapter, suggesting the framework may have more dimensions than the empirical chapters actually use.
6. **Flag missing callbacks:** empirical chapters that do not reference the framework at all (anti-pattern #1: the chapter that forgets it is part of a book).

**Severity ratings:**
- **Full coverage:** All framework dimensions are invoked across the empirical chapters
- **Minor gaps:** 1-2 dimensions are underrepresented but not absent
- **Orphaned dimensions:** 1+ dimensions defined in the theory chapter appear in no empirical chapter
- **Framework disconnect:** 1+ empirical chapters make no reference to the framework

#### Pass 6: Escalating Complexity

1. **For each successive empirical chapter**, ask: what does this chapter add that the previous one did not provide?
2. **Possible contributions:** a new case, a new mechanism, a harder test, a scope extension, a contradiction, a refinement, a new evidence type, a temporal extension.
3. **Flag plateaus:** sequences of 2+ chapters that reach the same type of finding with no added complexity.
4. **Check for the designed escalation:** In well-structured books, the sequence moves from easy cases (where the theory clearly works) to hard cases (where the theory is tested). Does this manuscript follow that pattern?

**Severity ratings:**
- **Escalating:** Each chapter adds a distinct contribution or tests the theory more stringently
- **Plateau:** 2+ adjacent chapters reach similar conclusions without added complexity
- **Declining:** Later chapters are less analytically ambitious than earlier ones

---

### Phase 4: Balance Audit (Pass 7)

**Goal:** Count the distribution of empirical material across the manuscript.

#### Pass 7: Evidence Balance Across the Book

1. **Count case/city/unit representation:** How many words, subsections, and block quotes does each empirical unit receive across the full manuscript?
2. **Count respondent type representation:** Are officer voices, activist voices, official voices, and community voices distributed proportionally, or does one type dominate?
3. **Count data source representation:** Are archival, interview, quantitative, and observational data used in proportion to their claimed importance?
4. **Flag imbalances:** Units, respondent types, or data sources that receive less than half the attention of the most-represented category.

**Severity ratings:**
- **Balanced:** No unit, type, or source is underrepresented by more than 30% relative to the most-represented
- **Mildly imbalanced:** One category is underrepresented (30-50% gap)
- **Significantly imbalanced:** One category receives less than half the attention of the dominant category
- **Missing:** A claimed empirical unit, respondent type, or data source is effectively absent from the manuscript

---

### Phase 5: Report

**Goal:** Produce the continuity report and write it to a markdown file named `[manuscript-name]-continuity-report.md`.

---

## The Continuity Report

The report has two parts: **Inventory** (the chapter-by-chapter reference table) and **Findings** (pass-by-pass diagnostics with resolution recommendations).

### Report Template

```markdown
# Continuity Report: [Manuscript Title]

*Generated [date] using book-continuity skill against 22-book corpus norms.*

**Architecture type:** [type] | **Total chapters:** [n] | **Total word count:** [n]
**Theory chapter(s):** [chapter number(s)] | **Framework dimensions:** [n]
**Empirical chapters:** [n] | **Cases/units:** [list]

---

# Part 1: Inventory

## Chapter Inventory

| Ch. | Title | Type | Cluster | Words | Verdict (abbreviated) | Bridge Target | Framework Terms Used | Cases Featured |
|-----|-------|------|---------|-------|----------------------|---------------|---------------------|---------------|
| 1 | [title] | Introduction | [cluster] | [n] | [1-sentence] | [what the bridge promises] | [terms] | [cases] |
| 2 | [title] | [type] | [cluster] | [n] | [1-sentence] | [bridge target] | [terms] | [cases] |
| ... | | | | | | | | |

## Framework Term Master List

| Term | Defined In | Chapters That Use It | Chapters That Omit It |
|------|-----------|---------------------|----------------------|
| [term] | Ch. [n] | Chs. [list] | Chs. [list] |

---

# Part 2: Findings

## Pass 1: Bridge-Opening Alignment

| Transition | Bridge Creates Demand? | Opening Fulfills? | Rating |
|-----------|----------------------|-------------------|--------|
| Ch. 1 → Ch. 2 | [yes/no + what] | [yes/no + how] | [Aligned/Loose/Mismatched/Missing] |
| Ch. 2 → Ch. 3 | ... | ... | ... |

### Findings

[For each Loose, Mismatched, or Missing transition, provide:]

### [Ch. N → Ch. N+1]: [Brief description]

**What:** [What the bridge promises vs. what the opening delivers]
**Why this matters:** [How the mismatch affects the reader's experience]
**How to fix:** [Specific revision instruction]
**Model:** [Corpus exemplar of a well-aligned transition, if applicable]

---

## Pass 2: Quote and Evidence Reuse

| Item | Chapters Where It Appears | Rating |
|------|--------------------------|--------|
| [quote/vignette/data point] | Chs. [list] | [Duplicate/Redundant/Acceptable] |

### Findings

[For each Duplicate or Redundant item:]

### [Item description]

**What:** [The repeated material and where it appears]
**Why this matters:** [How repetition weakens the manuscript]
**How to fix:** [Which chapter should own the material; how the other should reference it]

---

## Pass 3: Framework Vocabulary Consistency

| Chapter | Rating | Drift Instances |
|---------|--------|----------------|
| Ch. [n] | [Consistent/Minor/Significant] | [list of substituted terms] |

### Findings

[For each chapter with Minor or Significant drift:]

### Ch. [N]: [Chapter title]

**What:** [Which master terms are replaced by which substitutes]
**Why this matters:** [How vocabulary drift obscures the framework]
**How to fix:** [Which terms to standardize and where]

---

## Pass 4: Argument Arc and Verdict Coherence

### Verdict Sequence

| Ch. | Verdict (abbreviated) | Contribution to Thesis |
|-----|----------------------|----------------------|
| [n] | [verdict] | [what this adds] |

### Arc Rating: [Accumulating/Partially Repetitive/Repetitive/Incoherent/Thesis Gap]

[Narrative assessment of the argument arc: where it builds, where it plateaus, where it contradicts.]

### Findings

[For each issue:]

### [Issue description]

**What:** [The specific repetition, contradiction, or gap]
**Why this matters:** [How it weakens the book's argument]
**How to fix:** [Revision strategy]

---

## Pass 5: Theory Callbacks

### Coverage Matrix

| Framework Dimension | Ch. 3 | Ch. 4 | Ch. 5 | Ch. 6 | Ch. 7 | ... |
|--------------------|-------|-------|-------|-------|-------|-----|
| [dimension] | [x/ ] | [x/ ] | [x/ ] | [x/ ] | [x/ ] | ... |

### Findings

[For orphaned dimensions, missing callbacks, or over-concentration:]

### [Issue description]

**What:** [Which dimension is orphaned or which chapter lacks callbacks]
**Why this matters:** [How the gap affects the framework's credibility]
**How to fix:** [Where to add callbacks or which dimension to cut from the theory chapter]

---

## Pass 6: Escalating Complexity

### Escalation Sequence

| Ch. | What This Chapter Adds |
|-----|----------------------|
| [n] | [new case / new mechanism / harder test / scope extension / ...] |

### Arc Rating: [Escalating/Plateau/Declining]

[Narrative assessment of the complexity arc.]

### Findings

[For plateaus or declining complexity:]

### [Issue description]

**What:** [Which chapters plateau or decline]
**Why this matters:** [How the reader experiences redundancy]
**How to fix:** [Resequencing, differentiating findings, or adding analytical depth]

---

## Pass 7: Evidence Balance

### Distribution Table

| Case/Unit | Total Words | Chapters Featured | Block Quotes | Rating |
|-----------|------------|-------------------|-------------|--------|
| [unit] | [n] | Chs. [list] | [n] | [Balanced/Mild/Significant/Missing] |

### Findings

[For imbalanced or missing units:]

### [Issue description]

**What:** [Which unit is over- or under-represented]
**Why this matters:** [How imbalance affects the book's comparative claims]
**How to fix:** [Where to add material or redistribute evidence]

---

## Summary of Priorities

| Priority | Finding | Severity | Passes Affected |
|----------|---------|----------|----------------|
| 1 | [most impactful issue] | [rating] | [pass numbers] |
| 2 | [next issue] | [rating] | [pass numbers] |
| ... | | | |

## Reference Skills

| Issue | Consult |
|-------|---------|
| Bridge-opening alignment | `[chapter-type]/techniques/section-recipes.md`, Section 5 (bridges) and Section 1 (openings) |
| Evidence placement | `book-editor/SKILL.md`, Phase 6 (research needs), cross-chapter coordination |
| Framework vocabulary | `book-theory-chapter/SKILL.md`, universal move 1 (define core concepts) |
| Argument arc | `book-architecture/techniques/chapter-sequencing.md` |
| Chapter sequencing | `book-architecture/SKILL.md` |
| Evidence balance | `book-editor/SKILL.md`, Phase 6 (research needs), interview evidence scan |
```

---

## Evaluating Partial Manuscripts

When the researcher provides only some chapters:

- **Opening + closing chapters only (introduction + conclusion):** Run passes 4 (thesis convergence — does the conclusion's synthesis match the introduction's claims?) and 3 (vocabulary consistency between introduction and conclusion). Skip passes 1, 2, 5, 6, 7.

- **A sequence of 2-3 adjacent chapters:** Run passes 1 (bridge-opening for the transitions you have), 2 (quote reuse within the set), and 3 (vocabulary consistency). Note that passes 4-7 require the full manuscript.

- **All empirical chapters but no introduction/conclusion:** Run passes 1-3 and 5-7. Skip pass 4's thesis convergence test (no thesis statement available) but still assess verdict accumulation.

State explicitly which passes are possible given the available text and which require more of the manuscript.

---

## Relationship to Other Skills

| Skill | Relationship |
|-------|-------------|
| `book-editor` | The editor evaluates one chapter at a time. Continuity evaluates the connections between chapters. Run the editor first on individual chapters, then continuity on the full manuscript. |
| `book-architecture` | Architecture prescribes the book-level design (type, sequencing, theory placement). Continuity diagnoses whether the executed manuscript achieves the architectural intent. |
| `book-introduction` / `book-conclusion` | The introduction's roadmap and the conclusion's synthesis are key inputs for pass 4 (argument arc). Bridge-opening alignment (pass 1) draws on the bridge conventions from every chapter-type skill. |
| `book-theory-chapter` | The theory chapter's defined concepts are the master term list for pass 3 (vocabulary consistency) and the dimension list for pass 5 (theory callbacks). |

---

## Typical Workflow Integration

A typical revision workflow uses the skills in this order:

1. **`book-architecture`** -- Design the book's structure
2. **Chapter-type skills** -- Draft each chapter
3. **`book-editor`** -- Evaluate individual chapters, identify research needs
4. **Address research needs** -- Fill gaps identified by the editor
5. **`book-continuity`** -- Audit connections between revised chapters
6. **Final revision** -- Fix continuity issues before submission

The continuity audit is most valuable *after* individual chapters have been revised based on editorial reports, because pre-revision chapters may have structural issues that create false continuity flags.

---

*Technique file: `techniques/continuity-checks.md` -- Detailed checklist and examples for each audit type.*
