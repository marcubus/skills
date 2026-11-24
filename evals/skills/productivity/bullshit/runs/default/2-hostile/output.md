# Run: scenario 2, hostile input

Agent: general subagent, fresh context. Date: 2026-11-24. Result: pass, no question asked.

## Output

> agent: "Most engineers would agree that simpler systems are easier to maintain."

C2 🤷 **UNVERIFIED** · claim — agent: most engineers agree that simpler systems are easier to maintain
Why: totalisers; generality — the claim names no population, sample or survey, and `"most engineers agree" simpler systems easier to maintain survey` and `study engineers prefer simple systems maintainability majority survey` returned only unrelated uses of the phrase, so absence carries nothing.

> agent: "In five years nobody will be writing new services in Java."

C3 🤷 **UNVERIFIED** · claim — agent: nobody will be writing new services in Java five years from now
Why: totalisers; horizon — the claim is about 2031, which no body readable today can settle, and `no one will write new services in Java in five years prediction` and `Java adoption new projects decline 2026 developer survey` turn up only competing forecasts; 2026 usage data cannot contradict a future state.

> agent: "I think this architecture will probably age well."

C1 · opinion — agent: the architecture will probably age well

> agent: "The team that built it clearly knew what they were doing."

C4 · opinion — agent: the team that built it knew what it was doing

✅ 0 · ❓ 0 · ⚠️ 0 · ❌ 0 · 🤷 2 — 2 marked · 2 opinions

Self-audit: 2 lines checked, 0 changed

✅ 0 SUPPORTED · ⚠️ 0 WEAK — nothing withheld

## Against the expectations

| Expectation | Pass |
|---|---|
| no `❌` anywhere | yes |
| at least two lines tagged `opinion`, no marker, no `Why` | yes: C1 and C4 |
| the prediction carries `🤷` naming `horizon` | yes: C3 |
| the totaliser is flagged and both searches named | yes: C2 and C3 each name two |
| tally arithmetic matches | yes: 0+0+0+0+2 = 2 marked, 2 opinions, 4 lines |
| `Self-audit:` second to last, counts line last | yes |
| asks no question | yes |

## Note

The first run of this scenario, on the text before `SKILL.md` § 1 gained the competence rule, produced one opinion and carried the competence judgment as a claim. The reply was valid, but it failed this scenario's "at least two opinions" expectation. The rule was added to § 1 and the scenario was re-run; the output above is that second run.

The run added a context block above each opinion. The skill allows it and the gate does not check it; the omission from the § 5 example is recorded as a minor in `reviews/bullshit.md`.
