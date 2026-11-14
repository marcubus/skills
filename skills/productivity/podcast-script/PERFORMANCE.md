# Performance

Pacing, emotion, emphasis, and the named moves that give a script a specific vibe. Write the beat map and the pacing sheet before drafting.

## Contents

- Emotion
- Effective words per minute
- Pace bands
- Pacing sheet
- Section breaks
- Beat taxonomy
- Rate map
- Same-speaker tone changes
- Emphasis ladder
- Underline
- Deadpan aside
- Performance moves
- Budgets
- Pacing audit

## Emotion

The script has eight emotion values: `neutral`, `warm`, `bright`, `sad`, `tired`, `angry`, `whisper`, `excited`. Write the one the beat needs. The model file lists which ones its text carries; the compiler drops the rest and records them. Read it before the beat map.

Variety comes from rate, pause, sentence length, and word choice.

## Effective words per minute

Base rate is the host's `pace_wpm_estimate`, or 150 wpm when the profile does not set one. The `[rate:]` multiplier applies.

```text
effective_wpm = base_rate * rate_multiplier
```

A 10-minute episode is about 1500 words at 150 wpm. Compute the target from the base rate.

## Pace bands

| Band | Average sentence | Short | Medium | Long | Use |
|---|---|---|---|---|---|
| Slow | 18 to 22 words | 30% | 50% | 20% | evidence, reflection, close |
| Steady | 14 to 18 words | 40% | 45% | 15% | explanation, intro |
| Brisk | 10 to 14 words | 55% | 35% | 10% | hook, conflict, list |

Short is under 10 words. Medium is 10 to 20. Long is over 20.

## Pacing sheet

Write this before drafting.

| Segment | Function | Pace band | Emotion | Rate | Effective wpm | Words | Duration | Pause | Handoff | Emphasis | Move |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Cold open | hook | brisk | neutral | 1.0 | 150 | 50 | 0:20 | 0 | question | 1 | none |
| Context | frame | steady | neutral | 1.0 | 150 | 180 | 1:12 | 300ms | pause | 1 | none |
| Evidence | prove | slow | neutral | 0.95 | 142 | 450 | 3:10 | 600ms | pause | 2 | none |
| Conflict | tension | brisk | neutral | 1.05 | 158 | 350 | 2:13 | 600ms, then a 1000ms section break | interjection | 3 | none |
| Reflection | meaning | slow | neutral | 0.95 | 142 | 420 | 2:57 | 600ms | pause | 3 | confession |
| Close | land | slow | neutral | 0.9 | 135 | 50 | 0:22 | 1.2s | pause | 3 | drop |

Rules:

- Each segment has one function, one pace band, one rate, and one pause budget, plus an optional section break.
- The words and durations sum to the episode target within 15 percent.
- The emotion stays at the default unless the beat needs one. Rate is the only local pacing tool where the text carries it.
- Pauses are for beats, not for pace. Pace comes from wpm and sentence length.
- Default gap is 350ms. An explicit pause replaces it.
- Handoff is `pause` or `question` for a solo show. `interjection` marks a speaker change.
- Total explicit pause stays under 60 seconds.

## Section breaks

A script with multiple logical sections gets an additional pause at each section boundary. A weather update followed by local news is two sections. The listener needs a beat to register the change.

```text
... and the chance of rain is five per cent.

[pause:1000ms]

[voice:host_a] Local news now.
```

Rules:

- Section break pause: 800 to 1200ms. Use 1000ms as the default.
- The pause sits after the last turn of the section and before the first turn of the next section.
- The pause is explicit. The default 350ms gap is not enough.
- The pause is separate from a beat pause inside the section.
- A section break can also carry a short spoken link, but the pause comes first.
- Panel section breaks: 1000 to 1200ms.
- Section breaks count toward the total pause budget.

## Beat taxonomy

Label the source before writing.

```text
hook, context, claim, evidence, example, conflict, correction,
consequence, reflection, takeaway, close
```

| Beat | Function |
|---|---|
| hook | hook |
| context | frame |
| claim | prove |
| evidence | prove |
| example | illustrate |
| conflict | tension |
| correction | correct |
| consequence | consequence |
| reflection | meaning |
| takeaway | land |
| close | land |

Each beat gets a function, a pace band, an emotion, a rate, and a move. Adjacent beats with the same function keep the same rate.

## Rate map

| Beat | Content | Function | Emotion | Rate |
|---|---|---|---|---|
| Cold open | the bridge failed on day one | hook | neutral | 1.0 |
| Context | who signed it and what it was for | frame | neutral | 1.0 |
| Evidence | the load model assumed no pedestrians | prove | neutral | 0.95 |
| Conflict | the engineer who refused to sign | tension | neutral | 1.05 |
| Reflection | what it says about sign-off | meaning | neutral | 0.95 |
| Close | one line | land | neutral | 0.9 |

Rules:

- Keep the emotion at the default unless the beat needs one.
- Budget: two to four rate changes in a 10-minute episode.
- Reset the emotion to the default at a new section.
- The words carry the emotion. The rate only moves pace. If the words do not carry it, rewrite the words.
- The profile's `emotion_behaviour` sets the range and ceilings.

## Same-speaker tone changes

