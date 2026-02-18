# Phase 2: Systematic Genre Coding

You are executing Phase 2 of the genre-skill-builder workflow. Your goal is to systematically code each article for genre features, building the data that will reveal cluster patterns.

## Why This Phase Matters

Coding transforms impressions into data. By applying consistent categories across the corpus, you create the foundation for rigorous cluster discovery. This phase adapts the systematic coding approach from interview-analyst to genre analysis.

## Inputs

Before starting, read:
1. `analysis/genre-analysis-memo.md` — Phase 0: Scope section (code categories, model skill structure) and Phase 1: Immersion section (quantitative profile)
2. `analysis/corpus-data.json` — Structured per-article data from Phase 1
3. The `article-profiles/` folder — per-article profiles from Phase 1

## Your Tasks

### 1. Develop the Codebook

Create a systematic codebook with codes organized by category. Base codes on the model skill but adapt to your section type.

**Example codebook structure**:

```markdown
# Genre Codebook: [Section Type]

## Opening Move Codes

### OM-PHENOMENON
**Definition**: Opens by describing an empirical phenomenon, trend, or social condition.
**Indicators**: Statistical claims, descriptions of events, naming of social groups/practices.
**Example**: "Tasked with protecting children from abuse and neglect, U.S. child welfare authorities investigate the parents of over three million children each year."

### OM-STAKES
**Definition**: Opens by establishing importance, significance, or consequences.
**Indicators**: "Important," "significant," "crisis," claims about impact.
**Example**: "Housing instability poses severe consequences for families with children."

### OM-THEORY
**Definition**: Opens by invoking a theoretical framework, concept, or scholar.
**Indicators**: Named theory, cited theorist, conceptual terminology.
**Example**: "The concept of 'recognition' draws on several conceptual traditions."

### OM-CASE
**Definition**: Opens with a specific case, example, or vignette.
**Indicators**: Named individual, specific incident, narrative opening.
**Example**: "When Maria first arrived at the shelter..."

### OM-QUESTION
**Definition**: Opens with an explicit research question.
**Indicators**: Question mark, interrogative structure.
**Example**: "How do immigrant parents maintain connections with children abroad?"

[Continue for all code categories...]
```

### 2. Define Code Categories

Based on your model skill and section type, include these categories:

**A. Opening Moves** (required)
- How does the section begin?
- Codes: phenomenon, stakes, theory, case, question, other

**B. Structural Elements** (required)
- What organizational features are present?
- Codes: roadmap, limitations, callbacks, future-directions, data-preview, etc.

**C. Rhetorical Moves** (adapt to section type)
For Theory sections: gap-identification, synthesis, theory-exposition
For Introductions: hook, puzzle, preview
For Conclusions: restatement, implications, coda
For Methods: design-rationale, sampling-description, analysis-description

**D. Citation Patterns** (if applicable)
- Density: sparse (<2/para), moderate (2-4/para), dense (>4/para)
- Style: parenthetical-dominant, author-subject, quote-then-cite

**E. Linguistic Features** (select relevant)
- Hedging level: low, moderate, high
- Temporal markers: present, absent
- First person: present, absent

### 3. Code Each Article

For every article, apply all codes:

```markdown
## Article: [filename]

### Opening Move
- **Primary code**: OM-PHENOMENON
- **First sentence**: "Tasked with protecting children..."
- **Notes**: Classic empirical opening; data implied but not cited

### Structural Elements
- **Roadmap**: present (paragraph 5)
- **Data preview**: present (paragraph 3)
- **Limitations**: absent
- **Callbacks**: N/A (this is intro, not conclusion)

### Rhetorical Moves
- **Gap identification**: present (paragraph 4, "Yet we know little...")
- **Prior research synthesis**: present (paragraphs 2-3)
- **Contribution claim**: present (paragraph 5)

### Citation Pattern
- **Density**: moderate (3.2 per paragraph)
- **Dominant style**: parenthetical

### Linguistic Features
- **Hedging**: moderate
- **First person**: present ("This study examines...")
- **Temporal markers**: present ("In recent decades...")

### Overall Assessment
- **Preliminary cluster**: Gap-Filler candidate
- **Notes**: Efficient structure, data mentioned early, modest claims
```

### 4. Track Code Frequencies

Build a frequency matrix:

```markdown
## Code Frequency Summary

### Opening Moves
| Code | Count | Percentage |
|------|-------|------------|
| OM-PHENOMENON | 59 | 74% |
| OM-STAKES | 8 | 10% |
| OM-THEORY | 10 | 13% |
| OM-CASE | 2 | 3% |
| OM-QUESTION | 1 | 1% |

### Structural Elements
| Element | Present | Percentage |
|---------|---------|------------|
| Roadmap | 32 | 40% |
| Data preview | 56 | 70% |
| Gap statement | 72 | 90% |
| Contribution claim | 68 | 85% |

[Continue for all categories...]
```

### 5. Analyze Code Co-occurrence

Identify which codes appear together:

