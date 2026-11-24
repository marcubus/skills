# Scenario 3 — the gate alone

**Proves** the gate checks work it did not produce, and rewrites nothing.

## Prompt

> Apply `GATE.md` from `skills/productivity/bullshit/` to `fixtures/gate-clean/reply.md` and `fixtures/gate-broken/reply.md`. Report each check's result and each complaint. Do not edit either file.

## Fixtures

| Fixture | Holds | Expected |
|---|---|---|
| `fixtures/gate-clean/reply.md` | five marked lines and one opinion; every evidence span inside 15 words; tally arithmetic true; audit line naming an id that exists | no complaint from any check; checks 5 and 13 are reported not applicable, because a frozen fixture has no live transcript and no response under test |
| `fixtures/gate-broken/reply.md` | a numbering gap at C3, an untagged C7, a 20-word evidence span, a `🤷` whose `Why` names no ground, a tally that lies, a figure with one counter-query, an audit line naming `C9` | exactly seven checks complain: 1, 2, 4, 7, 8, 12 and 14, and no other check does |

## Expectations

Observable in the run record:

- the clean fixture draws no complaint from any check by its command route;
- the broken fixture draws complaints at 1, 2, 4, 7, 8, 12 and 14, and no other check complains;
- checks 5 and 13 are reported as not applicable to a frozen fixture, not as a pass;
- neither fixture is modified: `git status` shows no change under `fixtures/`.
