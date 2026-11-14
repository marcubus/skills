# Persona schema

Twenty-eight top-level fields, fixed names, fixed types, no padding. A profile is one YAML block followed by two allowed prose fields (`voice_note`, `eiq_justification`). Everything else is enumerated or a counted list.

Field order is fixed and follows the reading order an agent needs: identity, sound, body, word choice, emotion, show, close.

## Contents

- Shape
- Enumerations
- Validation rules
- Defaults
- The baseline set and EIQ
- Lifecycle
- Index line

## Shape

```yaml
id: string                     # lowercase, underscores, equals filename stem
version: 1                     # integer, bump on any change
display_name: string           # invented name, 1 to 4 words
nationality: british           # enum, 7 values, default british
sex: male                      # enum: male | female, default male
describing_words: [wry, measured, warm]   # 1 to 3, closed vocabulary
field_of_expertise: string     # 2 to 6 words, no sentence punctuation

vocal_fingerprint:
  vowel_colour: neutral        # broad | neutral | fronted | rounded | nasal_front
  consonant_crispness: crisp   # crisp | soft | clipped | slurred
  pitch_register: mid_mixed    # low_chest | low_mixed | mid_mixed | high_mixed | high_head
  pace_band: measured          # slow | measured | brisk | fast
  pace_wpm_estimate: 145       # integer, estimate, inside the band window
  stress_pattern: even         # even | terminal_rise | punch_first | trailing_off | spike_then_flat
  sentence_length_mix: balanced  # short_led | balanced | long_led
  timbre: warm                 # breathy | nasal | gravelly | bright | warm | flat
  laugh_shape: single_beat     # single_beat | staccato_run | descending_wheeze | silent_shake | bark | cackle | none
  laugh_placement: clause_end  # clause_end | self_deprecation | guest_error | punchline | never
  signature_interjection:
    tick_id: TICK-013            # must exist in tick-library.md
    phoneme_class: plosive     # open_back | open_front | long_front | rounded_back | nasal | fricative | plosive | affricate

tick_inventory: [TICK-003, TICK-013, TICK-019, TICK-029, TICK-037, TICK-047, TICK-055]
tick_density:
  baseline_per_100w: 2.5
  strained_per_100w: 4.0
  cap_per_100w: 5.5

breath_profile:                # see studio-craft.md, rules B1 to B6
  inhale: audible              # inaudible | soft | audible
  placement: clause_boundary   # clause_boundary | mid_clause | before_stressed_word | end_of_turn
  sigh_habit: once_per_segment # none | rare | once_per_segment | frequent
  laugh_breath: through_nose   # through_nose | voiceless | voiced_start
  fry: sentence_end            # none | sentence_end | under_strain

recording_context:             # see studio-craft.md, rules R1 to R6
  room: dry_studio             # dry_studio | treated_room | kitchen | live_room | outdoor | phone
  mic_distance: close          # close | mid | distant
  plosives: controlled         # controlled | audible | avoided
  breath_audibility: low       # none | low | audible
  room_tone: none              # none | faint | present

non_speech_sound:              # closed list, see studio-craft.md N1 to N5
  allowed: [page_turn, mug, chair]
  forbidden: [keyboard]

lexical_register:              # see voice-craft.md, rules L1 to L6
  contractions: always         # always | sometimes | never
  openers: ["Look,", "Right."] # 3 to 5 literals, 1 to 4 words each
  hedges: none                 # none | soft | heavy
  assertion: states            # states | qualifies | asks
  jargon_policy: explain       # explain | assume | avoid
  address_cohost: "Harriet"    # literal, or none
  address_listener: "you"      # you | you lot | everyone | listeners | none
  banned_words: [utilise]      # 0 to 10

exemplar_lines:                # baseline only, see voice-craft.md E1 to E7
  claim: string                # 8 to 30 words
  question: string
  disagreement: string
  laugh: string                # the laugh as a written sound
  never_says: [string, string, string]   # exactly 3, 4 to 20 words each

calibration_line: string       # 18 to 26 words, frozen, see K1 to K6

pronunciation_lexicon:         # 0 to 12 pairs, see P1 to P5
  - {written: "GDP", spoken: "gee dee pee"}

eiq: 0.4                       # float 0.0 to 1.0
eiq_justification: string      # one sentence, 40 words or fewer

emotion_behaviour:
  angry:      {on_cue: string, ticks_under_load: [tick_ids], eiq_modifier: string, cohost_divergence: string, ceiling: string}
  frustrated: {...}
  tired:      {...}
  intense:    {...}
  curious:    {...}
  happy:      {...}

recovery_behaviour:            # see emotion-engine.md, Q1 to Q5
  shape: apology               # apology | joke | subject_change | silence | walk_out
  latency: next_turn           # immediate | next_turn | next_segment
  first_line: string           # baseline register, no state word
  tell: string                 # one physical detail
  does_not: string             # one thing it never does while recovering

standing_dynamic:              # see show-craft.md, S1 to S8
  show_shape: two_host         # single_host | two_host
  relation: string             # 6 to 25 words, names a basis
  opens_show: self             # self | cohost | either
  closes_show: cohost          # self | cohost | either
  owns_subjects: [string]      # 1 to 3
  defers_on: [string]          # 1 to 3, no overlap
  running_joke: string         # one line, or none
  history: string              # 6 to 25 words, first person plural

handoff_protocol:              # see show-craft.md, H1 to H6
  takes_floor: waits           # waits | interrupts | overlaps
  bridge_out: [string, string] # 2 to 4 phrases, 1 to 5 words
  bridge_in: [string, string]
  max_overlap_words: 0         # 0 to 6
  yields_when: string          # 4 to 20 words, observable signal

mode_behaviour:                # see show-craft.md, M1 to M7
  enabled: [cold_open, intro, link, outro]   # 4 required, 3 optional
  cold_open: {pace_delta: 0, register_delta: 0, ticks: minimal, note: string}
  # one entry per enabled mode: listener_letter | correction | sponsor_read also legal

cue_scopes:
  episode_default: true
  segment_override: true
  line_override: true
  precedence: line > segment > episode

voice_note: string             # one paragraph, 60 to 110 words

provenance:
  brief: string
  assumptions_applied: [string]
  created: YYYY-MM-DD
  distinct_from: [persona_id]
  accepted_matches: [string]

canon_status:
  status: approved             # draft | approved | retired
  supersedes: null             # persona id, or null
```

