---
name: prose-craft
description: Sentence and paragraph craft guide for academic sociology writing. Three modes (argumentative, descriptive, evaluative) with empirically-derived benchmarks from AJS/ASR corpus. Invoked by other writing skills, not run standalone.
---

# Prose Craft

Sentence- and paragraph-level guidance for generating academic sociology prose. This skill is invoked by other writing skills (e.g., `qual-findings-writer`, `argument-builder`, `article-bookends`) to calibrate prose at the point of generation. It is not typically run standalone.

## How Other Skills Invoke This

When a writing skill generates prose, it specifies a mode:

- **Argumentative**: Theory sections, literature reviews, conceptual framing
- **Descriptive**: Methods, case narratives, scene-setting, process descriptions
- **Evaluative**: Results presentation, findings interpretation, summaries

The mode sets benchmarks for sentence length, paragraph density, and voice. All three modes share the same core rules.

## Project Integration

This skill does not read from or write to `project.yaml` or `progress.yaml`. It provides craft guidance that other skills apply during their own writing phases.

---

## Core Rules

These apply in all three modes. They are non-negotiable.

### The Deletion Test

Remove each word or phrase. If meaning doesn't change, delete it.

**Before**: "It is important to make its steps explicit so that we can see how it works."
**After**: "If we make the steps explicit, we can see how it works."

### Never Use Em Dashes

Em dashes are strongly associated with LLM-generated text. Do not use them. Ever. No en dashes used as em dashes either.

When you feel the urge to insert a dash, choose one of these instead:
- Split into two sentences
- Use a comma (if the aside is short and nonrestrictive)
- Use a colon (if what follows elaborates)
- Fold the aside into the main clause
- Move the aside to a different position in the sentence
- Drop the aside entirely

### Name the Agent

Passive voice hides who acted. Default to active voice with a named subject.

| Passive | Active |
|---------|--------|
| "Data were collected" | "We collected data" |
| "Deviants were labeled" | "Teachers labeled them as deviant" |
| "It has been shown that" | "Smith shows that" |

**Exception**: Passive is acceptable in evaluative mode for conventional results phrasing ("Coefficients were statistically significant"). Even then, prefer active when the agent is obvious.

### Use First Person

Use I/we for methods, claims, and analytical decisions. The myth of avoidance is false.

| Impersonal | Personal |
|------------|----------|
| "This study examines" | "We examine" |
| "The authors argue" | "I argue" |
| "It can be concluded" | "We conclude" |

### Replace Nominalizations with Verbs

Words ending in -tion, -sion, -ment, -ness, -ity drain energy.

| Abstract | Concrete |
|----------|----------|
| "The investigation of" | "We investigated" |
| "The development of efficacy" | "How teams develop confidence" |
| "The clarification of dynamics" | "Clarifying who does what" |

### Pair "This" with a Noun

Never start a sentence with "This" followed by a verb. Always specify what "this" refers to.

| Ambiguous | Clear |
|-----------|-------|
| "This shows that" | "This finding shows that" |
| "This is important because" | "This pattern is important because" |
| "This suggests" | "This result suggests" |

### No Throat-Clearing

Do not announce what you are about to do. Just do it.

**Cut**: "It is important to note that," "It merits attention that," "It should be noted that," "An attempt to shed light on"

### No Signposts

Do not label importance. Let the content demonstrate it.

**Cut**: "Importantly," "Overall," "More importantly," "Significantly," "Notably," "Interestingly," "Indeed,"

### No Meta-Commentary

Do not narrate the writing process or comment on rhetorical strategy.

**Before**: "This decision reflects a clear understanding of the reviewers' concerns."
**After**: "This decision addresses the reviewers' concerns."

### Subject and Verb Stay Close

Keep subject and verb within 12 words of each other.

**Before** (23 words apart): "The knowledge that criminalization of marijuana use can lead to a wide variety of other social ills has not prevented lawmakers..."
**After**: "Lawmakers know marijuana criminalization carries risks, but they haven't changed policy."

### Concrete Over Abstract

Replace abstract placeholders with specifics. Vague relation-words mark unfinished thinking.

| Placeholder | Ask yourself |
|-------------|--------------|
| "complex relation between" | What is the relation? |
| "a set of factors" | Which factors? Name them. |
| "a kind of" | What kind? Be specific. |

