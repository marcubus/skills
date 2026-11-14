# Verification: the twelve craft fields

Evidence for the revision that took profiles from sixteen fields to twenty-eight. Run these cases again if the tick library, the vocabulary, the craft rule sets or the emotion engine change, and diff.

Method: a throwaway validator in the scratch directory, outside the skill, deleted after the run. The skill still ships no code. Every check below exists as a readable test in `GATE.md`, so a reader can reproduce it without the script.

Status note: this file records the version 2 run, when the three profiles sat in `personas/`. They are now version 3, stored in `examples/` as guidance with no index line, and the gate numbers below were re-derived in `references/verification-revalidation.md`. Read the numbers here as the version 2 record.

## Contents

- What was added
- Profiles rebuilt at version 2
- The gate, with the new fields in place
- Collision attempt
- EIQ invariance
- Mutation tests: does each check actually bite
- What this does not prove

## What was added

Twelve field groups, three new reference files, five new rule sets, and two changes to existing files.

| Field group | Rules | File |
|---|---|---|
| `lexical_register` | L1 to L6 | voice-craft.md |
| `exemplar_lines` | E1 to E7 | voice-craft.md |
| `calibration_line` | K1 to K6 | voice-craft.md |
| `pronunciation_lexicon` | P1 to P5 | voice-craft.md |
| `recovery_behaviour` | Q1 to Q5 | emotion-engine.md |
| `mode_behaviour` | M1 to M7 | show-craft.md |
| `handoff_protocol` | H1 to H6 | show-craft.md |
| `standing_dynamic` | S1 to S8 | show-craft.md |
| `recording_context` | R1 to R6 | studio-craft.md |
| `breath_profile` | B1 to B6 | studio-craft.md |
| `non_speech_sound` | N1 to N5 | studio-craft.md |
| `canon_status` | V32, lifecycle section | persona-schema.md |

Existing files changed: `references/emotion-engine.md` invariants went from four to six, so the exemplars, calibration line, body, show and relationship are all frozen under EIQ. `references/phonetic-distinctness.md` now skips retired profiles and runs the side-by-side test against the stored calibration lines.

## Profiles rebuilt at version 2

```
des_larkin: v2 EIQ 0.1 fields 28 checks 0 failures
harriet_voss: v2 EIQ 0.45 fields 28 checks 0 failures
noor_haddad: v2 EIQ 0.85 fields 28 checks 0 failures
```

| Persona | Calibration line | Lexicon | Modes | Exemplar words | Voice note | Breath | Relation shape |
|---|---|---|---|---|---|---|---|
| des_larkin | 18 words, 6.8 s at 160 wpm | 2 pairs | 5 | 17, 15, 12, 13 | 105 | inaudible inhale, bark laugh | joke, next segment |
| harriet_voss | 22 words, 9.1 s at 145 wpm | 1 pair | 5 | 17, 14, 13, 11 | 103 | inaudible inhale, voiceless laugh | subject change, next segment |
| noor_haddad | 22 words, 8.2 s at 160 wpm | 1 pair | 5 | 18, 15, 11, 10 | 88 | audible inhale, nose laugh | apology, next turn |

Two breath profiles differ for a structural reason, not a stylistic one: harriet and des carry no BRE tick in their inventories, so B1 forces an inaudible inhale. Noor carries TICK-043, so an audible inhale is legal and B6 then forces controlled plosives at a close mic.

## The gate, with the new fields in place

```
des_larkin vs harriet_voss: PASS total=0 core=0 matches=[]
des_larkin vs noor_haddad: PASS total=1 core=1 matches=['pace_band']
harriet_voss vs noor_haddad: PASS total=2 core=1 matches=['vowel_colour', 'sentence_length_mix']
```

Cross-profile checks also ran: no shared tick above three per pair, no shared bridge phrase, no shared opener, one room and one mic distance across the three, identical object policy, and exactly one host opens and one closes in each pair.

## Collision attempt

mira_blake was built as a deliberate mirror of harriet_voss: same accent, register, pace, consonants, stress, sentence mix and signature class, with a new name, new openers, a new calibration line and a new lexicon.

```
initial                              FAIL  harriet_voss: total=7 core=3
1 signature plosive to rounded_back  FAIL  harriet_voss: total=6 core=3
2 sentence mix balanced to short_led FAIL  harriet_voss: total=5 core=3
3 stress even to spike_then_flat     FAIL  harriet_voss: total=4 core=3
4 consonants crisp to slurred        FAIL  harriet_voss: total=3 core=3
5 pace measured to slow              FAIL  harriet_voss: total=2 core=2
6 register low_mixed to low_chest    PASS  harriet_voss: total=1 core=1
```

