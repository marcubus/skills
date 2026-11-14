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

The compiled text is one file. Split it at section boundaries only when the target cannot take the whole episode, and record the split in the notes.
