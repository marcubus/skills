# Example beat map

Guidance only. A 10-minute episode at the default baseline. The target is 1500 words.

Most beats keep the default emotion. Two carry the one the beat needs, and the model file says what renders: `kokoro-tone` drops both and the notes record them. Variety still comes from rate, pause, sentence length, and word choice.

| Segment | Function | Content | Pace band | Emotion | Rate | Effective wpm | Words | Duration | Pause | Handoff | Emphasis | Move |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Cold open | hook | the bridge failed on day one | brisk | neutral | 1.0 | 150 | 50 | 0:20 | 0 | question | 1 | none |
| Context | frame | who signed it and what it was for | steady | neutral | 1.0 | 150 | 180 | 1:12 | 300ms | pause | 1 | none |
| Evidence | prove | the load model assumed a crowd that keeps moving | slow | neutral | 0.95 | 142 | 450 | 3:10 | 600ms | pause | 2 | none |
| Conflict | tension | the engineer who refused to sign | brisk | neutral | 1.05 | 158 | 350 | 2:13 | 600ms, then a 1000ms section break | pause | 3 | none |
| Reflection | meaning | what it says about sign-off | slow | sad | 0.95 | 142 | 420 | 2:57 | 600ms | pause | 3 | confession |
| Close | land | one line | slow | warm | 0.9 | 135 | 50 | 0:22 | 1.2s | pause | 3 | drop |

## Rate map

| Beat | Function | Emotion | Rate | Why it moves |
|---|---|---|---|---|
| Cold open | hook | neutral | 1.0 | baseline |
| Context | frame | neutral | 1.0 | settle |
| Evidence | prove | neutral | 0.95 | authority |
| Conflict | tension | neutral | 1.05 | lift |
| Reflection | meaning | sad | 0.95 | release |
| Close | land | warm | 0.9 | finality |

## Checks

- Total words: 1500. Within 15 percent of the target.
- Runtime: 10:14 of speech plus 4.3s of explicit pause, about 10:18.
- Rate changes: 4, at 1.0 to 0.95, 0.95 to 1.05, 1.05 to 0.95, and 0.95 to 0.9. Within the two to four budget for 10 minutes.
- Emotion: `sad` once, `warm` once. `kokoro-tone` drops both and the notes record them.
- Level 5: 0. This episode uses levels 1 to 3.
- Section break: 1000ms. Within 800 to 1200ms.
- Total explicit pause: 4.3s. Within 60s.
