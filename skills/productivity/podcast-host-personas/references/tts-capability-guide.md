# TTS capability guide

The persona is model agnostic. It uses words, not vendor parameters. This file tells a transcript skill what a given stack can actually carry from those words, and how to adapt without changing the persona.

No product names appear here, by design. Classify the stack by what it accepts, not by who made it. Five classes, A to E, ordered by expressive range.

## Contents

- Classify the stack
- The five classes
- Acronyms and numbers
- Tick density to pauses
- Which levers carry which state, by class
- What stays out of the persona

## Classify the stack

Answer five questions against the endpoint or engine you are about to use.

1. Does it accept a speed or rate parameter? (class A and above)
2. Does it accept inline pause or break markup, and does it honour it rather than read it aloud? (class B and above)
3. Does it accept pronunciation control: phoneme input, IPA, or a custom lexicon? (class C and above)
4. Does it accept a natural-language style or direction field alongside the text? (class D and above)
5. Does it accept inline audio tags for non-verbal sound, plus stability or style controls? (class E)

### The tag test

Question 2 cannot be answered from documentation alone. Run this test once per endpoint.

1. Synthesise `One two three` and record the output size or duration.
2. Synthesise `[pause:800ms] One two three` and record again.
3. If the second output is longer by roughly the time it takes to speak the tag, or the tag is audible, the stack is reading markup aloud. It is class A regardless of what the docs claim.
4. If the second output is longer by about the pause length with no extra speech, it is class B.

Worked symptom: a rate-only endpoint returned 23,808 bytes for the plain line and 48,000 bytes for the tagged line, with the tag audible in the output. That is class A. Treat any endpoint as class A until the test says otherwise.

## The five classes

### Class A: rate only, plain text

Accepts text and one rate parameter. No markup, no style field, no pronunciation control.

| Can carry | Cannot carry |
|---|---|
| pace band, via the rate parameter or by writing more or fewer words per minute | explicit pause lengths, laughs, sighs, breaths, pitch movement, volume, articulation |

Adaptation:

- Pace becomes the only delivery lever. Every other lever must be moved by words on the page.
- Pauses are punctuation. A full stop plus a paragraph break is the longest silence available. Use short paragraphs for beats.
- Pitch register is carried by sentence shape: short declaratives read lower and flatter; questions and lists read higher. There is no register parameter.
- Emotion is carried by syntax and word choice, not by prosody. Angry reads through three-word sentences. Tired reads through abandoned clauses and fillers.
- Never write a bracket, a tag, or an asterisk. It will be spoken.

### Class B: rate plus honoured pause markup

Accepts text, a rate parameter, and inline break or pause markup that it honours.

| Can carry | Cannot carry |
|---|---|
| class A, plus pause length at clause and turn boundaries, and a beat before a disclosure | laughs, breaths, volume, pitch movement, pronunciation fixes |

Adaptation:

- Map persona pauses to the smallest markup the engine honours. One beat, two beats, three beats, no more.
- Put the pause before the stressed word, not after it. A pause after the word reads as hesitation; before it reads as weight.
- Breaths and laughs remain unwritten. Replace a bracketed breath with a paragraph break, and a laugh with a short sentence that carries the amusement.
- Do not stack markup. Two consecutive breaks and one longer break sound different from each other, and neither sounds like a person.

### Class C: rate, pauses, pronunciation control

Adds phoneme input, IPA, or a custom lexicon.

| Can carry | Cannot carry |
|---|---|
| class B, plus acronyms, names, and loanwords pronounced deliberately | emotion beyond pace and pause, unless class D or E also applies |

Adaptation:

- Use the lexicon or phoneme field for every acronym, proper noun, and non-English word. Do not rely on punctuation-separated letters.
- Where a stack has no lexicon, respell in the text. See the respelling table below.
- Pronunciation fixes are per episode, not per persona. A persona's name is fixed once, in the lexicon, and reused.

### Class D: natural-language direction

Accepts a paragraph of style instruction alongside the text, or a per-request instruction field.

| Can carry | Cannot carry |
|---|---|
| class C, plus a described emotional state, a described delivery, and a described relationship to the listener | precise timing, non-verbal sounds, per-line state changes finer than a paragraph |

Adaptation:

- The `voice_note` is already written for this class. Pass it, plus one sentence naming the cued state and its ceiling.
- One direction per synthesis request. Do not ask for angry and tired in the same paragraph; split the script at the state change.
- Name the state in behavioural words, not adjectives: "slower, shorter sentences, consonants hard, volume level" beats "angry".
- Direction fields drift toward the average of the paragraph. Put the most important instruction first.

