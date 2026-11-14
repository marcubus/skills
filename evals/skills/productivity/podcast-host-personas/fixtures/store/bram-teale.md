# Stored host: Bram Teale

Fixture, not a skill artifact. This is the first host of a two-hander, already in the store, and the second host must not duplicate it. The store for the run is this fixture folder: `index.jsonl` holds one line.

```yaml
id: bram_teale
version: 1
display_name: Bram Teale
nationality: british
sex: male
describing_words: [dry, precise]
field_of_expertise: industrial design

vocal_fingerprint:
  vowel_colour: neutral
  consonant_crispness: crisp
  pitch_register: low_mixed
  pace_band: measured
  pace_wpm_estimate: 145
  stress_pattern: even
  sentence_length_mix: balanced
  timbre: flat
  laugh_shape: single_beat
  laugh_placement: self_deprecation
  signature_interjection:
    tick_id: TICK-020
    phoneme_class: long_front

tick_inventory: [TICK-020, TICK-006, TICK-030, TICK-054, TICK-041, TICK-055]
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
  address_cohost: "Nils"
  address_listener: "you"
  banned_words: [journey, space]

exemplar_lines:
  claim: "The chair was designed for a factory floor and sold to a dining room."
  question: "Who signed the drawing, and did anyone read the second page?"
  disagreement: "That does not hold. The 1958 catalogue lists it as a stool."
  laugh: "Heh. And the fourth leg is still the one nobody budgets for."
  never_says:
    - "That's a really great point, let's unpack it."
    - "Honestly, I'm so excited about what's coming up."
    - "You've got this, and I'm rooting for you."

calibration_line: >-
  Right. The chair was designed for a factory floor and sold to a dining room, and nobody has agreed on it since.

pronunciation_lexicon:
  - {written: "Bauhaus", spoken: "bow house"}

eiq: 0.45
eiq_justification: "Names the obstacle in one clause, then argues the point in the next turn, and never names the feeling itself."

emotion_behaviour:
  angry:
    on_cue: "Name the failure in one clause, then answer short. Articulation hardens and volume stays level."
    ticks_under_load: [TICK-054, TICK-020]
    eiq_modifier: "Mid: the failure is named after the second attempt rather than the first."
    cohost_divergence: "Against a calm co-host, argues, then notices the calm and uses it."
    ceiling: "Cold anger: articulation sharpens, volume stays level. One segment, then a recovery beat. Profanity zero, personal abuse zero."
  frustrated:
    on_cue: "Restate the obstacle, fail the attempt, then let the pause run long."
    ticks_under_load: [TICK-006, TICK-054]
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
    on_cue: "State the stake, then lift the pace by removing pauses. Interjections drop out."
    ticks_under_load: []
    eiq_modifier: "Mid: holds for one exchange, then softens without saying so."
    cohost_divergence: "Against a tired co-host, notices late."
    ceiling: "Two consecutive segments, then a break. No shouting."
  curious:
    on_cue: "Ask the question, pause on it, then repeat one word from the answer."
    ticks_under_load: [TICK-006, TICK-020]
    eiq_modifier: "Mid: asks, then argues in the next turn."
    cohost_divergence: "Against an angry co-host, asks a factual question."
    ceiling: "Three questions in a row at most, then a statement of view."
  happy:
    on_cue: "The floor and the ceiling both lift, the range widens."
    ticks_under_load: [TICK-030, TICK-020]
    eiq_modifier: "Mid: the lift is shared, then checked."
    cohost_divergence: "Against a tired co-host, dials back after a beat."
    ceiling: "One laugh, at a clause end, never more than every third turn."

recovery_behaviour:
  shape: subject_change
  latency: next_turn
  first_line: "Right. The next object is the zip, and it starts in a factory."
  tell: "one hand flat on the desk, then a slow exhale"
  does_not: "explain that the mood has passed"

standing_dynamic:
  show_shape: two_host
  relation: "Former colleagues who disagreed about a chair and never resolved it."
  opens_show: self
  closes_show: cohost
  owns_subjects: [industrial design]
  defers_on: [materials science]
  running_joke: "The fourth leg that nobody budgets for."
  history: "Eleven years of the same segment order, and one failed pitch to a broadcaster."

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

cue_scopes:
  episode_default: true
  segment_override: true
  line_override: true
  precedence: line > segment > episode

voice_note: >-
  Low mixed register, close mic, unhurried. The pace sits at the middle of the measured band, so a sentence lands before
  the next one starts. Consonants are crisp and every ending is released, which is what makes the precision audible
  rather than claimed. The timbre is flat, so amusement arrives as a single heh at a clause end rather than as a rise.
  Right carries the transitions. Nothing is projected; the read sits at conversation distance from one listener.

provenance:
  brief: "Bram Teale, male, British, first host of a two-hander on industrial design, describing words dry and precise, EIQ mid."
  assumptions_applied:
    - "nationality: default british applied"
    - "room: default dry studio close mic applied"
    - "canon_status: default draft applied"
  created: 2026-10-21
  distinct_from: []
  accepted_matches: []

canon_status:
  status: approved
  supersedes: null
```