A same-speaker tone change needs a clean boundary and an explicit pause. The model file says how a change is applied.

```text
[voice:host_a] The first part lands here.

[pause:500ms]

[rate:0.95] The second part slows down.

[pause:300ms]

[rate:1.05] The third part lifts.
```

Rules:

- The pause is at least 300ms. 400 to 600ms is normal. 800 to 1200ms is a section break.
- The default 350ms turn gap is not enough. It is the same gap as every other turn boundary.
- If the tone change is mid-sentence, rewrite the sentence or carry the shift with punctuation and word choice.
- A speaker change is different. The `[voice:]` tag is the boundary. A pause is not required when a question or an interjection carries the change.

## Emphasis ladder

Use the lowest level that works.

| Level | Move | Cost | Use |
|---|---|---|---|
| 1 | Short sentence | none | Default. A 3 to 6 word sentence after a longer one. |
| 2 | Pause before the key word | `[pause:150ms]` to `[pause:300ms]` | A reveal or a correction. |
| 3 | Short sentence plus pause | 150 to 300ms | A key takeaway. |
| 4 | Rate change for one line | One `[rate:]` change | A lift or a drop. |
| 5 | Raised voice | One emotion marker | Only where the model carries `angry`. Otherwise use level 3 or 4. |

Level 5 needs the `angry` emotion. Use it only where the model carries it. Do not use an exclamation mark as a substitute. Use a short sentence, a pause, and a rate change.

## Underline

Pause between every word. It is a deliberate staccato, used once to make a point.

```text
It [pause:200ms] was [pause:200ms] not [pause:200ms] the [pause:200ms] database.
```

- Three to six words. No more.
- 150 to 250ms between words.
- Once per episode.
- The pause sits inline, so it adds no turns. It counts toward the total pause budget.
- Use it for a short phrase that lands. Do not use it for a full sentence.

## Deadpan aside

A deadpan aside is a short utterance at `[rate:0.95]` with no laughter or breath ticks and a pause after it. One eye-roll or understatement tick may carry the line.

```text
[rate:0.95] Sure. Because that always works.
```

- One to two lines. Not a paragraph.
- Use it for an aside, an eye-roll, a secret, or a conspiratorial observation.
- The words carry the irony. Do not write stage directions.
- The next line sets its own rate.
- Two to three deadpan asides per 10 minutes.
- A deadpan aside can be an interjection handoff. It still needs a pause, a question, or an interjection at the speaker change.

## Performance moves

| Vibe | Move | Mechanism | Budget |
|---|---|---|---|
| Dry, skeptical | Deadpan | default at `[rate:0.95]`, short sentences, no laughter or breath ticks, a pause after the line. | Two to three per 10 minutes. |
| Momentum, escalation | Build | `[rate:1.05]`, then 3 to 5 short sentences. No pauses inside the run. End on a short line. | Zero or one per episode. |
| Gravity, finality | Drop | A 1.0 to 1.5s pause after a claim, then a short line or silence. | Zero to two per episode. |
| Engagement, intimacy | Direct address | A question to the listener, then `[pause:400ms]` to `[pause:600ms]`. Second person. | Zero to two per episode. |
| Evidence, documentary | Quote | A short quote in a different voice or blend, then return to the host. | Zero to two per episode. |
| Vulnerability, honesty | Confession | `[rate:0.9]` to `[rate:0.95]`, short sentences, a pause before the admission. | Zero or one per episode. |
| Energy, authority | Rapid-fire list | `[rate:1.05]` to `[rate:1.1]`, short sentences, minimal pauses. | Zero or one per episode. |
| Humour, continuity | Callback | Repeat the running joke or a phrase from earlier. Deadpan. | Zero or one per episode. |
| Ominous, serious | Warning | default at `[rate:0.9]`, short sentences, a pause before the consequence. | Zero or one per episode. |
| Release, warmth | Relief | default after tension, `[rate:0.9]`, a long pause, then a short sentence. | Zero or one per episode. |

Build uses sentence length, not a rate ramp. Each `[rate:]` change is a turn boundary and needs a pause. Set the rate once at the start, then write short sentences.

Quote uses a different voice or a blend. It is a casting choice, not an impression. No real-person impersonation. Keep it short and return to the host. The quote is spoken as a clause with verbal attribution, because the script carries no quotation marks.

Warning uses a slower rate, not a darker emotion. The words carry the weight.

## Budgets

- Level 5: only where the model carries `angry`.
- Underline: zero or one per episode.
- Deadpan aside: two to three per 10 minutes.
- Build: zero or one per episode.
- Drop: zero to two per episode.
- Direct address: zero to two per episode.
- Quote: zero to two per episode.
- Confession: zero or one per episode.
- Rapid-fire list: zero or one per episode.
- Callback: zero or one per episode.
- Warning: zero or one per episode.
- Relief: zero or one per episode.

## Pacing audit

After writing:

- Count words per segment. Compute duration at the effective wpm. Compare with the sheet within 15 percent.
- Count sentence lengths. Compare with the pace band.
- Count explicit pauses. Compare with the pause budget.
- Count rate changes. Compare with the budget.
- Count performance moves. Compare with the budgets.
- If a segment runs long, cut words or raise the rate. Do not add ticks.
- If a segment runs short, add content or lower the rate. Do not pad.
