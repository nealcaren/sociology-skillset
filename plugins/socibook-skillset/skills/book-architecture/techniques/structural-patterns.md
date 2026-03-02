# Structural Patterns

The concrete structural decisions that shape how books are built: theory chapter design, methods placement, historical context chapters, synthesis chapters, and word count allocation. This file documents the patterns visible in the 22-book corpus with real examples and decision rules.

Use this file alongside `chapter-sequencing.md` (for chapter ordering and transition techniques) and the main `SKILL.md` (for architecture type selection and quantitative benchmarks).

---

## Theory Chapter Patterns

The theory chapter is the single most consequential structural decision after architecture type selection. Approximately 12 of 22 books in the corpus have at least one standalone theory chapter. The choice of how many theory chapters to include -- and whether to include any at all -- depends on the complexity of the theoretical framework and the reader's need for scaffolding before the evidence.

### Single Theory Chapter

The most common pattern. One chapter lays out the framework, defines key concepts, specifies causal mechanisms, and positions the book in the literature. The reader exits the chapter holding a checklist of variables that the empirical chapters will assess.

**Kadivar** uses a single theory chapter to establish the framework for understanding how unarmed mass movements produce democratization. The chapter specifies the causal mechanism, identifies the variables that the quantitative and case study chapters will examine, and positions the argument against existing explanations. The framework is tight enough to fit in one chapter because it rests on a single central mechanism.

**Krimmel** uses a single theory chapter to lay out the constraints and facilitators that shape party clientelism. The chapter does double duty: it develops the theoretical argument and introduces the key historical variables that the subsequent period chapters will trace. Because the theory IS the historical trajectory, one chapter suffices.

**Decision rule:** A single theory chapter works when the framework rests on one central mechanism with clearly defined variables, and when the reader can hold the full framework in mind after one pass.

### Dual Theory Chapters

Two theory chapters appear when the book distinguishes between a broad analytical framework and a specific causal mechanism, or when the theoretical contribution has two distinct components that require separate development.

**Patashnik (2008)** separates general theory from specific mechanism across two chapters. The first chapter develops a general theory of reform durability -- why do some policy reforms stick while others erode? The second chapter specifies the particular mechanisms (institutional reconfiguration, policy feedback, creative destruction) that the six case chapters will assess. The separation allows the reader to absorb the general question before confronting the specific causal machinery.

**Smith and King** devote two chapters to theoretical architecture. The first establishes the racial politics framework -- the argument that American political development is structured by racial alliances. The second specifies the institutional orders through which those alliances operate. The two chapters together create the dual-lens (race + institutions) that every empirical chapter requires.

**Tesler** uses two chapters of scaffolding: one on racial attitudes as a general phenomenon in American politics, and a second developing the specific spillover hypothesis -- the claim that racial attitudes "spill over" into ostensibly non-racial policy domains. The first chapter establishes what racial attitudes are and how they operate; the second specifies the mechanism the book will test.

**Decision rule:** Two theory chapters work when the book makes a distinction between framework and mechanism, or when the reader must hold two analytically distinct concepts in mind simultaneously before the empirical chapters make sense.

### Triple Theory Chapters

Rare and risky. The heaviest theoretical scaffolding in the corpus.

**Mucciaroni** uses three theory chapters before any empirical material. Chapter 1 develops the theory of issue definition (how the framing of a policy question affects political outcomes). Chapter 2 develops the theory of institutional venues (how the site of decision-making shapes results). Chapter 3 develops the theory of threat perception (how majorities respond to perceived threats from minority claims). Each chapter introduces a variable that the reader must hold in mind when reading the case chapters. The triple scaffolding means the case chapters can move quickly -- they map each domain onto the three-variable framework without stopping to develop the theory -- but it also means the reader does not see evidence until roughly page 100.

**Decision rule:** Three theory chapters are warranted only when the reader genuinely needs to hold three or more independent concepts in mind before any case makes sense, and when the concepts are too complex to develop in fewer chapters. This is rare. The corpus contains only one instance.

