# Phase 5: Revision Support

## Why This Phase Matters

Identifying problems is only half the work. This phase helps the author actually address the feedback—revising theory sections, strengthening methods descriptions, clarifying findings, or adding appropriate caveats. The goal is a stronger manuscript, not just a list of things to fix.

---

## Your Tasks

### 1. Confirm Revision Priorities

Start with the user-confirmed response strategy from Phase 4:

```markdown
## Confirmed Revision Plan

### Priority 1 (Must Address)
- [ ] [Concern ID]: [Brief description] — [Section affected]
- [ ] [Concern ID]: [Brief description] — [Section affected]

### Priority 2 (Should Address)
- [ ] [Concern ID]: [Brief description] — [Section affected]
- [ ] [Concern ID]: [Brief description] — [Section affected]

### Priority 3 (Quick Fixes)
- [ ] [Concern ID]: [Brief description] — [Section affected]

### Declined (Response Only)
- [ ] [Concern ID]: [Brief description] — Response drafted
```

### 2. Commit Current State Before Revising

Before making any edits to the manuscript, stage and commit the current state so git tracks the baseline:

```bash
git add [manuscript-file] && git commit -m "peer-reviewer: Phase 4 complete, beginning revisions"
```

Then edit the manuscript in place. Git history serves as the revision trail — do NOT create version-suffixed copies (e.g., `-v2`, `-final`, `-working`).

### 3. Work Through Revisions Systematically

Address concerns in priority order. For each:

**Step 1: Locate the issue**
- Identify exact location in manuscript
- Read surrounding context
- Understand what's there now

**Step 2: Plan the revision**
- What needs to change?
- How much rewriting is required?
- Will this affect other sections?

**Step 3: Draft the revision**
- Write new/revised content directly into the manuscript file
- Maintain consistency with rest of manuscript
- Preserve author's voice

**Step 4: Verify the fix**
- Does this address the concern?
- Does it create new problems?
- Is it consistent with other sections?

### 4. Section-Specific Revision Guidance

#### Theory Section Revisions

For theoretical concerns, consider using patterns from `argument-builder`:

**Common theory revisions**:
- **Concept clarification**: Add definitional paragraph, cite sources
- **Application specificity**: Show how concept operates in your context
- **Engagement depth**: Move from citation to engagement
- **Gap sharpening**: Make the turn more specific

```markdown
### Theory Revision: [Concern ID]

**Original text**:
> [Quote from manuscript]

**Issue**: [What's wrong/missing]

**Revised text**:
> [New version]

**Changes made**:
- [Change 1]
- [Change 2]

**Citations added/modified**: [List]
```

#### Methods Section Revisions

For methodological concerns:

**Common methods revisions**:
- **Sampling clarity**: Specify selection criteria, saturation
- **Analytic transparency**: Describe coding process, provide examples
- **Validity discussion**: Address specific validity concerns
- **Data access**: Clarify what data was collected and how

```markdown
### Methods Revision: [Concern ID]

**Original text**:
> [Quote from manuscript]

**Issue**: [What's wrong/missing]

**Revised text**:
> [New version]

**Changes made**:
- [Change 1]
- [Change 2]

**New elements**: [Any new paragraphs, tables, appendices]
```

#### Findings Section Revisions

For findings concerns:

**Common findings revisions**:
- **Evidence strengthening**: Add quotes, examples
- **Claim calibration**: Adjust hedging to match evidence
- **Alternative interpretations**: Acknowledge and address
- **Connection to theory**: Make implications explicit

```markdown
### Findings Revision: [Concern ID]

**Original text**:
> [Quote from manuscript]

**Issue**: [What's wrong/missing]

**Revised text**:
> [New version]

**Changes made**:
- [Change 1]
- [Change 2]
```

### 5. Cross-Check Revisions

After completing revisions, verify:

**Internal consistency**:
- Do theory revisions align with methods and findings?
- Do methods revisions match what's described in findings?
- Are citations consistent throughout?

**Concern resolution**:
- Does each revision actually address the concern?
- Would the reviewer be satisfied?

**No new problems**:
- Did revisions introduce inconsistencies?
- Is the word count still appropriate?
- Does the argument still flow?

### 6. Commit Revisions

After completing each batch of revisions, commit to track progress:

```bash
git add [manuscript-file] && git commit -m "peer-reviewer: [brief description of revisions made]"
```

### 7. Optional: Re-Run Affected Reviewers

For major revisions, consider re-running the relevant reviewer persona:

```markdown
## Re-Review Request

**Reviewer**: [Name]
**Sections to re-review**: [List]
**Concerns addressed**: [List concern IDs]

**Question for re-review**: Does the revised manuscript now adequately address the concerns raised?
```

This can verify that revisions actually satisfy the perspective that raised the concern.

### 8. Prepare Response Document

If this is for an actual R&R, draft the response to reviewers:

```markdown
# Response to Reviewers

## Reviewer 1 [Perspective Name]

### Major Concern 1: [Title]
**Reviewer wrote**: "[Quote or summary]"

**Response**: We thank the reviewer for this observation. We have [action taken]. Specifically, [details]. See revised manuscript, [location].

### Major Concern 2: [Title]
**Reviewer wrote**: "[Quote or summary]"

**Response**: [Response]

### Minor Concerns
[Address each briefly]

---

## Reviewer 2 [Perspective Name]

[Same structure]

---

## Summary of Changes

| Section | Type of Change | Page/Para |
|---------|----------------|-----------|
| Theory | Expanded | p. 5, para 2 |
| Methods | Revised | p. 8-9 |
| Findings | Added table | p. 14 |
```

---

## Output Files to Create

1. **response-to-reviewers.md** - Draft response document (if applicable, e.g., for an actual R&R submission)

Revisions are made directly to the manuscript file. Git commits before and after revisions serve as the version trail — no separate revision log or section-specific files are needed.

---

## Guiding Principles

### Author's Voice
Revisions should sound like the author, not like a different writer. Match their style.

### Minimal Necessary Change
Fix the concern without rewriting everything. Targeted revisions are better than wholesale changes.

### Verify, Don't Assume
After revising, check that the concern is actually addressed. It's easy to think you fixed something when you didn't.

### Use Git as Your Log
Commit before and after revisions. The git history is the revision trail — don't duplicate it in separate files.

### Iterate with User
Major revisions should be reviewed by the user before moving on. Don't revise the entire manuscript without checkpoints.

---

## When You're Done

Report to the orchestrator:
- Revisions complete for [N] concerns
- Sections revised: [List]
- Changes logged
- Cross-check complete: [Pass/Issues found]
- Re-review run: [Yes/No, results]
- Response document drafted: [Yes/No]

Example summary:
> "**Revision support complete**. Addressed 4 major concerns and 5 minor concerns. Theory section: added 2 paragraphs clarifying concept application. Methods section: rewrote sampling description, added analytic transparency paragraph. Findings: added coding examples table as Appendix A. Cross-check passed—no inconsistencies found. Response to reviewers document drafted. Manuscript ready for user final review."
