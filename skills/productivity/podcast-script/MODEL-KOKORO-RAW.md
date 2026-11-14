# kokoro-raw

Kokoro read directly, with no tone layer. A plain text dialect: blank lines carry the pauses.

## Contents

- Capability
- Compile
- Pauses
- Emotion
- Pronunciation
- Splitting

## Capability

| Marker | In the text |
|---|---|
| `[voice:]` | Dropped. The speaker stays in the script, not the text. |
| `[emotion:]` | Dropped. |
| `[rate:]` | Dropped. |
| `[pause:]` | Blank lines. |
| `[sense:]` | Respelt in the text. |

## Compile

- `[voice:]` → drop. Record the speaker and the voice in the notes.
- `[emotion:]` → drop. Record it.
- `[rate:]` → drop. Record it.
- `[pause:]` → a blank line. A section break is two blank lines.
- `[sense:]` → respell.

## Pauses

A blank line is the only pause the text carries. A pause of 300ms or less is a comma or a full stop. A pause of more than 300ms is a blank line. A section break is two blank lines. The renderer splits on blank lines, so keep each spoken run as one paragraph.

## Emotion

The text carries no emotion control. The words do the work. Every emotion marker is dropped and recorded.

## Pronunciation

Respell every proper noun, acronym, and heteronym in the text. The model reads what is written.

## Splitting

The compiled text is one file. Split it at section boundaries only when the target cannot take the whole episode, and record the split in the notes.