## Enumerations

**nationality** (7): `british`, `australian`, `new_zealand`, `scottish`, `irish`, `spanish_accented_english`, `us`. These set vowel colour and stress defaults only. They are a starting constraint, not a dialect guide. An accent the enum does not carry, such as Northern Irish, Welsh or Canadian, takes the nearest listed value, records the choice in `assumptions_applied`, and carries the difference in `vowel_colour` and `stress_pattern`. The enum is not extended per persona.

**pitch_register** combines a band and a resonance site:

| Value | Band | Site | Reads as |
|---|---|---|---|
| low_chest | low | chest | authority, gravel, radio baritone |
| low_mixed | low | mixed | quiet authority, close-mic intimacy |
| mid_mixed | mid | mixed | default conversational, neutral |
| high_mixed | high | mixed | animated, younger, quick |
| high_head | high | head | bright, excitable, comedic |

`register_delta` in `mode_behaviour` and the state deltas move along this ladder, one row at a time. A +1 from `low_mixed` is `mid_mixed`.

**pace_band** with estimate windows, anchored to a 150 wpm conversational figure:

| Value | wpm window | Use |
|---|---|---|
| slow | 118 to 138 | deliberate, heavy, or aged |
| measured | 139 to 152 | default for interview and narrative |
| brisk | 153 to 166 | news, panel, list formats |
| fast | 167 to 186 | comedy, sport, high-arousal states |

Pace is an estimate unless measured. State the derivation in `provenance.brief` if it came from a supplied sample.

**sentence_length_mix**: `short_led` means 50 percent or more of sentences under 10 words. `balanced` means neither extreme dominates. `long_led` means 40 percent or more over 25 words.

**phoneme_class** is the dominant vowel or consonant family of the signature interjection. This is the axis that stops two personas sharing an interjection that sounds the same.

**tick policy** in `mode_behaviour`: `none` is no tick of any type, `minimal` is the signature interjection only, `baseline` is the declared density, `dense` is up to the cap.

## Validation rules

