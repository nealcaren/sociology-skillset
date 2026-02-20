---
name: contribution-framer
description: Identify your article's contribution type and generate a cross-section vocabulary threading template. Feeds into argument-builder, article-bookends, and abstract-builder for consistent framing across all sections. Based on analysis of 197 articles from AJS, ASR, Social Problems, Social Forces, Social Movement Studies, and Mobilization.
---

# Contribution Framer

You help sociologists identify the **contribution type** of their article and generate a **cross-section framing template** that ensures consistent positioning across all sections — abstract, introduction, theory, methods, findings, and conclusion. Your guidance is grounded in systematic analysis of 115 articles from *AJS*, *ASR*, *Social Problems*, and *Social Forces*.

## Why This Skill Exists

Every article makes one primary contribution, but that contribution must be framed consistently across every section. A Process-Tracing article organizes findings by mechanism stages, names the mechanism in the abstract, and affirms it in the conclusion. A Concept-Building article motivates a conceptual lacuna in the theory section, builds the concept through data, and demonstrates portability in the conclusion.

Without a unified framing template, downstream skills (argument-builder, article-bookends, abstract-builder) may identify different contribution types independently — producing an introduction that frames one kind of contribution and a conclusion that delivers another. The contribution-framer prevents this by creating a single profile early in the workflow.

## Project Integration

This skill reads from `project.yaml` when available:

```yaml
# From project.yaml
paths:
  drafts: drafts/sections/
```

**Project type:** This skill works for **all project types** (qualitative, quantitative, mixed methods). Contribution types are rhetorical strategies, not method-specific.

Updates `progress.yaml` when complete:
```yaml
status:
  contribution_profile: done
artifacts:
  contribution_profile: drafts/contribution-profile.md
```

## Connection to Other Skills

This skill is an **upstream dependency** for three writing skills:

| Skill | How It Uses the Profile |
|-------|------------------------|
| **argument-builder** | Matches theory section architecture to contribution type (e.g., PT → derive mechanism steps; FI → parallel competing accounts) |
| **article-bookends** | Matches introduction/conclusion structure to contribution type (e.g., CB → motivate lacuna in intro, consolidate concept in conclusion) |
| **abstract-builder** | Matches abstract archetype and move sequence to contribution type |

**Ideal sequence**: Run contribution-framer FIRST, then pass the contribution profile to downstream skills. Each downstream skill reads the profile and adapts its cluster selection, structure, and vocabulary accordingly.

**Can also run standalone**: If the user already has drafts and wants to check contribution alignment, the skill can audit existing sections for threading consistency.

## When to Use This Skill

Use this skill when users want to:
- Identify what type of contribution their article makes before drafting
- Generate a vocabulary threading template for consistent framing
- Check whether their existing draft sections align on the same contribution type
- Decide how to position an ambiguous contribution (hybrid types)
- Calibrate their contribution framing for a specific target journal

**Minimum input needed**:
- Research question or puzzle
- Main argument or key finding
- Data/methods description
- Target journal (optional but useful for calibration)

**Ideal input**:
- Theory/literature review section (draft or notes)
- Findings section (draft or notes)
- Abstract (if available)

## Core Principles (from Genre Analysis)

Based on systematic analysis of 115 articles across four top sociology journals:

### 1. One Article, One Primary Contribution Type
Every article makes one dominant contribution. Hybrids exist, but the abstract and conclusion reveal which type is primary. Classify by the dominant rhetorical move.

### 2. Opening Move ≠ Contribution Type
The introduction's opening move (phenomenon-led, theory-led, etc.) is a separate dimension from the contribution type. Many articles use a gap-filling opening move but pursue mechanism-identification or concept-building. Don't confuse how the article opens with what it contributes.

### 3. Vocabulary Threading Is Universal
90% of articles thread 5-8 key terms across ALL sections. The mechanism name, the coined concept, the competing account labels — these terms echo from abstract through conclusion. Strong threading is the norm, not the exception.

### 4. Contribution Type Determines Section Architecture
Each contribution type produces a distinctive structure at every section level. Process-Tracing organizes findings by mechanism stages. Concept-Building organizes findings by concept dimensions. Factor-Identifying organizes findings by comparative tests. The contribution type isn't just framing — it's architecture.

### 5. Journal Calibration Matters
ASR runs heavier on Concept-Building (32%) and lighter on Gap-Filler (6%). SP and SF have different profiles despite often being grouped together. Gap-Filling alone is risky at high-status journals; consider whether the contribution can be reframed.

### 6. Venue Positioning Is a Separate Dimension from Contribution Type
Based on coding ~230 articles on dimensions beyond contribution type, the single strongest differentiator between flagship and field-journal articles is **theoretical reach** — whether an article connects to sociology writ large or stays within its subfield. An article's contribution type (PT, CB, FI, etc.) and its venue positioning (flagship vs. field journal) are independent dimensions. The same Factor-Identifying article can be domain-internal (→ Mobilization) or domain-bridging (→ flagship).

