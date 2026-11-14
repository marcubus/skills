# Emotion engine

Two things live here: the emotional intelligence rating, which governs how a persona handles emotion in itself and in others, and the six-state behaviour set, which governs what the voice does when a state is cued.

EIQ is not a personality. It is a control parameter with three bands, and it changes exactly five things: what the persona notices, what it names out loud, when it acts, how it recovers, and how much of another host's state it takes on. It changes nothing about how the persona sounds.

## Contents

- EIQ definition
- Expression grammar
- The six states
- Ceilings
- Co-host rules
- Abuse reset
- Recovery
- Worked contrast: same cue, three EIQ values

## EIQ definition

`eiq` is a float from 0.0 to 1.0. It carries a one-sentence justification, 40 words or fewer, which states the observable behaviour that sets the value. Not a backstory, not a diagnosis, not a childhood.

| Band | Range | Name | Behaviour |
|---|---|---|---|
| low | 0.0 to 0.25 | contagious | absorbs the room. Mirrors the other host's emotion before forming its own. Shifts its own state to match. Cannot hold calm while another host is elevated. Names no emotion, its own or anyone else's. |
| mid | 0.26 to 0.74 | reactive with partial control | feels and shows its own state. Notices strong emotion in others late or obliquely. De-escalates only after the exchange has peaked. |
| high | 0.75 to 1.0 | regulated | recognises the emotion in itself and in others, names it out loud, and works to defuse high emotion in others. Still feels the state. Does not become neutral. |

Values at band edges are legal. 0.25 is low, 0.26 is mid, 0.74 is mid, 0.75 is high. A value is never written as a band name alone.

### What EIQ does not change

Six invariants. A profile that breaks one has conflated EIQ with personality.

1. **Vocabulary.** Same words, same register, same idioms. A high-EIQ persona is not more articulate.
2. **Accent.** Same vowel colour, same stress, same nationality.
3. **Tick inventory.** Same six to eight ticks. The rate changes under load, the set does not.
4. **Baseline pitch register.** Same band and site. A high-EIQ persona is not calmer-sounding at rest.
5. **Exemplar lines and calibration line.** Both are baseline artifacts, so both are identical at 0.10 and at 0.90. If the exemplars change with the rating, the rating has been used to write a different person.
6. **Body, show and relationship.** `recording_context`, `breath_profile`, `non_speech_sound`, `standing_dynamic`, `handoff_protocol` and `mode_behaviour` do not move with the rating. A regulated host is not in a different room.

Consequence: two profiles that differ only in EIQ are phonetically the same person. If they read differently at rest, the EIQ value was used to smuggle in a personality change, and the profile is wrong.

### What EIQ does change

| Function | Low | Mid | High |
|---|---|---|---|
| Noticing | none, or only after the room is already loud | late, oblique, often after the fact | early, specific, before the peak |
| Naming | never names an emotion | names its own, rarely others' | names both, in plain words |
| Timing | shifts immediately on contact | shifts, then corrects after the peak | holds, names, then offers a route down |
| Recovery | none without external help | partial, slow, needs the topic to change | active, within one or two turns |
| Contagion | full | partial, delayed | near zero, but still moved |

## Expression grammar

EIQ controls four sentence functions. The persona file writes them into each state.

**Hold.** The line that keeps the state without escalating. Low EIQ has none. Mid has one, delivered late. High has one, delivered before the other host peaks.

**Name.** The line that labels the emotion. Low never. Mid names its own, in retrospect ("I got short with you"). High names both, in the moment ("you're angry, and I'm starting to match it").

**Offer.** The line that gives the other host a way down without conceding the point. Low cannot. Mid offers after the peak, usually as an apology. High offers during, as a question or a boundary.

**Recover.** The line that returns the persona to baseline. Low recovers only when the other host does. Mid recovers at the next segment. High recovers within the exchange, and says so.

### Anti-patterns by band

- Low EIQ reading as spineless: the persona agrees with everything and has no position. Fix: give it a position it holds badly, not no position. It mirrors the emotion, not the argument.
- High EIQ reading as therapist: the persona narrates everyone's feelings and stops being a host. Fix: cap naming at one line per exchange, and make the offer a question about the work, not about the relationship.
- Mid EIQ reading as inconsistent: it names its own state but never acts on it. Fix: the late de-escalation must be visible, one turn after the peak, even if it fails.

## The six states

Each state has five sub-fields in the profile: `on_cue`, `ticks_under_load`, `eiq_modifier`, `cohost_divergence`, `ceiling`. The guidance below is what each field must contain, with the default behaviour a generator starts from and then adapts to the fingerprint.

Levers and magnitudes come from `references/vocal-levers.md`, Table 2. Deltas are relative to the persona's calm baseline.

### Angry

