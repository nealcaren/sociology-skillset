---
name: book-editor
description: Evaluate an existing academic monograph chapter against genre norms derived from 22 political sociology and American politics books. Diagnoses structural, functional, tonal, and paragraph-level issues with specific revision recommendations.
---

# Book Editor

You help researchers **evaluate existing chapter drafts** against empirically derived genre norms. Given a chapter draft (or excerpt), you identify the relevant chapter type, assess its structure, diagnose problems, and provide specific revision recommendations grounded in corpus evidence.

## File Management

This skill uses git to track progress. Before modifying any output file at a new phase:
1. Stage and commit current state: `git add [files] && git commit -m "book-editor: Phase N complete"`
2. Then proceed with modifications.

Do NOT create version-suffixed copies (e.g., `-v2`, `-final`, `-working`). The git history serves as the version trail.

## When to Use This Skill

Use this skill when the researcher has:
- A drafted chapter (full or partial) they want evaluated
- A sense of which chapter type it is (introduction, conclusion, empirical case, theory, context) -- or wants help identifying the type
- Interest in how the draft compares to published norms in political sociology and American politics monographs

This skill does NOT draft new prose. It evaluates existing prose against the norms established in the eight writing skills derived from a 22-book corpus. For drafting, use the relevant writing skill directly.

## What This Skill Does

The editor performs six diagnostic passes on a chapter draft, each targeting a different level of the text:

| Pass | Level | What It Tests |
|------|-------|--------------|
| 1 | **Chapter type and cluster** | Is the chapter identifiable as a known type? Does it fit a cluster within that type? |
| 2 | **Universal moves** | Are all required moves present? Are any missing or weak? |
| 3 | **Structural benchmarks** | Does the chapter meet quantitative norms for length, subsection count, proportions? |
| 4 | **Paragraph functions** | Can each paragraph be labeled with a named function? Are sequences well-ordered? |
| 5 | **Tone and register** | Is the prose register consistent with genre expectations? Are there tonal mismatches? |
| 6 | **Research needs** | Where does the chapter need new scholarly citations, interview evidence, quantitative data, or cross-chapter coordination? |

The output is a **diagnostic report** with a summary table, pass-by-pass findings, a categorized research needs inventory, and prioritized revision recommendations.

---

## The Reference Skills

This skill draws on all eight writing skills in the suite. Each skill defines chapter types, clusters, universal moves, benchmarks, and paragraph functions.

| Skill | Chapter Type | Key Reference Files |
|-------|-------------|-------------------|
| `book-introduction` | Introduction | SKILL.md, techniques/paragraph-functions.md, techniques/section-recipes.md, techniques/sentence-toolbox.md |
| `book-conclusion` | Conclusion | SKILL.md, techniques/paragraph-functions.md, techniques/section-recipes.md |
| `book-theory-chapter` | Theory/Framework | SKILL.md, techniques/paragraph-functions.md, techniques/section-recipes.md |
| `book-context-chapter` | Historical/Context | SKILL.md, techniques/paragraph-functions.md, techniques/section-recipes.md |
| `book-parallel-case` | Parallel case study | SKILL.md, techniques/paragraph-functions.md, techniques/section-recipes.md |
| `book-cross-issue` | Cross-issue thematic | SKILL.md, techniques/paragraph-functions.md, techniques/section-recipes.md |
| `book-quant-chapter` | Sequential quantitative | SKILL.md, techniques/paragraph-functions.md, techniques/section-recipes.md |
| `book-architecture` | Book-level structure | SKILL.md, techniques/chapter-sequencing.md, techniques/structural-patterns.md |

All skills are in `analysis/output/` relative to the repository root.

---

## Workflow

### Phase 1: Chapter Identification

**Goal:** Determine the chapter type, the cluster within that type, and the chapter's position in the book.

**Step 1: Identify the chapter type.**

Read the draft and ask:

| Question | If Yes |
|----------|--------|
| Does it open the book, establish a puzzle, and preview the argument? | **Introduction** |
| Does it synthesize across the book's cases and project forward? | **Conclusion** |
| Does it develop the book's analytical framework and position it in the literature? | **Theory/Framework** |
| Does it provide historical or institutional context before the empirical chapters? | **Context** |
| Does it go deep into one case within a comparative design? | **Parallel case** |
| Does it examine a theme or mechanism across multiple cases simultaneously? | **Cross-issue thematic** |
| Does it present statistical analyses that build cumulatively? | **Sequential quantitative** |

