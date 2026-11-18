# Pre-render check: panel-script, for kokoro-fastapi

Brought-in script. Checks 7 to 21, per `VERIFY.md`. The script is not rewritten. Only the compiled text was produced.

Verdict: **not ready to render.** Three checks fail, all in the script. The profiles and the panel plan pass.

## Compiled text

`panel-script-tts-kokoro-fastapi.txt`. 204 spoken words, about 1:27 at the panel rates.

Every marker resolved:

- `[voice:]` dropped, 16 markers.
- `[emotion:sad]` dropped, 1 marker.
- `[rate:]` dropped, 4 markers.
- `[pause:]` translated to blank lines, 12 markers. The three 1000ms and 1200ms breaks became double blank lines; the 300ms and 400ms breaks became one.
- `[sense:read=red]` respelt as `red`, 1 marker.

Twenty-one markers are dropped and thirteen are translated. None survives in the text. The text holds no payload, no heading, and no tag the model does not read.

## Failures

| Check | Result | Detail |
|---|---|---|
| 8 Forbidden characters | FAIL | No forbidden characters, but the markdown check finds the heading on line 1, `# panel-script (kokoro-fastapi)`. A compiler that reads the file as-is speaks it. |
| 9 Section breaks | FAIL | Four of five boundaries carry a 1000ms or 1200ms break. The boundary before the close carries 300ms. It needs 1000 to 1200ms. |
| 18 Pronunciation | FAIL | `Lachie` has no route. This model reads what is written, so the name is an unresolved guess. |

## Passes

| Check | Result | Detail |
|---|---|---|
| 7 Markers | PASS | Five marker types, no bare bracket. `sad` is in the eight. Rates are 0.95 to 1.1, inside 0.75 to 1.3. |
| 10 Same-speaker tone changes | PASS | The `[emotion:sad]` and every `[rate:]` land on a new speaker, at a sentence boundary, with a pause. |
| 11 Speaker changes | PASS | Every voice change has a pause, a question, or an interjection. |
| 12 Interjections | PASS | `Wait.` is two words at `[rate:1.05]`, followed by 300ms and a reset to `[rate:1.0]`. |
| 13 Emphasis and moves | PASS | No underlines, deadpan asides, builds, drops, direct address, quotes, confessions, lists, callbacks, warnings, or reliefs. |
| 14 Ticks | PASS | Four ticks, all permitted and all in the speaker's inventory: `right`, `wait`, `to be fair`, `the short version`. Density is 1.96 per 100 words, under the 2.0 panel baseline. |
| 15 Banlist and meta-commentary | PASS | No banned literal and no process commentary. The two source attributions in the earlier draft are gone. |
| 16 Text matches | PASS | The words match the script body after the markers resolve, apart from `read` respelt as `red`. |
| 17 Text only | PASS | Spoken words and nothing else. No payload, heading, comment, or code fence. |
| 19 Panel checks | PASS | Three profiles, each passing the gate. The plan carries a bridge phrase and a segment plan covering every host and segment. All three signature ticks appear in the script. The moderator opens and closes. Every panelist turn is one to three sentences. No two hosts share a tick, opener, or bridge. |
| 20 Claims trace | PASS | Every figure traces to `bridge-report.md`. Nine thousand and four thousand are the source's 9,140 and 3,913, rounded. No figure is invented. |
| 21 Handoff summary | PASS | Below. |

## Dropped markers

| Marker | Count | Where |
|---|---|---|
| `[voice:host_a]` | 6 | Turns 1, 6, 7, 11, 14, 16 |
| `[voice:host_b]` | 5 | Turns 2, 4, 8, 10, 12 |
| `[voice:host_c]` | 5 | Turns 3, 5, 9, 13, 15 |
| `[emotion:sad]` | 1 | Turn 6, the admission |
| `[rate:1.05]` | 1 | Turn 3, the interjection |
| `[rate:1.0]` | 1 | Turn 4, the reset |
| `[rate:1.0]` | 1 | Turn 14, the cost reset |
| `[rate:0.95]` | 1 | Turn 16, the closing line |

The text carries no voice, emotion, or rate control. The words carry all of it.

## Unresolved guesses

- `Lachie` is not respelt. The text says `Lachie`, and the model will guess.
- The speaker behind every turn is gone from the text. The profiles and the plan carry the casting; the text does not.

## What to fix before render

1. Strip the heading on line 1. It is the only markdown in the file.
2. Raise the pause before the closing line from 300ms to 1000ms.
3. Respell `Lachie`, or add a `[sense:]` route.

The script is otherwise renderable. No audio exists. The check stops here.
