# Verification: template revalidation and store split

Record of the pass that revalidated the blank template and the three worked examples at version 3, and separated guidance from the generated store. Run this again if the schema, the generator tables or the tick library change.

Method: a throwaway validator in the scratch directory, outside the skill, deleted after the run. The skill still ships no code. Every check below exists as a readable test in `GATE.md`.

Supersedes, where they differ, the gate numbers in `references/verification-2026-10-21.md` and `references/verification-craft-additions.md`.

## What changed

| Change | Where |
|---|---|
| Blank template and three worked examples moved from `personas/` to `examples/` | file tree |
| `personas/index.jsonl` emptied: it holds generated profiles only | store |
| V33 added: guidance and product never share a directory, examples are never indexed | `references/persona-schema.md` |
| V18 extended: any fingerprint value that departs from a generator table carries a deviation line | `references/persona-schema.md` |
| C2 extended to check deviations as well as defaults; C25 added for the storage split | `GATE.md` |
| Gate step 1 now adds the source example to the comparison set | `references/phonetic-distinctness.md` |
| Failure mode added: example promoted to the store | `GATE.md` |
| Store layout section and hard rule 15 | `SKILL.md` |

## Template check

| Check | Result |
|---|---|
| YAML block parses | pass |
| Top-level fields | 28 of 28, no extras, order matches the schema |
| `vocal_fingerprint` keys | 11 of 11 |
| `emotion_behaviour` states | six, all present |
| state sub-fields | five per state |
| `recovery_behaviour` keys | five |
| required modes enabled | cold_open, intro, link, outro |
| prefilled values | british, male, 2.5/4.0/5.5, `line > segment > episode`, draft |
| blank values documented | room, breath, non-speech, lexical, exemplars, voice note and rest resolve from the defaults table or the brief |

## Profile check, three examples at version 3

des_larkin 0.10 low, harriet_voss 0.45 mid, noor_haddad 0.85 high. All three: 28 fields, every rule V1 to V33 checked, no failures.

| Rule group | Result |
|---|---|
| identity, enums, pace window, tick count and signature | pass |
| describing words, vocabulary, contradiction pairs | pass |
| EIQ range, one-sentence justification | pass |
| six states, five sub-fields, load ticks inside the inventory | pass |
| ceilings in words, profanity zero and personal abuse zero | pass |
| voice note length, pace, register, signature literal, laugh | pass |
| lexical register, exemplars, calibration line, lexicon | pass |
| recovery, modes, handoff, standing dynamic, room, breath, objects | pass |
| lifecycle, version, supersedes | pass |
| table A frame with every departure logged | pass |

## Gate output

```
store: [] examples: ['des_larkin', 'harriet_voss', 'noor_haddad']
gate des_larkin vs harriet_voss:  total=0 core=0 matches=[]                     PASS
gate des_larkin vs noor_haddad:   total=1 core=1 matches=['pace_band']          PASS
gate harriet_voss vs noor_haddad: total=1 core=0 matches=['sentence_length_mix'] PASS
index lines: 0 -> []
FAILURES 0
```

Every match is written into `accepted_matches`: noor_haddad against des_larkin on pace band, and against harriet_voss on sentence length mix.

## Defects found and fixed

| # | Defect | Fix |
|---|---|---|
| 1 | noor_haddad carried `vowel_colour: neutral` while table A gives fronted for a Spanish-accented frame and her own voice note said "fronted vowels". Three-way contradiction, and the profile could not be rebuilt from its brief | set to fronted, gate re-run, `accepted_matches` rewritten |
| 2 | noor_haddad's pace match with des_larkin was undocumented | written into `accepted_matches` with a reason |
| 3 | noor_haddad's stress pattern and timbre departed from tables A and B with no deviation line | both logged in `assumptions_applied`; V18 and C2 extended so the class is now checkable |
| 4 | three angry ceilings said "no profanity, no personal attack" where V15 requires profanity zero and personal abuse zero | standardised in all three profiles |
| 5 | des_larkin sat two steps above the male register default while generator step 6 allows one, with nothing recording it | deviation logged in `assumptions_applied` |
| 6 | worked example B claimed three core matches at the gate; the derived values give three matches, one core | step 22 rewritten to the real numbers |
| 7 | worked example A claimed one core match on vowel colour, which stopped being true when defect 1 was fixed | corrected to no core match, two documented |
| 8 | voice note counts in the worked examples were wrong (96 against an actual 103, 104 against an actual 88) | corrected |
| 9 | the template told a reader to copy to `personas/<id>.md` without saying it is guidance | banner added, plus single-host notes for handoff and standing dynamic, and the outro sign-off note |
| 10 | the store index held three lines for what are now guidance files | emptied; examples carry no index line |

## Residual limits

- No audio was analysed. Pace, register and timbre remain perceptual codings with the derivation stated.
- The template is structure, not content. A reader who copies it still has to resolve every value, and the checklist is the only thing that catches a lazy copy.
- The example-comparison step in the gate is a written procedure. With no index line to read, nothing mechanical forces it; C25 and the gate step are the enforcement.
