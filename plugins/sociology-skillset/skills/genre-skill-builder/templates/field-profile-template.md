# Field Profile Template

Use this template when generating a field profile for an existing writing skill. A field profile adjusts a skill's generalist benchmarks and adds field-specific patterns for a particular sociology subfield. Replace all `{{placeholders}}` with actual values from the genre analysis.

**Key principle**: The field profile is the **single source of truth** for all field-specific guidance within the skill. Phase and technique files contain only generic hooks that say "when a field profile applies, read it." No field-specific content lives in phase or technique files.

---

```markdown
# Field Profile: {{Field Name}} ({{Abbreviation}})

This field profile adjusts {{skill_name}} guidance for articles targeting {{field_name}} venues. Based on genre analysis of {{corpus_size}} {{field_name}} articles.

## When to Apply This Profile

Apply when the target venue or subfield is {{field_name}}. Common venues:

- *{{Venue 1}}*
- *{{Venue 2}}*
- *{{Venue 3}}*
- {{Field name}} special issues in general journals
- Any article whose primary contribution is to {{field_name}} theory

Also apply when the article's core topic involves {{topic_keywords}} — even if targeting a generalist journal — as {{field_name}} conventions shape reader expectations.

## How {{Abbreviation}} Differs from Generalist Sociology

{{N}} key findings from comparing {{abbreviation}} {{section_type}} (n={{corpus_size}}) to the generalist corpus (n={{generalist_n}}, {{generalist_venues}}):

| Finding | Generalist | {{Abbreviation}} | Implication |
|---------|-----------|-----|-------------|
| {{Finding 1 label}} | {{generalist_value}} | {{field_value}} | {{implication}} |
| {{Finding 2 label}} | {{generalist_value}} | {{field_value}} | {{implication}} |
| {{Finding 3 label}} | {{generalist_value}} | {{field_value}} | {{implication}} |
{{Add more rows as needed}}

**Root pattern**: {{One-sentence summary of the field's distinctive writing identity}}

## Adjusted Benchmarks

### {{Section Type 1}} Benchmarks ({{Abbreviation}})

| Feature | Generalist Default | {{Abbreviation}} Adjusted | Notes |
|---------|-------------------|-------------|-------|
| Word count | {{generalist_range}} | **{{field_range}}** | {{note}} |
| Paragraphs | {{generalist_range}} | **{{field_range}}** | {{note}} |
| Opening move | {{generalist_distribution}} | {{field_distribution}} | {{note}} |
| {{Feature 4}} | {{generalist_value}} | **{{field_value}}** | {{note}} |
| {{Feature 5}} | {{generalist_value}} | **{{field_value}}** | {{note}} |
{{Add more rows as needed}}

{{#if multiple_section_types}}
### {{Section Type 2}} Benchmarks ({{Abbreviation}})

| Feature | Generalist Default | {{Abbreviation}} Adjusted | Notes |
|---------|-------------------|-------------|-------|
| {{Repeat for each section the skill covers}} |
{{/if}}

## Field-Specific Structural Patterns

{{#if structural_patterns}}
{{N}} structural patterns appear in {{percentage}}% of {{abbreviation}} {{section_type}}. These are not seen in the generalist corpus.

### 1. {{Pattern Name}} ({{percentage}}%, n={{count}})

{{Description of the pattern and what it does}}

**Function**: {{What rhetorical work this pattern does}}

**Signature moves**:
- {{Move 1}}
- {{Move 2}}
- {{Move 3}}

**Benchmarks**:
| Feature | Value |
|---------|-------|
| Median words | {{value}} |
| Median paragraphs | {{value}} |
| Modal opening | {{value}} |
| Citations (median) | {{value}} |
| {{Other feature}} | {{value}} |

**When to use**: {{Conditions where this pattern fits}}

**Example opening logic**: "{{Example template}}"

{{Repeat for each structural pattern}}
{{else}}
No distinctive structural patterns identified beyond standard moves. Use standard opening move distribution with adjusted benchmarks above.
{{/if}}

## Field-Specific Clusters

{{#if field_clusters}}
{{N}} empirically derived clusters describe distinct {{section_type}} strategies in {{abbreviation}}. These interact with — but don't replace — the contribution-type clusters (Gap-Filler, Theory-Extension, etc.).

### Cross-Cluster Summary

| Cluster | n (%) | Words | ¶ | Citations | {{Key Feature}} | Modal Opening |
|---------|-------|-------|---|-----------|---------|---------------|
| {{Cluster 1}} | {{n}} ({{%}}) | {{words}} | {{paras}} | {{cites}} | {{feature}} | {{opening}} |
{{Repeat for each cluster}}

{{Describe each cluster in detail}}

### Cluster Selection Guidance

When both a contribution type (from generalist clusters) and a {{abbreviation}} cluster apply:

| If contribution type is... | Consider {{abbreviation}} cluster... | Rationale |
|---------------------------|------------------------|-----------|
| {{Contribution type}} | {{Field cluster}} | {{Why}} |
{{Repeat for each combination}}

**Rule**: The contribution-type cluster determines *what* you promise; the {{abbreviation}} cluster determines *how* you open and *what benchmarks* to target.
{{else}}
No distinctive field-specific clusters identified. Use the skill's generalist clusters with the adjusted benchmarks above.
{{/if}}

## Opening/Closing Move Distributions

{{#if opening_moves}}
### Opening Move Distribution

| Opening Move | Generalist | {{Abbreviation}} | Δ |
|-------------|-----------|-----|---|
| {{Move 1}} | {{gen_%}} | {{field_%}} | {{delta}} |
| {{Move 2}} | {{gen_%}} | {{field_%}} | {{delta}} |
{{Repeat for each move}}

**Key shifts**: {{Summary of how opening move distribution differs}}
{{/if}}

{{#if closing_moves}}
### Closing Move Distribution

| Closing Move | Generalist | {{Abbreviation}} | Δ |
|-------------|-----------|-----|---|
| {{Move 1}} | {{gen_%}} | {{field_%}} | {{delta}} |
{{Repeat for each move}}
{{/if}}

## Signature Phrases

{{#if signature_phrases}}
Phrases characteristic of {{field_name}} {{section_type}}, organized by function. Use when the field profile is {{abbreviation}}.

### {{Function Category 1}} Phrases

{{List phrases with examples}}

### {{Function Category 2}} Phrases

{{List phrases with examples}}

### {{Abbreviation}} Phrases to Avoid

- {{Phrase/pattern to avoid}} ({{reason}})
{{Repeat}}
{{/if}}

## Field-Specific Prohibited Moves

In addition to the general prohibited moves in SKILL.md:

### Don't Do These in {{Abbreviation}} {{Section Type}}
- **{{Prohibited move 1}}** — {{reason}}
- **{{Prohibited move 2}}** — {{reason}}
- **{{Prohibited move 3}}** — {{reason}}
{{Repeat as needed}}

## Writing Checklists

### Before Finalizing a {{Abbreviation}} {{Section Type 1}}

Verify:

- [ ] **{{Check 1 label}}**: {{Check 1 description}}
- [ ] **{{Check 2 label}}**: {{Check 2 description}}
- [ ] **{{Check 3 label}}**: {{Check 3 description}}
{{Repeat as needed}}

{{#if multiple_section_types}}
### Before Finalizing a {{Abbreviation}} {{Section Type 2}}

Verify:

- [ ] **{{Check 1 label}}**: {{Check 1 description}}
{{Repeat as needed}}
{{/if}}
```

