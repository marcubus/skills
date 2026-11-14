# Show craft: modes, handoff, relationship

Three fields describe what a host is doing, as distinct from how the host sounds and what the host is feeling: `mode_behaviour`, `handoff_protocol`, `standing_dynamic`.

The six states answer "how does this host feel". They do not answer "what is this host doing". A tired host reading a correction and a tired host opening the show are different performances, and without modes the schema cannot tell them apart, so a script delivers every segment at baseline. Flat delivery across functions is the most common synthetic-podcast tell after audible markup.

## mode_behaviour

Seven modes. Four are required in `enabled`: `cold_open`, `intro`, `link`, `outro`. Three are optional: `listener_letter`, `correction`, `sponsor_read`.

A mode is a deviation from the persona's baseline, held for the length of that segment and then released. It never changes the fingerprint.

```yaml
mode_behaviour:
  enabled: [cold_open, intro, link, correction, outro]
  cold_open:        {pace_delta: 0,  register_delta: 0,  ticks: minimal,  note: "Starts on the content, not a greeting. First sentence is a claim or a number, never hello."}
  intro:            {pace_delta: 1,  register_delta: 0,  ticks: baseline, note: "Names the show and the guest, then hands to the co-host inside eight seconds."}
  link:             {pace_delta: 1,  register_delta: 0,  ticks: minimal,  note: "One sentence out, one sentence in. Never summarises what was just heard."}
  correction:       {pace_delta: -1, register_delta: 0,  ticks: none,     note: "States the error, states the correct figure, gives one clause of cause, moves on."}
  outro:            {pace_delta: -1, register_delta: -1, ticks: dense,     note: "Sign-off lands on the last word of the segment, then silence, no music talk."}
```

| Mode | pace_delta | register_delta | ticks | Note must say |
|---|---|---|---|---|
| cold_open | 0 | 0 | minimal | how the host starts without a greeting |
| intro | +1 | 0 | baseline | what is named, and where the turn hands over |
| link | +1 | 0 | minimal | what a link never does (usually summary or recap) |
| listener_letter | -1 | 0 | baseline | whether the host reads the letter in the writer's voice or their own |
| correction | -1 | 0 | none | how the earlier claim is handled without re-arguing it |
| sponsor_read | 0 | 0 | none | the one thing that would break the read |
| outro | -1 | -1 | dense | where the sign-off lands and what follows it |

M1. `pace_delta` is an integer from -2 to +2. `register_delta` is an integer from -1 to +1. Both are steps on the ladder in `references/persona-schema.md`, and both return to baseline when the mode ends. Every entry present in the object is checked, enabled or not: an unenabled mode may be omitted, but if it is written it carries all four values and obeys M3.
M2. `note` is 6 to 30 words, written as behaviour. A note that is only an adjective ("warm and conversational") fails.
M3. `correction` and `sponsor_read` take `ticks: none`. Laughter in either is a failure, and a laugh in a correction reads as contempt for the listener.
M4. `outro` carries `ticks: dense` and uses exactly one sign-off id from `tick_inventory`; the note says where that sign-off lands. A sign-off in the middle of a sentence sounds like an accident.
M5. A mode not in `enabled` is not performed. If a brief asks for a listener letter, the mode is enabled or the brief is refused, never left half-written.
M6. Precedence: a cued state beats a mode for pace and register, except in `correction` and `sponsor_read`, which cap the persona one step below its strained ceiling for that state. Nobody shouts a correction.
M7. `cold_open` may not begin with a greeting, the show name, or a question to the listener. Those are `intro`.

## handoff_protocol

How the persona takes the floor, gives it back, and whether it can talk over anyone. The six states cover divergence, not traffic.

```yaml
handoff_protocol:
  takes_floor: waits
  bridge_out: ["over to you", "what have you got"]
  bridge_in: ["right", "so"]
  max_overlap_words: 0
  yields_when: "the co-host draws breath"
```

H1. `takes_floor`: `waits`, `interrupts` or `overlaps`. `waits` requires `max_overlap_words: 0`. `interrupts` allows 0 to 3. `overlaps` requires 2 to 6.
H2. `bridge_out` and `bridge_in` hold 2 to 4 phrases of 1 to 5 words each, as literal strings.
H3. No bridge phrase repeats across two personas on the same show. Shared bridges erase the handoff, which is the one thing they exist to mark.
H4. `yields_when` is 4 to 20 words naming an observable signal, not a feeling ("when the co-host draws breath", not "when the co-host wants a turn").
H5. The protocol must survive strain. A `waits` persona that talks over a co-host when angry contradicts itself, so either `cohost_divergence` states the exception in words or `takes_floor` was set wrong.
H6. A single-host show sets `takes_floor: waits`, both bridge lists to `["not_applicable"]`, `max_overlap_words: 0`, and `yields_when: "not_applicable"`.

## standing_dynamic

The relationship, not the state. This is what makes a two-hander sound like two people who have done this before rather than two monologues cut together.

```yaml
standing_dynamic:
  show_shape: two_host
  relation: "Former colleagues who disagreed about a bridge and never resolved it."
  opens_show: self
  closes_show: cohost
  owns_subjects: [sports analytics]
  defers_on: [nutrition]
  running_joke: "The staircase that was signed off without a drawing."
  history: "Eleven years of the same segment order, and one failed pitch to a broadcaster."
```

S1. `show_shape`: `single_host` or `two_host`. This field also governs which other fields are applicable, so it is read before them.
S2. `single_host` sets `relation`, `running_joke` and `history` to `not_applicable`, `defers_on` to `[]`, and both `opens_show` and `closes_show` to `self`.
S3. `two_host` requires `relation` and `history` at 6 to 25 words each, and at least one subject in each of `owns_subjects` and `defers_on`.
S4. `owns_subjects` and `defers_on` hold 1 to 3 items each, with no overlap. A persona that both owns and defers on a subject has no position in the show.
S5. `running_joke` is one line the persona can reference with no setup, or `none`. It names no real event and carries no date.
S6. `relation` names the basis of the pairing, not the feeling. "Friends" is a feeling. "Former colleagues who disagreed about a bridge" is a basis, and it tells a writer who interrupts whom.
S7. `history` is written in the first person plural and is invented. It states the one thing both hosts know that the listener does not.
S8. When the co-host is already stored, exactly one of the pair opens the show and one closes it. Both claiming `self` is a fail, and so is neither.

## What these three fields are not

They are not emotion. Modes hold while a state moves underneath, and a profile that writes its emotion into a mode note has two places for the same behaviour.
They are not casting. Room, mic and voice are elsewhere.
And they are not per-episode. Modes and the relationship are stable across a series, which is why they are saved rather than briefed.