### Theory Embedded in Introduction

Several books -- particularly shorter ones and those with simpler theoretical contributions -- develop their framework entirely within the introduction, reserving all body chapters for empirical work.

**Fisher** embeds the theoretical contribution in the introduction. The book is shorter (~53,000 words) and the theory is compact enough to develop in the introduction's argument section without crowding out the puzzle, stakes, or roadmap.

**Mettler** similarly embeds theory in the introduction. The framework -- submerged state politics -- is stated compactly and the introduction carries the theoretical load, freeing all body chapters for empirical analysis.

**Decision rule:** Embed the theory in the introduction when (a) the theoretical contribution can be stated in 1,500--2,500 words, (b) the book has 5--6 body chapters and cannot afford to spend one on theory alone, or (c) the theory IS the comparative structure and develops more naturally alongside the evidence overview than in isolation.

### Decision Summary

| Pattern | When It Works | Corpus Examples | Risk |
|---------|--------------|-----------------|------|
| Single chapter | One central mechanism, clearly defined variables | Kadivar, Krimmel | Theory may feel underdeveloped if the framework is genuinely complex |
| Dual chapters | Framework + mechanism distinction, or two required lenses | Patashnik 2008, Smith & King, Tesler | Reader may disengage if both chapters are abstract |
| Triple chapters | Three independent concepts, all required for cases | Mucciaroni | Reader reaches evidence very late; maximum tolerable scaffolding |
| Embedded in intro | Simple theory, short book, or theory = structure | Fisher, Mettler | Theory may be under-specified if the contribution is actually complex |

---

## How Authors Handle Methods

Methods description is structurally consequential because it competes for space with theory and evidence. The corpus reveals two primary patterns: embedding methods in the introduction (the majority) or dedicating a standalone methods chapter (the minority).

### Embedded in Introduction (Most Common)

The majority of the 22 books embed case selection rationale, data description, and methodological overview in the introduction, typically in 800--1,500 words within the "evidence and approach" or "plan of the book" section.

**When embedded works:**
- The book relies on a single clear data source (e.g., one dataset, one archive, one set of interviews)
- The methods are conventional for the field (comparative case study, regression analysis, content analysis) and do not require extended justification
- The data description takes fewer than 1,500 words
- The reader does not need a separate methods discussion to evaluate the evidence

This is the default. Do not create a standalone methods chapter unless there is a positive reason to do so.

### Standalone Methods Chapter (3 of 22 Books)

Three books in the corpus devote a full chapter to methods, case selection, or research design. Each has a specific justification.

**Lichterman, Chapter 2: "Placing and Studying the Action"**
An ethnographic book where the method IS a form of argument. Lichterman's chapter justifies extended case method, describes the field sites, explains how the researcher gained access and navigated positionality, and develops the methodological principles that structure the empirical analysis. The chapter is necessary because ethnographic validity rests on the reader trusting the researcher's observational apparatus -- and that trust requires more than a paragraph in the introduction.

**Han et al., Chapter 2: "The Cases"**
A multi-case study with a complex case selection rationale. The chapter introduces all the cases, explains the selection logic, and provides enough context on each case that the thematic chapters can proceed without extended background sections. In a multi-case thematic architecture (Type F), where cases recur across chapters rather than getting their own chapters, a standalone case introduction is essential -- otherwise the reader encounters cases without context.

**Lowande, Chapter 3: "Counting on Action"**
A quantitative book where measurement is non-obvious. The chapter develops the measurement strategy for executive unilateral action -- a concept that is notoriously difficult to operationalize. The standalone chapter is warranted because the reader cannot evaluate the subsequent quantitative results without understanding how the dependent variable was constructed.

### Decision Rule for Standalone Methods

Create a standalone methods chapter when at least one of the following conditions holds:

