# Report

One file. This file fixes its shape.

## Contents

- Header
- Section order
- Source markers
- Numbers
- Prose rules
- Word band
- Sources section
- A worked example

## Header

Three plain lines, no markdown:

```
DEEP RESEARCH REPORT
<the topic, in plain words>
<YYYY-MM-DD>
```

Then a blank line, then BOTTOM LINE.

## Section order

Every section label is on its own line, in capitals, followed by a blank line and the text. No numbering, no punctuation, no decoration. The labels appear in this order, and this is the list the skeleton is built from.

**BOTTOM LINE.** Three sentences. What the topic is, the most important finding, and the thing most readers get wrong. A reader who stops here has the report's answer.

**THE QUESTION.** One paragraph. The question the report answers, why it matters now, and what is deliberately excluded. The exclusions are the ones in `exclusions:`, so the reader knows what a gap later means. An axis that ended thin is named in WHAT COULD NOT BE VERIFIED, not here.

**THE LANDSCAPE.** Two to four paragraphs. The field in plain terms: who is involved, how the pieces fit, what changed recently, and what the reader needs to hold in their head before the detail. When an axis covers this ground, THE LANDSCAPE carries only the framing.

**FINDINGS.** One ALL CAPS label per axis, in the order the reader needs them, each followed by one to four paragraphs. A label is a statement about the topic, never a question. "THE COST OF A FALSE POSITIVE" is a theme. "WHAT DOES IT COST" is not. It must differ from the fixed labels above, so an axis called Landscape is labelled THE LANDSCAPE IN PRACTICE. Each claim appears once: when an axis covers the ground of a fixed section, the axis carries the claim and the fixed section carries only its own material.

**THE NUMBERS.** The figures the report rests on, in prose. Each one is written to the rule under Numbers. When an axis covers this ground, THE NUMBERS carries the figures and that axis's FINDINGS block carries the interpretation; a figure appears once, in THE NUMBERS.

**WHAT PRACTITIONERS SAY.** First-hand accounts, labelled by who is speaking and in what capacity. Marketing copy belongs in THE LANDSCAPE as a claim, not here as experience.

**WHAT EVERYONE GETS WRONG.** The blindspots: the belief that is common, the evidence that contradicts it, and why the belief persists.

**WHERE THE SOURCES DISAGREE.** Every conflict, one paragraph each. Both figures, both sources, and the likely cause of the difference: different populations, different definitions, different dates, or different incentives.

**WHAT COULD NOT BE VERIFIED.** Every gap, one line each: what could not be established, and the phrasings or routes tried. Name the gap as a statement about the evidence, never as "this report found nothing"; write no line for a gap you cannot state.

**WHAT WOULD CHANGE THIS.** Two to four sentences. The evidence that would overturn each headline claim, and how a reader would recognise it. Give every headline claim a falsifier.

**SOURCES.** The tiered list, defined below.

Omit a section only when it would be empty, and say why in WHAT COULD NOT BE VERIFIED. When WHAT COULD NOT BE VERIFIED is itself empty, keep it with one line saying no gap survived the search. THE NUMBERS is never empty: on a topic with no figures, or with no figure above tier 3, write one sentence saying so.

## Source markers

Every sentence in the body, between the header and SOURCES, that carries a number or a date carries a marker at the end, after the full stop, with no space before it. A sentence carrying a name or a superlative carries one too; the block checks numbers and dates, and check 11 reads names and superlatives by hand:

```
Adoption reached 52 percent of the surveyed enterprises.[S4][S9]
```

- One to three markers per sentence. Three is the ceiling, not a target. The block counts them.
- The marker resolves to the `id` column of `sources.tsv`, and the source appears in SOURCES.
- A sentence that makes no factual claim carries none.
- The URL lives in SOURCES, never in the body.
- A marker is part of the deliverable. The report keeps it, because the marker is the proof.

## Numbers

For every figure: the value, the base, the date, and the method.

- Value. The number, in the unit the source used.
- Base. Of what, and of whom. "52 percent of 400 surveyed enterprises", not "52 percent".
- Date. When it was measured, not when it was published.
- Method. How it was measured, in one clause, or `method not stated`.

Write approximate ranges in words and measured figures as digits: "ten to fifteen percent", not "10-15%", but "52 percent of 400 surveyed enterprises". Keep figures, years, versions, and identifiers as digits. Keep each figure as its source states it, and present a conflict as two figures side by side rather than as an average that no source states. A figure published in another currency is converted once, with the rate and its date named in the sentence, and the original figure stays in the `note`.

## Prose rules

- Name who did what, in the active voice.
- Write the claim and its attribution in the same sentence: "according to the regulator's March 2026 review".
- Address the reader in the third person, as "a reader" or "anyone".
- Write full stops and commas, and let a quote carry any other punctuation. A quotation sits inside double quotes, and a dash inside one is part of the quotation. Outside a quotation, write letters, digits, spaces, and the punctuation of an ordinary sentence.
- Keep one idea per paragraph, 150 words or fewer. A short paragraph is allowed when it carries one consequence or one number. A gap line and a source entry are one line each.
- Keep one paragraph per line, unwrapped, so a check can read one argument at a time.
- Name the thing and the action, without the filler: "It is important to note that costs rose" becomes "costs rose".
- Let the tone and audience in the brief guide word choice; the section order and these rules do not change.

Three rules keep the page readable cold. Check 12 reads them.

- Write for a reader who has only this page: name the source, state the claim, and keep the conversation, the request, and the session out of it.
- Write about the topic. The audience is a reader, so the words podcast, episode, narration, tts, voice-over, slide deck, and audiobook stay out of the page.
- Speak the claim. State the finding, and leave out the process that produced it: "the research found" and "based on the search results" are process, and the page states the finding instead.

## Word band

Write 1,500 to 3,500 words. Deliver below 1,500 only when the topic cannot support more, and say why in WHAT COULD NOT BE VERIFIED. Go to 6,000 only when the user named a length or asked for breadth; otherwise stop at 3,500.

## Sources section

One entry per line, ordered by tier, then by id. Each entry carries the tier, the source id, the publisher or author, the title, the date, and the URL, in this shape:

```
Tier <n>. [<S#>] <publisher>, <title>, <date>. <url>
```

The id is what makes a marker resolvable by a cold reader. A source cited in the body but missing here is a broken marker. A source here but never cited is background, and its entry carries the word `background` between the date and the URL: `Tier <n>. [<S#>] <publisher>, <title>, <date>. background <url>`.

## A worked example

`examples/report.md` is a complete worked example at the word floor, on a small topic. It shows the header, the labels, the markers, a conflict paragraph, a gap line, a falsifier, and the tiered sources.
