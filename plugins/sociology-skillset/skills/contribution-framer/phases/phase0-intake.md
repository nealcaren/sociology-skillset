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

### 4. Identify Target Field

Determine whether a field-specific profile applies. Ask the user about their target venue or subfield, then check the `fields/` directory for available profiles.

If a field profile exists for the user's target field, read the corresponding `fields/{field}.md` file. This file contains all field-specific calibration adjustments, distribution expectations, and prohibited moves. It will be the single reference for field-specific guidance throughout all remaining phases.

**Note**: Field profiles are additive — they adjust distribution expectations on top of the contribution-type classification. Both dimensions apply simultaneously.

### 5. Assess Venue Positioning

Before calibrating for a specific journal, assess two dimensions that shape venue fit. These patterns are based on small samples (~20–70 articles per journal) and should be treated as suggestive tendencies:

**a. Theoretical reach**: Does the article connect to sociological theory beyond its subfield?

- **Domain-bridging** → flagship positioning is viable. The article speaks to general sociological questions (inequality, institutions, culture, power) through its specific topic.
- **Domain-internal** → field journal is the natural home. The article advances understanding within its subfield. This is a legitimate and valued contribution at field-specific venues.

**b. Claim scope**: How broadly do the conclusions reach?

- **Context-bounded** ("in this case, we found...") → tends to be uncommon at AJS, ASR, and SF. More accepted at SP and at field journals.
- **Domain-bounded** ("for [topic area], these patterns hold...") → accepted at all venues.
- **Generalizing** ("this tells us about [broad social process]") → common at ASR and SF.

**c. Methods-venue fit** (suggestive patterns):

- Interview-only or ethnographic work tends to appear at SP, ASR (occasionally), or field journals — less common at AJS or SF
- Large-N administrative/archival work appears everywhere but is especially concentrated at AJS, SF, and Mobilization
- SP tends to be the most methodologically diverse flagship

Present these observations to the user as tendencies, not rules. A single article can always be the exception.

### 6. Calibrate for Target Journal

If the user names a target journal, apply these calibrations:

| Journal | Contribution type notes | Venue positioning notes |
|---------|------------------------|------------------------|
| AJS | Mechanism-heavy (PT + FI combined ~55%). CB also strong. GF rare | Quantitative-leaning; very high domain-bridging; context-bounded claims rare |
| ASR | CB is modal (32%). GF very rare (6%). TE at ~12% | Broad methods; high domain-bridging; frequently generalizing claims |
| Social Problems | Balanced distribution. GF more accepted (~10%). All types viable | Qualitative-friendly (interviews, ethnography common); high domain-bridging; more tolerant of context-bounded claims than other flagships |
| Social Forces | Balanced distribution. GF more accepted (~10%). All types viable | Quantitative-leaning (admin data, experiments, computational); high domain-bridging; frequently generalizing; context-bounded rare |
| SMS | CB-heavy (33%), GF-tolerant (31%). PT rare (6%). Qualitative-friendly | Single-case and non-US work common; often domain-internal; context-bounded accepted |
| Mobilization | FI-heavy (38%), CB strong (36%). PT rare (7%). Quantitative adjudication niche | Large-N and US-centric; often domain-internal; context-bounded accepted |

**Flagship warning**: If the user has a Gap-Filler article targeting AJS or ASR, flag this and discuss whether reframing as PT (add a mechanism) or CB (coin a term) would strengthen the submission.

**Field journal note**: If targeting SMS or Mobilization, GF is a normal, accepted contribution type — do not pressure users to reframe. PT framing may be better positioned at a flagship.

**SP vs. SF note**: These two journals have different tendencies despite often being grouped together. SP tends to welcome qualitative, case-based work with theoretical ambition. SF tends toward quantitative work with generalizing claims. Consider which journal fits the article's methods and claim scope.

### 7. Confirm with User

Present your classification with:
1. **Contribution type** and rationale (which decision tree question triggered it)
2. **Confidence level** (high if clear, moderate if borderline, low if hybrid)
3. **Alternative type** (if the article could go either way, name the runner-up)
4. **Venue positioning** (theoretical reach and claim scope assessment)
5. **Journal fit** (if target journal named, how this type and positioning fit)

## Output

```markdown
## Contribution Classification

**Type**: [Process-Tracing / Concept-Building / Factor-Identifying / Theory-Extension / Gap-Filler]

**Rationale**: [Which decision tree question triggered this classification]

**Confidence**: [High / Moderate / Low]

**Alternative**: [Runner-up type, if any, with explanation of why primary was chosen]

**Target journal**: [Journal name, if provided]

**Field profile**: [Social Movements / None — which field profile applies, if any]

**Venue positioning**:
- Theoretical reach: [Domain-bridging / Domain-internal — with brief rationale]
- Claim scope: [Context-bounded / Domain-bounded / Generalizing]
- Methods fit: [Brief note on how methods align with target venue tendencies]

**Journal fit**: [How this type and positioning fit the target journal]

**Key terms identified** (preliminary):
1. [Term 1 — likely threading term]
2. [Term 2]
3. [Term 3]
4. [Term 4]
5. [Term 5]
```

## When You're Done

Return the classification to the orchestrator and **pause** for user confirmation before proceeding to Phase 1 (Profile Generation). The user must agree with the contribution type before the profile is generated.
