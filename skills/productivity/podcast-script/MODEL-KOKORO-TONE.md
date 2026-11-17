# kokoro-tone

Kokoro with the tone layer. The richest text dialect: every marker survives as an inline tag.

## Contents

- Capability
- Compile
- Tags
- Tag behaviour
- Emotion
- Pronunciation
- Splitting

## Capability

| Marker | In the text |
|---|---|
| `[voice:]` | Kept. Selects the speaker. |
| `[emotion:]` | Kept. `neutral` only. |
| `[rate:]` | Kept. A multiplier. |
| `[pause:]` | Kept. Silence at that point. |
| `[sense:]` | Kept. Resolved before synthesis. |

## Compile

- `[voice:]` → keep.
- `[emotion:]` → keep `neutral`. Compile any other value to nothing and record it.
- `[rate:]` → keep.
- `[pause:]` → keep.
- `[sense:]` → keep.

## Tags

| Tag | Example | Meaning |
|---|---|---|
| `[voice:name]` | `[voice:host_a]` | Select a speaker. Sticky. |
| `[emotion:neutral]` | `[emotion:neutral]` | Clear an emotion override and return to the default. |
| `[rate:1.05]` | `[rate:1.05]` | Multiply the base rate. Sticky. `[rate:1.0]` means no change. |
| `[pause:800ms]` | `[pause:1.2s]` | Add silence. At a turn boundary it replaces the default gap. Inline, it pauses mid-turn. |
| `[sense:word=sense]` | `[sense:bass=music]` | Choose a heteronym reading. |

Unknown `[tag:value]` pairs are left in the text and spoken. Use only the five known tags.

## Tag behaviour

Tags are independent slots. Changing `[voice:]` resets neither emotion nor rate. `[emotion:neutral]` clears only the emotion. `[rate:1.0]` is the reset; there is no separate reset tag.

`[emotion:]` and `[rate:]` start a new turn. They are boundaries, not inline modifiers. A same-speaker change lands at a sentence boundary and carries an explicit pause. A speaker change uses `[voice:]` as the boundary.

## Emotion

`neutral` is the only value this text carries. Any other value is dropped and recorded. `neutral` clears the override; the default baseline is no override at all.

## Pronunciation

Every proper noun, acronym, and heteronym gets a route. Use a `[sense:word=sense]` tag for a heteronym. Respell a name or a word-said acronym in the text.

## Splitting

The compiled text is one file. The request is not: kokoro-tone drops a body that runs too long upstream, so a long episode is sent in parts and the parts are joined. Splitting is the renderer's job. This section is the rule it implements and the rule the notes record.

- Cap the request, not the episode. 4000 characters is about four minutes of speech and is the default cap. 19700 characters in one request took nine minutes upstream and then died with a 502, so a single-request long-form render is not a safe default.
- Break at section pauses first. Each `[pause:1000ms]` or `[pause:1200ms]` is a natural seam, and the pause stays with the part it closes, so the silence renders inside that request instead of being lost between two.
- Break at turn boundaries next, when one section is still over the cap. A turn boundary is where the engine already inserts its own gap, so a cut there is inaudible.
- Repeat the sticky state at every seam. `[voice:]` and `[rate:]` persist only within one request, so the part after a seam must open with the voice and rate in force at that point. A seam that forgets them drops the voice or the rate for everything after it, and nothing in the audio says so.
- Never cut mid-sentence, and never truncate the episode to fit. A part is a request boundary, not an edit.
- Record the split in the notes: the number of parts, the cap, and where the seams fell.

The compiled text stays one file whatever the split. A reader must be able to render the episode again from the two files without knowing how it was cut the first time.
