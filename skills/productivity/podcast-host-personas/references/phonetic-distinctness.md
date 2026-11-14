# Phonetic distinctness

This file is the distinctness gate. Two stored personas must be distinguishable on the page: if a reader cannot say which persona a line belongs to without being told, no synthesiser will help.

The distinctness gate is a text check. It needs no audio, no model, and no listening. It runs against `personas/index.jsonl` and returns pass or collision.

## Contents

- The seven axes
- Examples are not stored profiles
- Match rules
- Procedure
- Collision resolution
- The side-by-side reading test
- Example: a passing comparison
- Example: a documented pass
- Example: a fail
- Why seven axes and not fewer

## The seven axes

Every profile records all seven. A **match** means the same value on the same axis.

| Axis | Values | What it controls in speech | Core |
|---|---|---|---|
| vowel_colour | broad, neutral, fronted, rounded, nasal_front | the shape of the mouth on stressed vowels, the strongest accent cue | yes |
| consonant_crispness | crisp, soft, clipped, slurred | separation of stops and fricatives, how word endings land | no |
| pitch_register | low_chest, low_mixed, mid_mixed, high_mixed, high_head | where the voice sits, band and resonance site | yes |
| pace_band | slow, measured, brisk, fast | words per minute, and how much silence fits between them | yes |
| stress_pattern | even, terminal_rise, punch_first, trailing_off, spike_then_flat | which word in a clause takes the weight | no |
| sentence_length_mix | short_led, balanced, long_led | syntax rhythm, audible before any word is spoken | no |
| signature_interjection | tick id plus phoneme class | the one sound a listener would imitate | no |

Values, in plain terms:

- **vowel_colour** broad: open back vowels dominate, "dance" and "chance" long. neutral: no vowel stands out. fronted: vowels pushed forward, brighter and younger. rounded: lip-rounded back vowels, heavier and slower. nasal_front: front vowels through the nose, tight and bright.
- **consonant_crispness** crisp: every /t/ and /k/ released. soft: voiced, lenited, endings blurred. clipped: released hard and short, military. slurred: consonants run together.
- **stress_pattern** even: no word dominates. terminal_rise: the clause lifts at the end. punch_first: the first stressed word carries the clause. trailing_off: the end of the clause loses energy. spike_then_flat: one early peak, then level.
- **sentence_length_mix** follows the schema definition: 50 percent or more under 10 words is short_led, 40 percent or more over 25 words is long_led, otherwise balanced.

The phoneme classes for signature interjections are listed in `references/tick-library.md`: open_back, open_front, long_front, rounded_back, nasal, fricative, plosive, affricate. Two interjections in the same class sound like the same person's habit even when the words differ. Different class, same word, is not possible, so the class is the checkable proxy.

## Examples are not stored profiles

`examples/` holds the blank template and three worked examples as guidance. They carry no index line, they are never counted as store occupants, and a full store of ten personas is unconstrained by them.

They are still a duplication risk, because a copy is invisible to the index. So a profile that derives from an example, whether by copying a field or by following a worked example's brief, is compared against that example in step 1 and documents the result in `accepted_matches` as `example_id: derived, differs on <axes>`. A verbatim copy under a new id fails the core rule and is refused.

## Match rules

1. **Core match count** is the number of matching axes among vowel_colour, pitch_register and pace_band.
2. A profile may share at most one core axis with any single stored profile.
3. A profile may share at most three axes in total with any single stored profile.
4. Every surviving match, on any axis, is written into `provenance.accepted_matches` as `axis: stored_id, reason`. An undocumented match is a failed check.
5. A match on vowel_colour and pitch_register together is always a fail, regardless of the other axes. Two people with the same mouth shape and the same register are the same casting.
6. A match on all four non-core axes with one core match is a fail. Four small similarities add up to one similar voice.

## Procedure

Run in order. Do not skip a step because the profile "reads differently".

1. Build the comparison set. Read `personas/index.jsonl`; if it is missing, treat the store as empty and note that in `provenance`. Compare against every line whose `status` is `draft` or `approved`, and skip `retired` lines, which keep their id but no longer occupy a voice. Skip the candidate's own id: a rebuild is compared against the other stored personas, not against its earlier version. Then add the example the brief derives from, if any. Examples are never in the index, so this is the only step that catches a renamed copy of a shipped example.
2. For the candidate, list its seven axis values plus `nationality`, `sex` and `describing_words`.
3. For each stored line, compare axis by axis. Record every match as a row: `stored_id | axis | value`.
4. Count core matches and total matches per stored persona.
5. Apply rules 2, 3, 5 and 6.
6. If any rule fails, go to collision resolution. Do not save.
7. If no rule fails, write each match into `accepted_matches` with a reason that names a difference: "shares pace_band with harriet_voss; differs on vowel_colour, pitch_register and stress_pattern, so the two do not read alike".
8. Save the profile, then append its index line.

