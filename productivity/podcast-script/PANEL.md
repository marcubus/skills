# Panel

Three or more hosts. A panel is not a two-host show with an extra voice. It needs a moderator, a turn order, and a reason for each voice to exist.

## Panel plan

Write this before drafting.

| Host | Role | Voice | Owns | Defers | Opens | Closes | Signature |
|---|---|---|---|---|---|---|---|
| Host A | moderator | af_heart | the through-line | the technical detail | yes | yes | right |
| Host B | expert | am_michael | infrastructure | policy | no | no | the short version |
| Host C | skeptic | bm_lewis | risk | implementation | no | no | not quite |

Rules:

- One moderator. The moderator opens, directs, and closes.
- Every panelist has a profile, a distinct voice, a role, a signature tick, and a bridge phrase.
- No two panelists share a signature, a bridge phrase, or an opener.
- The moderator owns the intro, the links, the corrections, and the outro.
- The panelists own the body. They answer the moderator's questions.
- Each panelist gets one turn per question, one to three sentences.
- The moderator names the next speaker or asks the next question.
- No two panelists answer the same question with the same point.

## Segment plan

| Segment | Lead | Respondents | Handoff | Length |
|---|---|---|---|---|
| Cold open | moderator | none | none | 20s |
| Intro | moderator | all | question | 30s |
| Topic 1 | moderator | Host B, Host C | question | 2m |
| Topic 2 | moderator | Host C, Host B | question | 2m |
| Close | moderator | all | pause | 30s |

Each topic has a lead, one or two respondents, a handoff, and a length. The plan covers every host and every segment.

## Handoffs

The moderator's question is the default handoff. It is natural, it names the next speaker, and it does not need a pause.

- Question handoff: the moderator asks, the panelist answers. Use this for most turns.
- Pause handoff: use at section breaks, 1000 to 1200ms.
- Interjection handoff: use sparingly. One per topic. Three hosts piling on sounds like a crowd.
- Every voice change still needs a pause, a question, or an interjection.
- `takes_floor: waits`, `max_overlap_words: 0`. No overlapping speech.
- Interjections are one to four words, `[rate:1.05]` to `[rate:1.1]`, followed by a short pause and a reset.

## Section breaks

A panel section boundary gets 1000 to 1200ms.

```text
... that is the weather picture.

[pause:1200ms]

[voice:host_a] [emotion:neutral] Local news now.
```

The pause is explicit. The default gap is not enough.

## Energy

- Lower than a two-host show. The moderator controls the pace.
- Do not let three hosts peak at once. One strained state at a time.
- Backchannels: one host per turn, max two per host per episode.
- Tick density: 2.0 baseline, 3.5 strained, 5.0 ceiling.
- One callback or running joke per episode, not per host.
- The moderator de-escalates. A panel that argues over itself is unlistenable.

## Panel profile fields

Replace the two-host `show` block with:

```yaml
show:
  shape: panel
  moderator: host_a
  panelists: [host_b, host_c]
  turn_order: [host_a, host_b, host_c]
  shared_history: "They built the same system in different teams."
  running_joke: "The dashboard nobody trusts."
```

The moderator's `handoff_protocol` names the next speaker. The panelists' `bridge_in` phrases accept the floor. No two panelists share a bridge.

## Limits

- Raise `MAX_TURNS` to 200 to 400.
- Raise `MAX_INPUT_CHARS` to 60000 or more.
- Raise `MAX_TOTAL_PAUSE_MS` if the panel uses a lot of explicit pauses.
- `MAX_ALIASES` at 64 is enough.
- One request, one master. Do not split the panel into separate renders.

## Panel checklist

- Every host has a profile that passes the gate.
- Every host has a distinct voice, signature, and bridge phrase.
- The moderator opens and closes.
- The panel plan covers every host and every segment.
- Every voice change has a pause, a question, or an interjection.
- Every panelist turn is one to three sentences.
- Backchannels are one per turn and within the per-host budget.
- Every logical section boundary has a section-break pause.
- No two panelists share a signature, opener, or bridge phrase.
- The turn count, input chars, and pause total fit the limits.
