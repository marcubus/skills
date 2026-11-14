# Models

The script is model-neutral. It marks intent with five markers: `[voice:]`, `[emotion:]`, `[rate:]`, `[pause:]`, `[sense:]`. A model file compiles those markers into one target's text dialect.

Each model file is the only place that model's rules live. This file is the registry and the choosing rules.

The skill produces text, not a payload. A model file says what the text carries, never how to call the service.

## Registry

| Model | Text dialect |
|---|---|
| [`kokoro-tone`](MODEL-KOKORO-TONE.md) | Inline tags for every marker |
| [`kokoro-fastapi`](MODEL-KOKORO-FASTAPI.md) | Plain text, punctuation for pauses |
| [`kokoro-raw`](MODEL-KOKORO-RAW.md) | Plain text, blank lines for pauses |
| [`elevenlabs`](MODEL-ELEVENLABS.md) | Inline emotion cues, punctuation for pauses |

## Choosing

Pick the model the user names. Default to `kokoro-tone`. Record the choice in the notes file.

The compile procedure is in `HANDOFF.md`; the rules for each dialect are in its model file.

## Adding a model

1. Copy the shape of `MODEL-ELEVENLABS.md`.
2. Fill the capability table and the text rules from the provider's docs.
3. Add a row to the registry above.
4. Add the model to the list in `SKILL.md`.
5. Run `VERIFY.md` against it.

A model that cannot carry a marker in text still supports the script: it compiles, and the loss is recorded in the notes.