## The 5 Contribution Types

| Type | Prevalence | Punchline | Signal Phrases |
|------|-----------|-----------|----------------|
| **Process-Tracing** | ~27% | Shows HOW (mechanism) | "works through," "the mechanism by which," "produces" |
| **Concept-Building** | ~27% | Names WHAT (new concept) | "we introduce," "we term," "the concept of" |
| **Factor-Identifying** | ~24% | Shows WHICH (account wins) | "contrary to," "not X but Y," "which factor" |
| **Theory-Extension** | ~11% | Shows WHERE (framework applies) | "extending," "applying X to Y," framework terms |
| **Gap-Filler** | ~9% | Shows THAT (exists) | "first to," "little research has," enumerated list |

See `clusters/` directory for detailed profiles with cross-section templates, signature moves, and exemplars.

## Contribution Type Decision Tree

1. **Does the article coin or introduce a new term/concept?**
   - Yes → **Concept-Building**
   - No → continue

2. **Does the article name an existing theoretical framework and apply it to a new domain?**
   - Yes → **Theory-Extension**
   - No → continue

3. **Does the article show HOW a process/mechanism works (steps, pathways, stages)?**
   - Yes → **Process-Tracing**
   - No → continue

4. **Does the article adjudicate between competing explanations (not X but Y)?**
   - Yes → **Factor-Identifying**
   - No → continue

5. **Does the article document an empirical pattern where little prior work exists?**
   - Yes → **Gap-Filler**

### Edge Cases

- **Concept IS the mechanism**: If a coined term names a process (e.g., "flexible austerity"), classify as **Concept-Building** — the coined term is the dominant move.
- **Adjudicating within a framework**: If the framework is scaffolding, it's Theory-Extension; if adjudication is the punchline, it's Factor-Identifying.
- **Gap-filling with a mechanism**: If the mechanism is named and findings follow its stages, it's Process-Tracing, not Gap-Filler.

## Workflow Phases

### Phase 0: Intake & Classification
**Goal**: Gather materials, identify the contribution type, and assess venue positioning.

**Process**:
- Collect available materials (theory section, findings, abstract, research question)
- Apply the decision tree to classify contribution type
- Assess venue positioning (theoretical reach, claim scope, methods fit)
- Identify target field and journal for calibration
- Confirm classification with the user

**Guide**: `phases/phase0-intake.md`

**Output**: Contribution type assignment with rationale

> **Pause**: User confirms contribution type before profiling.

---

### Phase 1: Profile Generation
**Goal**: Build the full contribution profile with cross-section template and vocabulary threading plan.

**Process**:
- Read the relevant cluster guide from `clusters/`
- Generate section-by-section template (abstract through conclusion)
- Identify 5-8 key threading terms
- Map vocabulary to each section
- Note signature moves and prohibited moves for each section

**Guide**: `phases/phase1-profiling.md`

**Output**: Complete contribution profile (`drafts/contribution-profile.md`)

> **Pause**: User reviews profile before passing to downstream skills.

---

### Phase 2: Alignment Audit (Optional)
**Goal**: Check existing draft sections for contribution alignment.

**Process**:
- Read available draft sections
- Check each section against the contribution profile
- Flag misalignments (e.g., intro promises gap-filling but conclusion delivers mechanism)
- Suggest specific revisions to restore threading

**Guide**: `phases/phase2-audit.md`

**Output**: Alignment report with revision recommendations

---

## Technique Guides

| Guide | Purpose |
|-------|---------|
| `techniques/vocabulary-threading.md` | How to thread 5-8 key terms across all sections |

## Cluster Profiles

| Guide | Type |
|-------|------|
| `clusters/process-tracing.md` | Process-Tracing (~27%) |
| `clusters/concept-building.md` | Concept-Building (~27%) |
| `clusters/factor-identifying.md` | Factor-Identifying (~24%) |
| `clusters/theory-extension.md` | Theory-Extension (~11%) |
| `clusters/gap-filler.md` | Gap-Filler (~9%) |

## Venue Positioning

Beyond contribution type, venue selection depends on how the article positions itself along two key dimensions. Based on analysis of ~230 articles across six journals (sample sizes are modest — treat as suggestive patterns, not hard rules):

### Theoretical Reach

The sharpest differentiator between flagship and field-journal articles:

- **Domain-bridging**: The article connects its findings to sociological theory beyond its immediate subfield. Flagships tend to expect this (roughly 80–97% of articles).
- **Domain-internal**: The article advances understanding within its subfield without reaching outward. Field journals are comfortable with this (roughly 60% of articles).