If the chapter is a hybrid (e.g., mixes cross-issue quantitative analysis with parallel case evidence), identify the **dominant** type and note the hybrid elements.

**Step 2: Identify the cluster.**

Each chapter type has 4-5 clusters. Use the decision tree in the relevant skill's SKILL.md to identify the cluster. The decision trees typically ask about evidence type, framework structure, authorial presence, and template rigidity.

If the draft does not clearly fit any cluster, identify the **closest** cluster and note the deviations. A chapter that fits no cluster may be structurally confused -- this is itself a diagnostic finding.

**Step 3: Identify the position.**

For empirical chapters (parallel case, cross-issue, quantitative), determine:
- Is this the first, middle, last, or anomalous case?
- What comes before and after this chapter in the book?
- Does the opening signal the chapter's position in the comparative architecture?

**Output:** A 2-3 sentence identification statement:
> "This chapter is a **[type]** in the **[cluster]** style, positioned as the **[position]** in the book's comparative architecture. The closest corpus exemplar is **[author, chapter]**."

---

### Phase 2: Universal Moves Audit

**Goal:** Test whether all required moves are present, and assess their strength.

Each chapter type has a set of universal moves (typically 6-8). Read the relevant skill's universal moves table and test each one.

**For each move, assign a rating:**

| Rating | Meaning |
|--------|---------|
| **Present** | The move is clearly executed and effective |
| **Weak** | The move is present but underdeveloped, misplaced, or unclear |
| **Missing** | The move is absent |

**Specific tests by move type:**

#### Claim/Thesis
- Can the reader state the chapter's central argument by the end of the second paragraph (for empirical chapters) or first section (for introductions)?
- Is the claim stated in the book's theoretical language, or in ad hoc terms?
- Test: quote the claim sentence. If you cannot find one, it is missing.

#### Theory Connection
- Does the chapter explicitly name the framework's variables and state what the theory predicts for this case/theme?
- Does it use the framework's own terminology?
- Test: could the reader map this chapter onto the book's framework after reading the theory connection?

#### Evidence Organization
- Are subsections analytically purposeful (arguing something) or merely topical (organizing by time period or subject)?
- Test: read each subsection heading. Does it signal an argument or just a topic?

#### Verdict
- Is the finding stated in 1-2 quotable sentences?
- Does it use the framework's language?
- Does it appear in a labeled conclusion section or equivalent?
- Test: could a reviewer cite this paragraph to summarize the chapter?

#### Calibration
- Does the chapter acknowledge what the evidence does not show?
- Does it address at least one rival explanation?
- Test: would a skeptical reader feel their objection was anticipated?

#### Bridge
- Does the chapter connect to what comes next?
- Is the bridge forward-pointing (creating demand for the next chapter) or merely summative?
- Test: does the reader know where the argument goes from here?

#### Opening Hook (introductions)
- Does the first 500 words establish that something important and non-obvious is happening?
- Does it start with the world, not with theory or literature?

#### Stakes Claim (introductions and conclusions)
- Does the reader know why this matters beyond the academic debate?
- Is the stakes claim earned by the evidence, or asserted without support?

**Output:** A table with each universal move, its rating, and a 1-sentence diagnostic note.

---

### Phase 3: Structural Benchmarks

**Goal:** Compare the chapter's quantitative features against corpus norms.

Measure (or estimate from the draft) the following and compare to the relevant skill's benchmarks:

| Metric | How to Assess | Where to Find Benchmarks |
|--------|--------------|------------------------|
| **Total word count** | Count or estimate | Cluster table in SKILL.md |
| **Subsection count** | Count labeled sections | Cluster table in SKILL.md |
| **Opening length** | Words before the first evidence subsection | Section-recipes.md, Section 1 |
| **Evidence body proportion** | % of chapter devoted to evidence | Section-recipes.md, proportions table |
| **Verdict length** | Words in the conclusion/verdict section | Section-recipes.md, Section 4 |
| **Bridge length** | Words in the bridge/transition | Section-recipes.md, Section 5 |
| **Quote density** | Number of direct quotations | Cluster table in SKILL.md |

**Proportion check:**

