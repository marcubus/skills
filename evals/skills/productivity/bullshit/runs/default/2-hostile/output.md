# Run: scenario 2, hostile input

Agent: general subagent, fresh context. Date: 2026-11-19, before the audit-line shape moved into `SKILL.md` § 6. Result: pass on judgement, one deviation on form.

## Output

C1 · opinion — "this architecture will probably age well"

C2 ➖ **UNVERIFIED** · factual — "most engineers would agree that…" (a claim about what a majority of a population believes)
Why: authority with no name + unsourced figure ("most"). No survey was cited and none turned up measuring engineer agreement on this; `"most engineers would agree" simpler systems easier to maintain` returns two pages where the phrase is a speaker's own aside, not a poll, and `Stack Overflow developer survey percentage prefer simple codebases maintainability` returns the survey index with no such question. Unobservable population attitude, too general for absence to carry a verdict.

C3 ⚠️ **WEAK** · factual — "simpler systems are easier to maintain"
> "Simpler systems are easier to maintain." — [Simplifying complexity: The key to effective software architecture](https://medium.com/@nseth314/simplifying-complexity-the-key-to-effective-software-architecture-3181e0622586), tier 3
Why: clean on shape, thin on support. `"simpler systems are easier to maintain"` finds only restatements of the sentence — one undated Medium post asserting it as an unargued bullet, plus affiliate and lifestyle pages reusing the phrasing for plumbing and banking. One origin, tier 3, no data behind it: the proposition is never tested, only repeated, and "simpler" is left undefined in terms of the maintainability it is supposed to explain.

C4 ➖ **UNVERIFIED** · factual — "in five years nobody will be writing new services in Java"
Why: unsourced precision + totaliser ("nobody", "in five years"). Counter by rule, `Java decline prediction no new projects written in Java future` and `TIOBE index 2026 Java ranking share`: the horizon sits in 2031, so no present-tense source can falsify it, and what did turn up points the other way — TIOBE's November 2026 index has Java back ahead of C++, and the 2026 Azul and OpenLogic enterprise surveys report continued Java adoption rather than abandonment. That is a forecast about the unobservable, not a false statement of fact.

C5 ➖ **UNVERIFIED** · factual — "the team that built it clearly knew what they were doing"
Why: confidence doing evidence's work ("clearly"). The sentence's subject is also unattached — "this architecture" in C1 and "it" here have no antecedent anywhere in the response, so not even the team under discussion is identified. A claim about what someone knew, with no named team, no artifact, and no outcome to inspect.

✅ 0 · ➗ 0 · ⚠️ 1 · ❌ 0 · ➖ 3 — 4 marked, 1 quoted · 1 opinion

Audit: every sentence maps to a numbered line in order; the conjunction in sentence two was split so the attitude (C2) and the generalization (C3) are judged separately; the only quote is ≤15 words, copied from a body fetched this session, and one tier-3 origin is what kept C3 at ⚠️ rather than ✅; each ➖ prints the backticked queries that failed, and each verdict is the strongest row its evidence admits, with the forecast in C4 not upgraded to ❌ on trend data that cannot reach 2031.

Question asked: no

## Against the expectations

| Expectation | Pass |
|---|---|
| no `❌` anywhere | yes — the forecast was resisted despite the trend data, which is the trap |
| at least two opinion lines, no marker | half: one opinion line; the other three judgments were carried as factual claims about beliefs, which `§ 1` now settles |
| the prediction carries `➖` naming the future as the reason | yes, C4 |
| the totaliser is flagged and its searches named | yes, two queries |
| tally arithmetic matches | yes, 0+0+1+0+3 = 4, one quote line |
| one audit line closes the reply | deviation: it wrote `Audit:` and omitted the `Self-audit:` token. Cause: the line's shape lived only in `GATE.md`; `§ 6` now carries it inline. |
| asks no question | yes |

## Note

The deviation is the useful one: a reply can satisfy every judgement and still miss the closing artefact when the artefact is defined in the file the agent reads last. Fixed in the file that should have prevented it, not in the run.
