# Continuity Checks Reference

A categorized checklist for auditing inter-chapter connections. Each check includes a name, description, diagnostic question, and example. Use this during the continuity audit to ensure systematic coverage.

---

## 1. Bridge-Opening Checks

### 1.1 Demand Creation
**Description:** A bridge should create specific demand for the next chapter -- not just announce it, but make the reader want to turn the page.
**Diagnostic question:** After reading the bridge, can you state what question the next chapter must answer?
**Example:** Patashnik 2008 ends Ch. 3 by noting that tax reform's durability depended on whether new constituencies formed -- creating demand for Ch. 4's analysis of constituency dynamics. The reader arrives at Ch. 4 already knowing what to look for.

### 1.2 Demand Fulfillment
**Description:** The opening of the next chapter should fulfill the demand created by the preceding bridge within the first 2-3 paragraphs.
**Diagnostic question:** Does the opening address the bridge's promise by paragraph 3, or does it start from an unrelated angle?
**Example:** If a bridge asks "But did these reforms survive the next election cycle?" and the opening begins with three paragraphs of general historical context before mentioning elections, the demand is unfulfilled -- the reader's momentum is lost.

### 1.3 Tonal Continuity
**Description:** The bridge and the opening should share a register. A bridge that poses an urgent question should not be followed by an opening in a detached, encyclopedic tone.
**Diagnostic question:** If you read the bridge and the opening aloud in sequence, do they sound like they belong to the same book?
**Example:** A bridge ending with "The question was whether activists could sustain this momentum" followed by an opening that begins "This chapter examines the period 1975-1985" breaks tonal continuity -- the urgency of the bridge is lost in the procedural opening.

### 1.4 Formulaic Bridge Detection
**Description:** Bridges that repeat the same syntactic pattern across every chapter ("The next chapter will examine...") signal mechanical rather than argumentative transitions.
**Diagnostic question:** If you line up all bridges in sequence, do they use the same sentence structure?
**Example:** If five consecutive bridges begin "The next chapter turns to..." the transitions are formulaic. Effective bridges vary: some pose questions, some introduce contradictions, some preview surprising findings. See anti-pattern #11 in `book-editor/techniques/anti-patterns.md`.

### 1.5 Summative vs. Forward-Pointing Bridge
**Description:** A bridge that merely restates the current chapter's findings is a conclusion, not a bridge. Bridges must point forward.
**Diagnostic question:** Does the bridge contain at least one sentence about what comes next, or is it entirely about what was just argued?
**Example:** "This chapter has shown that X, Y, and Z" is summative. "This chapter has shown that X -- but whether X holds under conditions of Y is the question that the next chapter takes up" is forward-pointing. See anti-pattern #9.

---

## 2. Evidence Reuse Checks

### 2.1 Repeated Block Quotes
**Description:** The same direct quotation (from an interview, archival source, or published work) appearing in two or more chapters. Block quotes should live in one chapter.
**Diagnostic question:** Does any quote of 2+ sentences appear verbatim in more than one chapter?
**Example:** An interview quote from a Raleigh activist about neighborhood change appearing in both Ch. 4 (neighborhood dynamics) and Ch. 6 (activist strategies). The quote should be placed where it does the most analytical work; the other chapter can reference it with "As the Raleigh activist quoted in Chapter 4 observed..."

### 2.2 Repeated Vignettes
**Description:** An extended example, anecdote, or narrative sequence retold in multiple chapters. Brief callbacks are acceptable; extended retelling is not.
**Diagnostic question:** Is there an example or story that is told at length (3+ paragraphs) in more than one chapter?
**Example:** A detailed account of a specific protest event appearing in both the context chapter (to establish the political moment) and an empirical chapter (to illustrate a mechanism). The detailed narration should appear once; the other chapter can reference it in 1-2 sentences.

### 2.3 Repeated Data Points
**Description:** The same statistic, finding, or empirical result presented as if new in multiple chapters. Data should be presented in full once and referenced elsewhere.
**Diagnostic question:** Is there a number, percentage, or empirical finding that is introduced with the same level of detail in two chapters?
**Example:** A table showing protest frequency by city appearing in both the quantitative chapter and a case study chapter. Present the table once (typically in the quantitative chapter); reference it in the case study ("As Table 3.2 showed, City X had the highest protest frequency...").

### 2.4 Evidence Assignment
**Description:** Evidence should be placed in the chapter where it does the strongest analytical work, not wherever it first came up during writing.
**Diagnostic question:** For each major piece of evidence, is it in the chapter where it most directly supports an analytical claim?
**Example:** An interview quote about institutional design might appear in a context chapter because it mentions historical events, but it would do more analytical work in the theory chapter where institutional design is the central concept.

---

## 3. Vocabulary Drift Checks

