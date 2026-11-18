# Evals: meeting-summary

Three scenarios. The skill produces a summary, then checks one it did not produce.

## Why this folder is outside the skill

`evals/productivity/meeting-summary/` mirrors the skill path. The skill never references this folder, and a fixture enters a run only because the prompt names its path.

## Fixtures

| File | Used by | What it carries |
|---|---|---|
| `fixtures/transcript.md` | 1 | 9 March; "Thursday" and "next week", an unassigned action, a proposal nobody agreed to |
| `fixtures/transcript-messy.md` | 2 | 3 April; an unknown speaker, a decision that is later reversed, "today" |
| `fixtures/summary-bad.md` | 3 | A summary with five defects: no decider, no owner, a relative date, a restatement, and a decision listed twice |

## 1. Main path

```text
summarise evals/productivity/meeting-summary/fixtures/transcript.md
```

Expect:

- `transcript-summary.md` beside the source.
- Three headings: Decisions, Actions, Notes.
- Every decision names the person who decided.
- Every action has an owner or is marked unassigned.
- "Thursday" becomes 12 March and "next week" becomes 16 March.
- The changelog action is marked unassigned.
- The parser rewrite is under Notes as a proposal, not under Decisions.
- No sentence restates another.
- Under 400 words.

## 2. Variant

```text
summarise evals/productivity/meeting-summary/fixtures/transcript-messy.md
```

Expect:

- The unknown speaker is marked unknown.
- "Today" becomes 3 April.
- The stale cache is recorded once, with the acceptance and the later reversal.
- The changelog fix is Ben's action, not the unknown speaker's.
- The parser rewrite is a decision, because Ana and Cleo agreed to it.
- No sentence restates another.

## 3. Gate alone

```text
check evals/productivity/meeting-summary/fixtures/summary-bad.md
```

Expect:

- The skill does not rewrite the summary.
- It reports failures by check number: 1, 2, 3, and 4.
- It names the duplicated decision and the restated sentence.
- It confirms check 5 passes.
- It stops before writing a new summary.

## Recorded run

| Run | Scenario | Result | Evidence |
|---|---|---|---|
| default | 1 main | pass | `runs/default/1-main/transcript-summary.md` |

## Regression notes

- A change to the checks keeps scenario 3 reporting the same four numbers.
- A change to the output section keeps the file name stable in scenario 1.