```markdown
## Co-occurrence Patterns

### Opening Move + Structure
- OM-PHENOMENON + early data preview: 45/59 (76%)
- OM-THEORY + named theorist in para 1: 8/10 (80%)
- OM-STAKES + policy implication: 6/8 (75%)

### Structural Combinations
- Roadmap + 5+ paragraphs: 28/32 (88%)
- No subsections + shorter length: correlation observed

### Emerging Cluster Signals
Based on co-occurrence, I see these groupings:
1. [Pattern A]: [codes that cluster]
2. [Pattern B]: [codes that cluster]
3. [Pattern C]: [codes that cluster]
```

### 6. Assign Preliminary Clusters

Based on coding patterns, assign each article to a preliminary cluster:

```markdown
## Preliminary Cluster Assignments

### Cluster A: [Working Name]
**Signature pattern**: [key codes that define this cluster]
**Articles**: [list article filenames]
**Count**: [n] ([%])

### Cluster B: [Working Name]
**Signature pattern**: [key codes that define this cluster]
**Articles**: [list article filenames]
**Count**: [n] ([%])

[Continue for 3-6 clusters...]

### Uncertain/Mixed
**Articles that don't fit cleanly**: [list]
**Notes on ambiguity**: [what makes them hard to classify]
```

### 7. Write Coding Memo

Document your coding process and emerging insights:

```markdown
## Coding Memo

### Process Notes
- [How did codes evolve during the process?]
- [What was difficult to code?]
- [What distinctions proved useful/useless?]

### Surprises
- [What patterns were unexpected?]
- [What assumptions from the model skill didn't hold?]

### Cluster Hypotheses Refined
- [How do preliminary clusters compare to Phase 1 hypotheses?]
- [What additional distinctions emerged?]

### Questions for Phase 3
- [What needs interpretation?]
- [Where are cluster boundaries unclear?]
- [What exemplars stand out?]
```

## Output Files to Create

1. **Per-article codes** — Save each article's codes to `article-codes/[author-year-slug].md`. Keep these as individual files; they are needed for batch production in later phases.

2. **Structured coding data** — Merge the per-article coding data (see the `article-codes.json` template in Section 3) into `analysis/corpus-data.json`. Add a `"coding"` key at the top level so Phase 1 data is preserved:

   ```json
   {
     "corpus_size": 80,
     "section_type": "introduction",
     "statistics": { ... },
     "articles": [
       {
         "filename": "article-01.md",
         "word_count": 756,
         "paragraph_count": 6,
         "has_subsections": false,
         "opening_type": "phenomenon",
         "opening_move": "phenomenon",
         "has_roadmap": true,
         "has_data_preview": true,
         "citation_density": "moderate",
         "preliminary_cluster": "gap-filler"
       }
     ]
   }
   ```

3. **Phase 2 memo section** — Append a `## Phase 2: Coding` section to `analysis/genre-analysis-memo.md`. The section should contain:

```markdown
## Phase 2: Coding

### Codebook

[Full codebook: all code categories and their definitions, indicators, and examples]

### Code Frequency Summary

#### Opening Moves
| Code | Count | Percentage |
|------|-------|------------|
| [code] | [n] | [%] |

#### Structural Elements
| Element | Present | Percentage |
|---------|---------|------------|
| [element] | [n] | [%] |

[Continue for all categories]

### Co-occurrence Patterns
[Key code combinations and what they suggest about clusters]

### Preliminary Cluster Assignments

#### Cluster A: [Working Name]
**Signature pattern**: [key codes]
**Articles**: [list]
**Count**: [n] ([%])

[Continue for each cluster]

#### Uncertain / Mixed
[Articles that don't fit cleanly, with notes on ambiguity]

### Coding Memo
#### Process Notes
[How codes evolved, what was difficult, what distinctions proved useful or useless]

#### Surprises
[Unexpected patterns; assumptions from model skill that didn't hold]

#### Cluster Hypotheses Refined
[How preliminary clusters compare to Phase 1 hypotheses]

#### Questions for Phase 3
[What needs interpretation, where cluster boundaries are unclear]
```

## Guiding Principles

1. **Consistency over speed**: Apply codes the same way across all articles.

2. **Refine as you go**: If a code isn't working, revise the definition mid-process—but recode earlier articles.

3. **Preserve uncertainty**: Mark unclear cases rather than forcing them into categories.

4. **Trust the model skill**: Start with model skill categories before inventing new ones.

5. **Co-occurrence reveals clusters**: Individual codes matter less than patterns of co-occurrence.

6. **Document decisions**: When you make a coding judgment, note why.

## When You're Done

Return a summary to the orchestrator that includes:
1. Codebook finalized (number of codes by category)
2. Key frequency findings (top opening moves, common structural elements)
3. Preliminary cluster count and names
4. Cluster sizes (n and % for each)
5. Edge cases and uncertainties
6. Most and least stable clusters
7. Questions for the user about coding decisions
8. Recommendation to proceed to Phase 3
