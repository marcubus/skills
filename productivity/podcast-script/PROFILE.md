# Host profile

A host profile is a typed description of a fictional host. It is written for the script writer, who needs to know how the host talks. Every field is a value, an enum, a number, or a literal string. Adjectives alone fail the gate. The profile describes the person, not the deployment: the model, the voices, and the handoff live in the script and `HANDOFF.md`.

Save one profile per host next to the script:

```text
<source-stem>-host-a-profile.md
<source-stem>-host-b-profile.md
```

A reader with no context can rebuild the host from the file. If a field needs the conversation to explain it, the profile is incomplete.

## Contents

- Template
- Describing words
- Field rules
- Solo fields
- Panel fields
- Profile gate

## Template

```yaml
id: des_larkin
display_name: Des Larkin
nationality: australian
sex: male
describing_words: [dry, precise, warm]
field_of_expertise: infrastructure

speech_habits:
  pace_band: steady
  pace_wpm_estimate: 145
  laugh_shape: heh
  laugh_placement: sentence_end

lexical_register:
  contractions: always
  openers: ["Look,", "The thing is,", "Right."]
  hedges: none
  assertion: states
  jargon_policy: explain
  address_cohost: "Harriet"
  address_listener: "you"
  banned_words: [utilise, journey, space]

exemplar_lines:
  claim: "The bridge was signed off on a model that assumed nobody would ever walk on it."
  question: "Who signed the drawing, and did they read the second page?"
  disagreement: "I don't think that holds. The load case changes once the market moves in."
  laugh: "Heh. Right. And the staircase is still there."
  never_says:
    - "That's a really great point."
    - "Let's unpack that."
    - "Absolutely, one hundred percent."

calibration_line: "Blimey, the second staircase is the one that tells you whether anybody read the drawings, and I have said so for eleven years."

tick_inventory: [TICK-006, TICK-020, TICK-030, TICK-060, TICK-070, TICK-090]
signature_tick: TICK-020
tick_density: {baseline: 2.5, strained: 4.0, ceiling: 5.5}

show:
  shape: two_host
  relation: "Former colleagues who disagreed about a bridge and never resolved it."
  opens_show: self
  closes_show: cohost
  owns_subjects: [infrastructure]
  defers_on: [policy]
  running_joke: "The staircase that was signed off without a drawing."
  history: "Eleven years of the same segment order, and one failed pitch to a broadcaster."

handoff_protocol:
  takes_floor: waits
  bridge_out: ["over to you", "what have you got"]
  bridge_in: ["right", "so"]
  max_overlap_words: 0
  yields_when: "the co-host finishes the clause"

mode_behaviour:
  cold_open: {pace_delta: 0, register_delta: 0, ticks: minimal, note: "Starts on the content, not a greeting."}
  intro: {pace_delta: 1, register_delta: 0, ticks: baseline, note: "Names the show and hands over inside eight seconds."}
  link: {pace_delta: 1, register_delta: 0, ticks: minimal, note: "One sentence out, one sentence in, no recap."}
  correction: {pace_delta: -1, register_delta: 0, ticks: none, note: "States the error and the correct figure, then moves on."}
  outro: {pace_delta: -1, register_delta: -1, ticks: dense, note: "Sign-off lands on the last word, then silence."}

emotion_behaviour:
  neutral: {on_cue: "The default. No performance beyond the words.", ticks_under_load: [], ceiling: "Most of the episode."}
  warm: {on_cue: "A concession or a welcome, then a slower clause.", ticks_under_load: [TICK-028], ceiling: "Two segments."}
  bright: {on_cue: "The voice lifts and the pace rises on a good turn.", ticks_under_load: [TICK-028, TICK-029], ceiling: "Laughter every third turn at most."}
  sad: {on_cue: "Pace drops, sentences shorten, a pause before the admission.", ticks_under_load: [TICK-006], ceiling: "One segment."}
  tired: {on_cue: "Pace drops, pauses lengthen, sentences start long and get abandoned.", ticks_under_load: [TICK-006, TICK-070], ceiling: "One segment at full tired, then a partial recovery."}
  angry: {on_cue: "The obstacle is named, then the response is short.", ticks_under_load: [TICK-082, TICK-083], ceiling: "One segment, no profanity, no personal attack."}
  whisper: {on_cue: "A conspiratorial aside, close and quiet.", ticks_under_load: [], ceiling: "One aside."}
  excited: {on_cue: "The stakes are stated, then the pace lifts by removing pauses.", ticks_under_load: [], ceiling: "Two segments, then a break."}
recovery_behaviour:
  shape: apology
  latency: next_turn
  first_line: "Right. The second staircase, then."
  tell: "A breath before the first word."
  does_not: "Explains that it has calmed down."
```

## Describing words

Use one to three words from this closed vocabulary. No contradiction pair.

```text
warm, dry, precise, curious, sceptical, patient, blunt, gentle, wry,
earnest, playful, measured, urgent, calm, intense, generous, guarded,
restless, meticulous, plainspoken, bookish, worldly, mischievous, steady
```

Contradiction pairs include warm and guarded, playful and measured, patient and urgent, gentle and blunt, and curious and steady.

