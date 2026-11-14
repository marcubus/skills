# Blank persona template

Guidance artifact. Lives in `examples/` beside the three worked examples, never in the store: it carries no index line and the distinctness gate never reads it.

Blank values are the ones to resolve: take the default from `persona-schema.md` and log it in `assumptions_applied`, or write the brief's value.

To build a real persona, copy it to `personas/<id>.md`, replace every value, delete the comments. Keep the field order: identity, sound, body, word choice, emotion, show, close. Then run the distinctness gate, run the checklist, and append one line to `personas/index.jsonl`.

```yaml
id:                          # display name lowercased, underscores, equals filename stem
version: 1
display_name:                # invented, 2 to 4 words
nationality: british         # british | australian | new_zealand | scottish | irish | spanish_accented_english | us
sex: male                    # male | female
describing_words: []         # 1 to 3, closed vocabulary, no contradiction pair
field_of_expertise:          # 2 to 6 words

vocal_fingerprint:
  vowel_colour:              # broad | neutral | fronted | rounded | nasal_front
  consonant_crispness:       # crisp | soft | clipped | slurred
  pitch_register:            # low_chest | low_mixed | mid_mixed | high_mixed | high_head
  pace_band:                 # slow | measured | brisk | fast
  pace_wpm_estimate:         # integer inside the band window
  stress_pattern:            # even | terminal_rise | punch_first | trailing_off | spike_then_flat
  sentence_length_mix:       # short_led | balanced | long_led
  timbre:                    # breathy | nasal | gravelly | bright | warm | flat
  laugh_shape:               # single_beat | staccato_run | descending_wheeze | silent_shake | bark | cackle | none
  laugh_placement:           # clause_end | self_deprecation | guest_error | punchline | never
  signature_interjection:
    tick_id:                 # must be in tick_inventory
    phoneme_class:           # open_back | open_front | long_front | rounded_back | nasal | fricative | plosive | affricate

tick_inventory: []           # 6 to 8 ids, max 2 per type
tick_density:
  baseline_per_100w: 2.5
  strained_per_100w: 4.0
  cap_per_100w: 5.5

breath_profile:              # rules B1 to B6 in studio-craft.md
  inhale:                    # inaudible | soft | audible
  placement:                 # clause_boundary | mid_clause | before_stressed_word | end_of_turn
  sigh_habit:                # none | rare | once_per_segment | frequent
  laugh_breath:              # through_nose | voiceless | voiced_start
  fry:                       # none | sentence_end | under_strain

recording_context:           # rules R1 to R6
  room:                      # dry_studio | treated_room | kitchen | live_room | outdoor | phone
  mic_distance:              # close | mid | distant
  plosives:                  # controlled | audible | avoided
  breath_audibility:         # none | low | audible
  room_tone:                 # none | faint | present

non_speech_sound:            # rules N1 to N5
  allowed: []                # page_turn | mug | chair | keyboard | phone_buzz | door | paper_cup | none
  forbidden: []

lexical_register:            # rules L1 to L6 in voice-craft.md
  contractions:              # always | sometimes | never
  openers: []                # 3 to 5 literals, 1 to 4 words each
  hedges:                    # none | soft | heavy
  assertion:                 # states | qualifies | asks
  jargon_policy:             # explain | assume | avoid
  address_cohost: ""         # literal, or none
  address_listener: ""       # you | you lot | everyone | listeners | none
  banned_words: []           # 0 to 10

exemplar_lines:              # baseline only, rules E1 to E7
  claim: ""                  # 8 to 30 words
  question: ""
  disagreement: ""
  laugh: ""                  # the laugh as a written sound
  never_says: []             # exactly 3, 4 to 20 words each

calibration_line: >-         # 18 to 26 words, frozen, rules K1 to K6
  

pronunciation_lexicon: []    # 0 to 12 pairs, rules P1 to P5
  # - {written: "", spoken: ""}

eiq:                         # float 0.0 to 1.0
eiq_justification: ""        # one sentence, 40 words maximum

emotion_behaviour:
  angry:
    on_cue: ""
    ticks_under_load: []
    eiq_modifier: ""
    cohost_divergence: ""
    ceiling: ""
  frustrated:
    on_cue: ""
    ticks_under_load: []
    eiq_modifier: ""
    cohost_divergence: ""
    ceiling: ""
  tired:
    on_cue: ""
    ticks_under_load: []
    eiq_modifier: ""
    cohost_divergence: ""
    ceiling: ""
  intense:
    on_cue: ""
    ticks_under_load: []
    eiq_modifier: ""
    cohost_divergence: ""
    ceiling: ""
  curious:
    on_cue: ""
    ticks_under_load: []
    eiq_modifier: ""
    cohost_divergence: ""
    ceiling: ""
  happy:
    on_cue: ""
    ticks_under_load: []
    eiq_modifier: ""
    cohost_divergence: ""
    ceiling: ""

recovery_behaviour:          # rules Q1 to Q5 in emotion-engine.md
  shape:                     # apology | joke | subject_change | silence | walk_out
  latency:                   # immediate | next_turn | next_segment
  first_line: ""             # baseline register, no state word
  tell: ""                   # one physical detail
  does_not: ""               # one thing it never does while recovering

standing_dynamic:            # rules S1 to S8; single_host sets relation, running_joke and history to not_applicable, defers_on to []
  show_shape:                # single_host | two_host
  relation: ""               # 6 to 25 words, names a basis
  opens_show:                # self | cohost | either
  closes_show:               # self | cohost | either
  owns_subjects: []          # 1 to 3
  defers_on: []              # 1 to 3, no overlap with owns_subjects
  running_joke: ""           # one line, or none
  history: ""                # 6 to 25 words, first person plural

handoff_protocol:            # rules H1 to H6; single_host sets both bridge lists to [not_applicable] and overlap to 0
  takes_floor:               # waits | interrupts | overlaps
  bridge_out: []             # 2 to 4 phrases, 1 to 5 words
  bridge_in: []
  max_overlap_words:         # 0 to 6, agrees with takes_floor
  yields_when: ""            # 4 to 20 words, observable signal

mode_behaviour:              # rules M1 to M7, four required; outro carries exactly one sign-off tick and says where it lands
  enabled: [cold_open, intro, link, outro]
  cold_open: {pace_delta: 0, register_delta: 0, ticks: minimal, note: ""}
  intro: {pace_delta: 1, register_delta: 0, ticks: baseline, note: ""}
  link: {pace_delta: 1, register_delta: 0, ticks: minimal, note: ""}
  outro: {pace_delta: -1, register_delta: -1, ticks: dense, note: ""}

cue_scopes:
  episode_default: true
  segment_override: true
  line_override: true
  precedence: line > segment > episode

voice_note: >-
  # 60 to 110 words, to a script writer. Name pace, register, one tick by its literal, and the laugh.

provenance:
  brief: ""
  assumptions_applied: []
  created:
  distinct_from: []
  accepted_matches: []

canon_status:
  status: draft              # draft | approved | retired
  supersedes: null           # persona id, or null
```
