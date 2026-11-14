# Two hosts

Two hosts are a relationship, not two monologues cut together. Each host has a profile from `PROFILE.md`. The script must sound like two people who have done this before.

For three or more hosts, use `PANEL.md`.

## Contents

- The relationship
- Distinct writing
- Speaker changes
- Handoff protocol
- Modes
- Engagement
- Curious follow-up
- Backchannels
- Section breaks
- Two-host checklist

## The relationship

The profile's `show` block defines the pairing.

```yaml
show:
  shape: two_host
  relation: "Former colleagues who disagreed about a bridge and never resolved it."
  opens_show: self
  closes_show: cohost
  owns_subjects: [infrastructure]
  defers_on: [policy]
  running_joke: "The staircase that was signed off without a drawing."
  history: "Eleven years of the same segment order, and one failed pitch to a broadcaster."
```

Rules:

- `relation` names the basis of the pairing, not the feeling. "Friends" is a feeling. "Former colleagues who disagreed about a bridge" is a basis.
- `history` is one thing both hosts know that the listener does not.
- `owns_subjects` and `defers_on` do not overlap.
- One host opens. One host closes.
- The running joke appears once per episode, with no setup.

## Distinct writing

Two hosts with different voices and the same register still sound like one narrator in different costumes.

- Each host has a distinct `lexical_register`.
- No shared openers. One host who opens with "Look," and another who opens with "Look," are the same person on the page.
- No shared bridge phrases.
- No shared signature tick.
- No more than three shared ticks.
- Each host has four exemplar lines and three never-says lines.
- Each host has a calibration line. Check the draft against it.

## Speaker changes

Every `[voice:]` change needs a conversational move:

1. Pause. The previous speaker finishes a thought, then `[pause:300ms]` or longer, then the next speaker starts.
2. Question. The previous speaker ends on a question. The next speaker answers it.
3. Interjection. The next speaker takes the floor with a short permitted tick or bridge phrase.

A bare voice tag with none of these reads as a cut.

Pause handoff:

```text
[voice:host_a] The model assumed nobody would ever walk on it.

[pause:500ms]

[voice:host_b] That is the part that gets me.
```

Question handoff:

```text
[voice:host_a] Who signed the drawing?

[voice:host_b] The same engineer who refused to sign the second one.
```

Interjection handoff:

```text
[voice:host_a] The bridge passed every load test.

[voice:host_b] [rate:1.1] Wait. Every test?

[pause:250ms]

[voice:host_a] [rate:1.0] Every test they ran.
```

Rules:

- Pause handoff: explicit `[pause:...]` of at least 300ms. 400 to 600ms is normal. 800 to 1200ms is a section break.
- Question handoff: the question ends with a question mark, and the next speaker answers it.
- Interjection handoff: one to four words. Use the host's `bridge_in` phrase or a permitted interjection from `TICKS.md`.
- Interjection rate: `[rate:1.05]` to `[rate:1.1]`. Never above 1.2 for a handoff.
- The interjection is its own short turn. A short pause follows: 200 to 300ms.
- The next turn resets to `[rate:1.0]`, or to the rate the host used before the interjection.
- Do not stack a fast rate on a fast rate. If the interjection uses `[rate:1.1]`, keep the emotion at the default.
- `takes_floor: waits`, `max_overlap_words: 0`. Overlap is not renderable.
- No two hosts share a bridge phrase.

## Handoff protocol

The profile's `handoff_protocol` holds literal bridges.

```yaml
handoff_protocol:
  takes_floor: waits
  bridge_out: ["over to you", "what have you got"]
  bridge_in: ["right", "so"]
  max_overlap_words: 0
  yields_when: "the co-host finishes the clause"
```

Use the bridges. Do not invent a new one each turn. The bridge out is the previous speaker's exit. The bridge in is the next speaker's entry.

## Modes

Each host has the five required modes: cold open, intro, link, correction, outro. A mode is a deviation from baseline, held for the segment and then released.

- Cold open starts on the content, not a greeting.
- Intro names the show and hands over inside eight seconds.
- Link is one sentence out, one sentence in. It never summarises what was just heard.
- Correction states the error, states the correct figure, gives one clause of cause, and moves on. No ticks.
- Outro lands on the last word, then silence. One sign-off.

Do not deliver cold open, link, and outro the same way. Mode collapse is a synthetic-podcast tell.

## Engagement

The second host adds, challenges, grounds, or humanises. It does not repeat the first host in different words.

- The second host asks the question the listener is thinking.
- Disagreement is specific and about the work, not the person.
- The second host grounds an abstraction in an example.
- The second host gives the consequence the first host skipped.
- The second host does not say "great point" or "absolutely".
- Under strain, turns shorten.
- One strained state at a time. Do not let both hosts escalate.
- Recover within one or two turns.

## Curious follow-up

The second host repeats one word from the answer and asks a short follow-up.

```text
[voice:host_a] The model assumed nobody would walk on it.

[voice:host_b] Nobody? Not even a maintenance crew?
```

One or two per segment. The follow-up is a question, so the handoff is already natural. It keeps the second host from repeating the first host's point.

## Backchannels

Backchannels are short acknowledgements: "uh-huh", "mm-hm", "exactly", "fair enough", "got it". Use them from `TICKS.md`.

- One host per turn. Do not stack backchannels.
- Max two per host per episode.
- They are not content. A host who backchannels every turn sounds like a laugh track.

## Section breaks

A two-host script with logical sections gets the same section-break pause as a solo script: 800 to 1200ms, explicit, after the last turn of the section and before the first turn of the next. The rule and snippet are in `PERFORMANCE.md`.

## Two-host checklist

- Each host has a profile that passes the gate.
- Each host has a distinct voice, register, signature, and bridge phrase.
- One host opens. One host closes.
- Every voice change has a pause, a question, or an interjection.
- Every interjection is one to four words, faster, and followed by a reset.
- Backchannels are within budget.
- Every logical section boundary has a section-break pause.
- No two hosts share a signature, opener, or bridge phrase.
- The second host adds, challenges, grounds, or humanises.
