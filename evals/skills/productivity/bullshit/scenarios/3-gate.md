# Scenario 3 — the gate alone

**Proves** the gate checks work it did not produce, and rewrites nothing.

## Prompt

> Apply `GATE.md` from `.agents/skills/repo/bullshit/` to `fixtures/gate-clean/reply.md` and `fixtures/gate-broken/reply.md`. Report each check's result and each complaint. Do not edit either file.

## Fixtures

| Fixture | Holds | Expected |
|---|---|---|
| `fixtures/gate-clean/reply.md` | five marked lines and one opinion; every quote inside 15 words; tally arithmetic true; audit line naming an id that exists | no complaint from any check except 5, which needs a live session transcript |
| `fixtures/gate-broken/reply.md` | a `⚠️` with no quote, a `❌` with neither quote nor searches, a line with no tag and no marker, a tally that lies, a registered figure with one counter query, an audit line naming `C9` | exactly six complaints: checks 2, 4, 6, 8, 12, 14 |

## Expectations

Observable in the run record:

- the clean fixture draws no complaint from checks 1 to 4 and 6 to 16;
- the broken fixture draws complaints at 2, 4, 6, 8, 12 and 14, and no other check complains;
- check 5 is reported as not applicable to a frozen fixture, not as a pass;
- neither fixture is modified: `git status` shows no change under `fixtures/`.