Ground each abstract claim in at least one concrete illustration.

### Kill Dead Metaphors

**Cut**: "cutting edge," "shed light on," "pave the way," "growing body of literature," "rich issue," "plant the seeds of," "covers terrain"

Keep metaphors only if they are fresh and developed across more than one sentence.

### Use "Because" Instead of "This Reflects"

Replace abstract reflection language with causal explanation.

**Before**: "This reflects a broader shift in the manuscript's theoretical orientation."
**After**: "Because the spatial framework is gone, the analysis now follows the interviews more closely."

---

## Anti-LLM Rules

These specifically counteract patterns that make prose sound machine-generated.

### No Ornamental Triplets

Two beats feel human. Three feels rhetorical. Cut the third item unless each names a distinct, analytically necessary category.

**Cut**: "clarity, coherence, and empirical grounding" (drop "coherence")
**Keep**: "race, class, and gender" (each term is analytically distinct)

### No Overbalanced Contrast

"Not X, but Y" constructions are usually redundant. Try one clause.

**Before**: "The paper is not merely descriptive, but analytically ambitious."
**After**: "The paper moves beyond description."

### No Evaluative Adverbs

Delete adverbs that do the work of evidence.

**Cut**: "convincingly demonstrates," "clearly shows," "effectively addresses"
**Keep**: "demonstrates," "shows," "addresses"

### No Stacked Adjectives

Excess enthusiasm reads as synthetic. One adjective is usually enough.

**Before**: "This is a thoughtful, rigorous, and sophisticated analysis."
**After**: "This is a careful analysis."

### No Excessive Hedging Chains

One hedge per claim. Do not stack them.

**Before**: "This might possibly suggest that there could be a relationship..."
**After**: "This suggests a relationship..."

### Paragraphs End Without a Moral

Do not "land the plane" with a summary statement. End after the analysis. Silence reads as confidence.

**Cut**: "Together, these changes underscore the manuscript's contribution to..."

### Break Symmetry

If three consecutive paragraphs start the same way, rewrite one. Let one be shorter, more direct, or structured differently. Vary sentence openings within paragraphs too.

### Allow Mild Awkwardness

Perfect prose is suspicious. Functional prose is human. Do not polish every sentence to the same sheen. Some roughness signals authenticity.

### Match Syntax to Logic

Coordinate clauses suggest equal importance. Show hierarchy through grammar.

**Before** (three equal clauses): "The theory is simple, it is important to make steps explicit, so we can see how it works."
**After** (subordination): "If we make the steps of this simple theory explicit, we can see how it works."

---

## Tone

The target tone is **serious, analytically forceful, controlled, and readable**. The prose should sound like a strong university press book or top-journal article in sociology. It should not sound like an op-ed, manifesto, magazine feature, TED-talk script, or pop-sociology trade book.

### Preferred

- **Direct**: State claims plainly. Avoid ceremony.
- **Measured**: Neither breathless nor bored. No drama, no flair.
- **Specific**: Prefer concrete nouns and named actors over abstractions.
- **Confident but not grandiose**: Assert findings without overselling. "We find" not "we powerfully demonstrate."
- **Unpretentious**: Plain words over fancy ones. "About" not "with regard to." "How" not "the way in which." "Depends on" not "predicated upon."
- **Mechanism-driven**: Prefer sentences that explain **how** something happens, not just that it does. "Departments often treated new reforms as confirmation of existing practice rather than as mandates for behavioral change" is better than "Departments resisted reform."
- **Precisely bounded**: Use language that signals scope. Prefer "often," "typically," "in many cases," "in the modal case," "as typically structured," "under these conditions," "in practice," "proved insufficient to," "rarely translated into." These are more honest and more useful than absolutist claims.
- **Calm around morally charged material**: Let evidence, cases, interviews, and outcomes carry the emotional weight. Do not amplify with language. "Interviewees repeatedly described the reform process as incomplete" is better than "The reform process was a hollow failure."

### Avoid