1. **Ethnographic research** where the method of observation requires its own justification -- where "being there" is not self-evident and the reader needs to understand how the researcher's presence shaped the data
2. **Quantitative research** where measurement is non-obvious -- where the dependent or independent variable is constructed through a process that requires extended explanation
3. **Multi-method research** where the methods need sequencing -- where the reader must understand why quantitative analysis precedes case studies (or vice versa) and how the methods complement each other
4. **Multi-case designs** (especially Type F) where the cases need introduction before they appear woven through thematic chapters

If none of these conditions holds, embed the methods in the introduction.

---

## Historical / Context Chapter Patterns

A historical or context chapter provides the background the reader needs before encountering the empirical chapters. It is not an empirical chapter -- it does not test the theory or present new findings. Its function is orientation: establishing the institutional, political, or historical landscape that the empirical chapters will analyze.

### When to Use a Standalone Context Chapter

**Decision rule:** If temporal change is NOT the main argument but the reader needs historical orientation before the empirical chapters make sense, use one or two standalone context chapters. If temporal change IS the argument, those chapters are empirical chapters, not context -- they should be classified accordingly.

### Single Context Chapter

**Bolton and Thrower, Chapter 3: "Outmanned and Outgunned"**
Traces the historical development of congressional capacity -- the staff, expertise, and institutional resources that Congress has (or lacks) relative to the executive branch. This chapter is not testing the theory; it is establishing the baseline condition (congressional weakness) that the subsequent chapters will analyze. The reader must understand what Congress lacks before they can understand how presidents exploit that weakness.

**SoRelle, Chapter 2: "Full Disclosure: Building the U.S. Political Economy of Credit"**
Traces the historical construction of the credit disclosure regime. The chapter establishes how the institutional landscape was built so that subsequent chapters can analyze what it produced. The historical detail is necessary context, not the argument itself.

**Krimmel, Chapter 3: "The Dance of Clientelism and Programmaticism"**
Provides the historical evolution of party organizations that subsequent chapters will analyze in more detail. This chapter sits at the boundary between context and empirical -- it establishes the historical baseline while also developing the argument. In a Historical Arc architecture, this kind of chapter often does double duty.

### Double Context Chapters

**Grumbach, Chapters 2--3: "The Mythos of American Federalism" + "From Backwaters to Battlegrounds"**
Two chapters of historical context before the quantitative analyses begin. Chapter 2 challenges the conventional understanding of American federalism as a system of healthy competition; Chapter 3 traces how state governments became the sites of national partisan conflict. Together, they establish the institutional and political landscape that the subsequent quantitative chapters analyze. Two context chapters are warranted here because the reader needs to unlearn a conventional narrative (federalism as beneficial) before they can absorb the book's evidence (federalism as democratic erosion).

### When Context Chapters Are Not Needed

Not every book requires a standalone context chapter. If the historical or institutional background can be covered in the introduction (in 1,000--2,000 words of background) or if each empirical chapter provides its own context at the start, a dedicated context chapter is unnecessary overhead. Books with fewer than 7 body chapters often cannot afford to spend one on context alone.

---

## Synthesis Chapter Patterns

A synthesis chapter draws explicit comparative conclusions after the empirical chapters. It is distinct from the conclusion: the synthesis chapter does analytical work (comparing cases, identifying patterns, refining the theory), while the conclusion does framing work (implications, stakes, limitations, future directions).

### When to Use a Standalone Synthesis Chapter

**Decision rule:** Use a standalone synthesis chapter when (a) the comparative insight is substantial enough for its own chapter -- typically when the book has three or more cases and the cross-case patterns are not self-evident, and (b) the conclusion has other work to do (policy implications, normative stakes, disciplinary positioning) that would crowd out the comparative analysis.

### Standalone Synthesis

**Brown-Saracino, Chapter 5**
Titled the same as the book, this chapter draws comparative conclusions across the four city case chapters. It identifies the ecological mechanisms that operate across all four cities, specifies the conditions under which different identity cultures emerge, and develops the theoretical contribution that no single case chapter could articulate. The synthesis chapter works here because the four cases are sufficiently different that the patterns require explicit comparative analysis -- the reader would not see them by simply reading the cases in sequence.

