# Pre-render check: panel-script, for kokoro-fastapi

Brought-in script. Checks 7 to 21, per `VERIFY.md`. The script is not rewritten. Only the compiled text was produced.

Verdict: **not ready to render.** Ten checks fail. The failures are in the script, not the dialect, so a compile cannot fix them.

## Compiled text

`panel-script-tts-kokoro-fastapi.txt`. 204 spoken words. Every marker resolved:

- `[voice:]` dropped, 16 markers.
- `[emotion:sad]` dropped, 1 marker.
- `[rate:]` dropped, 4 markers.
- `[pause:]` translated to blank lines, 6 markers. 1200ms became a double blank line; 300ms and 400ms became one.
- `[sense:read=red]` respelt as `red`, 1 marker.

Twenty-one markers are dropped in total. None survives in the text. The text holds no payload, no heading, no tag the model does not read.

## Failures

| Check | Result | Detail |
|---|---|---|
| 5 Script shape | FAIL | The first line is `# panel-script (kokoro-fastapi)`, a markdown heading. A compiler that reads the file as-is speaks it. |
| 6 Word count | FAIL | 204 words. No target is declared and no pacing sheet exists, so runtime cannot be verified. 204 words is about 1:22, short for a panel. |
| 8 Forbidden characters | FAIL | No forbidden characters, but the markdown check finds the heading on line 1. |
| 9 Section breaks | FAIL | One of five boundaries carries a 1000 to 1200ms break. The break before the cost segment is 1200ms. The boundaries before the load model, the sign-off, the staircase, and the close carry 300ms, 300ms, 300ms, and 400ms. |
| 11 Speaker changes | FAIL | Five voice changes have no pause, no question, and no interjection: host_b to host_c after the load model, host_b to host_c after the traffic figure, host_c to host_b after the record line, host_b to host_c after the staircase, and host_c to host_a on the closing line. |
| 12 Interjections | FAIL | `Wait.` is a permitted interjection, but it shares a turn with a question and the 300ms pause comes after the whole turn, not after the interjection. There is no reset to the host baseline in the following turn. |
| 14 Ticks | FAIL | `Wait` is TICK-079 and permitted. No host profiles exist, so inventory and density cannot be checked. None of the three signature ticks in the panel plan appears in the script: TICK-020, TICK-119, TICK-090. |
| 15 Banlist and meta-commentary | FAIL | Two instances of source commentary: `The review says it went around three weeks earlier` and `It says the record is good enough to show what was built`. Both describe the document rather than the event. |
| 18 Pronunciation | FAIL | `Lachie` has no route. This model reads what is written, so the name is an unresolved guess. |
| 19 Panel checks | FAIL | No host profiles. The panel plan has no bridge phrase per host and no segment plan, so it does not cover every segment. All three signature ticks are missing from the script. |

## Passes

| Check | Result | Detail |
|---|---|---|
| 7 Markers | PASS | Five marker types, no bare bracket. `sad` is in the eight. Rates are 0.95 to 1.1, inside 0.75 to 1.3. |
| 10 Same-speaker tone changes | PASS | The `[emotion:sad]` and `[rate:]` tags all land on a new speaker, at a sentence boundary, with a pause. |
| 13 Emphasis and moves | PASS | No underlines, deadpan asides, builds, drops, direct address, quotes, confessions, lists, callbacks, warnings, or reliefs. Nothing is over budget. |
| 16 Text matches | PASS | The words match the script body after the markers resolve, apart from `read` respelt as `red`. |
| 17 Text only | PASS | Spoken words and nothing else. No payload, heading, comment, or code fence. |
| 20 Claims trace | NOT RUN | The source report is not in this folder. The check needs `bridge-report.md` beside the script. |

## Dropped markers

| Marker | Count | Where |
|---|---|---|
| `[voice:host_a]` | 6 | Turns 1, 8, 10, 15, 19, 22 |
| `[voice:host_b]` | 5 | Turns 2, 5, 11, 13, 16 |
| `[voice:host_c]` | 5 | Turns 3, 6, 12, 17, 21 |
| `[emotion:sad]` | 1 | Turn 8, the admission |
| `[rate:1.05]` | 1 | Turn 3, the interjection |
| `[rate:1.1]` | 1 | Turn 12, the challenge |
| `[rate:1.0]` | 1 | Turn 19, the cost reset |
| `[rate:0.95]` | 1 | Turn 22, the closing line |

The text carries no voice, emotion, or rate control. The words carry all of it.

## Unresolved guesses

- `Lachie` is not respelt. The text says `Lachie`, and the model will guess.
- The speaker behind every turn is gone from the text. No turn map exists, because no profiles exist to name the voices.

## What to fix before render

1. Strip the heading. It is the only markdown in the file.
2. Add section-break pauses at the four boundaries that have 300ms or 400ms.
3. Add a pause, a question, or an interjection at the five bare voice changes.
4. Give `Wait.` its own turn, or move the pause to follow it.
5. Rewrite the two `the review says` lines as content.
6. Respell `Lachie`, or add a `[sense:]` route.
7. Write the three profiles, add the bridge phrases and the segment plan to the panel plan, and place each host's signature tick.

No audio exists. The check stops here.
