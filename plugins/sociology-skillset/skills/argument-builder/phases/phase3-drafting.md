# Phase 3: Drafting

## Why This Phase Matters

This is where planning becomes prose. The quality of your Theory section depends on sentence-level craft—how you open paragraphs, integrate citations, calibrate hedging, and build toward the turn. This phase transforms the paragraph map into publication-ready prose.

---

## Your Tasks

### 1. Draft by Paragraph

Work through the paragraph map one paragraph at a time. For each:

**Step 1: Open with purpose**
- Use the planned topic sentence (or refine it)
- Match opening type to function (see `techniques/sentence-toolbox.md`)

**Step 2: Build the paragraph**
- 4-7 sentences typical (129-165 words target)
- Each sentence advances the paragraph's function
- Vary sentence length and structure

**Step 3: Integrate citations**
- Follow the planned citation deployment
- Use appropriate patterns (parenthetical, author-subject, string)
- See `techniques/citation-patterns.md`

**Step 4: Calibrate hedging**
- Hedge predictions and mechanism claims
- Assert definitions and gap statements
- See hedging guide in `techniques/sentence-toolbox.md`

**Step 5: Transition out**
- Final sentence should set up the next paragraph
- Use transitional phrases or logical connectors

### 2. Draft by Function

Apply function-specific guidance:

#### DESCRIBE_THEORY Paragraphs
- Name the framework/theorist explicitly
- Explain how the concept works
- Include dimensions, mechanisms, or processes
- Use author-subject citations for canonical sources

**Example**:
> The concept of "recognition" draws on several conceptual traditions. According to Honneth (2003), recognition operates through three spheres: love (intimate relationships), rights (legal status), and esteem (social value). When individuals are denied recognition—through disrespect, exclusion, or degradation—they experience psychological harm and may struggle to develop positive self-relations (Taylor 1994). Lamont and colleagues (2016) have extended this framework to examine how low-status groups pursue recognition in everyday life, showing how stigmatized individuals actively resist misrecognition through boundary work and collective claims-making.

#### SYNTHESIZE Paragraphs
- Aggregate findings, don't summarize individual studies
- Use parenthetical strings efficiently
- Build toward a cumulative claim
- End with "what we know" before the gap

**Example**:
> Research on legal cynicism demonstrates that distrust of legal institutions is patterned by neighborhood context, race, and prior contact with police (Kirk and Papachristos 2011; Sampson and Bartusch 1998). Studies consistently find that residents of high-crime neighborhoods express cynicism about police responsiveness and fairness, even as they continue to call 911 for emergencies (Desmond et al. 2016; Gau and Brunson 2010). This literature highlights the coexistence of cynicism and reliance—a paradox that existing frameworks have struggled to explain.

#### PROVIDE_CONTEXT Paragraphs
- Open with phenomena, not scholars
- Use statistics, trends, or historical developments
- Keep citations minimal (2-3)
- Ground a subsection in empirical reality
- **Only use when shifting to empirical terrain the introduction did not cover**

**Example**:
> Congress passed the WWII Serviceman's Readjustment Act of 1944, better known as the GI Bill of 1944, to ease the transition back into civilian life for returning veterans. The law provided benefits to returning soldiers, including free healthcare, education subsidies, and business, home, and farm loans on favorable terms (Altschuler and Blumin 2009). The focus of the present study is the housing benefits of the GI Bill.

#### IDENTIFY_GAP Paragraphs
- Use the 4-part turn structure (see `techniques/turn-formula.md`)
- Be specific about what's unknown
- Connect directly to your study

**Example**:
> This literature highlights the importance of recognition for understanding how marginalized groups engage with institutions. Yet while research documents the pursuit of recognition in various settings, there is less attention to how recognition-seeking shapes encounters with legal authorities specifically. How do residents of high-crime neighborhoods understand their calls to police as demands for recognition? What meaning-making processes allow them to reconcile cynicism with reliance? These questions remain largely unexplored.

#### BRIDGE_TO_METHODS Paragraphs
- Transition from theory to the empirical analysis
- May briefly name the data or research design
- Do not write a full methods paragraph — just hand off
- Keep citations minimal (0-2)

**Example**:
> To test these expectations, we draw on linked administrative records from the Swedish population registers, which allow us to observe the full earnings trajectories of parents and their adult children across all employers in the Swedish economy. We describe the data and analytical strategy in the next section.

#### STATE_HYPOTHESES Paragraphs
- State formal directional predictions
- Number or label hypotheses clearly
- Connect each hypothesis to the theoretical reasoning above
- Use directional language ("will increase," "is associated with," "should reduce")

**Example**:
> This reasoning leads to our first hypothesis:
>
> HYPOTHESIS 1. — The more central students become in a peer network, the more ideologically consistent their beliefs will become.

#### STATE_QUESTIONS Paragraphs
- Articulate research questions clearly
- Connect questions to the gap
- **Do not add methods detail** — the methods section handles that

**Example**:
> This study examines how mothers in doubled-up households negotiate identity and dignity in shared living arrangements. Three questions guide the analysis: (1) How do guest mothers understand their position within host households? (2) What strategies do they use to maintain maternal identity when authority is constrained? (3) How do these negotiations vary by the character of the host-guest relationship?

