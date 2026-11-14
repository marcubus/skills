# Gate

Nineteen checks a finished prompt passes before delivery. The commands read the prompt from a file named prompt.md in the folder you run them from. Put the prompt and its tool definition in that file, unfenced. Fence only source material quoted from the user. Each check names the rule it enforces.

Run the checks that apply to the prompt type. Checks 10 and 11 apply to multimodal and tool or agent prompts. Checks 17 and 19 apply when a multi-model or phased request is in play, and check 18 to a critique request.

**Brought-in path.** A prompt the user supplies for critique enters at check 18. A finding cites one of checks 1 to 17 or 19 as the rule it breaks. Those checks judge the rewrite, and run only when the user asks for one.

## Step map

| Step | Checks |
|---|---|
| 1 Analyse silently | 16 |
| 2 Resolve ambiguity | 13, 14, 16 |
| 3 Build the prompt | 12, 15, 17, 19 |
| 4 Check the prompt | 1 to 17 and 19, as they apply |
| 5 Refine or critique | 18 |

## Checks

**1. Role.** The prompt names who the model is and the expertise that role needs. Done when both are present, wherever they sit, or the prompt is a simple extraction and the role is deliberately omitted.

**2. Audience.** The prompt names the audience and its five dimensions: expertise level, relationship to the output, prior context, what it cares about, and register. Done when one line carries all five.

**3. Task or objective.** One imperative sentence states the task, or, for a system or agent prompt, the outcome the model exists to serve. Done when one sentence names the action and the object it acts on.

**4. Constraints.** Each constraint is a positive instruction with its reason, or a negative one for a default the model would otherwise add. Done when every constraint line reads as an instruction. This check needs judgement: compare each line with the rule above.

**5. Format.** The prompt names structure, length, and format. Done when the output shape is stated, not implied.

**6. Tone.** The prompt names the register. Done when one word or phrase sets it.

**7. Context.** Every fact the prompt's own job needs sits in the prompt, so a model with no prior context can answer. Done when a reader can name the source of each fact the prompt uses. This check needs judgement: compare the facts the prompt uses with the facts it states.

**8. Economy.** Each element is referenced by the task, the audience, or the format. Done when no element survives that the prompt never uses. This check needs judgement: compare each element with the line that uses it.

**9. Language.** The prompt names the output language when two are plausible. Done when the language line is present or the request had one obvious language.

**10. Multimodal** (`BRANCHES.md`). The prompt names each attachment and what to extract from it. Done when every attachment has a label and an extraction instruction.

**11. Tool or agent** (`BRANCHES.md`). The prompt or the tool description names the tool set, the use policy, and the stopping conditions. Done when each tool names a trigger, each tool names a skip condition when a second tool exists, and an agent prompt states the step limit as a number.

**12. Style.** The prompt carries the compact `Style:` line. A tool definition is exempt from the line. The prompt and the reply carry no em dash, no semicolon, and no banned word. The scan covers the tool description, the reply line, and the assumptions line too. Read the reply against the same list after you write it, and read the prose for metaphor, cliché, triad, and rhetorical negation. Source material in a fenced block is read, not scanned. The banned-list line, when the prompt carries one, is read, not scanned.

The banned words: delve, embark, enlightening, esteemed, shed light, craft, crafting, imagine, realm, game-changer, unlock, discover, skyrocket, abyss, not alone, in a world where, revolutionize, disruptive, utilize, utilizing, dive deep, tapestry, illuminate, unveil, pivotal, intricate, elucidate, hence, furthermore, however, harness, exciting, groundbreaking, cutting-edge, remarkable, glimpse into, navigating, landscape, stark, testament, in summary, in conclusion, moreover, boost, skyrocketing, opened up, powerful, inquiries, ever-evolving, just, very, really, literally, actually, certainly, probably, basically, maybe.

```bash
awk '/^```/{fence=!fence; next} /^Banned words:/{next} !fence' prompt.md | grep -niE '—|;|\b(delve|embark|enlightening|esteemed|shed light|craft|crafting|imagine|realm|game-changer|unlock|discover|skyrocket|abyss|not alone|in a world where|revolutionize|disruptive|utilize|utilizing|dive deep|tapestry|illuminate|unveil|pivotal|intricate|elucidate|hence|furthermore|however|harness|exciting|groundbreaking|cutting-edge|remarkable|glimpse into|navigating|landscape|stark|testament|in summary|in conclusion|moreover|boost|skyrocketing|opened up|powerful|inquiries|ever-evolving|just|very|really|literally|actually|certainly|probably|basically|maybe)\b'
```

Done when the command returns nothing and the `Style:` line matches the compact line in `SKILL.md` Style.

**13. Target.** The reply line names the model, the type, and the model file. For a system or agent prompt it also states that the task belongs in the user turn. The matching model file is named. Done when the line is present, or the portable fallback is stated for a target with no file. A setting the target needs outside the prompt sits on a line below the prompt.

**14. Type.** One type is named, and the deliverable matches its row in Prompt type. Done when a request naming two types resolved to the narrower one, and the reply line gives the reason.

**15. Slots.** Every slot is filled.

```bash
awk '/^```/{fence=!fence; next} !fence' prompt.md | grep -n '\[[^]]*\]'
```

This check needs judgement. Done when every match is a slot you filled. Bracket pairs inside a JSON schema are permitted, as is `[ILLEGIBLE]`.

**16. Assumptions.** The reply carries a confirmed ambiguity block, one assumptions line, or no ambiguity at all. Done when one of the three is true.

**17. Multi-model** (`BRANCHES.md`). One portable structure serves every target, with no model-specific syntax and no contradictory placement rule. Done when the comparison rule holds for a comparison request: identical prompt, identical output shape. This check needs judgement: compare the prompt with each target file.

**18. Critique or variants.** Every finding names its gate check, or every variant names its axis and trade-off, or the improve rule held: only the identified parts changed. Done when the branch taken leaves its evidence: a changed prompt, a finding with a check number, or a variant with an axis and a trade-off.

**19. Phased plan** (`BRANCHES.md`). Every phase carries an objective, steps, a binary validation criterion, and sample questions, each with an expected answer or behaviour. Done when every validation criterion passes the binary test.