**Smith and King, Chapter 9: "Lessons for and from Theories of Racial Politics"**
A theoretical synthesis that steps back from the empirical material to assess what the cases collectively reveal about racial alliance politics. The chapter is positioned between the empirical chapters and the conclusion, doing the analytical work of comparative assessment while leaving the conclusion free to address broader implications.

### Synthesis Embedded in Conclusion

Some books fold the comparative synthesis into the conclusion rather than giving it a standalone chapter. This works when:
- The book has fewer than three cases and the comparison is straightforward
- The cross-case patterns have been made visible through forward bridges and backward calibration throughout the empirical chapters
- The conclusion is long enough (6,000--8,000 words) to accommodate both synthesis and implications

The risk of embedding synthesis in the conclusion is that one or both functions gets short-changed. If the conclusion must both compare the cases and address broader stakes, neither task may receive adequate development.

---

## Word Count Allocation Templates

These templates are drawn from the corpus benchmarks. They represent typical allocations, not prescriptions. The specific numbers will vary based on the number of cases, the complexity of the theory, and the total manuscript length.

### Architecture B: Parallel Cases (~105,000 words)

| Component | Words | Share |
|-----------|-------|-------|
| Introduction | 8,000 | 7.6% |
| Theory chapter(s) | 9,000--10,000 | 8.5--9.5% |
| 4 case chapters @ 14,000--16,000 each | 56,000--64,000 | 53--61% |
| Scope conditions or synthesis | 10,000--12,000 | 9.5--11.4% |
| Conclusion | 6,000--7,000 | 5.7--6.7% |

The case chapters dominate the word budget. Each case chapter must be long enough to develop the case fully -- a 10,000-word case chapter is almost always too thin for a qualitative case study. If four cases at 14,000 words each consume 56,000 words, the total body (excluding intro and conclusion) is approximately 75,000--86,000 words, leaving 19,000--29,000 for scaffolding.

**Key ratio:** If theory chapters plus introduction plus conclusion exceed 25% of the total manuscript, the scaffolding is crowding out the evidence.

### Architecture C: Thematic Progression (~100,000 words)

| Component | Words | Share |
|-----------|-------|-------|
| Introduction | 7,000--8,000 | 7--8% |
| Context / historical chapter(s) | 8,000--10,000 | 8--10% |
| 5--6 thematic chapters @ 10,000--14,000 each | 50,000--84,000 | 50--84% |
| Conclusion | 5,000--6,000 | 5--6% |

Thematic progression books tend to have somewhat shorter individual chapters than parallel case books because each chapter develops one dimension rather than a full case narrative. The range of 10,000--14,000 per chapter reflects this: quantitative chapters in this architecture (e.g., Grumbach, Tesler) sit at the lower end; mixed-methods chapters with extended qualitative evidence sit at the upper end.

**Key ratio:** Context chapters should not exceed 15% of the total manuscript. If two context chapters together consume 20,000 words in a 100,000-word book, they are taking space from the empirical chapters.

### Architecture D: Historical Arc (~110,000 words)

| Component | Words | Share |
|-----------|-------|-------|
| Introduction | 7,000--8,000 | 6.4--7.3% |
| Context / origins chapter | 8,000--10,000 | 7.3--9.1% |
| 4--6 period chapters @ 12,000--16,000 each | 48,000--96,000 | 43.6--87.3% |
| Conclusion | 5,000--6,000 | 4.5--5.5% |

Historical arc books tend toward the longer end of the corpus because each period chapter requires substantial archival or historical evidence. The context/origins chapter is sometimes the longest chapter in the book because it establishes the baseline from which all subsequent change is measured.

**Key ratio:** Period chapters should be roughly comparable in length. If one period chapter is twice as long as another, consider whether it is actually two periods that should be split, or whether some of its material belongs in a context chapter.

### Architecture E: Ethnographic (~115,000 words)