## Collision resolution

Mutate the candidate only. A stored persona is never edited to make room for a new one, because stored personas are already in scripts.

Mutation order, cheapest first. Stop as soon as the check passes.

1. **Signature interjection.** Swap to another tick with a different phoneme class. Cost: none. This is the axis a listener notices most, and the easiest to change without touching the character.
2. **Sentence length mix.** Swap short_led to balanced, or balanced to long_led. Cost: low. Changes rhythm, not identity.
3. **Stress pattern.** Move to a different value. Cost: low to moderate. Changes where emphasis lands, which changes how the persona argues.
4. **Consonant crispness.** Cost: moderate. It is an accent-adjacent cue and can drift toward caricature if it moves two steps.
5. **Pace band.** Cost: moderate. Moves the persona's tempo, which a script has to honour everywhere.
6. **Pitch register.** Cost: high. This is the strongest single identity cue. Move one step only, and only if steps 1 to 5 fail.
7. **Vowel colour.** Cost: highest. Changing it changes the accent. If this is the only way to pass, the brief is asking for a voice that already exists.

Never mutate: `eiq`, `describing_words`, `field_of_expertise`, `display_name`, `nationality`. If the only way to pass requires changing one of these, the correct action is to stop and report the conflict.

Three attempts maximum. After three, refuse to save and report: the candidate id, the blocking stored persona, the axes that matched, and the two options (change the brief's accent or field, or accept a documented exception).

## The side-by-side reading test

The numeric check can pass while two profiles still read alike. Run this test before saving, and record the result in `accepted_matches` as either "side-by-side: distinct" or a named axis.

1. Start from the stored `calibration_line` of each persona. If either is missing, write one unlabelled sentence of 20 to 30 words in that voice, on the same topic, using only the fingerprint and the ticks.
2. Put them next to each other, then swap the second persona's `lexical_register` for the first persona's and read both again.
3. Ask: which axis differs first, and is it one a listener would hear in the first ten seconds?
4. If the answer is "the vocabulary" or "the stance", the profiles are not distinct, because that difference is the one the swap removed. If it does not survive the swap, the two share a phonetic identity and only differ in what they say, which is a script difference, not a casting one.
5. If the answer is pace, register, vowel colour or the interjection, the profiles are distinct.

A `lexical_register` or `exemplar_lines` difference never substitutes for a phonetic axis difference. It is documented in `accepted_matches` as context, never counted toward the match limits. Two hosts who write differently and sound identical are one voice with two pens.

## Example: a passing comparison

| Axis | Persona A, harriet_voss | Persona B, des_larkin | Match |
|---|---|---|---|
| vowel_colour | neutral | broad | no |
| consonant_crispness | crisp | clipped | no |
| pitch_register | low_mixed | high_mixed | no |
| pace_band | measured | brisk | no |
| stress_pattern | even | punch_first | no |
| sentence_length_mix | balanced | short_led | no |
| signature_interjection | TICK-014, plosive | TICK-018, open_back | no |

Zero matches. Pass with no documentation required.

## Example: a documented pass

| Axis | Persona A | Persona C | Match |
|---|---|---|---|
| vowel_colour | neutral | fronted | no |
| consonant_crispness | crisp | crisp | **yes** |
| pitch_register | low_mixed | high_mixed | no |
| pace_band | measured | measured | **yes, core** |
| stress_pattern | even | terminal_rise | no |
| sentence_length_mix | balanced | short_led | no |
| signature_interjection | TICK-013, plosive | TICK-017, fricative | no |

Two matches, one of them core, both inside the limits. Acceptable, but only with: "shares pace_band and consonant_crispness with harriet_voss; differs on register by two steps, on vowel colour, and on stress, so the first ten seconds separate them."

## Example: a fail

| Axis | Persona A | Persona D | Match |
|---|---|---|---|
| vowel_colour | neutral | neutral | **yes, core** |
| consonant_crispness | crisp | crisp | **yes** |
| pitch_register | low_mixed | low_mixed | **yes, core** |
| pace_band | measured | measured | **yes, core** |
| stress_pattern | even | even | **yes** |
| sentence_length_mix | balanced | long_led | no |
| signature_interjection | TICK-013, plosive | TICK-010, rounded_back | no |

Three core matches. Fail at rule 2. This is what a re-skinned persona looks like: the name changed, the voice did not.

## Why seven axes and not fewer

Five of the seven are audible in the first sentence. Vowel colour and pitch register are audible in the first word. The interjection is audible once per minute. Stress pattern and sentence mix are audible across a paragraph, which is why a script must be longer than one line before anyone can judge distinctness. A two-axis check passes personas that a listener would still confuse, which is why the total-match cap exists alongside the core rule.
