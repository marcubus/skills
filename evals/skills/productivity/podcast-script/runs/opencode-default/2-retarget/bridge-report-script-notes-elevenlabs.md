# Script notes: bridge-report-podcast-script, retargeted to elevenlabs

## Model

`elevenlabs`. It reads inline audio tags, so emotion survives in the text. It has no voice or rate control, so both are dropped and recorded here.

## Source

`bridge-report-podcast-script.md`, written for `kokoro-tone`. The retarget compiles the markers; it does not rewrite the script. The words are unchanged apart from the two respellings the dialect requires.

## Counts

- Spoken words: 314, the same as the source script.
- Speech: about 2:05 at the source script's rates.
- Runtime: unchanged. The text carries no rate control, so the render runs at the voice default.
- Voices: `host_a` and `host_b`. Selected at render.

## Turn map

The model drops `[voice:]`, so the speaker lives here and in the source script, not in the text.

| Turn | Speaker | Opens with | Pause before |
|---|---|---|---|
| 1 | host_a | The bridge failed on its first day. | none, episode start |
| 2 | host_b | And nobody was hurt? | 600ms |
| 3 | host_a | Nobody was hurt. | turn break |
| 4 | host_b | So what did the model get wrong? | 400ms |
| 5 | host_a | It assumed a crowd that keeps walking. | turn break |
| 6 | host_b | They stop. | 400ms |
| 7 | host_a | The model assumed they move. | turn break |
| 8 | host_b | That is not a rounding error. | 600ms |
| 9 | host_a | No. It is a different bridge. | turn break |
| 10 | host_b | Who signed it? | 400ms |
| 11 | host_a | Lachie Fraser. | turn break |
| 12 | host_b | Did he sign the revision? | 400ms |
| 13 | host_a | He did not. | turn break |
| 14 | host_b | And the second staircase? | 600ms |
| 15 | host_a | Added during construction. | turn break |
| 16 | host_b | Which is the part that gets me. | 400ms |
| 17 | host_a | Mine too. | turn break |
| 18 | host_a | The bridge cost thirty one million. | 1000ms |
| 19 | host_b | What does the review actually recommend? | 400ms |
| 20 | host_a | Replace the bearing. | turn break |
| 21 | host_b | Will they do it? | 600ms |
| 22 | host_a | They will do the bearing. | turn break |
| 23 | host_a | One line. | 600ms |

Turn 17 and turn 18 are the same speaker, split by the 1000ms section break. The text carries that break as a double blank line.

## Dropped markers

| Marker | Where | Reason |
|---|---|---|
| `[voice:host_a]` | Every host_a turn | The model has no speaker control |
| `[voice:host_b]` | Every host_b turn | The model has no speaker control |
| `[rate:0.95]` | The crowd assumption | The model has no rate control |
| `[rate:1.05]` | The second staircase | The model has no rate control |
| `[rate:1.0]` | The cost paragraph | The model has no rate control |
| `[rate:0.95]` | They will do the bearing | The model has no rate control |
| `[rate:0.9]` | The closing line | The model has no rate control |

Every rate change is lost in the text. The render uses one rate for the whole episode. This is the largest thing the retarget gives up: the slow close and the fast staircase both flatten to the voice default.

## Kept markers

| Marker | Becomes |
|---|---|
| `[emotion:sad]` | `[sadly]` before `No. It is a different bridge.` |
| `[emotion:warm]` | `[warmly]` before `Mine too.` |

Both land at the start of the run they apply to, which is where the model file puts them.

## Pauses

| Script pause | Text |
|---|---|
| 400ms | one blank line, the same as a turn break |
| 600ms | one blank line, the same as a turn break |
| 1000ms | two blank lines |

The dialect collapses 400ms and 600ms into the same break, so the difference between a beat and a longer beat is lost. Only the 1000ms section break survives as a distinct mark. That is a limit of punctuation as pause control, not a compile error.

## Pronunciation

| Word | Route |
|---|---|
| Lachie | Respelt as `Locky` |
| bass | Respelt as `base`, from `[sense:bass=base]` |

Both respellings are the only word-level changes in the text. No `[sense:]` marker survives.

## What was lost

- Voice identity. The text is one stream; the turn map above is the only record of who speaks.
- Rate. Five changes, all gone. The pacing sheet in the source notes no longer describes the render.
- Pause precision. 400ms and 600ms are indistinguishable in the text.

The words are intact, so the episode can still be rendered. It will sound flatter than the `kokoro-tone` version, and the turn map is what a human editor needs to split it back into speakers if the render needs separate takes.

## Gate

Checks 7 to 20 of `VERIFY.md`, as a brought-in script. Source order and profile checks are skipped: this is a retarget, and the profiles belong to the original run.