| Component | Words | Share |
|-----------|-------|-------|
| Introduction | 7,000--9,000 | 6.1--7.8% |
| Theory chapter | 8,000--10,000 | 7--8.7% |
| Methods / setting chapter | 6,000--8,000 | 5.2--7% |
| 4--6 thematic chapters @ 12,000--16,000 each | 48,000--96,000 | 41.7--83.5% |
| Conclusion | 5,000--7,000 | 4.3--6.1% |

Ethnographic books tend to be the longest in the corpus because qualitative evidence -- interview quotations, field scenes, extended interpretive passages -- consumes more space than quantitative tables or archival summaries. The methods/setting chapter is a structural cost unique to this architecture; it does not appear in other types.

**Key ratio:** The methods chapter should not exceed 8% of the total manuscript. If the methods chapter is longer than an empirical chapter, it is doing too much -- consider moving some material (site descriptions, historical background on the field site) to a separate context chapter or distributing it across empirical chapters.

### Architecture A: Quant-then-Case (~100,000 words)

| Component | Words | Share |
|-----------|-------|-------|
| Introduction | 7,000--8,000 | 7--8% |
| Theory chapter | 9,000--11,000 | 9--11% |
| Quantitative chapter | 10,000--14,000 | 10--14% |
| 3--4 case chapters @ 12,000--16,000 each | 36,000--64,000 | 36--64% |
| Conclusion | 5,000--6,000 | 5--6% |

The quantitative chapter is typically shorter than the case chapters because it presents results compactly (tables, figures, coefficient estimates), while the case chapters develop process-tracing narratives that require more space. Kadivar's structure illustrates this: the cross-case quantitative chapter establishes the pattern efficiently; the case chapters -- paired, single, and anomalous -- develop the mechanisms at greater length.

### Architecture F: Multi-case Thematic (~95,000 words)

| Component | Words | Share |
|-----------|-------|-------|
| Introduction | 7,000--8,000 | 7.4--8.4% |
| Theory chapter | 8,000--10,000 | 8.4--10.5% |
| Methods / cases chapter | 8,000--10,000 | 8.4--10.5% |
| 4--5 thematic chapters @ 10,000--14,000 each | 40,000--70,000 | 42.1--73.7% |
| Conclusion | 5,000--6,000 | 5.3--6.3% |

Multi-case thematic books require a case introduction chapter (or substantial case descriptions in the introduction) because cases are not developed in their own chapters. The thematic chapters tend to be moderately long because they must develop both the theme and the cross-case comparison within each chapter.

---

## Allocation Diagnostics

After setting the word count allocation, run these checks:

| Diagnostic | Pass Criteria | Fix |
|-----------|--------------|-----|
| **Empirical share** | Empirical chapters receive 60--70% of total words | If below 60%, scaffolding is crowding out evidence; cut theory or context. If above 70%, check that theory and conclusion are adequately developed. |
| **Scaffolding ceiling** | Introduction + theory + conclusion together are less than 25% of total | If above 25%, the reader spends too long before and after the evidence. Embed theory in intro or cut introduction length. |
| **Chapter balance** | No empirical chapter is more than 1.5x the length of the shortest empirical chapter | If one chapter is dramatically longer, it may be doing the work of two chapters and should be split. If one is dramatically shorter, it may lack sufficient evidence and should be combined with another. |
| **Longest chapter test** | The longest chapter is the one doing the most analytical work | If the longest chapter is a theory chapter or context chapter, the scaffolding is over-built relative to the evidence. |
| **Introduction ceiling** | Introduction is 7,000--9,000 words | The 8,000-word introduction appears in 12 of 22 books in the corpus. Exceeding 9,000 words typically signals that the introduction is doing work that belongs in a standalone theory or context chapter. |
| **Conclusion floor** | Conclusion is at least 5,000 words | A conclusion under 5,000 words rarely has room for synthesis, implications, and stakes. If it is below 5,000, check that synthesis work is not being pushed into the last empirical chapter. |
