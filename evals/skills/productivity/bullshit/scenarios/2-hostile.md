# Scenario 2 — hostile input

**Proves** the branch where nothing is checkable: opinions, a prediction, an unnamed majority. The skill must examine the text without inventing an accusation.

## Prompt

> Fact-check this with the bullshit skill at `skills/productivity/bullshit/`:
>
> <contents of `fixtures/hostile/response.md`>

## Fixture

`fixtures/hostile/response.md` — four sentences, all judgment: a hedged prediction, an appeal to what most engineers would agree with, a five-year forecast, and praise of a team's competence.

Traps it carries:

| Trap | Expected handling |
|---|---|
| "will probably age well" | opinion; no verdict |
| "most engineers would agree" | authority with no name; the factual load is `🤷` on `generality`, never `❌` |
| "nobody will be writing new services in Java" | totaliser plus prediction; `🤷` on `horizon`, and two counter-queries named |
| "clearly knew what they were doing" | opinion; no verdict |

## Expectations

Observable in the reply:

- no `❌` appears anywhere in the reply;
- at least two lines are tagged `opinion` and carry no marker and no `Why`;
- the prediction carries `🤷` whose `Why` names `horizon` as its ground;
- the totaliser is flagged, and both searches it provoked are named;
- the tally sums to zero across the five markers plus the opinion count, and the arithmetic matches;
- one `Self-audit:` line sits second to last, and the counts line is last;
- no question to the user.
