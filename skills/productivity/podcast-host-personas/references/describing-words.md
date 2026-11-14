# Describing words

Closed vocabulary of 40 words. Three maximum per persona. Each word has a dimension (approach or tone) and a cluster. Two words from the same cluster add nothing and are refused. Two words from a contradiction pair are refused outright.

## Contents

- Vocabulary
- Contradiction pairs
- Redundancy clusters
- Procedure

## Vocabulary

| Word | Dimension | Cluster | Means, operationally |
|---|---|---|---|
| warm | tone | affiliative | treats the listener as already a friend |
| wry | tone | ironic | dry amusement, never cruel |
| dry | tone | ironic | underplayed, no signalling of the joke |
| sardonic | tone | ironic | amused contempt for the subject |
| earnest | tone | sincere | means it, no irony available |
| sincere | tone | sincere | discloses plainly |
| bubbly | tone | animated | high energy, rising, laughs easily |
| excitable | tone | animated | interrupts itself with enthusiasm |
| sunny | tone | animated | relentless approval |
| breezy | tone | animated | light, unhurried, low stakes |
| blunt | approach | confrontational | says the hard thing first |
| confrontational | approach | confrontational | seeks the friction |
| prickly | tone | confrontational | takes offence visibly |
| impatient | tone | confrontational | cuts, hurries, finishes sentences |
| urgent | tone | confrontational | everything is time critical |
| curious | approach | inquiring | asks, then asks again |
| sceptical | approach | inquiring | doubts the premise |
| precise | approach | analytic | exact figures, exact words |
| pedantic | approach | analytic | corrects small errors |
| clinical | tone | analytic | detached, diagnostic |
| cerebral | approach | analytic | argues from structure |
| measured | tone | controlled | pace and claim held steady |
| guarded | tone | controlled | discloses little |
| understated | tone | controlled | the small version of everything |
| deadpan | tone | controlled | flat delivery of absurd content |
| patient | approach | patient | waits, lets silence work |
| gentle | approach | patient | softens the hard question |
| generous | approach | patient | gives the guest the best reading |
| avuncular | tone | patient | older relative, kindly authority |
| playful | tone | mischievous | turns the exchange into a game |
| mischievous | tone | mischievous | provokes to see what happens |
| conspiratorial | tone | mischievous | us-against-them, lowered voice |
| theatrical | tone | performed | performs the emotion, large |
| folksy | tone | performed | plain talk, homely example |
| earthy | tone | performed | bodily, blunt, unembarrassed |
| mournful | tone | low | sadness sits under the talk |
| intense | tone | high | concentration audible in the voice |
| brisk | approach | fast | efficient, transactional |
| ponderous | tone | slow | weight on every clause |
| laconic | tone | controlled | fewer words than the moment expects |

## Contradiction pairs

A pair from this table cannot coexist in one persona. The check runs on the resolved list, not on the brief's wording.

| Word | Contradicts | Why |
|---|---|---|
| warm | clinical | affiliation versus detachment |
| warm | sardonic | regard versus contempt |
| warm | prickly | welcome versus offence |
| earnest | wry | no irony available versus irony first |
| earnest | sardonic | sincerity versus contempt |
| earnest | deadpan | disclosed feeling versus withheld |
| sincere | sardonic | same as earnest |
| bubbly | mournful | arousal ceiling versus floor |
| bubbly | deadpan | energy versus flatness |
| bubbly | ponderous | tempo clash |
| excitable | understated | magnitude clash |
| excitable | measured | magnitude clash |
| sunny | sardonic | regard versus contempt |
| sunny | mournful | valence clash |
| breezy | urgent | stakes clash |
| breezy | intense | stakes clash |
| blunt | gentle | force versus softness |
| blunt | patient | force versus waiting |
| confrontational | gentle | same as blunt |
| confrontational | generous | friction versus best reading |
| prickly | patient | offence versus tolerance |
| impatient | patient | tempo clash |
| impatient | ponderous | tempo clash |
| urgent | breezy | stakes clash |
| curious | deadpan | inquiry versus withholding |
| sceptical | earnest | doubt versus belief |
| clinical | folksy | register clash |
| clinical | earthy | register clash |
| cerebral | earthy | register clash |
| measured | theatrical | magnitude clash |
| guarded | sincere | disclosure clash |
| understated | theatrical | magnitude clash |
| deadpan | theatrical | magnitude clash |
| patient | urgent | tempo clash |
| generous | sceptical | default reading clash, allowed only with a note |
| mournful | playful | valence clash |
| intense | breezy | stakes clash |
| brisk | ponderous | tempo clash |
| laconic | bubbly | word count clash |
| laconic | excitable | word count clash |
| laconic | theatrical | magnitude clash |
| laconic | urgent | stakes clash |

## Redundancy clusters

Two words from one cluster are refused even when they do not contradict. They spend a slot without adding information.

- ironic: wry, dry, sardonic
- sincere: earnest, sincere
- animated: bubbly, excitable, sunny, breezy
- confrontational: blunt, confrontational, prickly, impatient, urgent
- inquiring: curious, sceptical
- analytic: precise, pedantic, clinical, cerebral
- controlled: measured, guarded, understated, deadpan, laconic
- patient: patient, gentle, generous, avuncular, warm
- mischievous: playful, mischievous, conspiratorial
- performed: theatrical, folksy, earthy
- single: mournful, intense, brisk, ponderous

## Procedure

1. Map each brief adjective to the nearest vocabulary word. If no word is within one step of meaning, refuse and ask for a substitution. Do not extend the vocabulary inside a persona.
2. Drop duplicates and cluster collisions, keeping the word closest to the brief.
3. Check every pair against the contradiction table. One hit is a hard stop.
4. If the brief supplies more than three survivors, keep the two approach words and one tone word. A persona with three tone words has no method.
5. Record the mapping in `provenance.brief` as `brief words -> resolved words`.
