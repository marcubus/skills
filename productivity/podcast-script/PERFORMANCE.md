# Performance

Pacing, emotion, emphasis, and the named moves that give a script a specific vibe. Write the beat map and the pacing sheet before drafting.

## Available presets

The default deployment renders only the baseline. No emotion preset is enabled by default.

- The default is the baseline. It is no override at all.
- `[emotion:neutral]` clears any override and returns to the default.

Every preset is disabled until the deployment is tuned. Do not write `warm`, `bright`, `sad`, `tired`, `angry`, `whisper`, or `excited`. They are documented in `VOICE.md` for later, not for this skill today.

Variety comes from rate, pause, sentence length, and word choice.

## Effective words per minute

Base rate is 150 wpm at the default. The `[rate:]` multiplier applies.

```text
effective_wpm = 150 * rate_multiplier
```

A 10-minute episode is about 1500 words. Compute the target from the show baseline.

## Pace bands

| Band | Average sentence | Short | Medium | Long | Use |
|---|---|---|---|---|---|
| Slow | 18 to 22 words | 30% | 50% | 20% | evidence, reflection, close |
| Steady | 14 to 18 words | 40% | 45% | 15% | explanation, intro |
| Brisk | 10 to 14 words | 55% | 35% | 10% | hook, conflict, list |

Short is under 10 words. Medium is 10 to 20. Long is over 20.

## Pacing sheet

Write this before drafting.

| Segment | Function | Pace band | Preset | Rate | Effective wpm | Words | Duration | Pause | Handoff | Emphasis | Move |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Cold open | hook | brisk | neutral | 1.0 | 150 | 50 | 0:20 | 0 | question | 1 | deadpan |
| Context | frame | steady | neutral | 1.0 | 150 | 140 | 0:56 | 300ms | pause | 1 | none |
| Evidence | prove | slow | neutral | 0.95 | 142 | 350 | 2:28 | 600ms | pause | 2 | none |
| Conflict | tension | brisk | neutral | 1.05 | 158 | 300 | 1:54 | 600ms | interjection | 3 | none |
| Reflection | meaning | slow | neutral | 0.95 | 142 | 350 | 2:28 | 600ms | pause | 3 | confession |
| Close | land | slow | neutral | 0.9 | 135 | 25 | 0:11 | 1.2s | pause | 3 | drop |

Rules:

- Each segment has one function, one pace band, one rate, one pause budget.
- The words and durations sum to the episode target within 15 percent.
- The preset stays at the default. Rate is the only local pacing tool.
- Pauses are for beats, not for pace. Pace comes from wpm and sentence length.
- Default gap is 350ms. An explicit pause replaces it.
- Total explicit pause stays under 60 seconds.

## Section breaks

A script with multiple logical sections gets an additional pause at each section boundary. A weather update followed by local news is two sections. The listener needs a beat to register the change.

```text
... and the chance of rain is five per cent.

[pause:1000ms]

[voice:host_a] [emotion:neutral] Local news now.
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

Each beat gets a function, a pace band, a rate, and a move. Adjacent beats with the same function keep the same rate.

## Preset intent

| Preset | Use when the content is doing this |
|---|---|
| neutral | every segment. The default is the only setting. |

## Rate map

| Beat | Content | Function | Preset | Rate |
|---|---|---|---|---|
| Cold open | the bridge failed on day one | hook | neutral | 1.0 |
| Context | who signed it and what it was for | frame | neutral | 1.0 |
| Evidence | the load model assumed no pedestrians | prove | neutral | 0.95 |
| Conflict | the engineer who refused to sign | tension | neutral | 1.05 |
| Reflection | what it says about sign-off | meaning | neutral | 0.95 |
| Close | one line | land | neutral | 0.9 |

Rules:

- Keep the preset at the default for the whole episode.
- Budget: two to four rate changes in a 10-minute episode.
- Presets are sticky. `[emotion:neutral]` returns to the default.
- The words carry the emotion. The rate only moves pace. If the words do not carry it, rewrite the words.
- The profile's `emotion_behaviour` sets the range and ceilings. Only the default is renderable today.

## Same-speaker tone changes

`[emotion:]` and `[rate:]` flush the current turn in the parser. A same-speaker change lands at a sentence boundary and carries an explicit pause.

```text
[voice:host_a] [emotion:neutral] The first part lands here.

