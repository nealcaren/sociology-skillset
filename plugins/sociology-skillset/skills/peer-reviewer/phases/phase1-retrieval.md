# Phase 1: Literature Retrieval

## Why This Phase Matters

Reviewer personas must be grounded in actual texts, not stereotypes. This phase retrieves full texts from the project's reference library for each confirmed reviewer perspective. The quality of the simulated review depends entirely on having substantive sources to read—we're building personas from what these scholars actually wrote, not from secondhand summaries.

---

## Your Tasks

### 1. Confirm Reviewer List

Start with the user-confirmed reviewer list from Phase 0. For each reviewer:

```markdown
## Confirmed Reviewers

1. **[Reviewer 1 Name/Perspective]**
   - Type: [Specific scholar / Theoretical camp]
   - Review focus: [Theory + Findings] OR [Methods + Findings]

2. **[Reviewer 2 Name/Perspective]**
   - Type: [Specific scholar / Theoretical camp]
   - Review focus: [Theory + Findings] OR [Methods + Findings]

3. **[Reviewer 3 Name/Perspective]** (if applicable)
   - Type: [Specific scholar / Theoretical camp]
   - Review focus: [Theory + Findings] OR [Methods + Findings]
```

### 2. Retrieve Sources for Each Reviewer

For each confirmed reviewer, search `references.bib` to find relevant sources.

**Search strategies**:

```bash
# For specific scholars (search by author field):
grep -i "author.*Lareau" references.bib -A 20 | grep -E "author|title|year|md_path"
grep -i "author.*Bourdieu" references.bib -A 20 | grep -E "author|title|year|md_path"

# For theoretical keywords (search across all fields):
grep -i "cultural capital" references.bib -B 5 -A 20 | grep -E "@|author|title|year|md_path"
grep -i "field theory" references.bib -B 5 -A 20 | grep -E "@|author|title|year|md_path"

# For year-range filtering:
grep -i "author.*Lareau" references.bib -A 20 | grep -E "year.*200[0-9]|year.*201[0-9]"
```

**Prioritize sources**:
1. **Foundational works** - The canonical text(s) that define the perspective
2. **Methodological statements** - Where they explain how to do research their way
3. **Recent work** - Shows current thinking and evolution
4. **Critiques of others** - Reveals what they value and what they reject

### 3. Retrieve Full Texts

For each identified source, read the full text using the `md_path` field from the `.bib` entry:

```bash
# Extract the md_path for a given citation key:
grep -A 30 "@.*{LareauUnequal2003" references.bib | grep "md_path"

# Then read the file at that path:
# Read: library/markdown/lareau_unequal_2003.md
```

If no `md_path` is present for a source, note it as unavailable for full-text reading.

Track retrieval status:

```markdown
## Source Retrieval: [Reviewer Perspective]

| Citation Key | Author(s) | Year | Title | Full Text? | Priority |
|--------------|-----------|------|-------|------------|----------|
| LareauUnequal2003 | Lareau | 2003 | Unequal Childhoods | Yes | Foundational |
| LareauUnequal2011 | Lareau | 2011 | Unequal Childhoods 2nd ed | Yes | Recent |
| LareauWeininger2003 | Lareau & Weininger | 2003 | Cultural capital in educational research | Yes | Methodological |
| LareauCultural2015 | Lareau | 2015 | Cultural knowledge and social inequality | No | Recent |
```

### 4. Assess Source Quality

For each reviewer, evaluate whether retrieved sources are sufficient:

**Strong foundation** (proceed confidently):
- 3+ full texts available
- Includes at least one foundational work
- Covers theoretical AND methodological/empirical dimensions

**Adequate foundation** (proceed with caution):
- 2 full texts available
- At least one substantive theoretical piece
- May need to note limitations in persona

**Weak foundation** (flag for user):
- 0-1 full texts available
- Missing foundational works
- User should add sources or reconsider perspective

```markdown
## Source Quality Assessment

| Reviewer | Full Texts | Foundational? | Methodological? | Assessment |
|----------|------------|---------------|-----------------|------------|
| Lareau | 4 | Yes | Yes | Strong |
| Interview methods | 2 | Yes | Yes | Adequate |
| Critical education | 1 | No | No | Weak - flag |
```

### 5. Organize Sources by Reviewer

Create a structured source list for each reviewer:

```markdown
## Sources for Reviewer: [Name/Perspective]

### Foundational Works
1. **[Title]** ([Year])
   - Citation key: [key]
   - Relevance: [Why this is foundational for this perspective]

### Methodological/Theoretical Statements
2. **[Title]** ([Year])
   - Citation key: [key]
   - Relevance: [What this reveals about their approach]

### Recent/Applied Work
3. **[Title]** ([Year])
   - Citation key: [key]
   - Relevance: [How this shows current thinking]

### Total: [N] sources with full text
```

### 6. Note Gaps and Limitations

Document any limitations for Phase 2:

```markdown
## Retrieval Limitations

### Reviewer: [Name]
- **Gap**: [Missing type of source]
- **Impact**: [How this affects persona construction]
- **Mitigation**: [How we'll handle this]

### Overall Assessment
[Summary of retrieval quality across all reviewers]
```

---

## Output Files to Create

None — present retrieval results (grep searches, source lists organized by reviewer, quality assessments, and any flags) in conversation for user review.

---

## Reference Library Reference

Key operations for this phase:

| Operation | Command |
|-----------|---------|
| **Semantic search** | `uv run plugins/sociology-skillset/scripts/rag.py search "concept or question"` |
| Search by author | `grep -i "author.*LastName" references.bib -A 20` |
| Search by keyword | `grep -i "keyword" references.bib -B 5 -A 20` |
| Search by year | `grep -i "author.*Name" references.bib -A 20 \| grep "year.*20XX"` |
| Get citation key | `grep -B 1 "author.*LastName" references.bib \| grep "@"` |
| Get md_path | `grep -A 30 "@.*{CitationKey" references.bib \| grep "md_path"` |
| Read full text | Read the file at the `md_path` value from the `.bib` entry |

**Tip**: Use `rag.py search` for conceptual/semantic search (finding passages about a topic even when exact keywords differ). Use `grep` for exact keyword or metadata lookups. Both complement each other.

---

## Guiding Principles

### Full Text Is Essential
Metadata alone isn't enough. We need to read what they actually wrote to build an informed persona.

### Quality Over Quantity
3 deeply relevant sources beat 10 tangentially related ones.

### Foundational Works Matter Most
The canonical texts define the perspective; recent work shows evolution.

### Note What's Missing
If a key work isn't available in `library/markdown/` (no `md_path` or file absent), flag it. The user may be able to add it.

---

## When You're Done

Report to the orchestrator:
- Sources retrieved for each reviewer
- Full text availability summary
- Any weak foundations flagged
- Ready for user review of source lists

Example summary:
> "**Retrieval complete**. Reviewer 1 (Lareau): 4 sources found in references.bib, all with full text in library/markdown/, strong foundation. Reviewer 2 (Interview methods): 3 sources found, all with full text, adequate foundation. Reviewer 3 (Critical education): Only 1 source with full text in library/markdown/—flagging for user. May need to add Bowles & Gintis or similar to references.bib, or reconsider this perspective. Sources organized and ready for user review before persona construction."
