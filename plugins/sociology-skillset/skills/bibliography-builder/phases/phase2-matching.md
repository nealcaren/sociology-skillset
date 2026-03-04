# Phase 2: BibTeX Matching

## Why This Phase Matters

The extracted citations are just text strings. To build a bibliography, you need the full bibliographic record from `references.bib`. This phase matches each citation to its corresponding BibTeX entry, handling ambiguities and variations.

## Your Tasks

### 1. Read references.bib

Read the `references.bib` file into memory. Parse each entry to extract:
- The entry key (e.g., `@article{smithSocialMovements2020,`)
- The `author` field
- The `year` field
- The `title` field
- All other fields needed for formatting

If the file location is uncertain, check the project root and the `references/` subdirectory.

### 2. Matching Strategy

The strategy depends on the citation format detected in Phase 0.

#### Pandoc Format (Primary — Direct Key Lookup)

For manuscripts using `[@citationKey]` syntax, matching is deterministic:

```
For each extracted citation key:
1. Look for a BibTeX entry whose key exactly matches the citation key
2. If exact match: record as Found
3. If no match: flag as Not Found (entry may need to be added to references.bib)
```

This is a direct string comparison. One lookup per citation, no ambiguity.

#### Legacy Format (Fallback — Author+Year String Matching)

For manuscripts using `(Author Year)` format, match against `.bib` entry fields:

**Step 1: Author surname + year match**
- Extract last name(s) and year from the in-text citation
- Scan BibTeX `author` and `year` fields for entries where the first author's surname and year both match

**Step 2: If multiple results, check title keywords**
- Look for distinctive words from the manuscript context
- Match against BibTeX `title` fields

**Step 3: If still ambiguous, present candidates to user**
- Show abbreviated titles from the matching `.bib` entries
- Ask user to identify the correct one

### 3. Handle Different Citation Types

#### Pandoc Format

All citation keys are handled identically — look up by entry key. No special handling needed for multi-author works.

#### Legacy Format

**Single author (Smith 2020):**
- Match surname "Smith" and year "2020" against BibTeX `author` and `year` fields
- Usually straightforward

**Two authors (Smith and Jones 2020):**
- Match both surnames against the BibTeX `author` field and year against `year`
- Verify both names appear in the matched entry

**Et al. (Smith et al. 2020):**
- Match first author surname and year
- May return multiple candidates — verify the matched entry has 3+ authors

**Year suffix (Lee 2020a, Lee 2020b):**
- Match surname and year; will return multiple candidates
- Use title keywords from manuscript context to distinguish
- User may need to identify which entry is which if context is insufficient

### 4. Record Match Status

For each citation, record:

| Status | Meaning |
|--------|---------|
| **Found** | Single unambiguous match |
| **Ambiguous** | Multiple possible matches |
| **Not Found** | No match in references.bib |
| **Year Mismatch** | Author found but year differs |
| **Name Variation** | Match found with different name form |

### 5. Build Match Table

Create a comprehensive match record.

**Pandoc format** (simplified — no ambiguity):

| Citation Key | Status | BibTeX Key | Title |
|-------------|--------|------------|-------|
| smithSocialMovements2020 | Found | smithSocialMovements2020 | "Social movements and..." |
| jonesNetworkDynamics2019 | Found | jonesNetworkDynamics2019 | "Network dynamics in..." |
| garciaImmigrantIncorp2021 | Found | garciaImmigrantIncorp2021 | "Immigrant incorporation..." |
| brownMigrationPatterns2018 | Not Found | — | — |

**Legacy format** (may have ambiguity):

| Citation | Status | BibTeX Key | Title (abbreviated) | Notes |
|----------|--------|------------|---------------------|-------|
| Smith 2020 | Found | smithSocialMovements2020 | "Social movements and..." | |
| Jones 2019 | Ambiguous | jonesOrg2019, jonesNetwork2019 | Two articles same year | User decision needed |
| García et al. 2021 | Found | garciaImmigrantIncorp2021 | Full authors: García, López, Martín | |
| Brown 2018 | Not Found | — | — | Not in references.bib |

## Output: Citation Matches

Present match results in conversation (do not save to a file):

```markdown
**Citations processed**: [X]
**Found**: [X]
**Ambiguous**: [X]
**Not Found**: [X]

## Successful Matches

| Citation | BibTeX Key | Full Reference |
|----------|------------|----------------|
| Smith 2020 | smithSocialMovements2020 | Smith, J. (2020). Social movements and change... |
| García et al. 2021 | garciaImmigrantIncorp2021 | García, M., López, R., & Martín, S. (2021)... |
| ... | ... | ... |

## Ambiguous Matches (User Decision Needed)

### Jones 2019
**In manuscript**: "(Jones 2019)" appears on p. 5, 12
**Context**: "...organizational dynamics (Jones 2019)..."

**Candidate 1**: jonesOrg2019
- Jones, A. B. (2019). Organizational theory and practice. *Journal A*.

**Candidate 2**: jonesNetwork2019
- Jones, C. D. (2019). Network dynamics in organizations. *Journal B*.

**Which is correct?** [User to specify]

## Not Found

| Citation | Match Attempted | Suggestion |
|----------|-----------------|------------|
| Brown 2018 | author surname "Brown" + year 2018 | Add entry to references.bib or check spelling |
| Williams 2021 | author surname "Williams" + year 2021 | No match — verify citation |

## Name Variations Noted

| In Manuscript | In references.bib | Status |
|---------------|-------------------|--------|
| Smith 2020 | Smith, John A. 2020 | Matched |
| García 2019 | Garcia 2019 (no accent) | Matched with variation |
```

## When You're Done

Present the match results in conversation. Ask:
1. For ambiguous matches: Which candidate is correct?
2. For not found: Should we skip these or add entries to `references.bib` first?
3. Any name variations need correction?

Once all matches are confirmed, proceed to Phase 3: Issue Review.
