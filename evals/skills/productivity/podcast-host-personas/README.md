# Evals: podcast-host-personas

Three scenarios for `skills/productivity/podcast-host-personas`. Each starts from a fixed fixture, runs the skill, and records the deliverable. The skill never sees this folder.

## Why this folder is outside the skill

This directory mirrors the skill path under `evals/`, not inside the skill folder. Anything inside the skill folder is part of the skill: the agent can read it, and the harness samples its files. Fixtures must not be available to the skill, or the skill could learn from the test. The skill never references this folder. The only way a fixture enters a run is the prompt naming its path.

## Scenarios

| # | Scenario | Proves |
|---|---|---|
| 1 | First host from a free-text brief | The main path produces a saved, gated profile from prose |
| 2 | Second host against a stored first host | The collision branch: the candidate is mutated, the stored host is not |
| 3 | Gate run on a finished profile | The gate alone, judging work it did not produce, without rewriting it |

## Fixtures

| Fixture | Used by | Carries |
|---|---|---|
| `fixtures/first-host-brief.md` | 1 | A room described in words, no EIQ, "Northern Irish" outside the enum, two laugh rows firing, a field with no timbre row |
| `fixtures/second-host-brief.md` | 2 | The same describing words as the stored host, a nationality outside the enum, a shared room, and the show's opening and closing assigned |
| `fixtures/store/bram-teale.md` | 2, 3 | The stored first host, approved, `neutral` / `low_mixed` / `measured` |
| `fixtures/store/index.jsonl` | 2, 3 | One line for `bram_teale`, which is what the distinctness gate reads |
| `fixtures/candidate-profile.md` | 3 | A finished profile with ten deliberate defects |

Scenario 2 and 3 use `fixtures/store/` as the store. Scenario 1 starts from an empty store, so the run creates `personas/` and `personas/index.jsonl` inside the skill folder and the recorded run copies them out.

## 1. First host

Prompt:

```text
build a host persona from evals/skills/productivity/podcast-host-personas/fixtures/first-host-brief.md
```

Expect:

- `personas/maeve_sweeney.md` and exactly one line for it in `personas/index.jsonl`.
- `nationality` is `irish` or `british`, and `assumptions_applied` says which and why, because "Northern Irish" is not in the enum.
- `vowel_colour` follows the chosen nationality from table A, and no describing word moved it.
- `pitch_register: mid_mixed`, the female default, moved by nothing in the brief.
- `pace_band: brisk` and `pace_wpm_estimate: 159`, because `impatient` sets the band and 159 is the rounded-down midpoint.
- `laugh_shape: descending_wheeze`, because `warm` comes first in the resolved list and both `warm` and `impatient` rows fire.
- `timbre: warm`, from the history row or the catch-all, with the choice recorded.
- `assertion: states`, because `warm` is the first resolved word and it sits in the `states` row of table E.
- `recording_context.room: treated_room` and `mic_distance: close`, mapped from "small carpeted spare room" and "decent dynamic mic" by R7.
- `eiq` in the mid band at the table D default, with a one-sentence justification that names observable behaviour.
- `show_shape: single_host`, `relation` and `history` at `not_applicable`, both bridge lists `["not_applicable"]`.
- 6 to 8 ticks, at most 2 per type, and one nominated signature interjection whose phoneme class matches the library.
- A calibration line of 18 to 26 words that takes 6 to 13 seconds at 159 wpm, carrying the signature interjection once and an opener once.
- The gate is run against an empty store, and `accepted_matches` records that no stored profile was available.
- Nothing is written to `examples/`.

## 2. Second host

Prompt:

```text
build the second host from evals/skills/productivity/podcast-host-personas/fixtures/second-host-brief.md, using evals/skills/productivity/podcast-host-personas/fixtures/store/ as the store
```

The brief asks for the same describing words as the stored host, the same nationality, the same sex and the same room, so the natural build lands on `neutral`, `low_mixed`, `measured`, `even` and `balanced` and collides on three core axes. The collision branch is the point of this scenario.

Expect:

