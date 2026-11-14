# Verification, 2026-10-21

Phase 4 output, kept as the regression fixture. If the tick library, the emotion engine or the describing vocabulary changes, re-run these cases and diff.

Method note: the checks were executed with a throwaway Python validator in the scratch directory, outside the skill. Nothing in this skill ships code; the same checks are written as readable tests in `GATE.md`.

Scope note: this file records the sixteen-field build. The three profiles were later extended to version 2 with twelve craft fields, so they now carry twenty-eight fields each and the checks run to C25.
Status note: the profiles are now at version 3 and live in `examples/` as guidance, not in the store. The gate numbers below are the version 2 record and were re-derived at version 3 in `references/verification-revalidation.md`, which supersedes them wherever the two differ. The reproduction steps and the six-state deltas still stand. The craft-field evidence is in `references/verification-craft-additions.md`. The lever deltas and the three-EIQ exchange below are unchanged by that revision, because the craft fields are baseline artifacts and do not move with `eiq`.

## Contents

- Test set
- Field check output
- Fingerprint comparison
- Collision attempt
- Six states, lever deltas against calm baseline
- Two-host exchange, co-host angry
- Quality checklist, all three
- Limits hit

## Test set

| Persona | EIQ | Band | Nationality | Sex | Field | Describing words |
|---|---|---|---|---|---|---|
| des_larkin | 0.10 | low, contagious | australian | male | sports analytics | blunt, brisk |
| harriet_voss | 0.45 | mid, reactive | british | female | urban design | wry, measured |
| noor_haddad | 0.85 | high, regulated | spanish_accented_english | female | food science | warm, curious |

Files: `examples/des_larkin.md`, `examples/harriet_voss.md`, `examples/noor_haddad.md`. They were saved to `personas/` during this run and later moved to `examples/` as guidance, which is why they carry no index line now.

## Field check output

```
des_larkin      V1 id PASS  des_larkin / des_larkin
des_larkin      V2 enums PASS  australian, male
des_larkin      V3 words PASS  ['blunt', 'brisk'] bad=[] contradictions=[]
des_larkin      V5 axes PASS  7 axes present
des_larkin      V6 wpm PASS  160 in 153-166
des_larkin      V7 ticks PASS  7 ids ['TICK-002','TICK-018','TICK-022','TICK-034','TICK-047','TICK-068','TICK-060'] missing=[]
des_larkin      V8 sig PASS  TICK-018 open_back
des_larkin      V9 density PASS  {'baseline_per_100w': 2.5, 'strained_per_100w': 4.0, 'cap_per_100w': 5.5}
des_larkin      V10 eiq PASS  0.1
des_larkin      V11 just PASS  1 sentence(s), 24 words
des_larkin      V12 states PASS  6 states x 5 fields
des_larkin      V13 load ticks PASS  outside inventory: []
des_larkin      V14 ceilings PASS  []
des_larkin      V15 abuse PASS  volume one step, pace plus twenty-five percent, no profanity...
des_larkin      V16 voice note PASS  102 words, signature literal present: True
des_larkin      V17 no vendors PASS  []
des_larkin      V18 brief PASS  105 chars
harriet_voss    ... all PASS, voice note 103 words
noor_haddad     ... all PASS, voice note 88 words
FAILURES: none
index lines: 3 consistent: True
tick library rows parsed: 72; vocab words: 40; contradiction rows: 42, covering 40 unique word pairs
```

Two failures were caught on the first run and fixed before saving: the voice notes for des_larkin and harriet_voss did not name their own signature interjection, which check V16 requires because the signature is the one sound a listener would imitate. The vocabulary was also one word short of the advertised forty, so `laconic` was added with four contradiction pairs.

## Fingerprint comparison

| Axis | harriet_voss | des_larkin | noor_haddad |
|---|---|---|---|
| vowel_colour | neutral | broad | neutral |
| consonant_crispness | crisp | clipped | soft |
| pitch_register | low_mixed | high_mixed | mid_mixed |
| pace_band | measured | brisk | brisk |
| stress_pattern | even | punch_first | trailing_off |
| sentence_length_mix | balanced | short_led | balanced |
| signature interjection | TICK-014 blimey, plosive | TICK-018 huh, open_back | TICK-006 hmm, nasal |

Pairwise result:

```
des_larkin vs harriet_voss: matches=[] core=[] -> PASS
des_larkin vs noor_haddad: matches=['pace_band'] core=['pace_band'] -> PASS
harriet_voss vs noor_haddad: matches=['vowel_colour','sentence_length_mix'] core=['vowel_colour'] -> PASS
```

