# elevenlabs

ElevenLabs. The only dialect that reads audio tags, so emotion survives in the text.

## Contents

- Capability
- Compile
- Audio tags
- Pauses
- Pronunciation
- Splitting

## Capability

| Marker | In the text |
|---|---|
| `[voice:]` | Dropped. The speaker stays in the script, not the text. |
| `[emotion:]` | An inline audio tag. |
| `[rate:]` | Dropped. |
| `[pause:]` | Punctuation and paragraph breaks. |
| `[sense:]` | Respelt in the text. |

## Compile

- `[voice:]` → drop. Record the speaker and the voice in the notes.
- `[emotion:warm]` → `[warmly]` at the start of the run, and drop the marker. Use the table below for the other values.
- `[rate:]` → drop. Record it.
- `[pause:]` → a paragraph break, or a full stop for a short pause.
- `[sense:]` → respell.

## Audio tags

Tags are inline, so emotion can change within one text. Put the tag at the start of the run it applies to.

| Marker | Audio tag |
|---|---|
| `[emotion:neutral]` | none |
| `[emotion:warm]` | `[warmly]` |
| `[emotion:bright]` | `[cheerfully]` |
| `[emotion:sad]` | `[sadly]` |
| `[emotion:tired]` | `[tired]` |
| `[emotion:angry]` | `[angry]` |
| `[emotion:whisper]` | `[whispering]` |
| `[emotion:excited]` | `[excited]` |

An unknown tag may be spoken, so use only the tags above. The model page is the authority if it changes.

## Pauses

The text carries no pause control. Map the pause to punctuation and line breaks: 300ms or less is a comma or a full stop, 301 to 799ms is one blank line, and 800ms or more is two blank lines.

## Pronunciation

Respell every proper noun, acronym, and heteronym in the text. The model reads what is written.

## Splitting

The compiled text is one file. Split it at section boundaries only when the target cannot take the whole episode, and record the split in the notes.
