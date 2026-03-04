# Citation Integration Patterns

How you integrate citations affects readability and signals your relationship to the literature. This guide covers the four primary patterns and when to use each.

---

## The Four Patterns

| Pattern | Frequency | Pandoc Syntax | Renders As | Best For |
|---------|-----------|---------------|------------|----------|
| **Parenthetical Support** | 50-55% | `[@smithHousing2020]` | (Smith 2020) | Synthesis, efficient documentation |
| **Author-as-Subject** | 20-25% | `@smithHousing2020 argues that...` | Smith (2020) argues that... | Canonical theorists, foundational works |
| **Citation Strings** | 15-20% | `[@a2020; @b2019; @c2018]` | (A 2020; B 2019; C 2018) | Establishing consensus, breadth |
| **Quote-then-Cite** | 5-10% | `[@kirkCultural2011, p. 45]` | (Kirk and Papachristos 2011, 45) | Key definitions, precise language |

**Pandoc note**: These `[@citationKey]` references render to standard `(Author Year)` format when processed with Pandoc and a CSL style file. The keys come from the lit-search database or `references.bib`.

---

## Pattern 1: Parenthetical Support (50-55%)

The most common pattern. The claim comes first; citations provide evidence without interrupting prose.

### Structure
> [Claim] [@citationKey].
> [Claim] [@key1; @key2].

### Examples
> "Research on legal cynicism demonstrates that distrust of legal institutions is patterned by neighborhood context and race [@kirkCulturalMechanisms2011]."

> "Mass incarceration has left thousands of Black and Brown men under 'mass supervision' through probation and parole [@mcneilBeyensMassSuperv2013, p. 3]."

> "Conspiracy beliefs have long proliferated in the United States [@bailynIdeologicalOrigins2017; @watersConspiracyTheories1997] and beyond [@imhoffConspiracyBeliefs2022; @swamiConspiracyTheories2012]."

### When to Use
- Synthesizing multiple studies
- Efficient documentation of established findings
- Building cumulative case without interruption
- Most claims in most paragraphs

### Strengths
- Keeps focus on the content, not the author
- Allows efficient synthesis of multiple sources
- Maintains prose flow

---

## Pattern 2: Author-as-Subject (20-25%)

The cited author performs the intellectual action. Gives prominence to the scholar.

### Structure
> @citationKey [argues/demonstrates/shows/conceptualizes] that...
> According to @citationKey...

### Examples
> "@connellMasculinities2005 conceptualizes hegemonic masculinity as the most honorable expression of manliness within a hierarchy of masculinities."

> "According to @puwarSpaceInvaders2004, numerical representation matters, but so does the construction of race and gender within larger social status hierarchies."

> "@duboisSoulsBlackFolk1903 so clearly explicated that individual agency, the imagined range of actions available to the self, was shaped through the ongoing reconciliation of consciousness."

### When to Use
- Introducing canonical theorists (Bourdieu, Goffman, Foucault)
- Foundational works you're building on or extending
- When the *who* matters as much as the *what*
- Theory-Extension clusters (prominent for named framework)

### Strengths
- Signals which scholars are central to your argument
- Shows theoretical lineage
- Appropriate respect for foundational contributions

### Caution
- Overuse makes prose feel like a literature parade
- Reserve for genuinely important sources

---

## Pattern 3: Citation Strings (15-20%)

Multiple citations bundled together, signaling consensus or breadth.

### Structure
> [Claim] [@key1; @key2; @key3].
> [Claim] [see @key1; @key2; cf. @key3].
> [Claim] [e.g., @key1; @key2].

### Examples
> "Scholarship on business-elite influence on populist movements links opposition to climate reform to climate denial and other far-right ideals [@dunlapClimateDenial2015; @brulleInstitutionalizingDelay2018; @hertelFernandezPoliticsScale2019]."

> "...the sociology of law, which demonstrates that legality is embedded in a complex set of cultural schemas [@ewickCommonPlace1998; @silbeyAfterLegal2005; @nielsenSituatedJustice2000]."

### String Modifiers
- **"see"**: Points to useful sources: `[see @smithHousing2019; @jonesUrban2020]`
- **"e.g."**: Indicates examples, not exhaustive: `[e.g., @brownMigration2018]`
- **"cf."**: Indicates comparison or contrast: `[cf. @leeAlternativeView2017]`