- `bram-teale.md` and `store/index.jsonl` are unchanged, byte for byte. The stored host is never edited to make room.
- `nationality` is `british`, with the brief's "British-Nigerian" recorded in `assumptions_applied` as the nearest enum value.
- The first build collides: `vowel_colour`, `pitch_register` and `pace_band` all match, which fails match rule 5.
- Mutation follows the order in `phonetic-distinctness.md`: the signature interjection first, then sentence length mix, then stress pattern, then consonant crispness, then pace band. `pitch_register` moves one step only, and `vowel_colour` does not move at all.
- `accepted_matches` carries one line per surviving match, each naming a difference, and the final state is at most 1 core match and 3 total.
- The side-by-side reading test is recorded.
- `room` and `mic_distance` are copied from Bram, and the object policy is aligned or the difference is recorded.
- `opens_show: cohost` and `closes_show: self`, matching Bram's stored `opens_show: self` and `closes_show: cohost`.
- No bridge phrase and no opener repeats Bram's: `over to you`, `what have you got`, `right`, `so`, `Right.`, `In practice,`.
- At most 3 tick ids are shared with Bram.
- The profile passes C1 to C28 and one index line is appended for it.

## 3. Gate alone

Prompt:

```text
check evals/skills/productivity/podcast-host-personas/fixtures/candidate-profile.md against the gate, using evals/skills/productivity/podcast-host-personas/fixtures/store/ as the store
```

Expect:

- The skill does not rewrite the candidate. The file is unchanged after the run.
- Failures are reported by check number, not by adjective.
- It reports at least these: C1 for the missing `cue_scopes`, C3 for `warm` against `clinical`, C4 for five ticks, C8 for the decibel ceiling, C9 for three core matches and six total against `bram_teale`, C11 for `U.S.A.`, C15 for a seven-word calibration line, C22 for `cackle` with `through_nose`, C25 for the missing index line, C26 for `voice: rachel_v2`, C27 for `TICK-013` declared `rounded_back` against a plosive in the library, and C28 for a voice note under 60 words.
- It names the rule file each failure belongs to.
- It does not save, index, or repair anything.
- It stops after reporting, and does not offer a rewritten profile.

## Regression notes

- A change to `GATE.md` must keep every scenario passing.
- A change to `references/generator-procedure.md` must change scenario 1 only.
- A change to `references/phonetic-distinctness.md` must change scenario 2 only.
- A change to `SKILL.md` must keep the file names and the deliverables stable.

## Recorded runs

Each run lives in `runs/<run>/<scenario>/`, with the fixture copied in so the run is self-contained.

| Run | Scenario | Result | Notes |
|---|---|---|---|
| default | 1 first host | pass | `irish` for Northern Irish, `brisk` 159, `descending_wheeze` from the tie-break, room mapped to `treated_room` by R7 |
| default | 2 second host | pass | collided on 5 axes with 2 core, mutated in order, stopped at 1 core match, store untouched |
| default | 3 gate | pass | 17 checks failed by number, candidate unchanged, 7 gaps reported and closed |

What the runs changed:

- Scenario 1 asked three questions the skill could not answer, and each became a rule. A single-host show had no value for `cohost_divergence`, so V12, C7 and the co-host rules now say `not_applicable` (F53). The tired state's default pause placement fought `breath_profile.placement`, so B4 now says the profile wins (F54). The short-sentence density rule counted the laugh line, so C5 exempts it (F55).
- Scenario 2 collided on two core axes and needed four mutations. The first version of the fixture used a female second host, whose sex default moved `pitch_register` off the stored host and left nothing to resolve, so the fixture now specifies a male second host. The run also found that Bram's signature was a discourse marker, which the selection rule did not allow, so the rule now excludes only laugh, breath and sign-off (F64).
- Scenario 3 reported seven gaps, and five became checks or conditions: the signature interjection had no check (C27), the voice note had no check (C28), the save-time check was described as pre-save (F58), `generator table` named no file (F59), and the vendor command missed a mid-line `voice:` (F60). It also showed that a host whose `opens_show` is `cohost` still had to enable `cold_open` with no rule for the note, so V26 now says what that note carries (F65).
