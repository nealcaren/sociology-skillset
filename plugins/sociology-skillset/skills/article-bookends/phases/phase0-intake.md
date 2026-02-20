# Phase 0: Intake & Assessment

You are assessing the user's materials and identifying the appropriate cluster style for their introduction and conclusion.

## Why This Phase Matters

The introduction and conclusion must match the contribution type. A gap-filler article needs different framing than a concept-building article. Before drafting, you must understand what kind of contribution the user is making and align the framing accordingly.

## Your Tasks

### 1. Gather Required Materials

Request these materials if not provided:
- **Theory/Literature Review section** (required)
- **Findings section** (required)
- **Abstract** (helpful but optional)
- **Target journal** (helpful for calibrating length/style)

### 1.5. Identify Target Field

Determine whether a field-specific profile applies. Ask the user about their target venue or subfield, then check the `fields/` directory for available profiles.

If a field profile exists for the user's target field, read the corresponding `fields/{field}.md` file. This file contains all field-specific benchmarks, structural patterns, signature phrases, and writing checklists. It will be the single reference for field-specific guidance throughout all remaining phases.

**Note**: Field profiles are additive — they adjust benchmarks and add field-specific patterns on top of the contribution-type cluster (Gap-Filler, Theory-Extension, etc.). Both dimensions apply simultaneously.

### 2. Read and Analyze the Theory Section

Identify the **positioning move**:

| Positioning | Indicators |
|-------------|------------|
| **Gap-filling** | "Little research has examined...", "We know less about...", identifies empirical gap |
| **Mechanism-identification** | "We identify the mechanism...", "How does X produce Y?", names a causal process, spells out causal chain |
| **Theory-extension** | Names specific framework, "X theory suggests...", applies existing framework to new domain |
| **Concept-building** | Introduces new term, critiques existing concepts, presents typology |
| **Synthesis** | Connects multiple literatures, "Drawing together...", integrates traditions |
| **Debate-resolution** | "Scholars disagree...", adjudicates between positions |

Identify the **arc structure**:
- Funnel (broad → specific)
- Building-blocks (concept → concept → concept)
- Dialogue (position 1 → position 2 → synthesis)

### 3. Read and Analyze the Findings Section

Identify:
- **Main argument** (the central claim)
- **Key mechanisms/findings** (the pillars)
- **Empirical scope** (who was studied, where, when)
- **Level of theoretical ambition** (description vs. explanation vs. new concept)

### 4. Assign Cluster Membership

Based on your analysis, assign the article to one of six clusters:

| Cluster | Key Indicators | Prevalence |
|---------|----------------|------------|
| **Gap-Filler Minimalist** | Empirical gap, funnel structure, substantive focus | 38.8% (SP/SF) |
| **Theory-Extension** | Named framework, application to new domain | 22.5% (SP/SF) |
| **Concept-Building** | New term introduced, conceptual critique | 15.0% (SP/SF) |
| **Synthesis Integrator** | Multiple traditions connected, integration claims | 17.5% (SP/SF) |
| **Problem-Driven Pragmatist** | Policy stakes, debate framing, empirical focus | 15.0% (SP/SF) |
| **Mechanism-Identifier** | Names causal mechanism, how/why question, mechanism developed over 2–4 paragraphs | 55% (AJS) |

**Target journal matters**: If the user is targeting *AJS* or *ASR*, check for Mechanism-Identifier first — it is the dominant cluster at high-status journals. If targeting *Social Problems* or *Social Forces*, the original five clusters are the primary options.

### 5. Confirm Scope

Ask the user:
- Do you need an **introduction only**, **conclusion only**, or **both**?
- What is your **target word count** for each section?
- Are there **specific elements** you want emphasized (e.g., policy implications)?

## Cluster-Specific Implications

### If Gap-Filler Minimalist:
- **Introduction**: Keep short (~600-700 words), phenomenon-led opening, data mention early
- **Conclusion**: Plan for length (~1,200-1,400 words), emphasis on implications
- **Ratio**: Conclusion should be ~2x introduction length

### If Theory-Extension:
- **Introduction**: Consider theory-led opening, name framework early
- **Conclusion**: Framework affirmation, moderate length
- **Ratio**: Closer to 1.4x

### If Concept-Building:
- **Introduction**: Longer to motivate conceptual need, include roadmap
- **Conclusion**: Can be proportionally brief if concept proven in findings
- **Ratio**: Nearly balanced (~1.0x)
- **Risk**: Higher deflation risk—calibrate ambition carefully

### If Synthesis Integrator:
- **Introduction**: Name multiple traditions, preview integration
- **Conclusion**: Must return to each tradition, integration claims
- **Risk**: Zero deflation tolerance—if you promise synthesis, deliver it

### If Problem-Driven Pragmatist:
- **Introduction**: Stakes-led or case-led opening, policy context
- **Conclusion**: Policy implications, may escalate to broader claims
- **Opportunity**: Escalation is common and acceptable

### If Mechanism-Identifier:
- **Introduction**: Phenomenon, case, or question-led opening. Name the mechanism and develop it over 2–4 paragraphs. No roadmap, no contribution list. Aim for 900–1,400 words.
- **Conclusion**: Affirm the mechanism worked. Return to opening case/puzzle. (Provisional — conclusion benchmarks pending empirical analysis.)
- **Ratio**: Estimated ~1.2–1.5x
- **Risk**: Named mechanisms create clear expectations — deflation occurs if conclusion retreats to "consistent with" rather than "demonstrates"

## Field-Specific Implications

When a field profile was identified in Step 1.5, consult the `fields/{field}.md` file for field-specific implications. The field profile will specify:

- Adjusted word count and paragraph count targets
- Field-specific opening move distributions
- Structural patterns unique to the field
- Roadmap and citation timing expectations
- Audience assumptions and vocabulary conventions
- Field-specific cluster selection guidance (if applicable)

Include the field profile and relevant field-specific cluster in the output summary.

## Output

Provide a summary with:

1. **Cluster assignment** and rationale (which cluster, why)
2. **Field profile** (if applicable — which field, which field-specific cluster if any)
3. **Contribution type** (gap-filling, extension, building, synthesis, debate)
4. **Main argument** (one sentence)
5. **Key findings** (3-4 bullets)
6. **Recommended approach**:
   - Introduction opening move (adjusted for field profile if applicable)
   - Introduction target length (field-adjusted benchmarks if applicable)
   - Conclusion target length
   - Key elements to include
   - Field-specific structural pattern to use (if field profile applies)
7. **Coherence considerations** (what promises must the intro make for the conclusion to deliver?)

## When You're Done

Return your assessment to the orchestrator and **pause** for user confirmation before proceeding to drafting.
