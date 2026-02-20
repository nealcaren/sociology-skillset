# Phase 1: Profile Generation

You are generating a complete contribution profile that will guide all downstream writing skills. The contribution type was identified in Phase 0; now you build the full cross-section template.

## Why This Phase Matters

The contribution profile is the single source of truth for how this article's contribution should be framed across all sections. Argument-builder, article-bookends, and abstract-builder will all read this profile. Inconsistencies here propagate everywhere.

## Inputs

Before starting, read:
1. The Phase 0 classification (contribution type, key terms, rationale)
2. The relevant cluster guide from `clusters/[type].md`
3. Whatever user materials are available (theory section, findings, abstract, research question)

## Your Tasks

### 1. Read the Cluster Guide

Read `clusters/[contribution-type].md` for the classified type. This contains:
- Cross-section template (what each section should do)
- Signature moves (what to do)
- Prohibited moves (what to avoid)
- Vocabulary threading pattern
- Exemplar articles

### 2. Identify Threading Vocabulary

From the user's materials, identify 5-8 key terms that should echo across all sections:

**For Process-Tracing**:
- The mechanism name
- Stage/step vocabulary (the sequential terms)
- Domain vocabulary (the empirical case)
- Outcome vocabulary (what the mechanism produces)

**For Concept-Building**:
- The coined term
- Definitional vocabulary (the concept's components/dimensions)
- Inadequacy vocabulary (what existing concepts miss)
- Domain vocabulary (the empirical case)

**For Factor-Identifying**:
- Account labels (names for competing explanations)
- Adjudication vocabulary ("contrary to," "rather than")
- Winning-account vocabulary
- Evidence vocabulary (what tests are used)

**For Theory-Extension**:
- Framework name and canonical terms
- Domain vocabulary (the new empirical site)
- Extension vocabulary ("extending," "applying," "building on")
- Boundary-condition vocabulary

**For Gap-Filler**:
- Gap vocabulary ("little research," "understudied," "first to")
- Enumeration vocabulary ("first," "second," "third")
- Contribution-claim vocabulary
- Implication vocabulary

### 3. Generate the Section-by-Section Template

For each section, specify:
- **What this section does** (its rhetorical function for this contribution type)
- **Structure** (how subsections/paragraphs should be organized)
- **Key threading terms** (which of the 5-8 terms appear here)
- **Signature move** (the single most important thing this section must do)
- **Prohibited move** (the single most important thing to avoid)

Sections to cover:
1. Abstract
2. Introduction
3. Theory/Literature Review
4. Methods
5. Findings
6. Conclusion

### 4. Generate the Contribution Profile

Write the profile as a single markdown document:

```markdown
# Contribution Profile

## Classification
- **Type**: [type]
- **Confidence**: [high/moderate/low]
- **Target journal**: [journal]

## Core Contribution Statement
[One sentence: what this article contributes, stated in the vocabulary of the contribution type]

## Threading Vocabulary
| Term | Role | Sections Where It Appears |
|------|------|--------------------------|
| [term 1] | [mechanism name / coined concept / etc.] | Abstract, Intro, Theory, Findings, Conclusion |
| [term 2] | [stage vocabulary / dimension / etc.] | Theory, Methods, Findings |
| [term 3] | ... | ... |
| ... | ... | ... |

## Section-by-Section Template

### Abstract
- **Function**: [what the abstract does for this type]
- **Key move**: [the single most important move]
- **Threading terms**: [which terms appear]
- **Avoid**: [what to avoid]

### Introduction
- **Function**: [what the introduction does]
- **Recommended opening move**: [phenomenon-led / theory-led / etc.]
- **Key move**: [e.g., name mechanism by paragraph 3]
- **Threading terms**: [which terms appear]
- **Avoid**: [what to avoid]

### Theory/Literature Review
- **Function**: [what the theory section does]
- **Structure**: [e.g., genealogy → gap → mechanism derivation]
- **Key move**: [e.g., derive mechanism steps from literature]
- **Threading terms**: [which terms appear]
- **Avoid**: [what to avoid]

### Methods
- **Function**: [what methods does for this type]
- **Key move**: [e.g., explain why design reveals the process]
- **Threading terms**: [which terms appear]

### Findings
- **Function**: [what findings does]
- **Structure**: [e.g., organized by mechanism stages]
- **Subsection logic**: [what each subsection corresponds to]
- **Threading terms**: [which terms appear]
- **Avoid**: [what to avoid]

### Conclusion
- **Function**: [what conclusion does]
- **Key move**: [e.g., affirm mechanism, generalize]
- **Threading terms**: [which terms appear]
- **Avoid**: [what to avoid]

## Signature Moves Checklist
- [ ] [Move 1 — from cluster guide]
- [ ] [Move 2]
- [ ] [Move 3]
- [ ] [Move 4]

## Prohibited Moves
- [ ] Avoid: [prohibited move 1]
- [ ] Avoid: [prohibited move 2]
- [ ] Avoid: [prohibited move 3]

## Downstream Skill Instructions
- **argument-builder**: Use [specific cluster/arc] to match this contribution type
- **article-bookends**: Use [specific cluster] for intro/conclusion
- **abstract-builder**: Use [specific archetype] for abstract
```

### 5. Map to Downstream Skills

For each downstream skill, specify which cluster or archetype the profile maps to:

| Contribution Type | argument-builder | article-bookends | abstract-builder |
|-------------------|-----------------|------------------|------------------|
| Process-Tracing | Mechanism-Identifier cluster | Mechanism-Identifier cluster | Process archetype |
| Concept-Building | Concept-Building cluster | Concept-Building cluster | Concept archetype |
| Factor-Identifying | (use parallel-accounts arc) | Mechanism-Identifier or Gap-Filler cluster | Adjudication archetype |
| Theory-Extension | Theory-Extension cluster | Theory-Extension cluster | Extension archetype |
| Gap-Filler | Gap-Filler cluster | Gap-Filler Minimalist cluster | Gap archetype |

Note: Not all downstream skills have exact 1:1 cluster matches. The profile should specify the closest match and note any adaptations needed.

## Output

Save the contribution profile to `drafts/contribution-profile.md` (or the path specified in `project.yaml`).

## When You're Done

Return the profile to the orchestrator and **pause** for user review. The user should confirm:
1. The threading vocabulary captures their key terms
2. The section-by-section template matches their intentions
3. The downstream skill mappings make sense

Once confirmed, the profile can be passed to argument-builder, article-bookends, or abstract-builder.