[pause:500ms]

[rate:0.95] The second part slows down.

[pause:300ms]

[rate:1.05] The third part lifts.
```

Rules:

- The pause is at least 300ms. 400 to 600ms is normal. 800 to 1000ms is a section shift.
- The default 350ms turn gap is not enough. It is the same gap as every other turn boundary.
- If the tone change is mid-sentence, rewrite the sentence or carry the shift with punctuation and word choice.
- A speaker change is different. The `[voice:]` tag is the boundary. A pause is optional there.

## Emphasis ladder

Use the lowest level that works.

| Level | Move | Cost | Use |
|---|---|---|---|
| 1 | Short sentence | none | Default. A 3 to 6 word sentence after a longer one. |
| 2 | Pause before the key word | `[pause:150ms]` to `[pause:300ms]` | A reveal or a correction. |
| 3 | Short sentence plus pause | 150 to 300ms | A key takeaway. |
| 4 | Rate change for one line | One `[rate:]` change | A lift or a drop. |
| 5 | Not available | none | The raised-voice preset is disabled. Use level 3 or 4. |

Level 5 needs the `angry` preset, which is disabled. Do not use an exclamation mark as a substitute. Use a short sentence, a pause, and a rate change.

## Underline

Pause between every word. It is a deliberate staccato, used once to make a point.

```text
It [pause:200ms] was [pause:200ms] not [pause:200ms] the [pause:200ms] database.
```

- Three to six words. No more.
- 150 to 250ms between words.
- Once per episode.
- Each word becomes its own turn, so it counts toward `MAX_TURNS` and the total pause budget.
- Use it for a short phrase that lands. Do not use it for a full sentence.

## Deadpan aside

A deadpan aside is a short utterance at `[rate:0.95]` with no ticks and a pause after it.

```text
[rate:0.95] Sure. Because that always works.
```

- One to two lines. Not a paragraph.
- Use it for an aside, an eye-roll, a secret, or a conspiratorial observation.
- The words carry the irony. Do not write stage directions.
- Return to the baseline rate on the next line with `[rate:1.0]`.
- Two to three deadpan asides per 10 minutes.
- A deadpan aside can be an interjection handoff. It still needs a pause, a question, or an interjection at the speaker change.

The `whisper` preset is disabled. A deadpan aside replaces it.

## Performance moves

| Vibe | Move | Mechanism | Budget |
|---|---|---|---|
| Dry, skeptical | Deadpan | default at `[rate:0.95]`, short sentences, no ticks, a pause after the line. | As needed. |
| Momentum, escalation | Build | `[rate:1.05]`, then 3 to 5 short sentences. No pauses inside the run. End on a short line. | Once per episode. |
| Gravity, finality | Drop | A 1.0 to 1.5s pause after a claim, then a short line or silence. | Once or twice. |
| Engagement, intimacy | Direct address | A question to the listener, then `[pause:400ms]` to `[pause:600ms]`. Second person. | One or two. |
| Evidence, documentary | Quote | A short quote in a different voice or blend, then return to the host. | One or two. |
| Vulnerability, honesty | Confession | default at `[rate:0.9]`, short sentences, a pause before the admission. | Once. |
| Energy, authority | Rapid-fire list | `[rate:1.05]` to `[rate:1.1]`, short sentences, minimal pauses. | Once. |
| Humour, continuity | Callback | Repeat the running joke or a phrase from earlier. Deadpan. | Once. |
| Ominous, serious | Warning | default at `[rate:0.9]`, short sentences, a pause before the consequence. | Once. |
| Release, warmth | Relief | default after tension, `[rate:0.9]`, a long pause, then a short sentence. | Once. |

Build uses sentence length, not a rate ramp. Each `[rate:]` change is a turn boundary and needs a pause. Set the rate once at the start, then write short sentences.

Quote uses a different voice or a blend. It is a casting choice, not an impression. No real-person impersonation. Keep it short and return to the host.

Warning uses a slower rate, not a darker preset. The words carry the weight.

## Budgets

- Level 5: unavailable.
- Underline: zero or one per episode.
- Deadpan aside: two to three per 10 minutes.
- Drop: zero or two per episode.
- Direct address: zero or two per episode.
- Quote: zero or two per episode.
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