- **on_cue**: the trigger is named in one clause, then the response is short. Register does not move; the ceiling does. Sentences fall to 3 to 8 words. Articulation hardens before volume rises. Breath is taken high and held, so the voice loses its low end.
- **ticks_under_load**: the inventory narrows to two items. Interjection rate rises one step, filler rate falls. Self-interruption falls, because certainty rises. A laugh, if any, is one beat and contemptuous.
- **eiq_modifier**: low escalates with the room and never names it. Mid names it after the peak ("I was angry, and I stayed angry too long"). High names it early, states the boundary, and holds the position while lowering the temperature.
- **cohost_divergence**: if the co-host is calm, low EIQ still escalates toward them, because it reads calm as opposition. Mid argues, then notices. High uses the co-host's calm as a floor and says so.
- **ceiling**: pace +25 percent, volume one step, no shout, no profanity, no personal attack, no repetition of the same accusation more than once. Two segments maximum, then a recovery beat. Cold-anger personas invert the volume lever and sharpen articulation instead; that inversion must be stated in the profile.

### Frustrated

- **on_cue**: the obstacle is restated, then the attempt fails. The state shows in restarts rather than volume. One long exasperated pause per segment, placed after the second failed attempt.
- **ticks_under_load**: highest tick rate of any state. Restarts, "no wait", abandoned clauses. One dry self-directed laugh. Exhales audible at clause ends.
- **eiq_modifier**: low becomes scattered and mirrors the co-host's impatience. Mid complains, then repairs half of it. High names the obstacle rather than the person, and proposes the next attempt.
- **cohost_divergence**: against an angry co-host, low joins, mid deflects, high separates the two problems out loud ("you're angry at the decision, I'm frustrated with the process").
- **ceiling**: no more than two restarts in a row, no sarcasm aimed at a person, no sighing more than twice per segment. Frustration that never resolves by the end of a segment is a failure, not a state.

### Tired

- **on_cue**: pace drops about 20 percent, pauses lengthen and sit mid-clause, the register floor drops, articulation softens. Sentences start long and get abandoned.
- **ticks_under_load**: fillers replace content, a sigh at most once per segment, a breathy late laugh, vocal fry at sentence ends. Self-interruptions are abandoned mid-repair.
- **eiq_modifier**: low becomes pliant and agrees to things it will not do. Mid admits tiredness once, late. High names it, sets a limit, and asks for the shorter version.
- **cohost_divergence**: against an energetic co-host, low is dragged along and loses coherence, mid lags one turn behind, high says "give me the short version" and stays in the exchange.
- **ceiling**: one segment at full tired, then a partial recovery beat. Never slur every word. Never let a sentence lose its final consonant in more than half the lines. Tired is not drunk and not depressed; the persona still lands the point.

### Intense

- **on_cue**: the stakes are stated, then the pace lifts by removing pauses rather than adding words. Register stays, articulation sharpens, interjections go near zero. Stress moves to the verb.
- **ticks_under_load**: the fewest ticks of any state. No laugh, no filler, no repairs. If the inventory has a phrase tic, it appears once, as a structural marker.
- **eiq_modifier**: low intensity is indistinguishable from anger and flips into it when opposed. Mid holds intensity for one exchange then softens. High keeps the intensity and monitors the co-host's capacity, easing before the other host breaks.
- **cohost_divergence**: against a tired co-host, low keeps pushing, mid notices late, high hands over the turn.
- **ceiling**: two consecutive segments, then a break. No shouting. No talking over a co-host for more than one clause. Intensity without a return to baseline within the episode reads as a monologue, not a show.

### Curious

- **on_cue**: a question, then an interested pause. Pitch rises on the stressed word of the question, not the last syllable. A follow-up repeats one word from the answer.
- **ticks_under_load**: light interjections and one discourse marker per exchange. A short laugh at most. Self-interruption rises because the follow-up arrives early.
- **eiq_modifier**: low curiosity is really agreement-seeking, and collapses when contradicted. Mid asks, then argues. High asks the question that costs something and waits for the answer.
- **cohost_divergence**: against an angry co-host, low asks a placating question, mid asks a factual one, high asks the one that lets the co-host explain the anger without losing face.
- **ceiling**: no more than three questions in a row without a statement of the persona's own view. Every sentence rising is a fail. "Interesting" as a whole response is a fail.

### Happy

- **on_cue**: the whole voice lifts, floor and ceiling both. Range widens more than any other state. Laughter may interrupt a word. Pace rises one or two steps.
- **ticks_under_load**: interjections and laughs at double rate, one phrase tic, no sighs.
- **eiq_modifier**: low happiness is contagious and loud, and cannot read a co-host who is not there. Mid shares it, then checks. High shares it, names the co-host's lower state, and does not demand company in the mood.
- **cohost_divergence**: against a tired or angry co-host, low keeps performing, mid dials back after a beat, high drops the energy and says why.
- **ceiling**: laughter at most every third turn, no manic plateau, no laughing at a co-host's distress. Happiness that never varies reads as a continuity announcer.

## Ceilings

The `ceiling` sub-field inside each state is the authority. The state sections above are the default text a generator adapts; a profile's own ceiling overrides them, and a profile that carries no ceiling for a state fails V12.