- **Dramatic**: No rhetorical crescendos, no breathless reveals, no building to a climax.
- **Flowery**: No ornamental language, no poetic flourishes, no literary affectation.
- **Performatively humble**: No "we humbly suggest," no "this modest contribution."
- **Breathlessly enthusiastic**: No "fascinating," "remarkable," "groundbreaking," "stunning."
- **Self-narrating**: No "as we will show," no "the reader will recall," no "it is worth emphasizing."
- **Prosecutorial**: No "guilty," "verdict," "condemned," "exposed," "damning," "irrefutable proof." Use "conclusion," "evidence indicates," "difficult to justify," "strongly supports."
- **Sloganized**: No lines built for pull quotes, talks, or trailers. "The system did exactly what it was designed to do" sounds forceful but explains nothing. Prefer: "The reform process repeatedly converted pressure for change into manageable administrative action."
- **Pop-sociology cadence**: No "Here's the twist," "But that's not what happened," "The real shock is," "Look closer and the story changes," "That's where everything falls apart." These are journalistic, not scholarly.
- **Wise-narrator voice**: No "The numbers confirm what everyone already knew," "This tells us everything we need to know," "The lesson is obvious," "The truth is simple." The author is not above the evidence delivering universal truths.
- **Absolutist**: No "all," "every," "none," "always" unless literally true and necessary. "Every reform failed" should be "Most reforms, as typically structured, did not produce measurable changes." "Cities simply absorbed reform" should be "In many cities, reform adoption was not matched by durable implementation."
- **Stacked intensifiers**: A paragraph should not keep raising emotional volume sentence after sentence. If "clear verdict," "systematically hollow," and "deeply empty" all appear in one paragraph, cut at least two.

### Memorable but Analytic Phrasing

Vivid language is fine when it sharpens the argument. Use it sparingly.

**Good examples**: "formally impressive but institutionally shallow," "visible adoption without behavioral transformation," "administratively manageable forms of reform," "compliance without change."

**Test**: Does the phrase compress a real analytical distinction into memorable form? If yes, keep it. If it just sounds good, cut it.

### Paragraph Sequence for Strong Claims

When making a significant point, follow this sequence:

1. State the finding
2. Explain the mechanism
3. Draw the implication

Example: "Cities adopted reforms rapidly. But those reforms were often absorbed through processes of reclassification, design weakening, and implementation erosion. As a result, visible policy change did not reliably alter frontline behavior."

### Sentence-Level Intensity Check

Before keeping a strong sentence, ask:

1. Is this sentence making an analytic claim, or just sounding forceful?
2. Is the scope accurate?
3. Could this appear in a strong university press book without sounding like magazine prose?
4. Is the intensity coming from the evidence or from the wording?
5. Does this sentence explain, rather than merely accuse?

If the answer to 4 is "from the wording," revise it down one notch.

### Quick Substitutions for Overheated Prose

If the sentence exists only for rhetorical force and adds no analytical content, the best fix is deletion. If it carries a real claim, tone it down:

| Avoid | Prefer |
|-------|--------|
| "The evidence delivers a clear verdict." | "The evidence points to a clear conclusion." Or cut entirely if the evidence was just presented. |
| "This was no innocent policy choice." | "This approach is difficult to defend in light of the evidence." Or cut if the evidence already speaks. |
| "The numbers confirm what organizers already knew." | "The quantitative findings align with organizers' assessments." |
| "The reform system is optimized for failure." | "The reform system repeatedly produced visible adoption without corresponding behavioral change." |
| "Departments hollowed out reform." | "Departments often translated reform into narrower and more manageable administrative forms." |
| "The implications are profound." | Cut. If the implications are profound, the reader will see it. |
| "This finding is striking." | Cut. State the finding and move on. |

The target register is a smart colleague explaining their work at a seminar: clear, specific, occasionally wry, never showy.

---

## Mode Benchmarks

These benchmarks are derived from analysis of 103 articles (33 AJS, 70 ASR, 61,100 sentences). They describe what published sociology prose actually looks like, filtered through editorial best practices.

### Format: Article vs. Book

The three modes below (argumentative, descriptive, evaluative) apply to both articles and books. But book prose differs systematically from article prose. These adjustments are based on analysis of 22 political sociology and American politics monographs (~2.5M words, ~88,000 sentences).

**When writing for a book**, apply the mode-specific guidance below but shift all targets in these directions:

| Metric | Article target | Book target | Why |
|--------|---------------|-------------|-----|
| Median sentence length | 23 words | 19 words | Books run shorter; 38% of sentences are under 15 words vs. 26% in articles |
| Sentences per paragraph | 4 | 3 | Books let paragraphs breathe; each does less heavy lifting |
| First person rate | ~10% | ~14% | Books use I/we more freely throughout, not just in methods |
| Passive voice | ~11% | ~7% | Books are more consistently active |
| Formal transitions | ~7% of sentences | ~2% of sentences | Books rely on paragraph breaks and conjunctions ("But," "And") instead of "However," "Moreover" |
| Sentence-initial conjunctions | Occasional | ~4% of sentences | "But" and "And" as sentence openers are a normal book register |

**What stays the same**: Core rules, anti-LLM rules, tone, hedging guidance, phrase substitutions. The shift is in rhythm and density, not in craft principles.

**Practical implications for book mode**:
- Paragraphs of 2-3 sentences are normal, not a sign of underdevelopment. A book paragraph can make one point and stop.
- Short sentences (under 15 words) should appear more often. Let them do standalone work.
- Cut most formal transition words. If a paragraph logically follows the previous one, the reader will follow without "Moreover." Use "But" over "However."
- Use first person for analytical moves throughout, not just in methods chapters. "I argue," "I trace," "I show" are standard book register.
- The over-35-word ceiling is tighter: only 15% of book sentences exceed it (vs. 19% in articles). If a sentence crosses 35 words, split it.

### Argumentative Mode

Use for: theory sections, literature reviews, conceptual framing, engagement with prior work.

| Metric | Target | Range |
|--------|--------|-------|
| Median sentence length | 25 words | 20-30 |
| Sentences per paragraph | 4-5 | 3-6 |
| Within-paragraph length stdev | 10-12 words | |
| Citation density | 0.5-1.0 per sentence | |
| First person rate | Low (~6%) | |
| Passive voice | Low (~10%) | |

**Distinctive traits**:
- Highest sentence length variation. Mix short framing sentences with longer analytical ones.
- Citation-dense. But cap at 3 citations per sentence. Break long citation strings across multiple sentences.
- Lower first-person. Literature review paragraphs summarize others' work. Use first person for your own claims ("I argue"), not for reporting the field.
- Watch for nominalization pileup. Theory prose attracts abstract nouns. Convert at least half to verbs.

**Paragraph rhythm**: Open with a short framing sentence (15-20 words). Build through longer analytical sentences. End with a claim or transition, not a summary.

### Descriptive Mode

Use for: methods, case narratives, historical context, process descriptions, scene-setting.

| Metric | Target | Range |
|--------|--------|-------|
| Median sentence length | 21 words | 15-25 |
| Sentences per paragraph | 3-4 | 2-5 |
| Within-paragraph length stdev | 8-10 words | |
| Citation density | Low (0-0.2 per sentence) | |
| First person rate | Moderate (~10-15%) | |
| Passive voice | Low for narrative (~9%), moderate for methods (~17%) | |

**Distinctive traits**:
- Shortest sentences. The cleanest prose in the corpus. Protect this; do not let it drift toward argumentative bloat.
- Tightest paragraphs. Three sentences that do their work and stop.
- Most concrete. Named actors, specific actions, observable details.
- Methods submode allows more passive ("Participants were randomly assigned") and more first person ("We collected," "We coded") in the same paragraph.

**Paragraph rhythm**: Vary sentence lengths but keep the overall pace brisk. Short paragraphs are fine. Let the material breathe.

### Evaluative Mode

Use for: results presentation, findings interpretation, discussion of evidence, summaries.

| Metric | Target | Range |
|--------|--------|-------|
| Median sentence length | 24 words | 18-28 |
| Sentences per paragraph | 4 | 3-5 |
| Within-paragraph length stdev | 9-11 words | |
| Citation density | Low (0-0.3 per sentence) | |
| First person rate | Moderate (~13%) | |
| Passive voice | Moderate (~11%) | |