### When to Use
- Establishing that a finding is robust across studies
- Showing breadth of a literature
- Documenting consensus
- Gap-Filler clusters (efficient synthesis)

### Strengths
- Demonstrates thorough literature engagement
- Establishes consensus quickly
- Shows pattern holds across multiple contexts

### Caution
- Long strings can feel like padding
- More than 5-6 citations starts to look excessive
- Make sure the claim actually applies to all cited sources

---

## Pattern 4: Quote-then-Cite (5-10%)

Direct quotation with attribution. Use sparingly and strategically.

### Structure
> As @citationKey notes, "..." [@key, p. page].
> @citationKey describes [concept] as "..." [@key, p. page].
> "[Quote]" [@citationKey, p. page].

### Examples
> "Legal cynicism is broadly conceived of as 'a *cultural orientation* in which the law and the agents of its enforcement are viewed as illegitimate, unresponsive, and ill-equipped to ensure public safety' [@kirkCulturalMechanisms2011, p. 443]."

> "According to @lamontDignityMorality2009 [p. 158]: 'Low-status groups (in this situation) are more likely to be resigned and passive instead of resilient.'"

### When to Use
- **Key definitions**: When the original language matters
- **Contested terms**: When precise wording is at stake
- **Foundational formulations**: Classic statements worth preserving
- **Concept-Builder clusters**: Detailed engagement with sources being critiqued or built upon

### When NOT to Use
- General findings (paraphrase instead)
- Routine claims (use parenthetical)
- To avoid writing your own synthesis (lazy quoting)

### Strengths
- Precision when language matters
- Shows close reading of sources
- Appropriate for definitions and key formulations

### Caution
- Overuse makes the section feel like a collage
- Should be rare (5-10% of citations max)
- Always include page numbers for quotes

---

## Cluster-Specific Patterns

| Cluster | Primary Pattern | Secondary Pattern | Notes |
|---------|-----------------|-------------------|-------|
| **Gap-Filler** | Parenthetical (70%) | Citation strings | Minimal author-subject |
| **Theory-Extender** | Author-subject + Parenthetical | Citation strings | Named theorist prominent |
| **Concept-Builder** | Quote-then-cite + Author-subject | Parenthetical | Detailed engagement |
| **Synthesis Integrator** | Mixed across traditions | Bridging citations | Citations from multiple traditions |
| **Problem-Driven** | Parenthetical | Context-heavy | More empirical/policy citations |

---

## Citation Density Benchmarks

Based on analysis of 80 articles:

| Metric | Median | Target Range (IQR) |
|--------|--------|-------------------|
| **Citations per paragraph** | 3.5 | 2.4-5.0 |
| **Citations per 1,000 words** | 24.2 | 18.9-32.0 |
| **Unique sources** | 35 | 26-43 |

### What These Mean

- **2.4-5.0 per paragraph**: Most paragraphs should have 2-5 citations
- **18.9-32.0 per 1,000 words**: A 1,500-word section should have ~30-48 citations
- **Under 26 citations**: May signal insufficient engagement
- **Over 50 citations**: May signal catalog-style rather than argument-style

---

## Common Mistakes

| Mistake | Problem | Solution |
|---------|---------|----------|
| All author-subject | Reads like a literature parade | Mix in parenthetical |
| No author-subject | Misses chance to highlight key theorists | Use for foundational sources |
| Excessive quoting | Looks like you can't synthesize | Paraphrase more; quote definitions only |
| Long citation strings | Feels like padding | Keep to 3-5 per string |
| Underciting | Signals superficial engagement | Aim for 3-5 per paragraph |
| Same pattern throughout | Monotonous prose | Vary deliberately |

---

## Integration Checklist

For each paragraph, verify:

1. **Pattern variety**: Are you using multiple patterns across the section?
2. **Author-subject for canonicals**: Are foundational theorists given appropriate prominence?
3. **Efficient strings**: Is consensus established without excessive strings?
4. **Quotes only for definitions**: Are you quoting only when language precision matters?
5. **Citation density**: Does the paragraph fall in the 2.4-5.0 range?
6. **Cluster alignment**: Does your citation pattern match your cluster?

---

## Field-Specific Patterns

When a field profile applies, consult `fields/{field}.md` for
field-specific patterns, phrase templates, and move distributions.
Field-specific patterns supplement the standard guidance above.