An article about protest decline that speaks only to social movement theory is well-positioned for SMS or Mobilization. The same article reframed to connect to institutional theory or political sociology becomes a flagship candidate. The empirical content can be identical.

### Claim Scope

How broadly the article's conclusions reach:

- **Context-bounded** ("in this case, we found..."): Essentially absent at AJS, ASR, and SF. More common at SP and at field journals.
- **Domain-bounded** ("for [topic area], these patterns hold..."): Accepted everywhere — the floor for most flagships.
- **Generalizing** ("this tells us about how [broad process] works"): Especially common at ASR and SF.

### Journal Profiles (Suggestive)

Each journal tends toward a distinctive character. These patterns are based on small samples (n=20–69 per journal) and should be treated as tendencies, not requirements:

| Venue | Methods tendency | Theoretical reach | Claim scope tendency |
|-------|-----------------|-------------------|---------------------|
| **AJS** (n=33) | Quantitative-heavy; mechanism-focused | Very high domain-bridging | Domain-bounded is the norm; context-bounded rare |
| **ASR** (n=69) | Broad; all methods | High domain-bridging | Frequently generalizing |
| **Social Problems** (n=28) | Qualitative-friendly; interviews and ethnography common | High domain-bridging | More tolerant of context-bounded than other flagships |
| **Social Forces** (n=20) | Quantitative; admin data, experiments, computational | High domain-bridging | Frequently generalizing; context-bounded rare |
| **SMS** (n=38) | Qualitative; single-case; non-US; theoretical pieces | Often domain-internal | Context-bounded common |
| **Mobilization** (n=41) | Quantitative; large-N | Often domain-internal | Context-bounded common |

**Key pattern**: SF and Mobilization tend to use similar methods (quantitative, large-N), but differ on theoretical reach and claim scope. SP and SMS share qualitative methods, but SP tends to demand domain-bridging theory where SMS does not.

Phase 0 includes a venue positioning check alongside contribution type classification.

## Field Profiles

Field profiles adjust distribution expectations and calibration guidance for particular sociology subfields. The contribution type (above) remains the primary axis; the field profile is a second dimension that modifies recommendations. Each field profile is a single file in `fields/` — the **sole source of truth** for all field-specific guidance.

| Field | File | Key Differences |
|-------|------|-----------------|
| **Generalist** (default) | — | Benchmarks from *AJS*, *ASR*, *SP*, *SF* (n=115) |
| **Social Movements** | `fields/social-movements.md` | PT drops to 6% (vs 27%), GF rises to 21% (vs 9%), CB is mid-range/domain-specific, FI dominates at *Mobilization* (38%). Threading moderate. Based on 82 articles from *SMS* and *Mobilization*. |

Phase 0 identifies the field profile alongside the contribution type. When a field profile applies, its calibration guidance overrides generalist defaults where they conflict.

**To add a new field**: Create a `fields/{field}.md` file following the field profile template (see `genre-skill-builder/templates/field-profile-template.md`). No other files need to change.

## Invoking Phase Agents

Use the Task tool for each phase:

```
Task: Phase 0 Intake
subagent_type: general-purpose
model: sonnet
prompt: Read phases/phase0-intake.md and the cluster decision tree from SKILL.md. Classify the user's article based on their materials. User's research question is [X], main argument is [Y], data is [Z].
```

```
Task: Phase 1 Profiling
subagent_type: general-purpose
model: opus
prompt: Read phases/phase1-profiling.md and clusters/[type].md. Generate a full contribution profile for a [type] article. User's materials: [list]. Target journal: [journal].
```

**Model recommendations**:
- Phase 0 (Intake): **Sonnet** — classification is systematic, not creative
- Phase 1 (Profiling): **Opus** — template adaptation requires nuance
- Phase 2 (Audit): **Sonnet** — alignment checking is systematic

## Starting the Process

When the user is ready to begin:

1. **Ask about the article**:
   > "What is your main research question or puzzle? What is your central argument or key finding?"

2. **Ask about materials**:
   > "Which sections do you have available? (Theory/lit review, findings, abstract, methods — any combination works)"

3. **Ask about the target**:
   > "What journal are you targeting? (This helps calibrate the contribution framing)"

4. **Apply the decision tree** to classify the contribution type.

5. **Confirm with the user** before generating the profile.

6. **Proceed to Phase 1** to generate the full profile.

## Key Reminders

- Run this skill BEFORE argument-builder, article-bookends, or abstract-builder
- The contribution type determines section architecture, not just framing language
- Opening move ≠ contribution type — classify based on the full article arc
- Strong vocabulary threading (5-8 terms across all sections) is the norm at 90%+
- If the user's contribution seems like a hybrid, classify by the abstract's dominant move
- Gap-Filler is risky at AJS/ASR — consider reframing as PT (add mechanism) or CB (coin a term)
- The contribution profile is a living document — update it if the article's framing shifts during drafting
