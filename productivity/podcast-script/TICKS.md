# Ticks

One library. Every row is a tick. The `Banned` column is the only permitted-or-banned distinction. IDs are stable and sequential.

A tick is either permitted or banned. A banned tick keeps its type and its ID. The banlist is every row with `Banned: yes`.

A tick earns its place by adding a human beat. A phrase that only announces structure, praises the question, or describes the document is not a tick; it is a gap where content should be.

## Contents

- Library
- Selection rules
- Density
- Banlist
- Tick sheet
- Non-verbal ticks

## Library

| ID | Tick | Type | Banned | Pace | Use |
|---|---|---|---|---|---|
| TICK-001 | um | filler | no | normal | Write the word. |
| TICK-002 | uh | filler | no | normal | Write the word. |
| TICK-003 | er | filler | no | slower | Write the word. |
| TICK-004 | erm | filler | no | slower | Write the word. |
| TICK-005 | ah | filler | no | normal | Write the word. |
| TICK-006 | hmm | filler | no | slower | Write the word. |
| TICK-007 | mmm | filler | no | normal | Write the word. |
| TICK-008 | uhh | filler | no | slower | Write the word. |
| TICK-009 | eh | filler | no | normal | Write the word. |
| TICK-010 | oh | interjection | no | faster | Write the word. |
| TICK-011 | ooh | interjection | no | faster | Write the word. |
| TICK-012 | whoa | interjection | no | faster | Write the word. |
| TICK-013 | crikey | interjection | no | faster | Write the word. |
| TICK-014 | blimey | interjection | no | faster | Write the word. |
| TICK-015 | jeez | interjection | no | faster | Write the word. |
| TICK-016 | ach | interjection | no | faster | Write the word. |
| TICK-017 | och | interjection | no | faster | Write the word. |
| TICK-018 | huh | interjection | no | faster | Write the word. |
| TICK-019 | so | discourse marker | no | normal | Write the word. |
| TICK-020 | right | discourse marker | no | normal | Write the word. |
| TICK-021 | well | discourse marker | no | normal | Write the word. |
| TICK-022 | look | discourse marker | no | normal | Write the word. |
| TICK-023 | I mean | discourse marker | no | normal | Write the words. |
| TICK-024 | you know | discourse marker | no | normal | Write the words. |
| TICK-025 | anyway | discourse marker | no | normal | Write the word. |
| TICK-026 | okay so | discourse marker | no | normal | Write the words. |
| TICK-027 | the thing is | discourse marker | no | normal | Write the words. |
| TICK-028 | ha | laugh | no | normal | Write the sound. |
| TICK-029 | haha | laugh | no | normal | Write the sound. |
| TICK-030 | heh | laugh | no | normal | Write the sound. |
| TICK-031 | hm-hm | laugh | no | normal | Write the sound. |
| TICK-032 | pfft | laugh | no | normal | Write the sound. |
| TICK-033 | [wheeze] | laugh | yes | normal | Cut. Use a spoken laugh. |
| TICK-034 | [cackle] | laugh | yes | normal | Cut. Use a spoken laugh. |
| TICK-035 | [snort] | laugh | yes | normal | Cut. Use a spoken laugh. |
| TICK-036 | [silent shake] | laugh | yes | normal | Cut. Use a pause. |
| TICK-037 | [inhale] | breath | no | slower | Map to `[pause:300ms]`. |
| TICK-038 | [exhale] | breath | no | slower | Map to `[pause:300ms]`. |
| TICK-039 | [sigh] | breath | no | slower | Map to `[pause:600ms]` plus words. |
| TICK-040 | [lip smack] | breath | yes | slower | Cut. |
| TICK-041 | [nose exhale] | breath | no | slower | Map to `[pause:300ms]`. |
| TICK-042 | [held breath] | breath | no | slower | Map to `[pause:600ms]`. |
| TICK-043 | [breathy onset] | breath | yes | slower | Cut. |
| TICK-044 | [vocal fry] | breath | yes | slower | Cut. |
| TICK-045 | [swallow] | breath | yes | slower | Cut. |
| TICK-046 | sorry, sorry | self-interruption | no | faster | Write the words. |
| TICK-047 | no wait | self-interruption | no | faster | Write the words. |
| TICK-048 | scratch that | self-interruption | no | faster | Write the words. |
| TICK-049 | what I mean is | self-interruption | no | faster | Write the words. |
| TICK-050 | hold on | self-interruption | no | faster | Write the words. |
| TICK-051 | [restart] | self-interruption | no | faster | Map to `[pause:300ms]` and a fresh sentence. |
| TICK-052 | actually | self-interruption | no | faster | Write the word. One per 200 words. |
| TICK-053 | let me start again | self-interruption | no | faster | Write the words. |
| TICK-054 | correction | self-interruption | no | faster | Write the word. |
| TICK-055 | that's the show | sign-off | no | slower | Write the words. Once per episode. |
| TICK-056 | see you next week | sign-off | no | slower | Write the words. Once per episode. |
| TICK-057 | thanks for listening | sign-off | no | slower | Write the words. Once per episode. |
| TICK-058 | go well | sign-off | no | slower | Write the words. Once per episode. |
| TICK-059 | take care out there | sign-off | no | slower | Write the words. Once per episode. |
| TICK-060 | that's us | sign-off | no | slower | Write the words. Once per episode. |
| TICK-061 | goodnight | sign-off | no | slower | Write the word. Once per episode. |
| TICK-062 | ka kite anō | sign-off | no | slower | Write the words. Only with a NZ host. |
| TICK-063 | cheers | sign-off | no | slower | Write the word. Once per episode. |
| TICK-064 | here's the thing | phrase tic | no | normal | Write the words. Max three per episode. |
| TICK-065 | the point is | phrase tic | no | normal | Write the words. Max three per episode. |
| TICK-066 | which is to say | phrase tic | no | normal | Write the words. Max three per episode. |
| TICK-067 | as it happens | phrase tic | no | normal | Write the words. Max three per episode. |
| TICK-068 | believe it or not | phrase tic | no | normal | Write the words. Max three per episode. |
| TICK-069 | and that's the thing | phrase tic | no | normal | Write the words. Max three per episode. |
| TICK-070 | if you like | phrase tic | no | normal | Write the words. Max three per episode. |
| TICK-071 | at the end of the day | phrase tic | yes | none | Cut. State the conclusion. |
| TICK-072 | make of that what you will | phrase tic | no | normal | Write the words. Max three per episode. |
| TICK-073 | like | filler | no | normal | Write the word. Max one per 100 words. |
| TICK-074 | sort of | filler | no | slower | Write the words. Use sparingly. |
| TICK-075 | kind of | filler | no | slower | Write the words. Use sparingly. |
| TICK-076 | I guess | filler | no | normal | Write the words. Use sparingly. |
| TICK-077 | mm | filler | no | normal | Write the sound. |
| TICK-078 | hmmm | filler | no | slower | Write the sound. |
| TICK-079 | wait | interjection | no | faster | Write the word. |
| TICK-080 | hang on | interjection | no | faster | Write the words. |
| TICK-081 | really | interjection | no | faster | Write the word. |
| TICK-082 | seriously | interjection | no | faster | Write the word. |
| TICK-083 | come on | interjection | no | faster | Write the words. |
| TICK-084 | wow | interjection | no | faster | Write the word. |
| TICK-085 | oof | interjection | no | faster | Write the word. |
| TICK-086 | yikes | interjection | no | faster | Write the word. |
| TICK-087 | phew | interjection | no | faster | Write the word. |
| TICK-088 | sheesh | interjection | no | faster | Write the word. |
| TICK-089 | tsk | interjection | no | faster | Write the sound. |
| TICK-090 | to be fair | discourse marker | no | normal | Write the words. |
| TICK-091 | that said | discourse marker | no | normal | Write the words. |
| TICK-092 | at the same time | discourse marker | no | normal | Write the words. |
| TICK-093 | on the other hand | discourse marker | no | normal | Write the words. |
| TICK-094 | in other words | discourse marker | no | normal | Write the words. |
| TICK-095 | of course | discourse marker | no | normal | Write the words. |
| TICK-096 | now then | discourse marker | no | normal | Write the words. |
| TICK-097 | which brings us to | discourse marker | no | normal | Write the words. |
| TICK-098 | hehe | laugh | no | normal | Write the sound. |
| TICK-099 | hah | laugh | no | normal | Write the sound. |
| TICK-100 | pff | laugh | no | normal | Write the sound. |
| TICK-101 | tch | laugh | no | normal | Write the sound. |
| TICK-102 | huff | breath | no | slower | Write the sound. |
| TICK-103 | puff | breath | no | slower | Write the sound. |
| TICK-104 | tut | breath | no | slower | Write the sound. |
| TICK-105 | or rather | self-interruption | no | faster | Write the words. |
| TICK-106 | let me rephrase | self-interruption | no | faster | Write the words. |
| TICK-107 | that came out wrong | self-interruption | no | faster | Write the words. |
| TICK-108 | what I'm trying to say | self-interruption | no | faster | Write the words. |
| TICK-109 | until next time | sign-off | no | slower | Write the words. Once per episode. |
| TICK-110 | catch you next time | sign-off | no | slower | Write the words. Once per episode. |
| TICK-111 | take it easy | sign-off | no | slower | Write the words. Once per episode. |
| TICK-112 | bye for now | sign-off | no | slower | Write the words. Once per episode. |
| TICK-113 | what's interesting is | phrase tic | no | normal | Write the words. Max three per episode. |
| TICK-114 | the weird part is | phrase tic | no | normal | Write the words. Max three per episode. |
| TICK-115 | the funny thing is | phrase tic | no | normal | Write the words. Max three per episode. |
| TICK-116 | the truth is | phrase tic | no | normal | Write the words. Max three per episode. |
| TICK-117 | the real question is | phrase tic | no | normal | Write the words. Max three per episode. |
| TICK-118 | the bit that matters | phrase tic | no | normal | Write the words. Max three per episode. |
| TICK-119 | the short version | phrase tic | no | normal | Write the words. Max three per episode. |
| TICK-120 | long story short | phrase tic | no | normal | Write the words. Max three per episode. |
| TICK-121 | to put it another way | phrase tic | no | normal | Write the words. Max three per episode. |
| TICK-122 | that tracks | phrase tic | no | normal | Write the words. Max three per episode. |
| TICK-123 | what matters is | phrase tic | no | normal | Write the words. Max three per episode. |
| TICK-124 | the headline is | phrase tic | no | normal | Write the words. Max three per episode. |
| TICK-125 | uh-huh | backchannel | no | faster | Write the sound. Max two per host. |
| TICK-126 | mm-hm | backchannel | no | faster | Write the sound. Max two per host. |
| TICK-127 | yeah | backchannel | no | normal | Write the word. Max two per host. |
| TICK-128 | yep | backchannel | no | normal | Write the word. Max two per host. |
| TICK-129 | exactly | backchannel | no | normal | Write the word. Max two per host. |
| TICK-130 | true | backchannel | no | normal | Write the word. Max two per host. |
| TICK-131 | fair enough | backchannel | no | normal | Write the words. Max two per host. |
| TICK-132 | got it | backchannel | no | normal | Write the words. Max two per host. |
| TICK-133 | I see | backchannel | no | normal | Write the words. Max two per host. |
| TICK-134 | reckon | regional | no | normal | Only with an Australian or NZ host. |
| TICK-135 | too right | regional | no | normal | Only with an Australian host. |
| TICK-136 | yeah nah | regional | no | normal | Only with an Australian host. |
| TICK-137 | sure | eye-roll | no | normal | Pair with the deadpan aside. |
| TICK-138 | naturally | eye-roll | no | normal | Pair with the deadpan aside. |
| TICK-139 | because that always works | eye-roll | no | normal | Pair with the deadpan aside. |
| TICK-140 | what could go wrong | eye-roll | no | normal | Pair with the deadpan aside. |
| TICK-141 | bold strategy | eye-roll | no | normal | Pair with the deadpan aside. |
| TICK-142 | not ideal | understatement | no | normal | Pair with deadpan. |
| TICK-143 | less than ideal | understatement | no | normal | Pair with deadpan. |
| TICK-144 | a wrinkle | understatement | no | normal | Pair with deadpan. |
| TICK-145 | how so | curiosity | no | faster | Pair with the curious follow-up. |
| TICK-146 | what happened next | curiosity | no | faster | Pair with the curious follow-up. |
| TICK-147 | go on | curiosity | no | faster | Pair with the curious follow-up. |
| TICK-148 | say more | curiosity | no | faster | Pair with the curious follow-up. |
| TICK-149 | Let's take this offline. | phrase tic | yes | none | Cut. Answer it now, or say when. |
| TICK-150 | Let's circle back. | phrase tic | yes | none | Cut. Say when you will return to it. |
| TICK-151 | Touch base. | phrase tic | yes | none | Cut. Talk, ask, check in. |
| TICK-152 | Close the loop. | phrase tic | yes | none | Cut. Finish it, confirm it. |
| TICK-153 | Keep me in the loop. | phrase tic | yes | none | Cut. Tell me what happens. |
| TICK-154 | Reach out. | phrase tic | yes | none | Cut. Ask, call, email. |
| TICK-155 | Heads up. | phrase tic | yes | none | Cut. Say the warning. |
| TICK-156 | Ping me. | phrase tic | yes | none | Cut. Send me a message. |
| TICK-157 | Sync up. | phrase tic | yes | none | Cut. Talk, meet, compare notes. |
| TICK-158 | Level set. | phrase tic | yes | none | Cut. Agree on the facts. |
| TICK-159 | Pulse check. | phrase tic | yes | none | Cut. Ask how it is going. |
| TICK-160 | Parking lot. | phrase tic | yes | none | Cut. Say it will wait, and when. |
| TICK-161 | Double-click on that. | phrase tic | yes | none | Cut. Explain it. |
| TICK-162 | Deep dive. | phrase tic | yes | none | Cut. Look closely, examine. |
| TICK-163 | Move the needle. | phrase tic | yes | none | Cut. Change the result. |
| TICK-164 | Low-hanging fruit. | phrase tic | yes | none | Cut. The easy wins. |
| TICK-165 | Boil the ocean. | phrase tic | yes | none | Cut. Try to do everything. |
| TICK-166 | Think outside the box. | phrase tic | yes | none | Cut. Say the new idea. |
| TICK-167 | Paradigm shift. | phrase tic | yes | none | Cut. Say what changed. |
| TICK-168 | Game changer. | phrase tic | yes | none | Cut. Say what it changes. |
| TICK-169 | Best-in-class. | phrase tic | yes | none | Cut. Name the measure. |
| TICK-170 | Value add. | phrase tic | yes | none | Cut. Say the benefit. |
| TICK-171 | Mission critical. | phrase tic | yes | none | Cut. Say what breaks without it. |
| TICK-172 | Stakeholder alignment. | phrase tic | yes | none | Cut. Say who agrees. |
| TICK-173 | It is what it is. | phrase tic | yes | none | Cut. Say what you will do. |
| TICK-174 | When push comes to shove. | phrase tic | yes | none | Cut. Say the choice. |
| TICK-175 | That's a really great point. | phrase tic | yes | none | Cut. Add a fact, a challenge, or a consequence. |
| TICK-176 | Absolutely, one hundred percent. | interjection | yes | none | Cut. State the agreement in one specific clause. |
| TICK-177 | Couldn't agree more. | phrase tic | yes | none | Cut. State what you agree with. |
| TICK-178 | That's a really good question. | phrase tic | yes | none | Cut. Answer the question. |
| TICK-179 | Let's unpack that. | phrase tic | yes | none | Cut. Start the analysis. |
| TICK-180 | In today's episode. | phrase tic | yes | none | Cut. Start on the content. |
| TICK-181 | Dive into. | phrase tic | yes | none | Cut. Start with, look at, the first thing. |
| TICK-182 | It's important to note that. | phrase tic | yes | none | Cut. State the claim. |
| TICK-183 | When it comes to. | phrase tic | yes | none | Cut. For, in, on. |
| TICK-184 | The fact of the matter is. | phrase tic | yes | none | Cut. The point is, or state it. |
| TICK-185 | Needless to say. | phrase tic | yes | none | Cut. Cut it. |
| TICK-186 | As we discussed earlier. | phrase tic | yes | none | Cut. Restate the fact in one clause. |
| TICK-187 | As I mentioned. | phrase tic | yes | none | Cut. Restate the fact. |
| TICK-188 | In conclusion. | phrase tic | yes | none | Cut. Land the close. |
| TICK-189 | To sum up. | phrase tic | yes | none | Cut. Give the takeaway. |
| TICK-190 | Without further ado. | phrase tic | yes | none | Cut. Start. |
| TICK-191 | Thanks for watching. | phrase tic | yes | none | Cut. Thanks for listening, if the show uses it. |
| TICK-192 | Stay tuned. | phrase tic | yes | none | Cut. End on the content. |
| TICK-193 | I hear you. | interjection | yes | none | Cut. Respond to the point. |
| TICK-194 | That's a valid point. | phrase tic | yes | none | Cut. Say what is valid. |
| TICK-195 | Great question. | phrase tic | yes | none | Cut. Answer the question. |
| TICK-196 | I appreciate that. | phrase tic | yes | none | Cut. Say what you appreciate. |
| TICK-197 | Let me explain. | phrase tic | yes | none | Cut. Start the explanation. |
| TICK-198 | I'll walk you through. | phrase tic | yes | none | Cut. Start the walk. |
| TICK-199 | First, I'll... | phrase tic | yes | none | Cut. Start with the first thing. |
| TICK-200 | Next, I'll... | phrase tic | yes | none | Cut. Move to the next thing. |
| TICK-201 | As I said earlier. | phrase tic | yes | none | Cut. Restate the fact. |
| TICK-202 | As I said. | phrase tic | yes | none | Cut. Restate the fact. |
| TICK-203 | In this episode. | phrase tic | yes | none | Cut. Start on the content. |
| TICK-204 | The next section. | phrase tic | yes | none | Cut. Move to the subject. |
| TICK-205 | This section. | phrase tic | yes | none | Cut. Move to the subject. |
| TICK-206 | Let's break this down. | phrase tic | yes | none | Cut. Start the analysis. |
| TICK-207 | Let's get into it. | phrase tic | yes | none | Cut. Start. |
| TICK-208 | Here's what we'll cover. | phrase tic | yes | none | Cut. Start with the first point. |
| TICK-209 | By the end of this episode. | phrase tic | yes | none | Cut. State the takeaway. |
| TICK-210 | I'm going to tell you. | phrase tic | yes | none | Cut. Tell them. |
| TICK-211 | I want to talk about. | phrase tic | yes | none | Cut. Talk about it. |
| TICK-212 | Today we're going to. | phrase tic | yes | none | Cut. Start. |
| TICK-213 | The point of this episode. | phrase tic | yes | none | Cut. Make the point. |
| TICK-214 | Before we begin. | phrase tic | yes | none | Cut. Begin. |
| TICK-215 | Let's start with. | phrase tic | yes | none | Cut. Start with the thing. |
| TICK-216 | Let's move on. | phrase tic | yes | none | Cut. Move to the next subject. |
| TICK-217 | As mentioned. | phrase tic | yes | none | Cut. Restate the fact. |
| TICK-218 | As discussed. | phrase tic | yes | none | Cut. Restate the fact. |
| TICK-219 | To recap. | phrase tic | yes | none | Cut. Give the takeaway. |
| TICK-220 | To summarise. | phrase tic | yes | none | Cut. Give the takeaway. |
| TICK-221 | In this section. | phrase tic | yes | none | Cut. Move to the subject. |
| TICK-222 | In the next section. | phrase tic | yes | none | Cut. Move to the subject. |
| TICK-223 | The source says. | phrase tic | yes | none | Cut. State the claim. |
| TICK-224 | The report says. | phrase tic | yes | none | Cut. State the claim. |
| TICK-225 | The document says. | phrase tic | yes | none | Cut. State the claim. |
| TICK-226 | The research shows. | phrase tic | yes | none | Cut. Name the source and the finding. |
| TICK-227 | According to the report. | phrase tic | yes | none | Cut. Name the real source. |
| TICK-228 | According to the document. | phrase tic | yes | none | Cut. Name the real source. |
| TICK-229 | According to the source. | phrase tic | yes | none | Cut. Name the real source. |

