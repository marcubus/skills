# Script craft

The editorial layer. A script is not the source read aloud. It is an edited narrative for the ear.

## Contents

- Runtime
- Structure
- Logical sections
- Selection
- Source discipline
- No meta-commentary
- Verbal attribution
- Paragraphs and sentences
- Punctuation for pacing
- Numbers and acronyms
- Eye-roll and understatement
- Self-review

## Runtime

Base estimate is 150 words per minute at neutral. The show baseline changes it. A 10-minute episode at the default is about 1500 words. Compute the target from the rate in `PERFORMANCE.md`.

Default target: 8 to 12 minutes. Long form up to about 45 minutes when the source is rich. Thin topics stay short. Do not pad. Do not truncate a genuinely deep source.

Declare the target before writing. Count spoken words, not tags.

## Structure

- No title line, no heading, no episode number. The filename carries the title.
- Cold open: 30 to 50 words. A concrete detail, a claim, or a number. No greeting.
- Intro: 100 to 150 words. Frame the episode and hand over.
- Body: 1000 to 1500 words for the default episode. Four to six sections with natural transitions.
- Wrap-up: 80 to 120 words. The key takeaways.
- Closing line: one statement that lands.
- No `END` marker. The engine would speak it.

## Logical sections

A script with multiple logical sections gets an explicit pause at each boundary. The rule and the snippet are in `PERFORMANCE.md` under section breaks.

A section can also open with a short spoken link, but the pause comes first. Do not announce a numbered chapter.

## Selection

Keep the findings that matter to a listening audience:

- What it is.
- Why it matters.
- The surprising bit.
- The practical takeaway.
- The one or two best stories.

Drop tables, methodology detail, source tiering, exhaustive fee breakdowns, and findings that only matter to a close reader. Keep at most two or three numbers per section.

If the source has more than six sections, the script does not need all of them. Pick the four to six with the strongest narrative. If a section is dropped, drop it entirely. Never gesture at missing material.

## Source discipline

- Read the saved source from disk. Do not write from conversation memory.
- Do not say "the report says" or "the document states". Speak the claim.
- Attribute major claims in speech, once each.
- If a claim is single-sourced, name the source. If a dimension was unverified, say so once.
- The script stands alone. It must not require the source.
- Do not carry report headings into the script.

## No meta-commentary

The script speaks the content, not the process. It does not describe the report, the source, the script, the instructions, the prompt, the sections, or the act of writing.

Cut or rewrite:

- "Let me explain."
- "I'll walk you through."
- "First, I'll..." and "Next, I'll..."
- "As I said earlier." and "As we discussed."
- "In this episode." and "The next section."
- "Let's break this down." and "Let's get into it."
- "Here's what we'll cover." and "By the end of this episode."
- "I'm going to tell you." and "I want to talk about."
- "The report says." and "The document says."
- "According to the report." and "According to the source."

Attribution is different. "According to Gartner, as of January 2026" names a real source and carries a claim. Keep it. "According to the report" names an artifact and says nothing. Cut it.

A spoken link is different. "Local news now" names the next subject. It does not describe the script. Keep it.

If a sentence describes the script, cut it or turn it into the claim. The listener wants the content, not the process.

## Verbal attribution

Use natural speech:

- "According to IT Jobs Watch, as of September 2026..."
- "In its January 2026 survey, Gartner found..."
- "The CNCF community survey puts the figure at..."

One attribution per major claim is enough. Do not rattle off a bibliography.

## Paragraphs and sentences

- One idea per paragraph. Around 100 to 150 words.
- Vary sentence length. A long sentence followed by a short one is the basic rhythm.
- If you run out of breath reading it, split it.
- The strongest emphasis is a short sentence after a longer one.
- Under strain, turns shorten. A long turn during conflict reads as a monologue.

## Punctuation for pacing

The engine treats punctuation as timing and intonation.

| Mark | Effect | Use |
|---|---|---|
| Period | Full stop, long pause, intonation reset. | Default sentence end. |
| Comma | Short breath pause. | Separate clauses the listener must parse. |
| Ellipsis | Trailing pause, falling intonation. | A reveal. One or two per episode. |
| Single hyphen | Brief parenthetical pause. | Asides. Use a spaced hyphen. |
| Semicolon | Mid-length pause. | Closely related clauses. |
| Colon | Pause with anticipation. | A setup before the explanation. |
| Question mark | Rising intonation on yes/no questions. | Rhetorical questions and direct address. |
| Exclamation mark | Higher energy. | Once per episode at most. |
| Blank line | Strong paragraph boundary. | Paragraph boundaries. A section break also needs an explicit pause. |

Avoid double hyphens, em dashes, en dashes, parentheses, quotation marks, slashes, emoji, and stacked punctuation. The engine reads characters, not formatting. No markdown.

## Numbers and acronyms

- Write numbers naturally. Prefer words for counts and statistics.
- Use digits only for plain cardinals, decimals, percentages, ranges, ordinals, and years. Write everything else as words.
- Write acronyms normally. Where the model spells them out, let it.
- Where an acronym should be said as a word, such as `SQL` to `sequel`, route it through the model's pronunciation control.
- Do not write `A.P.I.` or `A-I`. Use the written form and the pronunciation route.
- Keep engine-specific spellings in the handoff, not in the prose.

## Eye-roll and understatement

Write the observation as a short sentence. The words carry the irony. No stage directions, no parentheses, no bracketed notes.

```text
[rate:0.95] Sure. Because that always works.
```

```text
[rate:0.95] Not ideal.
```

The deadpan move is in `PERFORMANCE.md`. The words do the work.

## Self-review

Read the script back as if speaking it aloud. Fix any sentence that:

- Runs longer than 30 words.
- Has more than three commas.
- Has adjacent words the engine might slur.
- Uses a word the engine might stress on the wrong syllable.
- Uses a character from the avoid list.
- Changes emotion mid-sentence.
- Changes speaker without a pause, a question, or an interjection.
- Crosses a logical section boundary without a section-break pause.
