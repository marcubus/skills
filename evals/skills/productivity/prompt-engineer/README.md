# Evals: prompt-engineer

Three scenarios for `skills/productivity/prompt-engineer`. Each run starts from the fixture, runs the skill, and records the deliverable. The skill never sees this folder.

## Scenarios

| # | Scenario | Proves |
|---|---|---|
| 1 | One-shot prompt from a status report | The main path produces a finished, pasteable prompt |
| 2 | System prompt for a Qwen3 triage agent | The tool or agent branch, a stated model, and the missing-facts path |
| 3 | Critique of a weak prompt | The gate alone, judging work it did not produce, with no rewrite |

## Fixtures

| Fixture | Used by | Carries |
|---|---|---|
| `fixtures/atlas-status-report.md` | 1 | Three required summary contents, two named risks, one decision |
| `fixtures/triage-brief.md` | 2 | A stated model, an agent type, and five missing facts |
| `fixtures/weak-summary-prompt.md` | 3 | Six defects the gate must name |

## Expectations

### 1. One-shot

- `atlas-status-report-executive-summary-prompt.md` is a prompt, not the summary itself.
- The reply opens with one line naming Claude and the one-shot type.
- The prompt names a role, an audience, the task, a 5-sentence format, a tone, and a `Style:` line.
- The task names status, key risks, and the single decision.
- No unfilled square bracket survives.
- No em dash, no semicolon, no banned word in the prompt or the reply.

### 2. Agent

- `triage-brief-triage-agent-prompt.md` resolves the type to tool or agent and names the Qwen file.
- The agent prompt carries role and expertise, objective, audience, the loop, a numeric step limit, a tool trigger, error handling, an output contract, tone, constraints, a `Style:` line, and a language.
- A `create_ticket` definition follows the prompt, with a name, a description carrying a trigger, and typed parameters with one example.
- The five missing facts appear in an assumptions line, and any value written into the prompt is named there.
- A thinking switch or sampling setting sits below the prompt.
- No unfilled square bracket survives, except a schema bracket or `[ILLEGIBLE]`.

### 3. Critique

- `weak-summary-prompt-critique.md` reports findings and does not rewrite the prompt.
- Every finding names a gate check number.
- The findings name at least: missing audience (check 2), an ambiguous task verb (check 3), constraints without reasons (check 4), no output format (check 5), no `Style:` line (check 12).
- No invented facts about the supplier review.

## Runs

| Run | Scenario | Result | Evidence |
|---|---|---|---|
| default | 1 | pass | `runs/default/1-oneshot/` |
| default | 2 | pass | `runs/default/2-agent/` |
| default | 3 | pass | `runs/default/3-critique/` |
