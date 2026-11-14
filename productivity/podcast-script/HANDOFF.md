# Handoff

The handoff is the script compiled into one model's text dialect. The script carries markers; the compiled text carries tags. Read `MODELS.md` first: it holds the registry and the choosing rules. This file holds the compile procedure, the file names, and the notes contract.

The skill delivers text. It does not call a speech service, build a payload, or render audio. A request body, an endpoint, a key, and a response belong to the tool that renders the text, not to this skill.

## Choose the model

Pick one model per episode. `MODELS.md` holds the choosing rules.

The model file decides what the text can carry. The script keeps its markers either way.

## Compile

Run the model's compile rules against the script body. Keep the script file unchanged; write the result into a plain text file.

For each marker, the model either keeps it as text or the compiler translates or drops it:

- **Keep**: the marker stays in the text, because the model reads it.
- **Translate**: replace the marker with text the model reads, such as an inline cue or a paragraph break.
- **Drop**: drop the marker, keep the words, and record the loss in the notes.

A dropped marker is not a failure. It is a documented loss. State every dropped marker in the notes. `[sense:]` is always resolved, never dropped.

The script carries the markers it needs; every marker present is resolved. The compile step drops what the text cannot carry.

Done when every marker is resolved: kept, translated, or dropped and recorded. An unresolved marker left in the text is read aloud; a kept marker is read by the model.

## File name

Name the compiled text after the source and the model:

```text
<source-stem>-tts-<model>.txt
```

Example: `bridge-report-tts-elevenlabs.txt`.

The file holds the spoken text and the model's inline controls, and nothing else. No front matter, no headings, no comments, no payload.

## Pronunciation

Every proper noun, acronym, and heteronym needs a route. Resolve it the way the model file says.

Done when no unresolved `[sense:]` marker remains and every name has a route.

## Notes

Write `<source-stem>-script-notes.md` beside the script. A retarget writes `<source-stem>-script-notes-<model>.md` and leaves the original notes untouched. It carries what the text cannot:

- The model and why it was chosen.
- The beat map and the pacing sheet.
- Every dropped marker and the reason.
- The word count and the declared runtime.
- The speaker-to-voice casting.
- The turn map, run to speaker, when the model drops `[voice:]`.
- The panel plan, when the script is a panel.
- Unresolved guesses, pronunciation routes, and gaps.

## Deliver

State:

- The model.
- The script path and the compiled text path.
- The word count, runtime, and voices.
- Every dropped marker.
- Any unresolved guesses or gaps.

Report the script and the compiled text as the deliverables. The render is the next step, so the handoff ends before audio exists.
