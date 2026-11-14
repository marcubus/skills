# Voice

Casting, rate, and pause. The script marks voice and rate; the model file says how they compile.

## Casting

- Use a stable speaker label in `[voice:]`, such as `host_a` for a solo or two-host show, and `host_a`, `host_b`, `host_c` for a panel. The model file says whether the label survives in the text.
- The script names speakers, not voices. Record the voice casting in the notes.
- A multi-host script keeps one label per speaker. Where the model drops `[voice:]`, the notes carry a turn map: which runs belong to which speaker.

| Role | Character |
|---|---|
| Narrator or host A | clear, steady |
| Host B | distinct from host A in timbre |
| Guest or panelist | contrast against both |

Cast for contrast. Pick the voices when you cast, and record them in the notes.

## Emotion

The script marks emotion with `[emotion:]`. The model file says how the marker compiles, and which values it carries.

- The words carry the emotion. The rate only moves pace.
- If a passage needs more weight, slow the rate and shorten the sentence.

## Rate

- `[rate:]` multiplies the base rate. Keep it within 0.75 to 1.3.
- `[rate:1.0]` means no change. Use it to reset a sticky rate.
- Rate is sticky across voice changes. Reset it at the next speaker's first turn when that speaker should not inherit it.
- Do not stack two rate changes on one line. State the dominant rate once.
- A same-speaker rate change lands at a sentence boundary and carries an explicit pause.
- Useful bands: `0.9` for a close or a warning, `0.95` for evidence, `1.0` for explanation, `1.05` for a build or a list.

## Pause

- `[pause:800ms]` or `[pause:1.2s]` adds silence at that point.
- An explicit pause replaces the default turn gap where the model has one.
- One explicit pause per boundary. Total explicit pause stays under 60 seconds.
- Where the model has no pause control, compile the pause to punctuation.
- Use pauses for beats and section breaks, not for pace.
- A logical section boundary gets 800 to 1200ms.
- A same-speaker tone change gets 300 to 600ms.
- An interjection handoff gets 200 to 300ms after the interjection.
- A panel section break gets 1000 to 1200ms.

## Voice changes

Changing `[voice:]` resets neither emotion nor rate. If the new speaker should not inherit the previous rate, add `[rate:1.0]`.

A voice change is a speaker change. It needs a pause, a question, or an interjection. See `MULTIHOST.md` and `PANEL.md`.
