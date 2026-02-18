# Phase 1: Corpus Immersion

You are executing Phase 1 of the genre-skill-builder workflow. Your goal is to build a quantitative profile of the corpus—understanding the landscape before coding individual features.

## Why This Phase Matters

Quantitative profiling establishes the baseline. Before coding rhetorical moves, you need to know what "typical" looks like: median word counts, paragraph distributions, structural patterns. This phase creates the benchmarks that later define clusters.

## Inputs

Before starting, read:
1. `analysis/genre-analysis-memo.md` — Phase 0: Scope section (scope and model skill, corpus manifest)
2. The corpus files themselves (in the location specified)

## Your Tasks

### 1. Extract Basic Statistics for Each Article

For every article in the corpus, extract:

```markdown
## Article: [filename]

### Basic Counts
- **Word count**: [n]
- **Paragraph count**: [n]
- **Sentence count**: [n] (if feasible)
- **Character count**: [n]

### Structural Features
- **Has subsections**: [yes/no]
- **Subsection count**: [n]
- **Subsection headings**: [list if present]
- **Has numbered/bulleted lists**: [yes/no]

### First/Last Elements
- **Opening sentence**: "[first sentence]"
- **Opening sentence type**: [context/literature/theory/question/claim]
- **Closing sentence**: "[last sentence]"
```

### 2. Calculate Corpus-Level Statistics

Aggregate the per-article data:

```markdown
## Corpus Statistics

### Word Count
- **Median**: [n]
- **Mean**: [n]
- **IQR**: [Q1]-[Q3]
- **Range**: [min]-[max]
- **Outliers**: [articles significantly above/below]

### Paragraph Count
- **Median**: [n]
- **Mean**: [n]
- **IQR**: [Q1]-[Q3]
- **Range**: [min]-[max]

### Subsections
- **Articles with subsections**: [n] ([%])
- **Median subsection count** (when present): [n]
- **Common headings**: [list top 3-5]

### Words per Paragraph
- **Median**: [n]
- **Range**: [min]-[max]
```

### 3. Identify Structural Patterns

Look for recurring structural elements:

**Opening patterns**:
- What percentage start with context-setting?
- What percentage start with literature references?
- What percentage start with claims/arguments?
- What percentage start with questions?

**Organizational patterns**:
- Is there a typical paragraph sequence?
- Are subsections used consistently or variably?
- Is there a recognizable "turn" or pivot point?

**Closing patterns**:
- How do sections typically end?
- What elements appear in final paragraphs?

### 4. Flag Outliers and Notable Examples

Identify articles that stand out:

**Length outliers**:
- Unusually short (bottom 10%)
- Unusually long (top 10%)
- Note: Outliers may represent different clusters

**Structural outliers**:
- Unusual organization
- Many subsections vs. none
- Distinctive formatting

**Quality exemplars**:
- Articles that seem particularly well-crafted
- Could serve as models for technique guides

### 5. Generate Initial Hypotheses

Based on quantitative patterns, hypothesize about clusters:

```markdown
## Initial Cluster Hypotheses

Based on the quantitative profile, I observe:

1. **Length variation**: [describe]
   - Possible cluster distinction: [hypothesis]

2. **Subsection usage**: [describe]
   - Possible cluster distinction: [hypothesis]

3. **Opening sentence patterns**: [describe]
   - Possible cluster distinction: [hypothesis]

These hypotheses will be tested through systematic coding in Phase 2.
```

### 6. Create Data Files

Structure the data for later phases:

**corpus-statistics.json**:
```json
{
  "corpus_size": 80,
  "section_type": "introduction",
  "statistics": {
    "word_count": {
      "median": 761,
      "mean": 823,
      "q1": 612,
      "q3": 945,
      "min": 342,
      "max": 1523
    },
    "paragraph_count": {
      "median": 6,
      "mean": 6.2,
      "q1": 5,
      "q3": 8,
      "min": 3,
      "max": 12
    }
  },
  "articles": [
    {
      "filename": "article-01.md",
      "word_count": 756,
      "paragraph_count": 6,
      "has_subsections": false,
      "opening_type": "phenomenon"
    }
  ]
}
```

## Output Files to Create

1. **Per-article profiles** — Save each article's profile to `article-profiles/[author-year-slug].md`. Keep these as individual files; they are needed for batch production in later phases.

2. **Structured corpus data** — Save the `corpus-statistics.json` output (see Section 6) to `analysis/corpus-data.json`. If the file already exists (from a prior phase), merge the new data into it rather than overwriting.

3. **Phase 1 memo section** — Append a `## Phase 1: Immersion` section to `analysis/genre-analysis-memo.md`. The section should contain:

```markdown
## Phase 1: Immersion

### Corpus Statistics

#### Word Count
- **Median**: [n]
- **Mean**: [n]
- **IQR**: [Q1]–[Q3]
- **Range**: [min]–[max]
- **Outliers**: [articles significantly above/below]

#### Paragraph Count
- **Median**: [n]
- **IQR**: [Q1]–[Q3]
- **Range**: [min]–[max]

#### Subsections
- **Articles with subsections**: [n] ([%])
- **Median subsection count** (when present): [n]
- **Common headings**: [top 3–5]

#### Words per Paragraph
- **Median**: [n]
- **Range**: [min]–[max]

### Structural Patterns

#### Opening Patterns
[Percentages for context-setting, literature reference, claims, questions]

#### Organizational Patterns
[Notes on paragraph sequence, subsection use, pivot points]

#### Closing Patterns
[Notes on how sections typically end]

### Outliers and Exemplars
[List notable articles with brief rationale]

### Comparison with Model Skill
| Metric | Model Skill | This Corpus | Difference |
|--------|-------------|-------------|------------|
| Median word count | [X] | [Y] | [note] |
| Median paragraphs | [X] | [Y] | [note] |
| % with subsections | [X] | [Y] | [note] |

### Initial Cluster Hypotheses
1. **[Observation]**: [hypothesis about possible cluster distinction]
2. [...]

### Questions for User
[Any patterns that need user input before proceeding]
```

## Guiding Principles

1. **Quantify before qualifying**: Count everything that can be counted. Qualitative coding comes in Phase 2.

2. **Variation is signal**: Large IQRs and outliers suggest cluster differentiation.

3. **Preserve granularity**: Keep per-article data even when reporting aggregates.

4. **Compare to model skill**: How do your statistics compare to the model skill's benchmarks?

5. **Document surprises**: Note anything unexpected—these often become analytical insights.

## Comparison with Model Skill

Compare your corpus statistics to the model skill's benchmarks:

| Metric | Model Skill | Your Corpus | Difference |
|--------|-------------|-------------|------------|
| Median word count | [X] | [Y] | [note] |
| Median paragraphs | [X] | [Y] | [note] |
| % with subsections | [X] | [Y] | [note] |

Note significant differences—they may reflect section-type differences or venue differences.

## When You're Done

Return a summary to the orchestrator that includes:
1. Corpus size confirmed
2. Key statistics (median word count, paragraph count)
3. Notable structural patterns
4. Outliers flagged (with article names)
5. Initial cluster hypotheses (2-4 possibilities)
6. Comparison to model skill benchmarks
7. Questions for the user about patterns observed
8. Recommendation to proceed to Phase 2
