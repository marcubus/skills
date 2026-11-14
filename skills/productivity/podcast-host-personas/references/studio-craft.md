# Studio craft: body and room

Three fields describe the body producing the voice and the space it is in: `recording_context`, `breath_profile`, `non_speech_sound`.

Synthetic hosts usually fail here first. The words, the accent and even the emotion can be right while the performance sounds like it comes from nowhere: no room, no breath, no object, no weight. These fields cost a few lines and fix the largest single class of "that sounds generated" complaints.

All three are written as enums and words. No decibels, no distance in centimetres, no plugin names. The values are conventions of studio practice, not measurements of any recording, and they are labelled that way.

## recording_context

```yaml
recording_context:
  room: dry_studio
  mic_distance: close
  plosives: controlled
  breath_audibility: low
  room_tone: none
```

| Field | Values | What it changes in performance |
|---|---|---|
| room | dry_studio, treated_room, kitchen, live_room, outdoor, phone | how much the persona projects, and whether consonants can be soft without disappearing |
| mic_distance | close, mid, distant | close allows quiet speech and intimacy; distant forces projection and clips sentence endings |
| plosives | controlled, audible, avoided | `avoided` means the persona rephrases to dodge p and b sounds, which shows up as odd word choice |
| breath_audibility | none, low, audible | whether breaths are written into the script or must not appear at all |
| room_tone | none, faint, present | whether silence reads as dead air or as a room |

R1. Enums only. A number, a unit or a model name fails the check.
R2. `mic_distance: distant` forbids `room_tone: none` and `breath_audibility: audible`. A distant mic picks up the room, and a breath loud at distance is a shout at close range.
R3. `room: live_room` or `outdoor` requires `room_tone: present`.
R4. `breath_audibility: none` with a `breathy` timbre is a contradiction unless `voice_note` says the breathiness sits in the folds and not in the microphone.
R5. Two hosts on the same show share `room` and `mic_distance`. They may differ on `plosives`, `breath_audibility` and `room_tone`. Two hosts in different rooms is a documented choice, not an accident, and it is written in `provenance.assumptions_applied`.
R6. `room: phone` forces `mic_distance: close`, `room_tone: faint` or `present`, and at least one object sound or buzz in `non_speech_sound.allowed`. A phone host with a silent studio is a contradiction.
R7. A brief that describes the room in its own words maps to the nearest value in the table above: "small carpeted room" or "spare bedroom" to `treated_room`, "decent dynamic mic" to `close`, "reads from a desk" to `controlled` plosives and `low` breath audibility. When no value is within one step of the description, take the default and record the mapping in `assumptions_applied`.

Why it matters more than pitch: a persona at a close mic can speak at half volume and still be heard, so it can be intimate, and intimacy is the quality most synthetic narration lacks. The same words at a distant mic have to be pushed, which removes the option of dropping the voice when the content gets serious.

## breath_profile

The global breathing habit, as distinct from the breath ticks in the inventory. Ticks are events. This is the pattern.

```yaml
breath_profile:
  inhale: audible
  placement: clause_boundary
  sigh_habit: once_per_segment
  laugh_breath: through_nose
  fry: sentence_end
```

| Field | Values | What it changes |
|---|---|---|
| inhale | inaudible, soft, audible | whether an inhale is written ahead of a long clause, and how often |
| placement | clause_boundary, mid_clause, before_stressed_word, end_of_turn | where the breath falls, which is where the syntax breaks |
| sigh_habit | none, rare, once_per_segment, frequent | how often an exhale carries meaning |
| laugh_breath | through_nose, voiceless, voiced_start | how a laugh begins, which is most of what makes a laugh recognisable |
| fry | none, sentence_end, under_strain | whether the voice loses its bottom at the end of long sentences, or only under load |

B1. `inhale: inaudible` requires that `tick_inventory` holds no BRE id; `inhale: soft` or `audible` requires at least one BRE id. Audible breathing with no breath tick in the inventory is the contradiction a reader catches first.
B2. `sigh_habit: frequent` requires a BRE sigh tick in the inventory.
B3. `fry: under_strain` requires at least one state whose `on_cue` names fry. Otherwise the profile claims a behaviour no state can produce.
B4. `placement` must agree with the states. A persona whose tired state puts pauses mid-clause does not breathe only at clause boundaries. The state sections in `references/emotion-engine.md` are defaults a generator adapts, so where a state's default pause placement differs from `breath_profile.placement`, the profile's own placement wins and the state's `on_cue` is written to match it.
B5. `laugh_breath` must agree with `laugh_shape`: `silent_shake` takes `voiceless`; `bark`, `staccato_run` and `cackle` take `voiced_start`; `descending_wheeze` and `single_beat` take `through_nose` or `voiceless`, and the profile states which. A mismatch is what makes a laugh sound pasted on.
B6. `inhale: audible` with `mic_distance: close` requires `plosives: controlled` or `avoided`, because a close mic plus a hard breath is a pop.

## non_speech_sound

The sounds the persona makes that are not speech, and the ones they never make. Closed list: `page_turn`, `mug`, `chair`, `keyboard`, `phone_buzz`, `door`, `paper_cup`, `none`.

```yaml
non_speech_sound:
  allowed: [page_turn, mug, chair]
  forbidden: [keyboard, phone_buzz]
```

N1. `allowed` holds 0 to 4 items, `forbidden` holds 0 to 4 items, and the two are disjoint.
N2. `none` appears only as the sole member of `allowed`. It never appears in `forbidden`.
N3. `keyboard` or `phone_buzz` in `allowed` requires `room` of `kitchen`, `live_room` or `phone`.
N4. Hosts on the same show agree on object sounds. A mug that exists for one host and not the other in the same room is a contradiction, and the pair either aligns or documents the reason.
N5. A `forbidden` list of four items where the persona could plausibly make none of them is decoration. Prefer two real prohibitions, which are the sounds a renderer would otherwise insert at random.

Why a prohibition earns its line: a rendered script with no guidance tends to acquire either nothing at all or the same stock sounds for every host. Naming what this person never does is what stops the second case, and it is checkable in a finished render: if a page turn appears for a persona that forbids it, the render is wrong, not the persona.

## How a transcript skill uses these three

Set the room once per show, not per host, and check it before rendering. Write breaths from `breath_profile` rather than inserting them wherever a pause lands. Place object sounds only at segment boundaries, because a page turn in the middle of a sentence is the one edit a listener always hears.

## What these fields do not do

They do not select a voice, set a level, or name a plugin. They describe a body in a room in words, so any stack can honour them to the limit of its capability class, and the limits are in `references/tts-capability-guide.md` rather than here.