The section-recipes file for each chapter type includes a proportions table. For parallel case chapters:

| Section | Target % | Target Words (in a 10,000-word chapter) |
|---------|----------|----------------------------------------|
| Opening | 5-8% | 500-800 |
| Theory connection | 2-5% | 200-500 |
| Evidence body | 65-75% | 6,500-7,500 |
| Verdict | 5-10% | 500-1,000 |
| Bridge | 1-3% | 100-300 |

Flag any section that deviates by more than 50% from the target proportion.

**Output:** A benchmarks comparison table showing the draft's values, the corpus norms, and a pass/flag rating for each metric.

---

### Phase 4: Paragraph Function Diagnosis

**Goal:** Test whether each paragraph is doing identifiable work, and whether the paragraph sequence follows a recognizable pattern.

Each chapter type's `techniques/paragraph-functions.md` defines named functions (e.g., CASE_OPEN, THEORY_CONNECT, EVIDENCE_PRESENT, QUOTE_INTEGRATE, VERDICT_DELIVER). The specific functions vary by chapter type.

**Step 1: Label paragraphs.**

Read through the draft and assign each paragraph a function label. Use the function names from the relevant paragraph-functions.md file.

Focus on:
- The **opening** (first 3-5 paragraphs): do they follow a recognizable cluster sequence?
- The **closing** (last 3-5 paragraphs): do they include VERDICT_DELIVER and CHAPTER_BRIDGE?
- Any **unlabelable paragraphs**: these are doing two things (split them) or nothing (cut them)
- Any **runs of 3+ paragraphs with the same function**: these may need variation or consolidation

**Step 2: Check the sequence.**

Each cluster has a characteristic paragraph sequence (documented in paragraph-functions.md under "Paragraph Sequences by Cluster"). Compare the draft's sequence to the expected pattern.

Common sequence problems:
- THEORY_CONNECT appearing before CASE_OPEN (theory before the world)
- EVIDENCE_PRESENT without interpretive sentences (data dump)
- QUOTE_INTEGRATE without framing (orphaned quotes)
- VERDICT_DELIVER distributed across 5+ paragraphs (no quotable finding)
- CHAPTER_BRIDGE that re-argues instead of pointing forward

**Step 3: Diagnose the evidence body.**

For the middle 60-75% of the chapter:
- Does every EVIDENCE_PRESENT paragraph contain an interpretive sentence?
- Is every quote framed before and interpreted after?
- Do SUBSECTION_BRIDGE paragraphs advance the argument or merely announce topics?
- Are subsection lengths roughly balanced (no 3,000-word section next to a 300-word one)?

**Output:** A paragraph-level diagnostic noting the strongest sequences, the weakest sequences, and specific paragraphs that need revision.

---

### Phase 5: Tone and Register

**Goal:** Assess whether the prose register is consistent with genre expectations.

**Reference:** Invoke `prose-craft` in **book mode** for sentence- and paragraph-level benchmarks. Book prose runs shorter (median 19 words vs. 23 in articles), uses shorter paragraphs (3 vs. 4 sentences), more first person (~14% vs. ~10%), less passive voice (~7% vs. ~11%), and far fewer formal transitions (~2% vs. ~7%).

Academic monographs in political sociology operate in a characteristic register: analytical, confident, and declarative, but not polemical. The specific tone varies by cluster:

| Cluster Type | Expected Register |
|-------------|------------------|
| Analytical (Patashnik) | Formal-analytical. Declarative claims. Evidence-driven. Minimal hedging. No first person. |
| Ethnographic (Brown-Saracino) | First-person observational. Sensory detail. Reflective interpretation. Moderate hedging. |
| Biographical-Vignette (Mucciaroni) | Narrative-analytical. Story-driven openings. Institutional analysis in analytical register. |
| Mechanism-Tracing (Kadivar) | Methodological-analytical. Case-selection language. Mechanism enumeration. Formal throughout. |
| Problem Definer (introductions) | Urgency without polemic. Policy stakes. Accessible analytical prose. |
| Democratic Reckoning (conclusions) | Normative shift. Political urgency. New empirical material. |

**Tonal flags to check:**

