# kokoro-fastapi

Kokoro without the tone layer. A plain text dialect: no inline controls.

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
| `[pause:]` | Punctuation and paragraph breaks. |
| `[sense:]` | Respelt in the text. |

## Compile

- `[voice:]` → drop. Record the speaker and the voice in the notes.
- `[emotion:]` → drop. Record it.
- `[rate:]` → drop. Record it.
- `[pause:]` → a paragraph break, or a full stop for a short pause.
- `[sense:]` → respell.

## Pauses

The text carries no pause control. Map the pause to punctuation and line breaks: 300ms or less is a comma or a full stop, 301 to 799ms is one blank line, and 800ms or more is two blank lines.

## Emotion

The text carries no emotion control. The words do the work. Every emotion marker is dropped and recorded.

## Pronunciation

Respell every proper noun, acronym, and heteronym in the text. The model reads what is written.

## Splitting

The compiled text is one file. Split it at section boundaries only when the target cannot take the whole episode, and record the split in the notes.