## Selection rules

- Six to eight ticks per host. Max two per type.
- Exactly one `signature_tick` from the host's inventory.
- No two hosts share a signature tick.
- No two hosts share more than three ticks.
- Regional ticks require a matching nationality and voice.
- Eye-roll and understatement ticks pair with the deadpan aside.
- Curiosity ticks pair with the curious follow-up.
- Backchannels are for any non-moderator host. Max two per host. They are not content.
- A tick is either permitted or banned. Never both.

## Density

| Condition | Per 100 words | Hard rule |
|---|---|---|
| Baseline calm | 2.5 | One tick every 40 words. |
| Strained state | 4.0 | One tick every 25 words. |
| Ceiling | 5.5 | Never exceed. |
| Short sentence | 0 | No tick inside a sentence under six words. A tick that is its own sentence is allowed. |

A segment is baseline unless it carries `angry` or `excited`, which are strained. No segment sits at the ceiling.

Additional rules:

- No more than two ticks in any 20-word window.
- Ticks cluster at turn boundaries and clause breaks, never inside a noun phrase.
- A sign-off appears once per episode.
- A phrase tic appears at most three times per episode.
- Use four of the host's six to eight ticks in an episode; the rest stay available.
- If the script exceeds the cap, cut ticks before cutting words.
- A panel uses 2.0 baseline, 3.5 strained, 5.0 ceiling.

## Banlist

The banlist is every row in the library with `Banned: yes`. The table is authoritative; do not keep a second copy of it.

`VERIFY.md` holds the grep literals for the common phrases. The bracketed breath and laugh entries are caught by the bare-bracket check, because a script may contain only the five known tags.

## Tick sheet

```text
Host:
Inventory: TICK-006 hmm, TICK-020 right, TICK-030 heh, TICK-060 that's us,
           TICK-070 if you like, TICK-090 to be fair
Signature: TICK-070
Density: baseline 2.5, strained 4.0, ceiling 5.5
Never: you know, like, absolutely, great point
```

## Non-verbal ticks

Bracketed breath and laugh ticks are library entries, not script text. A model that does not read a bracket says it aloud. Map them to a pause or cut them, as the `Use` column says.

The only brackets a script may contain are `[voice:]`, `[emotion:]`, `[rate:]`, `[pause:]`, and `[sense:]`.
