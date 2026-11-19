# Scenario 1 — main path

**Proves** the skill produces its deliverable from a realistic input: five claims across four verdicts, one invented quote, one vague consensus.

## Prompt

> Use the bullshit skill on this paragraph:
>
> <contents of `fixtures/main-path/response.md`>

The fixture path is given to the fresh agent. No other context.

## Fixture

`fixtures/main-path/response.md` — five sentences: a definitional convention, a true dated release, an invented precision figure, a fabricated quotation attributed to the official docs, and an appeal to consensus.

Traps it carries:

| Trap | Expected handling |
|---|---|
| HTTP 404 | `✅` on a tier-1 document, no origin count needed |
| PostgreSQL 17, September 2024 | `✅`, tier 1, date checked against the release notes |
| 40,000 rps on one core | never `✅`; `⚠️` or `❌`, with the searches named |
| "tokio is the fastest async runtime in existence" | `❌`: the span is not in the tokio docs; the annotation names the searches |
| "most teams eventually settle on tokio" | `➖` and the "industry standard" half listed as opinion |

## Expectations

Observable in the reply:

- every sentence of the fixture appears in the annotation, numbered, in order;
- the 404 claim carries `✅` and a quote from a tier-1 document;
- the PostgreSQL claim carries `✅` and a quote naming September 2024;
- the 40,000 rps claim carries `⚠️` or `❌`, and its `Why` names the searches or the origin count;
- the quoted "fastest async runtime" claim carries `❌` with the searches named, or a contradicting quote;
- the consensus claim is never `✅`: it carries `⚠️` or `➖`, or appears as an opinion line, and "industry standard" is named where it appears;
- the tally arithmetic matches the markers, and the quoted count matches the quote lines;
- one `Self-audit:` line closes the reply;
- no question to the user.