**Distinctive traits**:
- Alternates between reporting and interpreting. A results sentence followed by a "so what" sentence.
- Allows some conventional passive for results ("coefficients were significant," "models were estimated"). But push interpretation toward active first person: "We find," "These results suggest."
- Table/figure references are short and direct: "Table 2 shows X." Do not embellish.
- Findings sentences carry the most hedging. One hedge per claim is enough. "Results suggest" is fine. "Results seem to possibly suggest" is not.

**Paragraph rhythm**: Lead with the finding (often short: "The effect was significant"). Follow with magnitude, comparison, or interpretation. End with implication or transition. Do not end with a paragraph-level moral.

---

## Sentence Length Targets

The corpus median is 23 words. The distribution:

| Length | Share | Guidance |
|--------|-------|----------|
| Under 15 words | 26% | Use freely. Short sentences are punchy and common. |
| 16-25 words | 31% | The sweet spot. Most sentences should land here. |
| 26-35 words | 23% | Acceptable for complex claims. Check that subject and verb are close. |
| Over 35 words | 19% | Use sparingly. If a sentence exceeds 35 words, look for a place to split. |

**The key finding is variation, not uniformity.** Within a single paragraph, sentence lengths should range by at least 15 words from shortest to longest (median range in the corpus: 23 words). A paragraph of five 24-word sentences is worse than a paragraph mixing 10, 28, 15, 32, and 19.

---

## Transition Words

Use transitions to signal logical relationships, not to fill space. The corpus shows:

**Common (use when needed)**:
- "However," (contrast)
- "For example," / "For instance," (illustration)

**Moderate (use occasionally)**:
- "Thus," / "Therefore," (consequence)
- "Similarly," (parallel)
- "Moreover," / "Furthermore," (addition)
- "Although" / "While" (concession, at sentence start)

**Avoid or minimize**:
- "Indeed," (usually empty emphasis)
- "Importantly," / "Notably," (signposting, cut these)
- "Accordingly," (stiff)
- "In turn," (vague)

**Coordinating conjunctions as sentence openers** ("But," "And," "Yet") appear in the corpus and are acceptable in moderation. "But" is more common than "However," in mid-paragraph positions and reads as more direct.

About 7% of sentences in the corpus open with a formal transition. Do not exceed this. If every paragraph starts with "However" or "Moreover," the prose sounds mechanical.

---

## Hedging

Hedge when warranted. Do not hedge reflexively.

**One hedge per claim**:
- "Results suggest" (fine)
- "may indicate" (fine)
- "might possibly tend to suggest" (not fine)

**Specific hedges over vague ones**:
- "The relationship is stronger in urban than rural areas" (specific qualification)
- "might possibly be related under some conditions" (cowardly loophole)

**Common hedges in the corpus** (frequency per sentence):
- "may" (4.0%), "likely" (2.3%), "could" (1.8%), "might" (1.2%), "suggest" (0.8%)

Use "may" and "likely" as your defaults. Reserve "might" and "could" for genuinely uncertain claims. Avoid "perhaps" and "arguably" (both under 0.3% in the corpus).

---

## Phrase Substitutions

Quick reference for common academic bloat:

| Avoid | Use |
|-------|-----|
| "It is important to note that X" | X |
| "It has been shown that X" | "Smith shows X" |
| "There is evidence that X" | "Evidence shows X" |
| "There is a growing body of literature" | "Recent studies" |
| "Data were collected" | "We collected data" |
| "This study is concerned with X" | "This study examines X" |
| "An attempt to shed light on X" | "I investigate X" |
| "The investigation of X" | "We investigated X" |
| "A correlation was obtained" | "We found a correlation" |
| "It can be concluded that X" | "We conclude X" |
| "with regard to" | "about" |
| "the way in which" | "how" |
| "predicated upon" | "depends on" |
| "in the context of" | "in" or "during" |
| "managed to maintain" | "kept" |
| "were able to" | "could" |

---

## Calibration

**Goal**: Prose that sounds like a knowledgeable colleague presenting work clearly. Specific, measured, occasionally direct to the point of bluntness. Never showy.

**Not the goal**: Beautiful prose. Prize-winning prose. Prose that calls attention to itself. The writing should be invisible; the ideas should be visible.

**Final check**: If a paragraph could appear in a press release, a TED talk, or a LinkedIn post, it is too dramatic. If it could appear in a legal contract, it is too stiff. The target is the space between.