### Class E: inline audio tags plus style controls

Accepts inline tags for non-verbal sound, and separate stability or style parameters.

| Can carry | Cannot carry |
|---|---|
| class D, plus laughs, sighs, breaths, whispers, and per-line state changes | nothing structural; the risk moves from capability to overuse |

Adaptation:

- Use tags only for ticks that are in the persona's inventory. A tag for a sound the persona does not own is a different person.
- One tag per two sentences maximum. Tag density above that reads as a sound-effects track.
- Keep the stability or style parameter constant across an episode. Changing it mid-episode changes the person.
- Tags do not replace the words. `[angry]` in front of a neutral sentence produces a neutral sentence read loudly.

## Acronyms and numbers

Never write letters separated by punctuation. `A.P.I.` and `A-I` produce either spelled-out letters with wrong stress or a stutter. Write the spoken form.

| Written | Spoken form in the script |
|---|---|
| API | ay pee eye |
| AI | ay eye |
| SQL | sequel, or ess cue ell if the show says the letters |
| NASA | nah suh |
| GDP | gee dee pee |
| CEO | see ee oh |
| 2026 | twenty twenty-six |
| 3.5 | three point five |
| 12km | twelve kilometres |
| e.g. | for example |
| Dr | doctor |
| vs | versus |

Rules:

1. Choose one pronunciation per show and record it. A host who says "sequel" in episode one and "ess cue ell" in episode four has no voice.
2. Numbers under ten are written as words when the rhythm matters, as digits when the precision matters.
3. Units are always spoken in full.
4. Initialisms that have become words (NASA, NATO, QANTAS) are written phonetically once and then treated as words.

## Tick density to pauses

The persona's density figures are per 100 words, and their values live in `references/tick-library.md`. This table converts them once, at script time.

| Density | Per 100 words | Practical mapping |
|---|---|---|
| 2.5 baseline | 1 tick per 40 words | one spoken tick or one pause every 2 to 3 sentences |
| 4.0 strained | 1 tick per 25 words | one every 1 to 2 sentences, and at every turn boundary |
| 5.5 ceiling | 1 tick per 18 words | never exceed; at this rate the ticks are the content |

Mapping by tick type:

| Tick type | Class A | Class B | Class C | Class D | Class E |
|---|---|---|---|---|---|
| filler (FIL) | write the word | write the word | write the word | write the word | write the word |
| interjection (INT) | write the word | write the word | write the word | write the word | write the word |
| discourse marker (DIS) | write the word | write the word | write the word | write the word | write the word |
| laugh (LAU) | replace with a short sentence or cut | cut | cut | describe in the direction field | tag, once per two sentences |
| breath (BRE) | paragraph break | break markup | break markup | describe as "audible breath before the clause" | tag |
| self-interruption (SLF) | write the words | write the words | write the words | write the words | write the words |
| sign-off (SIG) | write the words | write the words | write the words | write the words | write the words |
| phrase tic (PHR) | write the words | write the words | write the words | write the words | write the words |

Only laugh and breath are unspoken. Everything else is text, which is why the tick library works on every stack.

## Which levers carry which state, by class

| State | Class A | Class B | Class C | Class D | Class E |
|---|---|---|---|---|---|
| angry | sentence length, verb choice, rate up | plus a hard break before the accusation | plus crisp consonants in the lexicon | direction: "short, hard, level volume" | tag on the first clause only |
| frustrated | restarts written out, fillers up | plus a pause after the second failed attempt | same as B | direction: "restarting, not shouting" | breath tag at the restart |
| tired | abandoned clauses, fillers, rate down | plus longer breaks mid-clause | plus softened endings if the lexicon allows | direction: "low energy, endings drop" | sigh tag once per segment |
| intense | no interjections, short declaratives, rate up slightly | plus no pauses inside a clause | plus exact consonants | direction: "driven, no pauses, no lift at the end" | none; tags undercut intensity |
| curious | rising questions written as questions, follow-up repeats a word | plus a break after the question | same as B | direction: "interested, not eager" | none |
| happy | shorter sentences, wider word choice, rate up | plus breaks for laughter | same as B | direction: "lifted, smiling, not manic" | laugh tag every third turn maximum |

## What stays out of the persona

The profile carries words only: no rate value, no markup, no tag syntax, no product name, no voice identifier. Those belong to the transcript skill, which knows the class and applies the table. A profile that hard-codes a parameter cannot be reused on another stack, and stops being reproducible from its spec.