#### THEORETICAL_SYNTHESIS Paragraphs
- Restate the argument in concise, summary form
- Draw together threads from multiple subsections
- Do not preview findings — synthesize the theoretical logic

**Example**:
> Thus, when state formation is in its nascent stages, embedding ideas and practices of the state is less a matter of constructing abstract mutual obligations between states and citizens than of establishing tangible ongoing relationships between individual officials who represent the state and individual leaders who credibly represent their communities' shared interests. A relational perspective shows that establishing the state as sole authority would require state officials to monopolize collective problem-solving to undercut these relationships with their competitors.

### 3. Draft Subsection by Subsection

If using subsections:
- Draft complete subsection before moving to next
- Ensure internal coherence within subsection
- Check that subsection accomplishes its architectural purpose

After each subsection, pause for user review if appropriate.

### 4. Maintain Cluster Style

As you draft, ensure prose style matches cluster:

| Cluster | Style Markers |
|---------|---------------|
| **Gap-Filler** | Efficient synthesis, sharp turn, minimal elaboration |
| **Theory-Extender** | Framework exposition, named theorist prominent |
| **Concept-Builder** | Definitional precision, confident terminology |
| **Synthesis** | Even treatment of traditions, bridging language |
| **Problem-Driven** | Even-handed debate presentation OR heavy context |

### 5. Track Progress

As you draft, note:
- Actual word count per paragraph
- Actual citations per paragraph
- Any deviations from the plan
- Paragraphs that need revision

### 6. Track Citations Used

Maintain a running list of every citation as you use it. For each citation, record:

```json
{
  "citations": [
    {
      "author": "Kirk and Papachristos",
      "year": "2011",
      "context": "legal cynicism patterning",
      "paragraph": 3,
      "pattern": "parenthetical"
    },
    {
      "author": "Connell",
      "year": "2005",
      "context": "hegemonic masculinity concept",
      "paragraph": 5,
      "pattern": "author-subject"
    }
  ]
}
```

**Why track citations?**
- Enables bibliography generation without parsing the document
- Allows Zotero ID lookup in Phase 5
- Helps verify citation density during revision
- Creates audit trail of sources used

Save incrementally to `citations.json` as you draft.

---

## Guiding Principles

### Draft, Don't Perfect
Get prose on the page. Revision comes in Phases 4-5.

### Follow the Map
The paragraph map exists for a reason. Stick to it unless you discover a structural problem.

### Don't Duplicate the Introduction
The theory section picks up where the introduction left off. If your opening paragraph reads like a second introduction — phenomenon framing, statistics, stakes — you're writing a "mini paper." Start with the scholarly conversation.

### Topic Sentences Are Anchors
If you're struggling with a paragraph, return to the topic sentence. What is this paragraph trying to accomplish?

### Vary Citation Integration
Don't use the same pattern throughout. Mix parenthetical, author-subject, and (sparingly) quote-then-cite.

### Read Aloud
Prose that sounds awkward when read aloud needs revision. Academic writing should still flow.

### The Turn Is Sacred
Draft the turn with special care. It's the most important paragraph.

---

## Common Drafting Problems

| Problem | Solution |
|---------|----------|
| Paragraph too long | Split into two; each should have one main function |
| Paragraph too short | Develop the idea more; add supporting material |
| Literature parade | Synthesize, don't list; what do the studies collectively show? |
| Missing topic sentence | Add clear opening that signals function |
| Buried turn | Move turn sentence to start of paragraph; add contrastive marker |
| Hedging definitions | Definitions are assertions; remove "may," "might" |
| Over-asserting mechanisms | Mechanisms are claims; add appropriate hedging |
| Opening duplicates intro | Cut phenomenon framing; start with scholars or concepts |
| Closing previews findings | Replace PREVIEW with BRIDGE_TO_METHODS or THEORETICAL_SYNTHESIS |

---

## Field-Specific Adjustments

When a field profile was identified in Phase 0, apply the field-specific
guidance from `fields/{field}.md`. Field profiles override generalist
defaults where they conflict. Key areas that field profiles may adjust:

- Target word count and paragraph count
- Opening move distribution and structural patterns
- Citation timing and density
- Audience assumptions and vocabulary
- Prohibited moves specific to the field

Refer to the field profile's benchmarks table and writing checklist for
this section.

## Output Files to Create

1. **theory-section.md** - Full draft prose organized by subsection
2. **theory-memo.md** - Append a `## Phase 3: Drafting Notes` section with notes on deviations, concerns, and areas flagged for revision
3. **citations.json** - Running list of all citations used (author, year, context, paragraph, pattern)

---

## When You're Done

Report to the orchestrator:
- Draft complete (yes/no)
- Word count achieved
- Citation count achieved
- Turn drafted (provide sentence)
- Closing function used
- Any structural changes from plan
- Areas flagged for revision

Example summary:
> "**Draft complete** (`theory-section.md`). 1,487 words across 10 paragraphs (target: 1,500). 36 citations (target: 35). Turn at paragraph 6: 'Yet while research documents the pursuit of recognition in various settings, there is less attention to how recognition-seeking shapes encounters with legal authorities specifically.' Closing: BRIDGE_TO_METHODS. One deviation: Split planned paragraph 4 into two for clarity. Flagged paragraphs 7-8 for transition smoothing in revision. Drafting notes appended to `theory-memo.md`. Ready for Phase 4: Turn refinement."
