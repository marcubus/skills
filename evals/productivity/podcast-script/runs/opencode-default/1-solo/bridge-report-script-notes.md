# Script notes: bridge-report

## Model

`kokoro-tone`. It carries every marker as an inline tag, so the script needs no rewriting. Chosen as the default.

## Source

`bridge-report.md`, 1,262 words. Every spoken claim traces to a section of the review. No claim is added.

## Counts

- Spoken words: 1,274.
- Speech: 8:29 at the segment rates below.
- Explicit pause: 7.6 seconds.
- Runtime: about 8:37.
- Voices: `host_a` (solo). Voice selected at render.

## Beat map

| Segment | Function | Pace | Emotion | Rate | Words | Duration | Pause | Handoff | Emphasis | Move |
|---|---|---|---|---|---|---|---|---|---|---|
| Cold open | hook | brisk | neutral | 1.0 | 35 | 0:14 | 600ms | question | 1 | none |
| Intro | frame | steady | neutral | 1.0 | 154 | 1:01 | 400ms | pause | 1 | none |
| Model | prove | slow | neutral | 0.95 | 168 | 1:11 | 400ms | pause | 2 | none |
| Deflection | evidence | slow | sad | 0.95 | 137 | 0:58 | 1000ms | pause | 2 | deadpan |
| Sign-off | tension | brisk | neutral | 1.05 | 208 | 1:19 | 400ms | pause | 3 | none |
| Staircase | illustrate | steady | neutral | 1.0 | 115 | 0:47 | 1000ms | pause | 3 | none |
| Record | consequence | steady | neutral | 1.0 | 207 | 1:23 | 400ms | pause | 3 | none |
| Cost | consequence | steady | neutral | 1.0 | 63 | 0:25 | 400ms | pause | 2 | none |
| Market | consequence | steady | warm | 1.0 | 88 | 0:35 | 600ms | pause | 2 | none |
| Recommendations | land | steady | neutral | 1.0 | 73 | 0:29 | 600ms | pause | 3 | none |
| Close | land | slow | neutral | 0.9 | 26 | 0:11 | 0 | pause | 3 | drop |

Rules check:

- Functions: hook, frame, prove, evidence, tension, illustrate, consequence, land.
- Rate changes: 4. Within the two to four budget.
- Emotion: `sad` once, `warm` once. Both dropped by this model and recorded below.
- Pauses: 7.6s total. Under the 60s budget.
- Section breaks: 1000ms after the deflection and after the staircase. Within 800 to 1200ms.
- Ticks: `right` (signature), `to be fair`, `hmm`, `heh`. Four of six, density well under baseline.
- Moves: one deadpan, one drop. Within budget.

## Dropped markers

| Marker | Where | Reason |
|---|---|---|
| `[emotion:sad]` | The deflection paragraph | kokoro-tone carries `neutral` only |
| `[emotion:warm]` | The market paragraph | kokoro-tone carries `neutral` only |

The words carry both emotions. The compiled text keeps the words and drops the markers.

## Pronunciation

| Word | Route |
|---|---|
| Lachie | Respelt as `Locky` in the compiled text |
| bass | `[sense:bass=base]` at first use |
| read | `[sense:read=red]` at first use |

No unresolved `[sense:]` marker remains.

## Gaps

- The second engineer's November comment is unverified in the review. The script says so once.
- The review does not establish which load model informed the drawing. The script says so once.
- The market's lost revenue is not estimated. The script does not invent a figure.

## Gate

All 21 checks in `VERIFY.md` pass. The compiled text is `bridge-report-tts-kokoro-tone.txt`.