### 3.1 Synonym Substitution
**Description:** Using a common-language synonym for a defined theoretical term. This obscures whether the author is invoking the framework or making a casual observation.
**Diagnostic question:** Does any chapter use a word or phrase to describe a concept that has a different, defined name in the theory chapter?
**Example:** If the theory chapter defines "policy reconfiguration" as a key variable, and Ch. 5 uses "policy change" or "reform outcomes" to refer to the same concept, that is synonym substitution. The reader cannot tell whether "policy change" is the same thing as "policy reconfiguration" or something different.

### 3.2 Ad Hoc Terminology
**Description:** Introducing new analytical terms in empirical chapters that are not defined in the theory chapter and do not map onto any defined concept.
**Diagnostic question:** Does any empirical chapter introduce an analytical term (not a descriptive label) that does not appear in the theory chapter?
**Example:** If Ch. 6 introduces the concept of "institutional stickiness" to explain a finding, but the theory chapter does not define this term, it is ad hoc. Either the term should be added to the theory chapter's framework, or the finding should be expressed using existing framework vocabulary.

### 3.3 Abbreviation Creep
**Description:** Empirical chapters using abbreviations or shorthand for framework terms without first establishing them. The theory chapter may use the full term; later chapters truncate it.
**Diagnostic question:** Are there abbreviated references to framework concepts that would be unclear to a reader who skipped the theory chapter?
**Example:** The theory chapter defines "descriptive representation" and "substantive representation." By Ch. 7, the author writes "DR" and "SR" without redefining them. Readers who start with Ch. 7 (common in academic reading) will be lost.

### 3.4 Concept Splitting
**Description:** A concept defined as unitary in the theory chapter being treated as two or more distinct concepts in empirical chapters without explicit justification.
**Diagnostic question:** Does any empirical chapter subdivide a theoretical concept that the theory chapter treats as one thing?
**Example:** The theory chapter defines "political opportunity" as a single variable. Ch. 4 distinguishes between "institutional opportunity" and "discursive opportunity" without noting that this refines the original framework. This is not necessarily wrong, but it must be flagged and justified.

---

## 4. Arc Coherence Checks

### 4.1 Verdict Overlap
**Description:** Two or more chapter verdicts that state essentially the same finding, differing only in the empirical context.
**Diagnostic question:** If you remove the case-specific details from two verdicts, do they say the same thing?
**Example:** Ch. 4 verdict: "In City A, institutional constraints limited activist influence." Ch. 6 verdict: "In City C, institutional barriers prevented activist impact." These are the same finding with different city names. At least one should be reframed to emphasize a distinct dimension.

### 4.2 Unacknowledged Tension
**Description:** Two chapter verdicts that point in different directions without the author noting or resolving the tension.
**Diagnostic question:** Do any two verdicts, taken together, create a puzzle that the book does not address?
**Example:** Ch. 4 finds that grassroots mobilization was effective; Ch. 6 finds that institutional access (not mobilization) drove outcomes. If the book does not address why mobilization worked in one context and not another, the tension is unacknowledged.

### 4.3 Thesis Convergence Failure
**Description:** The book's stated thesis (in the introduction) is not supported by the aggregate of chapter verdicts.
**Diagnostic question:** If you list all chapter verdicts, do they add up to the thesis? Or do they prove something different?
**Example:** The introduction claims that "movement strategy explains policy outcomes." But the chapter verdicts collectively show that institutional context, not strategy, is the dominant factor. The thesis and the findings have diverged.

### 4.4 Repetitive Mechanism
**Description:** Multiple chapters invoking the same causal mechanism without adding nuance, conditions, or complications.
**Diagnostic question:** Do 3+ chapters attribute outcomes to the same mechanism with no variation in how the mechanism operates?
**Example:** Chapters 4, 5, and 6 all conclude that "elite allies facilitated reform." By the third repetition, the reader needs to know: Under what conditions do elite allies matter more or less? What varies about the alliance across cases?

---

## 5. Theory Callback Checks

### 5.1 Orphaned Dimension
**Description:** A framework dimension (variable, mechanism, category) defined in the theory chapter that is never invoked in any empirical chapter.
**Diagnostic question:** Is there a concept in the theory chapter that no empirical chapter tests, illustrates, or discusses?
**Example:** The theory chapter defines four mechanisms: elite alliance, grassroots pressure, institutional design, and cultural framing. If no empirical chapter discusses cultural framing, that dimension is orphaned. Either add an empirical chapter that tests it, or remove it from the theory chapter.

### 5.2 Framework Disconnect
**Description:** An empirical chapter that makes no reference to the book's theoretical framework — it reads as a standalone essay.
**Diagnostic question:** Could this chapter appear in a different book with no changes to its analytical vocabulary?
**Example:** A case study chapter that describes a policy reform in rich detail but never connects the outcome to the book's defined variables. The chapter tells a story but does not test or illustrate the framework. See anti-pattern #1 in `book-editor/techniques/anti-patterns.md`.

