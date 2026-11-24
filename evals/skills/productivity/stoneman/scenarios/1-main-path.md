# Scenario 1: main path

## Prompt

> Read `skills/productivity/stoneman/SKILL.md` and follow it for this reply. Answer this question: `fixtures/main-path/question.md`. Write your answer to `output.md` in this folder and nothing else.

## Fixture

`fixtures/main-path/question.md`. Three replicas, pool 20 each, `max_connections` 100, error `FATAL: sorry, too many clients already`, and the negation "the pool is not leaking".

## Expectations, in `output.md`

- Names the cause as connections held outside the pool (idle transactions, or another client), not a pool leak, because the fixture rules the leak out.
- Carries `20`, `100`, and `3` unchanged, with their roles clear.
- Keeps `max_connections` and the error string verbatim, in backticks or a fence.
- Carries a negation where the fixture has one: the leak stays ruled out.
- Uses no prefix, no "Sure", no closing summary after a list.
- Is shorter than a plain-prose answer to the same question, on the same content.

## Run

`runs/default/1-main-path/output.md`