## Field rules

- `id` is the display name lowercased with underscores. It is independent of the filename stem.
- `nationality` is `australian`, `british`, `american`, `irish`, `scottish`, `new_zealand`, or `canadian`.
- `sex` is `male`, `female`, or `unspecified`. It describes the host.
- `speech_habits` describes how the host talks: pace, laugh shape, and laugh placement.
- `field_of_expertise` is one to four words.
- `laugh_shape` is `ha`, `heh`, `hm-hm`, or `none`.
- `laugh_placement` is `sentence_end`, `turn_end`, or `none`.
- `pace_band` is `slow`, `steady`, or `brisk`.
- `pace_wpm_estimate` is a number from 110 to 190.
- `lexical_register.contractions` is `always`, `sometimes`, or `never`.
- `hedges` is `none`, `soft`, or `heavy`.
- `assertion` is `states`, `qualifies`, or `asks`.
- `jargon_policy` is `explain`, `assume`, or `avoid`.
- `openers` holds three to five literal strings of one to four words.
- `address_cohost` and `address_listener` are literal strings.
- `banned_words` holds zero to ten words.
- `exemplar_lines` holds four lines of 8 to 30 words and exactly three `never_says` lines.
- `calibration_line` is 19 to 23 words and takes 6 to 13 seconds at `pace_wpm_estimate`.
- `tick_inventory` holds six to eight `TICK-###` IDs from `TICKS.md`.
- `signature_tick` is one ID from `tick_inventory`.
- `tick_density` uses the density table in `TICKS.md`.
- `show.shape` is `single_host`, `two_host`, or `panel`.
- `handoff_protocol.takes_floor` is `waits`. One host speaks at a time.
- `mode_behaviour` carries the five required modes: `cold_open`, `intro`, `link`, `correction`, `outro`. Each mode has `pace_delta`, `register_delta`, `ticks`, and a one-line `note`. `pace_delta` is -1, 0, or +1, applied as a 0.05 rate step. `register_delta` is -1, 0, or +1, applied as one step more or less formal. `ticks` is `none`, `minimal`, `baseline`, or `dense`.
- `emotion_behaviour` carries all eight emotions: `neutral`, `warm`, `bright`, `sad`, `tired`, `angry`, `whisper`, `excited`. They are the values the script may put in `[emotion:]`. `ticks_under_load` draws on the full library and does not count toward `tick_inventory`.
- `recovery_behaviour` carries `shape` (`apology`, `correction`, or `self_deprecation`), `latency` (`next_turn` or `next_segment`), `first_line`, `tell`, and `does_not`. Use it after a strained segment: the host recovers in the stated shape and latency.

## Solo fields

For one host, replace `show` with:

```yaml
show:
  shape: single_host
  opens_show: self
  closes_show: self
  owns_subjects: [infrastructure]
  running_joke: "The staircase that was signed off without a drawing."
```

Omit `relation`, `history`, `address_cohost`, `defers_on`, and `handoff_protocol`. A solo host has no co-host to hand off to.

## Panel fields

For three or more hosts, replace `show` with:

```yaml
show:
  shape: panel
  moderator: host_a
  panelists: [host_b, host_c]
  turn_order: [host_a, host_b, host_c]
  owns_subjects: [infrastructure]
  defers_on: [policy]
  shared_history: "They built the same system in different teams."
  running_joke: "The dashboard nobody trusts."

tick_density: {baseline: 2.0, strained: 3.5, ceiling: 5.0}
```

The moderator opens, directs, and closes. Every panelist has a distinct signature tick and bridge phrase. `moderator`, `panelists`, and `turn_order` hold the `[voice:]` labels, such as `host_a`, not the profile `id`.

## Profile gate

The profile is not ready until every check passes.

| Check | Pass condition |
|---|---|
| Fields | Every field has a value or a named default. |
| Scope | Every field describes the host. Voice, model, and the deliverable handoff belong to the script. |
| Describing words | One to three from the vocabulary, no contradiction pair. |
| Pace | `pace_wpm_estimate` is numeric and agrees with the calibration line. |
| Register | Every register subfield for the shape present: seven for solo, eight for two-host and panel. Openers literal, no shared openers with another host. |
| Exemplars | Four lines of 8 to 30 words, three never-says lines. |
| Calibration | 19 to 23 words, 6 to 13 seconds at the declared pace. |
| Ticks | Six to eight IDs, max two per type, one `signature_tick` from the inventory. |
| Handoff | Two-host and panel: literal bridges, observable `yields_when`, `takes_floor: waits`. |
| Dynamic | `two_host`: relation and history present, one host opens, one closes. `single_host`: opens and closes are self. `panel`: moderator, panelists, turn_order, and shared_history present; the moderator opens and closes. |
| Modes | Five required modes with pace, register, ticks, note. |
| Emotion | All eight emotions with three subfields each, ceilings in words. |
| Recovery | Shape, latency, first line, tell, does not. |
| Distinctness | No shared signature tick, opener, or bridge phrase. |
| No adjectives | No field is an adjective-only description. |

A profile that fails the gate is not used. Fix the profile before writing the script.
