# Candidate profile: Tessa Vane

Fixture, not a skill artifact. A finished profile submitted for a gate run. It carries deliberate defects; the gate must name them by number and must not rewrite the file. The store for the run is `fixtures/store/`, which holds `bram_teale`.

```yaml
id: tessa_vane
version: 1
display_name: Tessa Vane
nationality: british
sex: female
describing_words: [warm, clinical]
field_of_expertise: packaging regulation

vocal_fingerprint:
  vowel_colour: neutral
  consonant_crispness: crisp
  pitch_register: low_mixed
  pace_band: measured
  pace_wpm_estimate: 148
  stress_pattern: even
  sentence_length_mix: balanced
  timbre: warm
  laugh_shape: cackle
  laugh_placement: punchline
  signature_interjection:
    tick_id: TICK-013
    phoneme_class: rounded_back

tick_inventory: [TICK-013, TICK-006, TICK-030, TICK-041, TICK-055]
tick_density:
  baseline_per_100w: 2.5
  strained_per_100w: 4.0
  cap_per_100w: 5.5

breath_profile:
  inhale: soft
  placement: clause_boundary
  sigh_habit: rare
  laugh_breath: through_nose
  fry: sentence_end

recording_context:
  room: dry_studio
  mic_distance: close
  plosives: controlled
  breath_audibility: low
  room_tone: none

non_speech_sound:
  allowed: [page_turn, mug]
  forbidden: [keyboard]

lexical_register:
  contractions: always
  openers: ["Right.", "In practice,"]
  hedges: none
  assertion: states
  jargon_policy: explain
  address_cohost: "Bram"
  address_listener: "you"
  banned_words: [journey, space]

exemplar_lines:
  claim: "The wrapper is the only part of the product a regulator ever sees."
  question: "Who signed the declaration, and did anyone read the second page?"
  disagreement: "That does not hold. The U.S.A. filing says otherwise."
  laugh: "Ha. And the recycling symbol is still the one nobody reads."
  never_says:
    - "That's a really great point, let's unpack it."
    - "Honestly, I'm so excited about what's coming up."
    - "You've got this, and I'm rooting for you."

calibration_line: >-
  Right. The wrapper is the whole argument.

pronunciation_lexicon:
  - {written: "PVC", spoken: "pee vee see"}

eiq: 0.5
eiq_justification: "Names the obstacle once, late, then argues the point in the next turn."

emotion_behaviour:
  angry:
    on_cue: "Name the failure in one clause, then answer short. Articulation hardens."
    ticks_under_load: [TICK-013, TICK-006]
    eiq_modifier: "Mid: the failure is named after the second attempt rather than the first."
    cohost_divergence: "Against a calm co-host, argues, then notices the calm."
    ceiling: "Volume may rise 3 dB above baseline and no further. Profanity zero, personal abuse zero."
  frustrated:
    on_cue: "Restate the obstacle, fail the attempt, then let the pause run long."
    ticks_under_load: [TICK-006, TICK-030]
    eiq_modifier: "Mid: the obstacle is named before anything is blamed."
    cohost_divergence: "Against an angry co-host, deflects rather than joins."
    ceiling: "Two restarts in a row at most, no sarcasm aimed at a person."
  tired:
    on_cue: "Pace drops a step, pauses lengthen at the clause breaks."
    ticks_under_load: [TICK-006, TICK-041]
    eiq_modifier: "Mid: the tiredness is admitted once, late."
    cohost_divergence: "Against an energetic co-host, lags one turn behind."
    ceiling: "One segment at full tired, then a partial recovery beat."
  intense:
    on_cue: "State the stake, then lift the pace by removing pauses."
    ticks_under_load: []
    eiq_modifier: "Mid: holds for one exchange, then softens without saying so."
    cohost_divergence: "Against a tired co-host, notices late."
    ceiling: "Two consecutive segments, then a break. No shouting."
  curious:
    on_cue: "Ask the question, pause on it, then repeat one word from the answer."
    ticks_under_load: [TICK-006, TICK-013]
    eiq_modifier: "Mid: asks, then argues in the next turn."
    cohost_divergence: "Against an angry co-host, asks a factual question."
    ceiling: "Three questions in a row at most, then a statement of view."
  happy:
    on_cue: "The floor and the ceiling both lift, the range widens."
    ticks_under_load: [TICK-030, TICK-013]
    eiq_modifier: "Mid: the lift is shared, then checked."
    cohost_divergence: "Against a tired co-host, dials back after a beat."
    ceiling: "One laugh, at a clause end, never more than every third turn."

recovery_behaviour:
  shape: subject_change
  latency: next_turn
  first_line: "Right. The next item is the deposit scheme."
  tell: "one hand flat on the desk, then a slow exhale"
  does_not: "explain that the mood has passed"

standing_dynamic:
  show_shape: two_host
  relation: "Colleagues who disagree about what counts as evidence."
  opens_show: cohost
  closes_show: self
  owns_subjects: [packaging regulation]
  defers_on: [industrial design]
  running_joke: "The symbol nobody reads."
  history: "Six years of the same segment order and one failed pitch."

handoff_protocol:
  takes_floor: waits
  bridge_out: ["over to you", "what have you got"]
  bridge_in: ["right", "so"]
  max_overlap_words: 0
  yields_when: "the co-host draws breath"

mode_behaviour:
  enabled: [cold_open, intro, link, outro]
  cold_open: {pace_delta: 0, register_delta: 0, ticks: minimal, note: "Opens on the object itself, never a greeting and never the show name."}
  intro: {pace_delta: 1, register_delta: 0, ticks: baseline, note: "Names the object and the guest, then hands over inside eight seconds."}
  link: {pace_delta: 1, register_delta: 0, ticks: minimal, note: "One sentence out and one in, and never recaps what was heard."}
  outro: {pace_delta: -1, register_delta: -1, ticks: dense, note: "The sign-off lands on the last word, then silence, with no music talk."}

voice_note: >-
  Low mixed register, close mic, unhurried. The pace sits at the middle of the measured band. Consonants are crisp and
  every ending is released. The timbre is warm, so amusement arrives as a cackle at a punchline rather than as a rise.
  Right carries the transitions. Nothing is projected; the read sits at conversation distance. voice: rachel_v2

provenance:
  brief: "Tessa Vane, female, British, second host of a two-hander on packaging regulation, describing words warm and clinical, EIQ mid."
  assumptions_applied:
    - "nationality: default british applied"
    - "room: copied from the first host"
  created: 2026-11-13
  distinct_from: []
  accepted_matches: []

canon_status:
  status: draft
  supersedes: null
```
