# Scenario 3: the check alone

## Prompt

> Read /optimus/workspace/skills/skills/productivity/stoneman/SKILL.md and apply its § Pre-send check to /optimus/workspace/skills/evals/skills/productivity/stoneman/fixtures/gate-alone/reply.md, with /optimus/workspace/skills/evals/skills/productivity/stoneman/fixtures/main-path/question.md as the user's message. Report every question the reply fails, with the offending text. Do not rewrite the reply. Then repeat for `fixtures/gate-clean/reply.md`, which passes. Write the audit to `output.md` in this folder and nothing else.

## Fixture

`fixtures/gate-alone/reply.md`, with six planted defects, one per question:

| Question | Defect |
|---|---|
| Floor | `max_conn` where the system setting is `max_connections`, and the error string dropped |
| Floor | the source's "not leaking" becomes "the pool is the problem" |
| Floor | `120` invented as the limit, where the source says 100 |
| Once | the closing "In short:" restates the list |
| Preamble | the `Sure!` opener |

`fixtures/gate-clean/reply.md` carries none of these, and answers the same question.

## Expectations, in `output.md`

- Names the floor failures: the reshaped setting, the dropped negation, the invented limit.
- Names the summary that repeats its list, and the preamble.
- Quotes the offending text for each.
- Rewrites nothing: the fixture's wording appears only as a quote.
- Invents no defect the clean fixture does not carry, and reports the clean fixture as passing.

## Run

`runs/default/3-gate/output.md`