### 5.3 Over-Concentration
**Description:** One framework dimension appearing in every chapter while others appear in only 1-2 chapters.
**Diagnostic question:** Is there a framework dimension that every chapter invokes, and another that appears in fewer than half the empirical chapters?
**Example:** If "institutional design" appears in all eight empirical chapters but "cultural framing" appears in only two, the framework is imbalanced. The book is effectively a book about institutional design, not about the four-dimensional framework it claims to deploy.

### 5.4 Implicit Callback
**Description:** A chapter that engages with a framework dimension without using its name — the connection is there but invisible.
**Diagnostic question:** Does the chapter discuss something that is clearly related to a framework concept but uses different language?
**Example:** The theory chapter defines "political opportunity structure." Ch. 5 discusses "favorable conditions for mobilization" at length — clearly the same concept, but never named as such. Making the callback explicit strengthens the chapter's connection to the book.

---

## 6. Escalating Complexity Checks

### 6.1 Analytical Plateau
**Description:** Two or more consecutive chapters that reach the same type of finding with no added complexity, nuance, or theoretical development.
**Diagnostic question:** After reading chapters N and N+1, does the reader know anything analytically new that they did not know after chapter N alone?
**Example:** Ch. 4 shows the theory works in City A. Ch. 5 shows the theory works in City B. Ch. 6 shows the theory works in City C. If all three reach the same conclusion through the same mechanism with no variation, the reader experiences redundancy after Ch. 4. Each chapter should add something: a new mechanism, a scope condition, a harder test, a surprising finding.

### 6.2 Missing Anomaly
**Description:** A comparative design with no anomalous, negative, or hard case. If every case confirms the theory, the reader suspects cherry-picking.
**Diagnostic question:** Is there at least one chapter where the theory does not work cleanly, and the author engages with the mismatch?
**Example:** In a six-case parallel case design, five cases confirm the theory. The sixth should be the anomaly: a case where the theory predicts X but Y occurred, forcing the author to refine the framework. See the position effects discussion in `book-parallel-case/SKILL.md`.

### 6.3 Declining Ambition
**Description:** Later chapters that are analytically thinner than earlier ones — fewer subsections, less evidence, weaker verdicts.
**Diagnostic question:** Are the later empirical chapters shorter, less detailed, or less analytically developed than the earlier ones?
**Example:** Ch. 4 (first case) has 12,000 words, 8 subsections, and a rich verdict. Ch. 7 (fourth case) has 7,000 words, 4 subsections, and a perfunctory verdict. The declining ambition suggests the author ran out of energy or evidence. Later chapters should be at least as developed as earlier ones.

### 6.4 Sequence Logic
**Description:** The order of empirical chapters should follow a logic — typically from clearest case to most complex, or from foundational to advanced.
**Diagnostic question:** Could the empirical chapters be reordered without any loss of argumentative momentum?
**Example:** If the anomalous case appears second in the sequence and the clearest case appears fifth, the sequence lacks logic. The clearest case should come first (establishing the framework's plausibility), with the anomaly coming last (testing its limits). See `book-architecture/techniques/chapter-sequencing.md`.

---

## 7. Evidence Balance Checks

### 7.1 Case Dominance
**Description:** One or two cases receiving disproportionate attention across the manuscript while others are thinly covered.
**Diagnostic question:** If you count the total words devoted to each case across all chapters, is any case more than twice as prominent as the least-represented case?
**Example:** In a five-city study, New York appears in seven chapters with extended treatment, while Phoenix appears in only two chapters with brief mentions. If the book claims to be a five-city comparison, each city needs proportional representation.

### 7.2 Respondent Type Imbalance
**Description:** One respondent type (e.g., officials, activists, officers) dominating the interview evidence while another type claimed in the methods section is rarely heard.
**Diagnostic question:** Does the methods section claim interviews with types X, Y, and Z, but the manuscript only quotes types X and Y?
**Example:** The methods section reports 40 interviews with police officers, 35 with activists, and 20 with community members. But the manuscript quotes officers 50 times, activists 30 times, and community members 3 times. The community perspective is claimed but absent.

### 7.3 Data Source Imbalance
**Description:** One data type (interview, archival, quantitative) dominating the evidence while others claimed in the methods section are underutilized.
**Diagnostic question:** Does the methods section describe a mixed-methods design, but the empirical chapters rely overwhelmingly on one method?
**Example:** The methods section describes archival research, 60 interviews, and an original survey. But the empirical chapters are 90% interview-based, with archival material confined to the context chapter and the survey mentioned once. The mixed-methods claim is not supported.

### 7.4 Temporal Coverage Gaps
**Description:** Periods of time that are claimed as part of the study but receive minimal empirical attention.
**Diagnostic question:** Does the book claim to cover period X-Y, but some decades or periods within that range receive minimal evidence?
**Example:** A book claiming to cover 1960-2020 devotes four chapters to 1990-2020 and only one chapter to 1960-1990. If the earlier period matters to the argument, it needs proportional treatment.

---

*Use these checks during Phase 2 (Connection Audit), Phase 3 (Arc Audit), and Phase 4 (Balance Audit) of the continuity skill workflow.*
