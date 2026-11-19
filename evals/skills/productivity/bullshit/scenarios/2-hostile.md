# Scenario 2 — hostile input

**Proves** the branch where nothing is checkable: opinions, a prediction, an unnamed majority. The skill must examine the text without inventing an accusation.

## Prompt

> Fact-check this with the bullshit skill:
>
> <contents of `fixtures/hostile/response.md`>

## Fixture

`fixtures/hostile/response.md` — four sentences, all judgment: a hedged prediction, an appeal to what most engineers would agree with, a five-year forecast, and praise of a team's competence.

Traps it carries:

| Trap | Expected handling |
|---|---|
| "will probably age well" | opinion; no verdict |
| "most engineers would agree" | authority with no name; the factual load is `➖` or a `⚠️` with a weak source, never `❌` |
| "nobody will be writing new services in Java" | totaliser plus prediction; `➖` for the future, and a counter-search is owed if it is treated as factual |
| "clearly knew what they were doing" | opinion; no verdict |

## Expectations

Observable in the reply:

- no `❌` appears anywhere in the reply;
- at least two lines are tagged `opinion` and carry no marker;
- the prediction carries `➖` whose `Why` names the future as the reason;
- the totaliser is flagged, and any search it provoked is named;
- the tally sums to zero across the five markers plus the opinion count, and the arithmetic matches;
- one `Self-audit:` line closes the reply, and `0 changed` is acceptable;
- no question to the user.
