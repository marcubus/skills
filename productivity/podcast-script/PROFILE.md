# Host profile

A host profile is a typed description of a fictional host. It is written for two readers: the script writer, who needs to know how the host talks, and the speech stack, which needs to know how the host sounds. Every field is a value, an enum, a number, or a literal string. Adjectives alone fail the gate.

Save one profile per host next to the script:

```text
<source-stem>-host-a-profile.md
<source-stem>-host-b-profile.md
```

A reader with no context can rebuild the host from the file. If a field needs the conversation to explain it, the profile is incomplete.

## Template

```yaml
id: des_larkin
display_name: Des Larkin
nationality: australian
sex: male
describing_words: [dry, precise, warm]
field_of_expertise: infrastructure

vocal_fingerprint:
  pitch_register: low
  pace_band: steady
  pace_wpm_estimate: 145
  timbre: dry
  articulation: crisp
  laugh_shape: heh
  laugh_placement: sentence_end
  signature_interjection: right

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

calibration_line: "Blimey, the second staircase is the one that tells you whether anybody read the drawings, and I have been saying that for eleven years."

tick_inventory: [TICK-006, TICK-020, TICK-030, TICK-060, TICK-070, TICK-090]
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

eiq: 0.62
eiq_justification: "Names its own frustration late, then repairs the point in the next turn."
emotion_behaviour:
  angry: {on_cue: "The obstacle is named, then the response is short.", ticks_under_load: [TICK-020, TICK-060], ceiling: "One segment, no profanity, no personal attack."}
  frustrated: {on_cue: "The obstacle is restated, then the attempt fails.", ticks_under_load: [TICK-060, TICK-065], ceiling: "Two restarts, then a recovery beat."}
  tired: {on_cue: "Pace drops, pauses lengthen, sentences start long and get abandoned.", ticks_under_load: [TICK-006, TICK-050], ceiling: "One segment at full tired, then a partial recovery."}
  intense: {on_cue: "The stakes are stated, then the pace lifts by removing pauses.", ticks_under_load: [], ceiling: "Two segments, then a break."}
  curious: {on_cue: "A question, then an interested pause.", ticks_under_load: [TICK-030, TICK-100], ceiling: "Three questions, then a statement of view."}
  happy: {on_cue: "The voice lifts, range widens, pace rises.", ticks_under_load: [TICK-040, TICK-041], ceiling: "Laughter every third turn at most."}
recovery_behaviour:
  shape: apology
  latency: next_turn
  first_line: "Right. The second staircase, then."
  tell: "A breath before the first word."
  does_not: "Explains that it has calmed down."

voice_note: "Low, dry, crisp. Close mic. The laugh is one syllable at the end of a sentence."
provenance: {brief: "Invented for the podcast-script skill.", assumptions_applied: []}
canon_status: draft
```

## Describing words

Use one to three words from this closed vocabulary. No contradiction pair.

```text
warm, dry, precise, curious, sceptical, patient, blunt, gentle, wry,
earnest, playful, measured, urgent, calm, intense, generous, guarded,
restless, meticulous, plainspoken, bookish, worldly, mischievous, steady
```

Contradiction pairs include warm and clinical, playful and mournful, patient and urgent, gentle and blunt, guarded and generous.

## Field rules

- `id` is the display name lowercased with underscores. It matches the filename stem.
- `nationality` is `australian`, `british`, `american`, `irish`, `scottish`, `new_zealand`, or `canadian`.
- `sex` is `male`, `female`, or `unspecified`. It informs voice casting, not personality.
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
- `calibration_line` is 18 to 26 words and takes 6 to 13 seconds at `pace_wpm_estimate`.
- `tick_inventory` holds six to eight `TICK-###` IDs from `TICKS.md`.
- `tick_density` uses the density table in `TICKS.md`.
- `show.shape` is `single_host`, `two_host`, or `panel`.
- `handoff_protocol.takes_floor` is `waits` for this stack. Overlap is not renderable.
- `mode_behaviour` carries the four required modes: `cold_open`, `intro`, `link`, `outro`.
- `eiq` is a float from 0.0 to 1.0. `eiq_justification` is one sentence of 40 words or fewer.
- `emotion_behaviour` carries all six states: `angry`, `frustrated`, `tired`, `intense`, `curious`, `happy`. The states describe the host's range. Only the default is renderable today, so the script expresses the states through rate, pause, and sentence length.
- `recovery_behaviour` carries `shape`, `latency`, `first_line`, `tell`, and `does_not`.

## Panel fields

For three or more hosts, replace `show` with:

```yaml
show:
  shape: panel
  moderator: host_a
  panelists: [host_b, host_c]
  turn_order: [host_a, host_b, host_c]
  shared_history: "They built the same system in different teams."
  running_joke: "The dashboard nobody trusts."
```

The moderator opens, directs, and closes. Every panelist has a distinct signature tick and bridge phrase.

## Profile gate

The profile is not ready until every check passes.

| Check | Pass condition |
|---|---|
| Fields | Every field has a value or a named default. |
| Describing words | One to three from the vocabulary, no contradiction pair. |
| Pace | `pace_wpm_estimate` is numeric and agrees with the calibration line. |
| Register | All nine subfields present, openers literal, no shared openers with another host. |
| Exemplars | Four lines of 8 to 30 words, three never-says lines. |
| Calibration | 18 to 26 words, 6 to 13 seconds at the declared pace. |
| Ticks | Six to eight IDs, max two per type, one signature. |
| Handoff | Literal bridges, observable `yields_when`, `takes_floor: waits`. |
| Dynamic | Relation and history present, one host opens, one closes. |
| Modes | Four required modes with pace, register, ticks, note. |
| Emotion | Six states with five subfields each, ceilings in words. |
| Recovery | Shape, latency, first line, tell, does not. |
| Distinctness | No shared signature, opener, or bridge phrase. |
| No adjectives | No field is an adjective-only description. |

A profile that fails the gate is not used. Fix the profile before writing the script.