---

## Template Variables Reference

| Variable | Source | Example |
|----------|--------|---------|
| `{{field_name}}` | User input | "Social Movement Studies" |
| `{{abbreviation}}` | User input | "SMS" |
| `{{skill_name}}` | Existing skill being profiled | "article-bookends" |
| `{{section_type}}` | Skill's target section | "introductions and conclusions" |
| `{{corpus_size}}` | Phase 1 data | "39" |
| `{{generalist_n}}` | From existing skill's SKILL.md | "80" |
| `{{generalist_venues}}` | From existing skill's SKILL.md | "*Social Problems* and *Social Forces*" |
| `{{topic_keywords}}` | Phase 0 field identification | "protest, collective action, activism" |

## How This Template Differs from Skill Templates

A field profile is **not a standalone skill** — it's a supplemental file within an existing skill's `fields/` directory. Key differences:

| Aspect | Skill (SKILL.md) | Field Profile (fields/*.md) |
|--------|-------------------|---------------------------|
| **Scope** | Covers a full article section | Adjusts one skill for one subfield |
| **Workflow** | Has its own phase files | No phase files — hooks in existing phases reference this file |
| **Clusters** | Defines contribution-type clusters | May define field-specific clusters that interact with skill clusters |
| **Benchmarks** | Generalist defaults | Overrides generalist defaults with field-specific values |
| **Standalone** | Yes | No — requires the parent skill |

## Integration with Parent Skill

After creating a field profile, verify:

1. The parent skill's `SKILL.md` has a **Field Profiles** section listing the new profile
2. The parent skill's Phase 0 file has a **field identification step** that checks `fields/`
3. All phase and technique files have **generic hooks** referencing `fields/{field}.md`
4. The field profile covers **all section types** the parent skill handles