V1. `id` matches `^[a-z][a-z0-9_]{2,40}$` and equals the filename stem. Display names and ids carry no hyphen: the id is the display name lowercased with underscores between words.
V2. `nationality` and `sex` are in the enums. If absent in the brief, the default is applied and named in `assumptions_applied`.
V3. `describing_words` has 1 to 3 items, all in `references/describing-words.md`, no contradiction pair, no two words from the same redundancy cluster. A trait the operator supplies outside the vocabulary stays in `provenance.brief` as written, and the nearest vocabulary word is used for the field, with the mapping recorded (V34).
V4. `field_of_expertise` is 2 to 6 words, no sentence punctuation.
V5. All seven distinctness axes are present and use enumerated values.
V6. `pace_wpm_estimate` sits inside the window for its `pace_band`.
V7. `tick_inventory` has 6 to 8 ids, all present in `references/tick-library.md`, no type holding more than two.
V8. `signature_interjection.tick_id` appears in `tick_inventory` and its `phoneme_class` matches the library entry.
V9. `tick_density` matches the density table in `references/tick-library.md` unless a documented exception sits in `accepted_matches`.
V10. `eiq` is between 0.0 and 1.0 inclusive.
V11. `eiq_justification` is one sentence of 40 words or fewer, with no personality adjective outside the describing-word vocabulary, no diagnosis, no backstory.
V12. All six states exist with all five sub-fields. `ticks_under_load` may be empty for `intense` only, where `on_cue` says the state drops ticks. A single-host show sets `cohost_divergence` to `not_applicable` in all six states, because there is no second host to diverge from.
V13. Every `ticks_under_load` entry is in `tick_inventory`.
V14. No `ceiling` contains a number of decibels, the word decibel, a percentage of volume, or markup. Ceilings are words and lever steps.
V15. The `angry` ceiling states profanity zero and personal abuse zero.
V16. `voice_note` is one paragraph of 60 to 110 words, naming pace, register, one tick by its literal, and the laugh. It quotes no real person; short quoted ticks are expected.
V17. No field contains a vendor name, product name, model name, or voice identifier.
V18. `provenance.brief` is sufficient to rebuild the profile: name, field, accent, sex, describing words, EIQ target, show shape. A fingerprint value that departs from a generator table carries a deviation line with its reason in `assumptions_applied`, because a rebuild that follows the tables would otherwise produce a different voice.
V19. `distinct_from` lists every stored persona the new one collided with, and `accepted_matches` explains every surviving match.
V20. `version` increments on any edit. An edit that changes an axis invalidates the index line and requires the distinctness gate to be re-run.

Field-level rules for the twelve craft fields live in their own files and are numbered there.

V21. `lexical_register` holds all eight sub-fields with enumerated or counted values, and passes L1 to L6.
V22. `exemplar_lines` holds four baseline lines and exactly three `never_says` lines, and passes E1 to E7.
V23. `calibration_line` is 18 to 26 words, contains the signature interjection literal once and an opener once, and takes 6 to 13 seconds at the declared pace.
V24. `pronunciation_lexicon` holds 0 to 12 pairs and passes P1 to P5. Every `spoken` form is syllables in plain letters.
V25. `recovery_behaviour` holds all five sub-fields, and `latency` is consistent with the EIQ band: low never `immediate`, high never `next_segment` unless `accepted_matches` says why.
V26. `mode_behaviour` enables at least `cold_open`, `intro`, `link` and `outro`, gives every mode entry present all four values, and passes M1 to M7. A host whose `opens_show` is `cohost` still enables `cold_open`, and its note says how the handover works.
V27. `handoff_protocol` passes H1 to H6, and `max_overlap_words` agrees with `takes_floor`.
V28. `standing_dynamic` passes S1 to S8, and `show_shape` governs which of its fields read `not_applicable`.
V29. `recording_context` uses enums only and passes R1 to R6.
V30. `breath_profile` passes B1 to B6, and its breath claims agree with the BRE ids in `tick_inventory`.
V31. `non_speech_sound` passes N1 to N5, with `allowed` and `forbidden` disjoint.
V32. `canon_status.status` is `draft`, `approved` or `retired`. `supersedes` is `null` or the id of a stored persona whose status is `retired`.
V33. Storage separates guidance from product. `examples/` holds the blank template and the worked examples, banners included; `personas/` holds generated profiles only, each with one index line. An example never carries an index line, and the distinctness gate never reads one. A profile derived from an example takes a new id, saves to `personas/`, and is compared against that example at gate step 1 before it may be saved.
V34. An operator override is honoured and recorded. A field the brief states is used as stated, and a value that departs from a generator table carries a line in `assumptions_applied` naming the value, the reason and the table value it replaced. A name the operator chose is kept, including one that coincides with a public or fictional figure, provided the field, traits and voice are invented and the choice is recorded. An override that makes the profile contradict itself is reported with both ways out, never applied silently.
V35. `assumptions_applied` is a list of lines, each in one of four shapes, so C2 reads it mechanically rather than trusting prose:
  - `default: <field> = <value>` for a field the brief left silent and the schema defaulted.
  - `stated: <field> = <value>` for a field the brief states and no table contradicts.
  - `override: <field> = <value>; table says <table value>; because <reason>` for any value that departs from a table, a default or a derived rule. The table value is named even when the reason is obvious.
  - `history: <version> <what changed>` for a version bump.
  A line in no shape fails C2. A field that needs no line is one the brief states and no table touches, one derived from a table without adjustment, or one chosen from a closed list by rule, such as the signature interjection or the bridges. A catch-all row is still a row: a field with no listed row takes the catch-all value and records it as an `override` naming that value.

