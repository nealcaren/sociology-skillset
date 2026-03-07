---
name: book-quant-chapter
description: Write sequential quantitative evidence chapters for academic monographs -- chapters that present statistical analyses building one layer of a cumulative argument. Guides cluster selection, structural planning, and drafting based on genre analysis of quantitative chapters across Grumbach, Tesler, Bolton & Thrower, Kadivar, and related books.
---

# Sequential Quantitative Evidence Chapter

You help researchers write **sequential quantitative evidence chapters for academic monographs** -- the empirical chapters where a statistical analysis of a large-N dataset makes a specific claim that contributes one step in a cumulative argument. Given the book's theoretical framework, the chapter's position in the cumulative sequence, and the available data and results, you guide users through selecting a chapter cluster, structuring the chapter, and drafting publication-ready prose.

## File Management

This skill uses git to track progress. Before modifying any output file at a new phase:
1. Stage and commit current state: `git add [files] && git commit -m "book-quant-chapter: Phase N complete"`
2. Then proceed with modifications.

Do NOT create version-suffixed copies (e.g., `-v2`, `-final`, `-working`). The git history serves as the version trail.

## When to Use This Skill

Use this skill when the researcher has:
- A defined theoretical framework (the book's argument is established, typically in an introduction or theory chapter)
- Statistical results to present (regression output, experimental results, descriptive patterns from a dataset)
- Knowledge of where this chapter sits in the book's cumulative sequence (first quantitative chapter, middle extension, payoff chapter, causal explanation)
- Prior chapters whose findings this chapter builds on, and subsequent chapters whose questions this chapter sets up

This skill assumes the data analysis is complete. The task is presenting one analytical layer within a cumulative architecture -- bridging from prior findings, stating the research question, presenting results, interpreting them for the book's argument, and bridging forward.

## Overview: What a Sequential Quantitative Evidence Chapter Does

A sequential quantitative evidence chapter is not a standalone empirical article. It is one layer in a cumulative argument. Its purpose is to show what one statistical analysis contributes to the book's building case. The chapter must simultaneously:

- **Bridge from prior chapters** -- explicitly connect to the findings already established and state what question remains
- **State the research question** -- identify the specific empirical claim this chapter will adjudicate
- **Present data and methods** -- describe the dataset, measures, and analytical approach with enough detail for credibility but not so much that the reader loses the argument
- **Present results** -- walk the reader through tables and figures, converting statistical output into substantive claims
- **Interpret for the argument** -- state what the results mean for the book's cumulative case, not just what they show statistically
- **Address alternatives** -- acknowledge rival explanations and demonstrate robustness
- **Deliver a verdict** -- state the chapter's main finding in quotable form
- **Bridge forward** -- set up the next chapter's question

Target length: **9,000--15,000 words** (corpus range: 8,000--18,000). Chapters that must introduce new measurement strategies or extensive historical context tend to be longest.

---

## The Eight Universal Moves

Every sequential quantitative evidence chapter, regardless of cluster, executes these eight moves. They are non-negotiable. Their order and emphasis vary by cluster, but omitting any one produces a structurally incomplete chapter.

| # | Move | Function | Diagnostic Question |
|---|------|----------|-------------------|
| 1 | **Prior-chapter bridge** | Connect to the cumulative argument so far | Does the reader know what has been established and what question remains? |
| 2 | **Research question** | State the specific empirical question this chapter addresses | Can the reader identify the chapter's central question by the end of the second paragraph? |
| 3 | **Data and methods** | Establish the evidentiary basis | Does the reader know what data, what measures, and what analytical approach will be used? |
| 4 | **Results presentation** | Walk the reader through tables and figures | Can the reader follow the results without needing to read the tables independently? |
| 5 | **Interpretation** | State what the results mean for the book's argument | Does the reader know what the findings contribute to the cumulative case? |
| 6 | **Robustness and alternatives** | Demonstrate that the finding is not an artifact | Has the author addressed the most obvious rival explanations? |
| 7 | **Verdict** | State the chapter's main finding | Can the reader quote the finding in 1--2 sentences? |
| 8 | **Forward bridge** | Set up the next chapter | Does the reader know where the argument goes from here? |

No quantitative chapter in the corpus opens with a literature review. No quantitative chapter opens with a methods section. The empirical puzzle, research question, or illustrative case comes first.

---

## The Four Chapter Clusters

### Cluster 1: The Domain Extender

**Defining logic:** Apply the same model or analytical framework to a new domain, outcome, or level of analysis. The chapter's task is to show that the theory generalizes beyond the domain where it was first demonstrated. The cumulative logic is: "the prior chapter showed X in domain A; this chapter shows X also holds in domain B."

**Exemplars:** Tesler (2016), Chapters 3--6; Grumbach (2023), Chapters 3--4

**Signature features:**
- Opens by naming the new domain and explaining why it matters for the argument's generalizability
- Prior-chapter bridge is brief and efficient -- one or two sentences establishing what has been shown
- The same core independent variable (racial resentment in Tesler; party control in Grumbach) is tested in a new context
- Results are presented comparatively: "in the pre-Obama era, the effect was X; in the Obama era, it was Y"
- Verdict states the extension: "racialization was not limited to presidential evaluations; it extended to evaluations of public figures"
- Forward bridge announces the next domain extension

**Structural sequence:**
1. Illustrative anecdote or case introducing the new domain (300--800 words)
2. Prior-chapter bridge + research question (200--500 words)
3. Data and methods for this domain (500--1,500 words)
4. Main results, typically 2--4 tables/figures (2,000--4,000 words)
5. Robustness / alternative explanations (500--1,500 words)
6. Verdict (200--500 words)
7. Forward bridge to next domain (200--500 words)

| Benchmark | Target |
|-----------|--------|
| Word count | 10,000--14,000 |
| Tables | 2--3 |
| Figures | 4--8 |
| Results-to-prose ratio | 40--50% of chapter devoted to results and interpretation |
| Opening type | Domain-specific anecdote or illustrative case |
| Verdict style | Extension claim ("not limited to... also extends to...") |
| Bridge style | Explicit naming of next domain |

**When to use:** The book's argument works by showing that a single mechanism operates across multiple domains. Each chapter applies the same analytical template to a different outcome or context. The contribution is scope -- the theory is more general than prior work recognized.

---

### Cluster 2: The Foundation Layer

**Defining logic:** Establish the statistical landscape before case studies or mechanism-tracing chapters. The chapter maps a broad empirical pattern that the rest of the book will explain. The cumulative logic is: "here is the pattern; subsequent chapters will show why it exists."

**Exemplars:** Kadivar (2022), Chapter 2; Patashnik (2023), Chapter 2; Grumbach (2023), Chapter 3

**Signature features:**
- Opens with contrasting cases that illustrate the variation to be explained, then pivots to: "but what about the full universe of cases?"
- More extensive data and methods section than other clusters, because this chapter introduces the dataset the book will rely on
- Descriptive results precede inferential results -- the reader sees the pattern before seeing the regression output
- Results are presented with specific quantitative translations: "a democracy with six years of mobilization has a 71 percent lower failure risk"
- Verdict confirms the broad pattern and states the mechanism question: "the findings confirm a robust association, but what are the mechanisms?"
- Forward bridge is methodological: "statistical analysis discovers regularities; qualitative methods identify mechanisms"

**Structural sequence:**
1. Contrasting cases or empirical puzzle introducing the variation (500--1,000 words)
2. Research question: does the pattern hold across the full universe? (200--500 words)
3. Data: universe of cases, measures, coding decisions (1,000--2,000 words)
4. Methods: analytical approach (500--1,000 words)
5. Descriptive results: tables and figures showing the pattern (1,000--2,000 words)
6. Inferential results: regression output with controls (1,500--3,000 words)
7. Robustness and alternative explanations (500--1,500 words)
8. Verdict (300--500 words)
9. Forward bridge to qualitative/mechanism-tracing chapters (300--500 words)

| Benchmark | Target |
|-----------|--------|
| Word count | 9,000--12,000 |
| Tables | 4--6 (including descriptive tables and regression tables) |
| Figures | 2--4 |
| Results-to-prose ratio | 35--45% |
| Opening type | Contrasting cases or empirical puzzle |
| Verdict style | Pattern confirmed + mechanism question stated |
| Bridge style | Methodological pivot ("statistical analysis shows the pattern; the next chapters explain why") |

**When to use:** The book is mixed-methods. This chapter provides the quantitative foundation that case studies or process-tracing chapters will build on. The contribution is the broad statistical pattern; the mechanism is left for later chapters.

---

### Cluster 3: The Mechanism Test

**Defining logic:** Test the specific causal mechanism proposed by the theory. This chapter goes beyond establishing a pattern to showing how the mechanism operates -- through mediation analysis, interaction effects, or organizational-level evidence. The cumulative logic is: "prior chapters showed the pattern exists; this chapter shows why."

**Exemplars:** Grumbach (2023), Chapter 5; Bolton & Thrower (2022), Chapters 4--6; Tesler (2016), Chapter 5

**Signature features:**
- Opens by restating the pattern from prior chapters, then pivoting to the mechanism question: "If not ordinary voters, who might be driving state policy resurgence?"
- Introduces a new variable or a new operationalization that captures the mechanism (interest group activists in Grumbach; congressional capacity in Bolton & Thrower)
- Results presented as interaction effects or mediation paths, not just main effects
- Substantial space devoted to defining and measuring the mechanism variable
- Robustness checks are particularly elaborate because mechanism claims are harder to establish than association claims
- Verdict names the mechanism explicitly

**Structural sequence:**
1. Prior-chapter bridge restating the pattern + mechanism question (300--800 words)
2. Theoretical derivation of the mechanism and its predictions (500--1,500 words)
3. Data: new variable or dataset that captures the mechanism (500--1,500 words)
4. Methods: interaction models, mediation, or organizational analysis (300--800 words)
5. Main results with interpretation (2,000--4,000 words)
6. Robustness and alternative mechanisms (1,000--2,000 words)
7. Verdict naming the mechanism (300--500 words)
8. Forward bridge (300--500 words)

| Benchmark | Target |
|-----------|--------|
| Word count | 12,000--16,000 |
| Tables | 2--5 |
| Figures | 3--6 |
| Results-to-prose ratio | 35--45% |
| Opening type | Prior-finding restatement + mechanism question |
| Verdict style | Mechanism named ("interest group activists are the primary drivers"; "capacity is the binding constraint") |
| Bridge style | What the mechanism implies for the next analytical step |

**When to use:** The book has already established a statistical pattern and now needs to explain it. The chapter introduces the causal mechanism -- a mediating variable, an organizational process, or an interaction effect -- that accounts for the pattern.

---

### Cluster 4: The Payoff Chapter

**Defining logic:** The chapter where the book's core finding lands. All prior chapters have been building toward this moment: the demonstration that the mechanism identified in earlier chapters produces the outcome the book is ultimately about. In Grumbach, this is democratic backsliding. In Tesler, this is the grand synthesis of the white/nonwhite divide. The cumulative logic is: "everything we have shown leads to this."

**Exemplars:** Grumbach (2023), Chapters 7--8; Tesler (2016), Chapter 7; Bolton & Thrower (2022), Chapter 6

**Signature features:**
- Opens with a bridge that summarizes the cumulative argument so far: "The evidence in previous chapters raises the possibility that..."
- Introduces the book's most consequential dependent variable (the State Democracy Index in Grumbach; the white/nonwhite political divide in Tesler)
- May introduce new measurement (Grumbach constructs the SDI using 61 indicators and Bayesian IRT)
- Results presented with explicit normative or substantive weight: "the magnitude of democratic contraction from Republican control is surprisingly large, over one-half of a standard deviation"
- Verdict is the book's thesis restated as an empirical conclusion
- Forward bridge connects to the conclusion chapter or to explanatory follow-up

**Structural sequence:**
1. Cumulative bridge: "previous chapters have shown X, Y, and Z" (500--1,000 words)
2. The stakes: why this particular outcome matters (300--800 words)
3. New measurement or data introduction, if applicable (500--2,000 words)
4. Main results (2,000--4,000 words)
5. Robustness and alternative explanations (1,000--2,000 words)
6. Verdict -- the book's central finding stated as empirical conclusion (300--800 words)
7. Forward bridge to conclusion or explanatory chapter (300--500 words)

| Benchmark | Target |
|-----------|--------|
| Word count | 10,000--15,000 (may span two chapters as in Grumbach 7+8) |
| Tables | 2--4 |
| Figures | 3--5 |
| Results-to-prose ratio | 35--40% |
| Opening type | Cumulative summary bridge |
| Verdict style | Book thesis as empirical conclusion ("the results point to the Republican Party as the antidemocracy coalition") |
| Bridge style | Connection to conclusion or causal explanation |

**When to use:** This is the chapter the reader has been waiting for. All prior quantitative chapters were building toward this moment. The chapter presents the book's most consequential finding -- the one that will appear in reviews, syllabi, and citations.

---

## Cluster Summary Table

| Cluster | Opening | Prior Bridge | Results Style | Verdict Style | Words |
|---------|---------|--------------|---------------|---------------|-------|
| Domain Extender | Domain-specific anecdote | Brief, efficient | Comparative (old vs. new domain) | Extension claim | 10,000--14,000 |
| Foundation Layer | Contrasting cases | Theoretical, from intro/theory chapter | Descriptive then inferential | Pattern + mechanism question | 9,000--12,000 |
| Mechanism Test | Prior finding + mechanism question | Restates established pattern | Interaction/mediation | Mechanism named | 12,000--16,000 |
| Payoff Chapter | Cumulative summary | Full summary of all prior findings | Consequential DV with normative weight | Book thesis as empirical conclusion | 10,000--15,000 |

---

## How Position Affects Structure

### First Quantitative Chapter

- Establishes the empirical baseline -- the fact of the pattern the book will explain
- Must carry more theoretical framing than subsequent chapters, because the reader is entering the quantitative evidence for the first time
- Data and methods section is longest here, because the dataset is being introduced
- Forward bridge must be especially clear, because the reader needs to understand the cumulative architecture
- **Grumbach Ch. 3:** establishes the fact of state policy resurgence and its partisan character
- **Kadivar Ch. 2:** establishes the cross-national association between mobilization duration and democratic survival
- **Tesler Ch. 2:** establishes that racial attitudes structured the 2008 and 2012 elections

### Middle Extension Chapters

- Each adds one analytical layer to the cumulative case
- Prior-chapter bridge is brief: "As I showed in the last chapter..." followed by the new question
- Data and methods are shorter if the dataset is the same; longer if a new dataset or measure is introduced
- Forward bridge points to the next extension or to the payoff
- **Tesler Chs. 3--6:** each extends racialization spillover to a new domain (public figures, policies, Congress, party ID)
- **Grumbach Chs. 4--6:** each adds a layer (voter responsiveness, activist mechanism, policy learning test)
- **Bolton & Thrower Chs. 4--5:** each tests a different dimension of capacity (discretion, oversight)

### The Payoff Chapter

- Where the core finding lands -- the dependent variable the reader cares about most
- Opens with a bridge that recapitulates the full cumulative argument
- May introduce new measurement to capture the consequential outcome
- Verdict carries normative weight and connects to the book's title or central metaphor
- **Grumbach Chs. 7--8:** democratic backsliding measured and explained
- **Tesler Ch. 7:** the grand synthesis -- "America was not post-racial. It was most-racial."
- **Bolton & Thrower Ch. 6:** the test of whether capacity moderates presidential unilateral action

### Final Quantitative Chapter (Before Conclusion)

- May be the payoff chapter (above) or a causal explanation chapter
- Closes the quantitative argument; the conclusion chapter will synthesize
- Forward bridge connects to the book's normative or policy implications
- **Grumbach Ch. 8:** explains the asymmetric pattern of backsliding
- **Tesler Ch. 7:** delivers the book's title claim as empirical conclusion

---

## How to Present Results

### The Table-Then-Discussion Pattern

The dominant pattern across all four books: present a table or figure, then devote one or more paragraphs to interpreting it. The interpretation paragraph performs three functions:

1. **State what the reader should see** -- name the key coefficient, trend, or comparison
2. **Translate into substantive terms** -- convert the statistical output into language a non-specialist can grasp
3. **Connect to the argument** -- state what this means for the cumulative case

Grumbach on the effect of IGA donors:
> "The results show that as the share of IGA fundraising for Republican candidates in a state grows, the Republicans in the state legislature become more conservative. The effect is larger than those of the legislator level analysis shown earlier and is massive in substantive terms: a one standard deviation increase in the percent of money that comes from IGA donors makes the state's average Republican legislator 0.33 standard deviations more conservative in office."

Kadivar on the effect of mobilization duration:
> "Keeping other variables at their observed values, the relative possibility of breakdown for a democracy with one year of unarmed mobilization is 18 percent less than a democracy that emerged without unarmed mobilization. A democracy that originated with three years of unarmed mobilization has a relative likelihood of failure that is 34 percent less than a democracy with one year..."

### Figures Before Tables

Three of four books lead with figures before tables. The typical sequence:
1. Time-series or descriptive figure showing the broad pattern
2. Regression table with formal results
3. Coefficient plot or marginal effects plot translating the regression into visual form

Kadivar is the partial exception: descriptive tables (survival rates by mobilization duration) precede the regression output, functioning as an accessible preview of the main finding.

### When to Use Figures vs. Tables

- **Figures** for trends over time, comparisons across groups, and marginal effects -- anything where the visual pattern IS the argument
- **Tables** for full regression output where the reader needs to see control variables, multiple specifications, and standard errors
- **Coefficient plots** when presenting interaction effects or comparing effect sizes across specifications

---

## Cluster Decision Tree

### Question 1: What is this chapter's role in the cumulative sequence?

- **Extending the theory to a new domain** --> likely **Domain Extender**
- **Establishing the broad statistical pattern** before qualitative chapters --> likely **Foundation Layer**
- **Testing the specific causal mechanism** --> likely **Mechanism Test**
- **Delivering the book's most consequential finding** --> likely **Payoff Chapter**

### Question 2: Is this the first, middle, or culminating quantitative chapter?

- **First** --> likely **Foundation Layer** (if followed by case studies) or **Domain Extender** (if followed by more quantitative chapters extending to new domains)
- **Middle** --> likely **Domain Extender** or **Mechanism Test**
- **Culminating** --> likely **Payoff Chapter**

### Question 3: Does this chapter introduce a new mechanism variable or test an interaction?

- **Yes, a new mediating or moderating variable** --> **Mechanism Test**
- **No, same IV applied to a new DV** --> **Domain Extender**
- **No, same IV but the DV is the book's most consequential outcome** --> **Payoff Chapter**

### Question 4: What follows this chapter?

- **More quantitative chapters** --> **Domain Extender** or **Mechanism Test**
- **Qualitative case studies or process tracing** --> **Foundation Layer**
- **The conclusion** --> **Payoff Chapter**

### Confirming selection:

If answers point to different clusters, prioritize **the chapter's role in the cumulative sequence** (Question 1). A chapter that tests a mechanism but is also the first quantitative chapter should use the Mechanism Test template with an expanded data/methods section borrowed from the Foundation Layer. Name the primary cluster and any borrowed elements before drafting.

---

## Technique Guides

For paragraph-level and section-level drafting guidance, consult:

| Guide | What It Covers |
|-------|---------------|
| `techniques/paragraph-functions.md` | 11 named paragraph functions (BRIDGE_FROM_PRIOR, QUESTION_STATE, DATA_INTRODUCE, TABLE_SETUP, TABLE_INTERPRET, FIGURE_NARRATE, MECHANISM_CLAIM, ROBUSTNESS_TRANSITION, ALTERNATIVE_ADDRESS, VERDICT_STATE, BRIDGE_FORWARD) with internal structure and real verbatim examples |
| `techniques/section-recipes.md` | Section-by-section drafting recipes for the Opening, Data and Methods, Main Results, Robustness, and Verdict sections, with real examples showing how published authors wrote each section; plus cluster-specific variations |

Read these guides before drafting begins.

---

## Workflow

### Phase 1: Cluster Selection and Structural Planning

**Goal:** Determine the chapter's cluster, position, and section architecture before any drafting begins.

**Steps:**
1. Read the book's theoretical framework, the prior chapter(s), and the statistical results to be presented
2. Determine the chapter's position: first quantitative chapter, middle extension, mechanism test, or payoff
3. Walk through the decision tree to select a cluster
4. Identify any elements borrowed from adjacent clusters (e.g., a Mechanism Test that borrows the contrasting-cases opening from the Foundation Layer)
5. Map the section structure with approximate word counts per section
6. Determine:
   - Opening type (anecdote, contrasting cases, cumulative bridge, prior-finding restatement)
   - Data/methods length (brief if same dataset as prior chapter; long if new dataset or measure)
   - Results presentation order (figures first or tables first? descriptive then inferential?)
   - Verdict style (extension claim, pattern + question, mechanism named, thesis as conclusion)
   - Bridge type (next domain, methodological pivot, next analytical layer, conclusion connection)

**Pause:** Confirm cluster selection and structural plan before drafting.

---

### Phase 2: Drafting

**Goal:** Draft each section following the selected cluster's sequence, applying word count targets.

**Steps:**
1. Read `techniques/section-recipes.md` for the recipe matching your cluster. Read `techniques/paragraph-functions.md` for paragraph-level moves.
2. Draft the opening. The first two paragraphs must establish the prior-chapter bridge and the research question. Use the opening type prescribed by your cluster.
3. Draft the data and methods section. It must name the dataset, the key variables, and the analytical approach. Length depends on whether the dataset is new to this chapter.
4. Draft each results section. For each table or figure:
   - Write a TABLE_SETUP paragraph before presenting the result
   - Present the table or figure
   - Write a TABLE_INTERPRET paragraph stating what the result shows
   - Write a paragraph connecting the result to the cumulative argument
5. Draft the robustness section. Address the most obvious rival explanations.
6. Draft the verdict. It must be quotable in 1--2 sentences and explicitly connect to the book's cumulative argument.
7. Draft the forward bridge. It must name what the next chapter will do and why the current chapter's findings make that next step necessary.
8. Verify all eight universal moves are present:
   - [ ] Prior-chapter bridge establishes what has been shown and what remains
   - [ ] Research question identified by paragraph 2
   - [ ] Data and methods described with enough detail for credibility
   - [ ] Results walked through with substantive interpretation
   - [ ] Interpretation connects results to the cumulative argument
   - [ ] Robustness and alternatives addressed
   - [ ] Verdict stated in quotable form
   - [ ] Forward bridge sets up the next chapter

**Pause:** Review the full draft against the structural plan.

---

### Phase 3: Calibration and Revision

**Goal:** Test the draft against cluster benchmarks and the eight universal moves. Revise as needed.

**Calibration checks:**

| Test | Pass Criteria |
|------|---------------|
| **Total word count** | Within cluster range |
| **Tables and figures count** | Within cluster range |
| **Results-to-prose ratio** | Within cluster range; check that results sections include interpretation, not just output |
| **Opening type** | Matches cluster prescription |
| **Verdict placement** | In labeled conclusion section or final paragraphs; quotable in 1--2 sentences |
| **Bridge quality** | Both prior-chapter bridge and forward bridge are explicit and specific |
| **Cumulative logic** | Reader can identify what this chapter adds to the argument that prior chapters did not provide |

**Universal move tests:**

| Test | Question | Fix if Failing |
|------|----------|---------------|
| **Bridge test** | Does the reader know what has been shown and what remains? | Add a "prior chapters showed X; this chapter asks Y" paragraph in the opening |
| **Question test** | Can the reader state the chapter's empirical question by paragraph 2? | Move the research question earlier; add "This chapter investigates whether..." |
| **Data test** | Does the reader know what dataset, measures, and methods will be used? | Add a data paragraph naming the N, the key variables, and the analytical approach |
| **Results test** | Can the reader follow the results without independently reading the tables? | Add TABLE_INTERPRET paragraphs after each table/figure; convert coefficients to substantive terms |
| **Interpretation test** | Does the reader know what the results mean for the book's argument? | Add MECHANISM_CLAIM paragraphs connecting results to the cumulative case |
| **Robustness test** | Has the chapter addressed the most obvious rival explanations? | Add an ALTERNATIVE_ADDRESS section with at least two rival explanations |
| **Verdict test** | Can a reader quote the finding in 1--2 sentences? | Rewrite the verdict paragraph with a signal phrase and explicit claim |
| **Forward test** | Does the reader know where the argument goes next? | Add a BRIDGE_FORWARD paragraph naming the next chapter and stating why the current findings make it necessary |

**Revision priorities** (in order):
1. Cumulative logic -- if the reader cannot see how this chapter builds on prior chapters and enables subsequent ones, the chapter has failed its sequential function
2. Verdict clarity -- if the verdict is not quotable, the chapter's contribution is invisible
3. Results interpretation -- if the reader must read the tables independently to understand the findings, the prose has failed
4. Prior-chapter bridge -- without it, the chapter is a standalone article, not a book chapter
5. Forward bridge -- without it, the reader does not know where the argument goes
6. Robustness -- rival explanations must be addressed, especially in mechanism test chapters
7. Word count -- trim or expand to match cluster benchmarks

---

## Anti-Patterns

### 1. Results without interpretation

The most common failure mode in quantitative chapters. If the chapter presents a regression table and moves directly to the next analysis without stating what the results mean in substantive terms, the reader is left to do the analytical work themselves. Every table and figure must be followed by a paragraph that states what the reader should see and why it matters. Grumbach translates every coefficient: "a one standard deviation increase in the percent of money that comes from IGA donors makes the state's average Republican legislator 0.33 standard deviations more conservative in office." Bolton and Thrower do the same: "We reveal a ubiquitous prediction in the theoretical literature on discretion -- the ally principle -- is contingent on congressional capacity." The results paragraph is not optional.

### 2. No bridge to the next chapter

A quantitative chapter that ends with the verdict and stops has failed its sequential function. Every chapter in the corpus bridges forward explicitly. Grumbach: "In the next chapter, I describe how national activists and activist groups became more coordinated and invested in state politics in recent years." Kadivar: "The findings of this chapter confirm a robust association between unarmed mobilization and democratic durability, but what are the mechanisms underlying this association? I explore these questions in the following chapters." The forward bridge is typically 2--4 paragraphs at the chapter's close.

### 3. Methods section too long

If the data and methods section exceeds 25% of the chapter (outside the Foundation Layer cluster), it has displaced the results and interpretation. Mechanism Test and Domain Extender chapters should aim for 10--15% methods. The data and methods section should create confidence in the analysis, not exhaustively document every coding decision. Save the coding appendix for an online supplement.

### 4. No alternative explanations addressed

A quantitative chapter that presents only its preferred model without addressing rivals will read as naive to methodologically sophisticated readers. Every chapter in the corpus addresses at least one alternative. Grumbach: "Donors and politicians act strategically in ways that make it difficult to study causal relationships in campaign finance research. It could be the case that politicians cause changes to donor behavior rather than the other way around." Bolton and Thrower: "readers may be concerned that capacity is caused by interbranch conflict." Tesler uses embedded experiments as robustness. Kadivar tests whether a simple dummy (any mobilization vs. none) performs as well as his continuous duration measure (it does not). Address the most obvious objection and demonstrate your results survive it.

### 5. The chapter that could be an article

If the chapter presents a complete standalone analysis with no reference to prior or subsequent chapters, it is an article, not a book chapter. The sequential logic -- "prior chapters showed X; this chapter shows Y; the next chapter will show Z" -- is what makes a quantitative chapter a chapter rather than a journal submission. Every opening must bridge backward; every closing must bridge forward.

### 6. Figures and tables with no narrative guidance

If the chapter says "Table 3 presents the results" and offers no TABLE_SETUP or TABLE_INTERPRET paragraph, the reader is abandoned. The setup paragraph tells the reader what to look for; the interpret paragraph tells the reader what they found. Kadivar's descriptive tables are preceded by text explaining what each column means; his regression output is followed by text converting coefficients to percentage reductions in failure risk. The table is the evidence; the prose is the argument.

### 7. The payoff chapter that does not recapitulate

If the Payoff Chapter opens as if it were a standalone analysis, the reader has lost the cumulative thread. Grumbach opens Chapter 7 by explicitly naming the cumulative arc: "The Trump presidency has generated new concerns about authoritarianism and democratic backsliding in the United States... Yet there has been no such systematic inquiry into subnational dynamics." Chapter 8 opens: "Across alternative measures and model specifications, the results are remarkably clear." The payoff chapter must remind the reader of everything that has been established before delivering the culminating finding.

---

## Word Count Reference Table

| Chapter Position | Domain Extender | Foundation Layer | Mechanism Test | Payoff Chapter |
|------------------|----------------|-----------------|----------------|----------------|
| First quantitative | 10,000--12,000 | 9,000--12,000 | 12,000--14,000 | -- |
| Middle extension | 10,000--14,000 | -- | 12,000--16,000 | -- |
| Culminating / payoff | -- | -- | -- | 10,000--15,000 |

---

## Output Expectations

By the end of this workflow, provide the user with:
- A **cluster selection rationale** (1--2 paragraphs explaining why this cluster fits and where this chapter sits in the cumulative sequence)
- A **structural plan** with section-by-section word count targets
- A **full draft** of the quantitative evidence chapter
- A **calibration memo** assessing the draft against cluster benchmarks and universal moves, with specific revision recommendations
