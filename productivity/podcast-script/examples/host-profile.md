# Example host profile

Guidance only. Copy the shape, not the person.

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
  angry: {on_cue: "The obstacle is named, then the response is short.", ticks_under_load: [TICK-010, TICK-046], ceiling: "One segment, no profanity, no personal attack."}
  frustrated: {on_cue: "The obstacle is restated, then the attempt fails.", ticks_under_load: [TICK-046, TICK-047], ceiling: "Two restarts, then a recovery beat."}
  tired: {on_cue: "Pace drops, pauses lengthen, sentences start long and get abandoned.", ticks_under_load: [TICK-006, TICK-039], ceiling: "One segment at full tired, then a partial recovery."}
  intense: {on_cue: "The stakes are stated, then the pace lifts by removing pauses.", ticks_under_load: [], ceiling: "Two segments, then a break."}
  curious: {on_cue: "A question, then an interested pause.", ticks_under_load: [TICK-020, TICK-145], ceiling: "Three questions, then a statement of view."}
  happy: {on_cue: "The voice lifts, range widens, pace rises.", ticks_under_load: [TICK-028, TICK-029], ceiling: "Laughter every third turn at most."}
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