Both surviving pairs are documented in `accepted_matches` in the profile files. No pair exceeds one core match or three total matches.

## Collision attempt

Candidate `mira_blake` was deliberately built as a near-copy of harriet_voss: neutral vowels, crisp consonants, low_mixed register, measured pace, even stress, balanced sentences, plosive interjection.

```
INITIAL CANDIDATE
  vs harriet_voss  FAIL  matches=all seven, core=3
  RESULT: COLLISION

AFTER 1 signature interjection: plosive -> fricative
  vs harriet_voss  FAIL  matches=6, core=3

AFTER 2 sentence mix: balanced -> short_led
  vs harriet_voss  FAIL  matches=5, core=3

AFTER 3 stress: even -> spike_then_flat
  vs harriet_voss  FAIL  matches=4, core=3

AFTER 4 consonants: crisp -> slurred
  vs harriet_voss  FAIL  matches=3, core=3
  (soft was rejected at this step because it would match noor_haddad)

AFTER 5 pace: measured -> slow
  vs harriet_voss  FAIL  matches=['vowel_colour','pitch_register'], core=2

AFTER 6 register: low_mixed -> low_chest
  vs harriet_voss  PASS  matches=['vowel_colour'], core=1
  vs des_larkin    PASS  matches=['sentence_length_mix'], core=0
  vs noor_haddad    PASS  matches=['vowel_colour'], core=1
  RESULT: CLEAR
```

Six mutations to separate a mirror. That is the expected cost of a deliberate copy, and the reason the procedure mutates the candidate rather than trusting a rename. The candidate was not saved; the test required the resolution, not a fourth profile.

## Six states, lever deltas against calm baseline

Magnitudes follow `references/vocal-levers.md` Table 2: 0 no change, +/-1 slight, +/-2 clear, +/-3 large. Pace is a percentage of the persona's own baseline. Register is band movement; a number in brackets is the ceiling only.

### harriet_voss, calm 145 wpm, low_mixed

| State | Pace | Pause | Register | Pitch move | Volume | Articulation | Sentence | Interjections | Laugh | Self-interrupt |
|---|---|---|---|---|---|---|---|---|---|---|
| angry | +15% | -1 | 0 (ceil +2) | +1 | 0 | +2 | -2 | -1 | 0 | -1 |
| frustrated | +8% | -1 | 0 | +1 | +1 then - | 0 | -1 | +2 | +1 | +2 |
| tired | -20% | +3 | 0 (floor -1) | -2 | -2 | -2 | +1 then -2 | +1 | -1 | +1 |
| intense | +10% | -2 | 0 | -1 | +1 | +2 | -1 | -2 | 0 | -2 |
| curious | +5% | +1 after question | 0 | +2 | 0 | +1 | -1 | +1 | +1 | +1 |
| happy | +10% | -1 | floor +1 | +3 | +1 | +1 | -1 | +2 | +3 | +1 |

Cold anger: volume does not rise, articulation does. That is the inversion declared in her profile.

### des_larkin, calm 160 wpm, high_mixed

| State | Pace | Pause | Register | Pitch move | Volume | Articulation | Sentence | Interjections | Laugh | Self-interrupt |
|---|---|---|---|---|---|---|---|---|---|---|
| angry | +25% | -2 | 0 (ceil +2) | +2 | +2 | +1 | -2 | +1 | 0 | -1 |
| frustrated | +10% | -1 | 0 | +1 | +1 | 0 | -1 | +2 | +1 | +2 |
| tired | -20% | +3 | 0 (floor -1) | -2 | -2 | -2 | +1 then -2 | +1 | -1 | +1 |
| intense | +10% | -2 | 0 | -1 | +1 | +2 | -1 | -2 | 0 | -2 |
| curious | +5% | -1 before, +1 after | 0 | +2 | 0 | +1 | -1 | +1 | +1 | +1 |
| happy | +15% | -1 | floor +1 | +3 | +1 | +1 | -1 | +2 | +3 | +1 |

Hot anger: pace and volume both rise, which is the profile most at risk of caricature. The ceiling is two segments, and the recovery beat is mandatory.

### noor_haddad, calm 160 wpm, mid_mixed