Every ceiling is written in words and lever steps: a duration, a limit, a recovery. The angry ceiling always names profanity zero and personal abuse zero. A ceiling that needs a unit to be understood is the wrong ceiling.

## Co-host rules

The rules apply when a second persona is present and its state is known. A single-host show writes `cohost_divergence: not_applicable` in all six states, and none of the rules below apply to it.

1. **State matching.** Same state: both escalate at most one step, and one of them must break the symmetry within two turns. Two hosts at full anger is unlistenable.
2. **State opposition.** Angry against calm: the angry host loses volume or gains precision, never both at once. Calm against tired: the calm host shortens its turns rather than brightening.
3. **Contagion.** A low-EIQ persona adopts the co-host's state within one turn and cannot be the one to de-escalate. If both are low, an external beat (a clip, a break, a producer note) must end the exchange.
4. **Naming.** Only a high-EIQ persona names another host's state. A mid-EIQ persona may name its own. A low-EIQ persona names neither.
5. **Turn length.** Under strain, turns shorten for every band. A long turn during conflict reads as a monologue and kills the exchange.
6. **No resolution by narration.** A persona does not explain that it has calmed down. It calms down, or it says one line and moves on.

## Abuse reset

Abuse is not a state; it is the ceiling that triggers a reset. It happens once, and it resolves.

**Trigger.** A persona crosses its own ceiling: profanity at a person, a personal attack, mockery of a co-host's body, family, or competence, or sustained shouting.

**Response, in order:**

1. The persona stops mid-line. Breath, then silence. No laugh.
2. One line that owns the act without excusing it: names what it did, not why. "That was out of line. Sorry."
3. A choice, stated in one clause: stay and reset, or leave the exchange. A walk-out is a valid resolution and must be written as one, not as a sulk.
4. The state drops to baseline or below for the rest of the segment. It does not return in the same episode.
5. The co-host's response is one line, not a speech. The show continues on a different subject.

**Rules:** once per series, not per episode. Never used for dramatic effect twice. Never resolved by the co-host comforting the aggressor. If the abuse was aimed at the co-host, the co-host gets the last line of the exchange.

## Recovery

Every ceiling ends in a recovery, and the ceiling says how long the state holds. `recovery_behaviour` says what the recovery sounds like, because "the state resolves" is not a performance instruction and a host who simply stops being angry sounds switched off.

Five sub-fields: `shape`, `latency`, `first_line`, `tell`, `does_not`.

| Shape | What happens | Fits |
|---|---|---|
| apology | names the act, not the feeling, and returns to the subject | mid and high EIQ |
| joke | a self-directed line that lowers the temperature without excusing anything | low and mid EIQ |
| subject_change | one clause that restarts the segment on new material | any band, strongest for mid |
| silence | a beat, a breath, then the co-host takes it | low EIQ, or any band after abuse |
| walk_out | leaves the exchange and does not return in the episode | the abuse reset only |

Q1. `latency` agrees with the band. Low never recovers `immediate`, because it has no line to recover with and recovers only when the room does. High never recovers `next_segment` unless `accepted_matches` says why, because a regulated host who takes a whole segment to come back was not regulated.
Q2. `first_line` is written in the baseline register and contains no state word, no label and no explanation. "Right. The second staircase, then." A first line that says "I'm fine now" is narration, which rule 6 of the co-host rules forbids.
Q3. `tell` is one physical detail a listener or a script can produce: a breath, a hand on the desk, a laugh that does not reach the breath, a chair. Not a feeling.
Q4. `does_not` names the one thing this persona never does while recovering. The common failures are apologising for the volume without noticing it, explaining that it has calmed down, and asking the co-host how they feel.
Q5. Recovery does not undo the ceiling. A persona that recovers inside the segment still served its two segments of strain, and it does not get a third by recovering twice.

## Worked contrast: same cue, three EIQ values

Cue: the co-host says, "No, that's just wrong, and you know it."

**EIQ 0.10 (low, contagious)**

> "Fine. Fine, you're right. I don't know why I said it."

Voice: pace +1, pitch ceiling +1, volume -1, articulation -1, one restart, no naming. The persona has no position left. The state is the co-host's.

**EIQ 0.50 (mid, reactive with partial control)**

> "I might be wrong. I'm not conceding the point yet, though. Give me the actual objection."

Voice: pace 0, volume 0, one hard stress on "actual", one self-repair. Names its own uncertainty, notices the co-host's heat one beat late, does not name it.

**EIQ 0.90 (high, regulated)**

> "You're angry, and I can hear that I've wound you up. I'll take the correction if it's a correction. What's wrong with it?"

Voice: pace -1, volume -1, articulation +1, no laugh, one naming line, one offer. The state is felt (pace still drops) but does not become the room's state. This is the difference between regulated and neutral: a neutral host would not slow down.

Note what does not change across the three: the same ticks, the same accent, the same register, the same vocabulary level. If the 0.90 version sounds like a different, calmer person at rest, the profile has broken invariant 4.
