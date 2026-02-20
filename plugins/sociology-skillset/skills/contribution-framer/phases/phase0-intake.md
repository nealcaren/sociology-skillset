# Phase 0: Intake & Classification

You are classifying the user's article into one of five contribution types. This classification determines the cross-section framing template that will guide all downstream writing.

## Why This Phase Matters

Misclassifying the contribution type produces misaligned sections — an introduction that promises one thing and a conclusion that delivers another. Getting the type right here prevents costly rewrites later.

## Your Tasks

### 1. Gather Available Materials

Request whatever the user has:
- **Research question or puzzle** (required)
- **Main argument or key finding** (required)
- **Data/methods description** (required)
- **Theory/literature review section** (ideal — best signal for classification)
- **Findings section** (ideal — reveals how contribution is delivered)
- **Abstract** (helpful — often states the contribution type directly)
- **Target journal** (helpful — calibrates expectations)

### 2. Apply the Decision Tree

Work through these questions in order:

**Question 1: Does the article coin or introduce a new term/concept?**
- Look for: a new coined term, a redefined concept, a typology with new names
- If YES → **Concept-Building**
- If NO → continue

**Question 2: Does the article name an existing theoretical framework and apply it to a new domain?**
- Look for: a named framework (field theory, world polity theory, inhabited institutions) applied to a domain the original formulation didn't address
- If YES → **Theory-Extension**
- If NO → continue

**Question 3: Does the article show HOW a process/mechanism works?**
- Look for: sequential stages, pathways, steps; the article promises to trace a process
- If YES → **Process-Tracing**
- If NO → continue

**Question 4: Does the article adjudicate between competing explanations?**
- Look for: "not X but Y," "contrary to," competing accounts given equal theoretical weight
- If YES → **Factor-Identifying**
- If NO → continue

**Question 5: Does the article document an empirical pattern where little prior work exists?**
- Look for: "first to," "little research has," enumerated contribution list
- If YES → **Gap-Filler**

### 3. Check for Hybrid Types

If the article seems to combine types, classify by the **dominant rhetorical move**:

| Hybrid | Classification Rule |
|--------|-------------------|
| Concept + Mechanism | **Concept-Building** if term is coined; **Process-Tracing** if mechanism is traced but not named with a new term |
| Adjudication + Framework | **Factor-Identifying** if adjudication is the punchline; **Theory-Extension** if framework is the scaffolding |
| Gap-filling + Mechanism | **Process-Tracing** if mechanism is named; **Gap-Filler** if contributions are enumerated |

### 4. Calibrate for Target Journal

If the user names a target journal, apply these calibrations:

| Journal | Note |
|---------|------|
| AJS | Mechanism-heavy (PT + FI combined ~55%). Concept-Building also strong. Gap-Filler rare |
| ASR | Concept-Building is modal (32%). Gap-Filler very rare (6%). Theory-Extension at ~12% |
| SP/SF | Most balanced distribution. Gap-Filler more accepted (~10%). All types viable |

**Warning**: If the user has a Gap-Filler article targeting AJS or ASR, flag this and discuss whether reframing as PT (add a mechanism) or CB (coin a term) would strengthen the submission.

### 5. Confirm with User

Present your classification with:
1. **Contribution type** and rationale (which decision tree question triggered it)
2. **Confidence level** (high if clear, moderate if borderline, low if hybrid)
3. **Alternative type** (if the article could go either way, name the runner-up)
4. **Journal fit** (if target journal named, how this type fits)

## Output

```markdown
## Contribution Classification

**Type**: [Process-Tracing / Concept-Building / Factor-Identifying / Theory-Extension / Gap-Filler]

**Rationale**: [Which decision tree question triggered this classification]

**Confidence**: [High / Moderate / Low]

**Alternative**: [Runner-up type, if any, with explanation of why primary was chosen]

**Target journal**: [Journal name, if provided]

**Journal fit**: [How this type fits the target journal's distribution]

**Key terms identified** (preliminary):
1. [Term 1 — likely threading term]
2. [Term 2]
3. [Term 3]
4. [Term 4]
5. [Term 5]
```

## When You're Done

Return the classification to the orchestrator and **pause** for user confirmation before proceeding to Phase 1 (Profile Generation). The user must agree with the contribution type before the profile is generated.