## Defaults

| Field | Default | When |
|---|---|---|
| nationality | british | brief silent |
| sex | male | brief silent |
| cue_scopes | all three true, precedence line > segment > episode | always |
| tick_density | the density table in `references/tick-library.md` | unless documented |
| version | 1 | new profile |
| canon_status | status `draft`, supersedes `null` | new profile |
| recording_context | dry_studio, close, controlled, low, none | brief silent |
| non_speech_sound | allowed `[page_turn, chair]`, forbidden `[]` | brief silent |
| breath_profile | audible, clause_boundary, rare, through_nose, none | brief silent |
| mode_behaviour | the four required modes at their table values | brief silent |
| handoff_protocol | waits, 0 overlap, two bridges each | two-host brief silent |
| describing_words | none | brief must supply or the generator refuses |

`display_name`, `field_of_expertise` and `describing_words` have no defaults. A missing name is a refusal, not an invention, because the name collides with the store and with the listener's expectations.

## The baseline set and EIQ

Four artifacts describe the persona at rest and are invariant under `eiq`: `lexical_register`, `exemplar_lines`, `calibration_line`, and the fingerprint's baseline register. Two profiles differing only in EIQ therefore carry the same words, the same exemplars and the same calibration line. If a high-EIQ version reads calmer at rest, the rating was used to smuggle in a personality change.

`recording_context`, `breath_profile`, `non_speech_sound`, `standing_dynamic`, `handoff_protocol` and `mode_behaviour` are also invariant under EIQ. They describe the body, the show and the relationship, none of which a rating changes.

## Lifecycle

`canon_status.status` moves `draft` to `approved` to `retired`. Nothing else moves.

1. A new profile is `draft`. Drafts are checked by the distinctness gate and may be saved, because the distinctness gate is what decides whether they survive.
2. `approved` means the profile is in scripts. Approved profiles are the ones a transcript skill may read.
3. `retired` means it is out of use. Retired profiles stay in the store and in the index, so their ids are never reused, but the distinctness gate skips them: a retired persona no longer blocks a new one.
4. A replacement sets `supersedes` to the retired id, takes a new id, and carries `distinct_from` naming the persona it replaced. A retiring edit to the same id is not allowed, because scripts already reference it by name.
5. Editing an approved profile in place bumps `version` and keeps the status. Editing a profile that changes an axis re-runs the distinctness gate.

## Index line

`personas/index.jsonl` holds one JSON object per line for a reading agent to compare without parsing the profile:

```json
{"id":"harriet_voss","version":1,"status":"approved","nationality":"british","sex":"female","describing_words":["wry","measured"],"field":"urban design","show_shape":"two_host","vowel_colour":"neutral","consonant_crispness":"crisp","pitch_register":"low_mixed","pace_band":"measured","stress_pattern":"even","sentence_length_mix":"balanced","signature_interjection":"TICK-014","interjection_phonemes":"plosive","eiq":0.4,"supersedes":null,"created":"2026-10-21"}
```

The index is the collision surface. A missing line means the persona is invisible to the distinctness gate and will duplicate silently. A line with `status: retired` is still read for id uniqueness and skipped for matching.

An index with no line means an empty store. The three worked examples live in `examples/` and are deliberately absent from the index, so a persona derived from one is compared against that example rather than against every example in the skill.
