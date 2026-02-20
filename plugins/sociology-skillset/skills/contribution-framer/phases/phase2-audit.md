# Phase 2: Alignment Audit (Optional)

You are checking whether existing draft sections align with the contribution profile. This phase is optional — use it when the user already has draft sections and wants to verify consistency.

## Why This Phase Matters

Draft sections often drift from the intended contribution type. An introduction may promise gap-filling while the conclusion delivers a mechanism. The audit catches these misalignments before they reach reviewers.

## Inputs

Before starting, read:
1. The contribution profile from Phase 1 (`drafts/contribution-profile.md`)
2. Whatever draft sections the user provides

## Your Tasks

### 1. Check Each Section Against the Profile

For each available draft section, verify:

**Threading Check**:
- Do the 5-8 threading terms from the profile actually appear?
- Are any key terms missing from sections where they should appear?
- Are there rogue terms (vocabulary from a different contribution type)?

**Architecture Check**:
- Does the section's structure match the profile's template?
- Are findings organized according to the contribution type's logic (stages for PT, dimensions for CB, competing accounts for FI)?

**Move Check**:
- Does the section execute its signature move?
- Does the section commit any prohibited moves?

### 2. Flag Misalignments

For each misalignment found, specify:
- **Section**: Which section has the problem
- **Expected**: What the profile says this section should do
- **Found**: What the section actually does
- **Severity**: High (wrong contribution type), Medium (missing signature move), Low (missing threading term)
- **Fix**: Specific revision suggestion

### 3. Check Cross-Section Consistency

Beyond individual sections, check:
- Does the abstract's contribution claim match the conclusion's delivery?
- Does the introduction's promise match the findings' organization?
- Does the theory section's gap/lacuna match the conclusion's contribution claim?
- Are there contradictory framing signals (e.g., gap vocabulary in intro + mechanism vocabulary in conclusion)?

### 4. Generate Alignment Report

```markdown
# Alignment Audit Report

## Overall Assessment
**Alignment**: [Strong / Moderate / Weak]
**Primary issue**: [Brief description of biggest misalignment, if any]

## Section-by-Section

### Abstract
- **Threading**: [✓ / ✗] [details]
- **Architecture**: [✓ / ✗] [details]
- **Signature move**: [✓ / ✗] [details]

### Introduction
- **Threading**: [✓ / ✗] [details]
- **Architecture**: [✓ / ✗] [details]
- **Signature move**: [✓ / ✗] [details]

[Continue for each available section...]

## Cross-Section Consistency
- **Abstract ↔ Conclusion**: [aligned / misaligned — details]
- **Introduction ↔ Findings**: [aligned / misaligned — details]
- **Theory ↔ Conclusion**: [aligned / misaligned — details]

## Revision Recommendations

### High Priority
1. [Specific revision with section, current text, suggested change]

### Medium Priority
1. [Specific revision]

### Low Priority
1. [Specific revision]

## Threading Vocabulary Audit

| Term | Abstract | Intro | Theory | Methods | Findings | Conclusion |
|------|----------|-------|--------|---------|----------|------------|
| [term 1] | ✓/✗ | ✓/✗ | ✓/✗ | ✓/✗ | ✓/✗ | ✓/✗ |
| [term 2] | ✓/✗ | ✓/✗ | ✓/✗ | ✓/✗ | ✓/✗ | ✓/✗ |
| ... | ... | ... | ... | ... | ... | ... |
```

## When You're Done

Return the alignment report to the orchestrator. If misalignments are found, recommend specific sections for revision using the relevant downstream skill (argument-builder for theory, article-bookends for intro/conclusion, abstract-builder for abstract).