| Flag | Description | Example |
|------|-------------|---------|
| **Register break** | A sentence that shifts register unexpectedly | Colloquial phrase in otherwise formal prose |
| **Over-hedging** | Excessive qualification that weakens claims | "It might perhaps be suggested that there could be..." |
| **Under-hedging** | Unsupported certainty about contested claims | "This proves conclusively that..." (in qualitative work) |
| **Journalistic intrusion** | Prose that reads like longform journalism rather than scholarship | Dramatic phrasing, cliffhangers, rhetorical questions used for effect rather than structure |
| **Passive voice overuse** | Hiding agency in analytical claims | "It was found that..." instead of "The analysis shows..." |
| **Verdict inflation** | Claiming more than the evidence supports | A case study claiming to "demonstrate" a universal law |
| **Framework disconnection** | Analytical language that does not match the book's own framework | Using ad hoc terms instead of the framework's defined concepts |

**Output:** A tone assessment noting the overall register, any tonal flags with specific examples, and recommendations for tonal consistency.

---

### Phase 6: Research Needs Diagnosis

**Goal:** Identify where the chapter requires new material — scholarly citations, interview evidence, quantitative data, or cross-chapter coordination — before structural or prose revision can be fully effective.

This pass synthesizes findings from Phases 2–5. Some research needs are flagged during earlier passes (e.g., "engage secondary literature" rated Weak in the universal moves audit); this phase consolidates them and adds needs that emerge from the full-chapter reading.

**Step 1: Scholarly literature scan.**