| State | Pace | Pause | Register | Pitch move | Volume | Articulation | Sentence | Interjections | Laugh | Self-interrupt |
|---|---|---|---|---|---|---|---|---|---|---|
| angry | -10% | +1 | 0 (ceil +1) | -1 | 0 | +2 | -1 | -1 | 0 | -2 |
| frustrated | -5% | +1 | 0 | 0 | 0 | +1 | -1 | +1 | +1 | 0 |
| tired | -10% | +2 | 0 (floor -1) | -2 | -1 | -1 | +1 then -1 | +1 | -1 | +1 |
| intense | +10% | -2 | 0 | -1 | +1 | +1 | -1 | -2 | 0 | -2 |
| curious | +5% | +1 after question | 0 | +2 | 0 | +1 | -1 | +1 | +1 | +1 |
| happy | +10% | -1 | floor +1 | +3 | +1 | +1 | -1 | +2 | +3 | +1 |

Her tired state is the one that shows the ceiling doing work: pace drops only ten percent, because a twenty percent drop plus soft consonants plus long pauses would read as unwell rather than tired on air.

## Two-host exchange, co-host angry

Cue from des_larkin, angry, hot profile:

> "Look, that number's rubbish. You can't compare a lab result to a supermarket shelf and call it the same thing."

The responder is noor_haddad with EIQ varied and every other field held constant.

**EIQ 0.10, low, contagious**

> "Huh. Yeah. No, you're right, it's rubbish. I don't know why I said it."

Pace +2, volume -1, one interjection from her inventory, no naming, no offer, no position. She has adopted his state and his argument. This is the failure the brief ruled out.

**EIQ 0.50, mid, reactive with partial control**

> "I'm not sure it's rubbish. Hmm. I'm also not sure I've explained it well. Give me the actual objection."

Pace 0, pause +1 before the concession, one filler, one self-repair. She names her own uncertainty and not his anger, and the de-escalation arrives after the exchange has already peaked.

**EIQ 0.85, high, regulated**

> "You're angry, and I can hear the comparison is the part that's wrong. Fair. Give me the actual objection and I'll take it."

Pace -1, volume 0, articulation +2, no laugh, one naming line, one offer about the work. She still feels it: the pace drop is the tell, and a neutral host would not slow down.

Across the three: same accent, same register, same tick inventory, same vocabulary level. Only the four EIQ functions change: noticing, naming, timing, recovery. Invariant 4 holds.

## Quality checklist, all three

| Check | des_larkin | harriet_voss | noor_haddad |
|---|---|---|---|
| C1 required fields | PASS | PASS | PASS |
| C2 defaults logged | PASS, none applied | PASS, none applied | PASS, none applied |
| C3 describing words | PASS blunt, brisk | PASS wry, measured | PASS warm, curious |
| C4 tick count and overlap | PASS, 7 ids, 0 shared with either | PASS, 7 ids, 0 shared with either | PASS, 7 ids, 0 shared with either |
| C5 tick density | PASS, 2.5 baseline | PASS, 2.5 baseline | PASS, 2.5 baseline |
| C6 EIQ | PASS 0.10, 24 words | PASS 0.45, 20 words | PASS 0.85, 25 words |
| C7 six states | PASS | PASS | PASS |
| C8 ceilings in words | PASS, no digits or markup | PASS | PASS |
| C9 distinctness | PASS, 1 core match max | PASS | PASS, documented |
| C10 no real person | PASS | PASS | PASS |
| C11 acronyms | PASS, none present | PASS | PASS |
| C12 reproducible | PASS | PASS | PASS |

### Five-question sanity read

| Question | des_larkin | harriet_voss | noor_haddad |
|---|---|---|---|
| What does he do with a pause? | almost nothing at baseline, which is the fingerprint | uses it as pressure, longer than comfortable | pauses after the question, not before |
| One sound a listener would imitate? | "huh" | "blimey" | "hmm" |
| Response to an angry co-host? | joins and escalates | lowers volume, sharpens consonants | names both states, offers a route |
| Two axes to change for a second host? | register and vowel colour | pace and register | vowel colour and stress |
| Rebuildable next year from the file? | yes | yes | yes |

## Limits hit

1. No audio was analysed. Pace, pitch register and timbre are perceptual codings with a stated method, not measurements. The emotion shifts are coded observations checked for direction against the published literature, not acoustic data from these speakers.
2. Four of the ten podcasters carry the strained-state documentation, as the brief required. The other six have calm-state profiles only.
3. The verified literature supports direction, not magnitude. The +/- steps in the emotion table are design conventions calibrated to be audible, not published effect sizes.
4. Faye D'Souza was dropped from the shortlist because her first-party podcast output was weaker than the alternatives; Róisín Ingle took the Irish female slot and Amit Varma the Indian male slot.
5. Spanish is scoped to Spanish-accented English only. No non-English output is supported, and the fingerprint axes would need a parallel set.
6. The skill has no scripts by request. Every check is a readable procedure, which means a careless agent can skip one. The checklist is the only enforcement.