Six mutations to separate a copy. The first five each cleared one axis and left the core breach open, which is the order working as written: the cheap axes go first and are not enough on their own. Nothing was saved; the test ends at the first passing mutation. What the attempt proves is that the new fields cannot rescue a phonetic duplicate: mira had a different vocabulary, different openers, a different calibration line and a different lexicon, and the gate failed it anyway.

## EIQ invariance

The same profile rebuilt at 0.10, 0.50 and 0.90, with only the rating, the justification, the per-state co-host line and the recovery latency changed.

```
lexical_register       identical
exemplar_lines         identical
calibration_line       identical
recording_context      identical
breath_profile         identical
non_speech_sound       identical
standing_dynamic       identical
handoff_protocol       identical
mode_behaviour         identical
tick_inventory         identical
```

Angry co-host cue, one line each:

| EIQ | Line | What moved |
|---|---|---|
| 0.10 | "Yeah. Yeah, you're right. It's rubbish. I don't know why I said it." | adopts the state and the argument, names nothing, recovery waits for the next segment |
| 0.50 | "I'm not sure it's rubbish. Hmm. I'm also not sure I've explained it well. Give me the actual objection." | keeps a position, names its own uncertainty, one turn late |
| 0.90 | "You're angry, and I can hear the comparison is the part that's wrong. Fair. Give me the objection and I'll take it." | names both states, offers a route about the work, recovers next turn |

Same accent, same register, same ticks, same four exemplar lines, same calibration line. The rating changed four sentences and no sound.

## Mutation tests: does each check actually bite

Twenty-four deliberate defects, one per rule, each injected into a copy of a stored profile.

```
hedges heavy with assertion states               C13  yes  L1 states+hedges
two openers                                      C13  yes  openers count
banned word is a describing word                 C13  yes  banned is describing word warm
exemplar claim 40 words                          C14  yes  claim 40 words
exemplar laugh two ticks                         C14  yes  laugh has 2 ticks
two never_says lines                             C14  yes  never_says count
calibration 30 words                             C15  yes  calibration 30 words
calibration missing opener                       C15  yes  calibration missing opener
lexicon dotted letters                           C16  yes  dotted letters P.H.
lexicon unused word                              C16  yes  P2 HACCP unused
audible inhale with no BRE id                    C22  yes  B1 audible without BRE id
frequent sigh without TICK-039                     C22  yes  B2
laugh breath mismatch                            C22  yes  B5 voiced_start
correction mode with ticks                       C18  yes  M3 correction
outro without sign-off placement                 C18  yes  M4 outro
relation three words                             C20  yes  relation 3 words
owns and defers overlap                          C20  yes  S4 overlap
distant mic with no room tone                    C21  yes  R2 tone
objects overlap lists                            C23  yes  N1 overlap
angry ceiling in decibels                        C8   yes  angry ceiling digits/markup/decibel
low EIQ recovering immediately                   C17  yes  Q1 low immediate
high EIQ recovering next segment                 C17  yes  Q1 high next_segment
supersedes a persona that is not retired         C24  yes  supersedes harriet_voss not retired
mode note too short                              C18  yes  link note 3 words

mutations 24, caught 24, missed 0
```

The first run caught 22 of 24, and both misses were real defects in the checks rather than in the fixture.

1. **C18 missed an unenabled mode.** The mutation put `ticks: baseline` into `correction`, which noor does not enable, so a check that only walked `enabled` never looked at it. M1 and V26 now say every mode entry present is checked, enabled or not.
2. **C8 missed the word decibel.** The check searched for digits, percent, dB and markup, so "three decibels above baseline" passed with no digit in it. V14 and C8 now name the word itself.

Two defects in the profiles were also caught and fixed at this stage: des_larkin's `intense` state emptied its tick list without saying so in `on_cue`, which V12 requires, and his voice note named pace and pitch but never the word register, which V16 requires. Both were fixed in the profile, not in the rule.

## What this does not prove

- No audio was analysed or rendered. Room, breath and object sound are conventions of studio practice written as enums, not measurements.
- The checks are reading procedures. A careless agent can skip one; the checklist is the only enforcement, which is the cost of shipping no code.
- Mode precedence over a strained state (M6) is stated, not exercised: no fixture drives a tired persona through a correction while a co-host is angry. That is the first test to run when a transcript skill consumes a profile.
- Cross-profile rules were tested on pairs drawn from three profiles in one room. A real show with different rooms, or a panel, would exercise R5 and N4 harder than this set does.