For each major section, ask:
- Does this section make claims about a scholarly literature without citing it?
- Does the chapter use concepts (e.g., "policy window," "decoupling," "protest cycle") that originate in published scholarship without attribution?
- Are there empirical claims that published work has tested (supporting or contradicting the chapter's findings)?
- Is the citation density appropriate for the chapter type? Context chapters and theory chapters require heavy citation; empirical case chapters require moderate citation; cross-issue chapters vary by template.

Flag sections where the chapter is operating in a "scholarly vacuum" — making claims that intersect with established literatures without engaging them.

**Step 2: Interview evidence scan.**

For each analytical claim, ask:
- Is this claim supported by at least one interview quote or paraphrase?
- Are the supporting quotes drawn from diverse respondent types (officers, officials, activists, community members) or concentrated in one type?
- Are all study cities represented proportionally, or do 2–3 cities dominate the evidence?
- Are there sections where the author's analytical voice asserts a pattern without grounding it in specific respondent testimony?

Flag claims that lack interview support and sections where evidence is drawn from too few cities or respondent types.

**Step 3: Quantitative/empirical evidence scan.**

- Does the chapter reference data (protest counts, adoption rates, killing statistics) without providing the numbers?
- Are there claims about patterns ("most cities," "the majority of officers") that could be quantified from existing data?
- Does the chapter reference tables or figures that are placeholders?
- Are published empirical findings cited with enough specificity (sample size, effect size, caveats) for the reader to evaluate them?

**Step 4: Cross-chapter coordination scan.**

- Does the chapter reuse block quotes or extended vignettes that appear in adjacent chapters?
- Does the chapter make claims that contradict or are in tension with claims in other chapters?
- Is evidence placed in the chapter where it has the strongest analytical fit, or could it serve another chapter better?

**Output:** A categorized list of research needs, organized by type (scholarly, interview, quantitative, cross-chapter), with specific locations and search guidance for each.

---

## The Diagnostic Report

After completing all five passes, produce a structured diagnostic report and **write it to a markdown file** in the same directory as the chapter draft, named `[chapter-filename]-editorial-report.md`.

The report has two sections: **Analysis** (what the diagnostic found) and **Action** (what to do about it). The Analysis section presents findings without recommendations. The Action section translates findings into specific, prioritized revision tasks.

### Report Structure

```markdown
# Editorial Report: [Chapter Title]

*Generated [date] using book-editor skill against 22-book corpus norms.*

**Chapter type:** [type] | **Cluster:** [cluster] | **Position:** [position]
**Closest corpus exemplar:** [author, chapter]
**Word count:** [n] | **Sections:** [n] | **Quote density:** [n]

---

# Part 1: Analysis

## Summary

| Dimension | Rating | Key Finding |
|-----------|--------|------------|
| Universal moves | [Strong/Mixed/Weak] | [1-sentence summary] |
| Structural benchmarks | [Within norms/Flagged] | [1-sentence summary] |
| Paragraph functions | [Well-sequenced/Issues] | [1-sentence summary] |
| Tone and register | [Consistent/Flagged] | [1-sentence summary] |

## Universal Moves

| Move | Rating | Note |
|------|--------|------|
| [move] | [Present/Weak/Missing] | [diagnostic] |

## Structural Benchmarks

| Metric | Draft | Corpus Norm | Rating |
|--------|-------|-------------|--------|
| [metric] | [value] | [range] | [Pass/Flag] |

### Section Proportions

| Section | Words | % of Chapter | Assessment |
|---------|-------|-------------|------------|
| [section] | [n] | [n%] | [Pass/Flag/Note] |

## Paragraph Functions

[Sequence analysis organized by chapter section. For each major section:
- What paragraph functions appear and in what order
- Strongest sequences (and why)
- Weakest sequences (and why)
- Any unlabelable paragraphs or runs of 3+ same-function paragraphs]

## Tone and Register

[Overall register assessment, then specific flags as a table:]

| Flag | Location | Example | Severity |
|------|----------|---------|----------|
| [flag type] | [section name] | [quoted text] | [Minor/Moderate/Significant] |

## Anti-Pattern Check

| Anti-Pattern | Applies? | Note |
|-------------|----------|------|
| [pattern name] | [Yes/No/Partially] | [1-sentence explanation] |

---

# Part 2: Action

## Research Needs

Identify specific locations in the chapter where new research is required before revision can proceed. Distinguish the *type* of research needed. Not every chapter will have needs in every category; include only categories that apply.

### Scholarly Literature

Where the chapter needs engagement with published scholarship that is currently absent. For each need, specify:
- **Location:** Which section or paragraph
- **Gap:** What literature is missing (name the field, debate, or specific strand)
- **Purpose:** What the citation would do (ground a claim, establish a foil, document a method, provide a counterfactual)
- **Candidates:** Suggest 2–3 specific authors or works if known from the corpus or field knowledge; otherwise describe what to search for

Example: "The Descriptive Surprise section challenges movement-consequences models without citing them. Engage Amenta (2010) on political mediation, Andrews (2001) on local protest effects, or Giugni (1998) on policy outcomes. Purpose: establish what the chapter's finding contradicts."

### Interview / Qualitative Evidence

Where the chapter needs additional interview material — either quotes not yet integrated from the existing dataset, or evidence from respondent types currently underrepresented. For each need, specify:
- **Location:** Which section or analytical claim lacks evidentiary support
- **Gap:** What perspective or city is missing (e.g., "no activist voice in this section," "Detroit appears only once in the chapter")
- **Type:** Whether this requires (a) searching existing transcripts for relevant passages, (b) identifying a respondent type whose perspective is absent, or (c) noting that a claim is made without any interview support
- **Search guidance:** Suggest search terms, respondent categories, or city cases that would fill the gap

### Quantitative / Empirical Evidence

Where the chapter makes claims that need data support, or where existing data presentations are incomplete. For each need, specify:
- **Location:** Which claim or section
- **Gap:** What data is missing (a statistic, a table, a figure, a comparison)
- **Type:** Whether this requires (a) new analysis of existing data, (b) sourcing a published finding, or (c) building a table or figure from evidence already in the chapter
- **Specificity:** What the analysis should show and what data sources might support it

### Cross-Chapter Evidence

Where evidence from other chapters could strengthen this chapter, or where this chapter's evidence should be checked against other chapters for duplication or inconsistency. For each need, specify:
- **Location:** Which section
- **Issue:** Reused quote, contradictory claim, or evidence that would be better placed elsewhere
- **Resolution:** Which chapter should own the evidence and how the other should reference it

## Priority Revisions

Numbered list of specific revision tasks, ordered by impact. Each item includes:
- **What to change** (specific section, paragraph, or structural element)
- **Why** (which diagnostic finding motivates this)
- **How** (concrete revision instruction, not vague advice)
- **Corpus model** (which published chapter demonstrates the target pattern, if applicable)

Format:

### 1. [Imperative verb phrase, e.g., "Define the protest window concept formally"]

**What:** [Specific location and element to revise]
**Why:** [Which finding — e.g., "Universal move 4 (establish key variable) rated Weak"]
**How:** [Concrete instruction — e.g., "Add a 150-word paragraph after the opening
that defines the concept's components: what opens the window, what properties it has,
what closes it. Use the same definitional structure as Patashnik's 'policy
reconfiguration' concept in Reforms at Risk Ch. 2."]
**Model:** [Corpus exemplar, if applicable]

### 2. [Next revision]
...

## Section-Specific Notes

[For each section of the chapter, 1-3 sentences of targeted advice.
Only include sections that need attention — skip sections that pass all checks.]

## Reference Skills

| Issue | Consult |
|-------|---------|
| [issue from the diagnostics] | [specific skill file path] |
```

---

### Revision Priority Framework

When producing recommendations, use this priority order:

1. **Missing universal moves** -- a chapter without a verdict or without a theory connection is structurally incomplete. Fix these first.
2. **Verdict clarity** -- if the verdict is not quotable in 1-2 sentences, the chapter fails its comparative function. This is the single most important paragraph.
3. **Claim-verdict alignment** -- the claim announced in the opening must be the claim the verdict delivers. Misalignment means the chapter argues one thing and concludes another.
4. **Opening effectiveness** -- the first page must establish the case and its stakes. A buried or slow opening loses the reader.
5. **Section proportions** -- a bridge that is 500 words when the norm is 50-300, or a recap that is 40% of the chapter, signals structural imbalance.
6. **Theory connection** -- if the reader cannot see how this chapter relates to the framework, it is a standalone essay, not a book chapter.
7. **Paragraph-level issues** -- orphaned quotes, data dumps, unlabelable paragraphs. These matter but are lower priority than structural issues.
8. **Tonal consistency** -- register breaks, journalistic intrusions, over-hedging. Polish last.

---

## Evaluating Partial Chapters

When the user provides only part of a chapter (e.g., opening and bridge but not the evidence body), adjust the diagnostic:

- **Opening only:** Run the universal moves audit for moves that should appear in the opening (claim announcement, theory connection, position signal). Run paragraph function diagnosis on the available paragraphs. Assess tone. Skip structural benchmarks that require the full chapter.

- **Opening + bridge/closing:** Assess claim-verdict alignment (does the opening's claim match the closing's verdict?). Check bridge length and content against norms. Test for new evidence in the bridge (an anti-pattern). Assess whether the bridge is forward-pointing or merely summative.

- **Evidence body excerpt:** Label paragraph functions. Check for interpretive sentences in evidence paragraphs. Assess quote integration. Check subsection purpose (argumentative vs. topical headings).

State explicitly which passes are possible given the available text and which require more of the chapter.

---

## Evaluating Chapters Outside the Corpus Genre

The benchmarks and clusters derive from 22 political sociology and American politics monographs. If the chapter under review comes from a different field or genre:

- **Adjacent fields** (historical sociology, comparative politics, public policy): The structural norms (universal moves, section proportions, paragraph functions) transfer well. Tonal norms may differ -- flag this and note where field conventions diverge.

- **Distant fields** (natural sciences, humanities, professional fields): The universal moves framework is still useful as a diagnostic, but specific benchmarks (word counts, quote density, subsection counts) should be treated as suggestive rather than normative. State this caveat in the report.

- **Non-academic books** (trade press, general audience): The skill's norms do not apply. Decline the evaluation or limit it to structural observations.

---

## Cross-Reference to Writing Skills

After producing the diagnostic, point the user to the specific writing skill and technique files that address their chapter's weaknesses:

| If the Issue Is... | Consult |
|--------------------|---------|
| Weak or missing opening | `[chapter-type]/techniques/section-recipes.md`, Section 1 |
| Missing theory connection | `[chapter-type]/techniques/section-recipes.md`, Section 2 |
| Evidence organization | `[chapter-type]/techniques/section-recipes.md`, Section 3 |
| Weak verdict | `[chapter-type]/techniques/section-recipes.md`, Section 4 |
| Bridge problems | `[chapter-type]/techniques/section-recipes.md`, Section 5 |
| Paragraph-level issues | `[chapter-type]/techniques/paragraph-functions.md` |
| Sentence-level craft | `book-introduction/techniques/sentence-toolbox.md` (introduction only) |
| Chapter sequencing | `book-architecture/techniques/chapter-sequencing.md` |
| Book-level structure | `book-architecture/SKILL.md` |
