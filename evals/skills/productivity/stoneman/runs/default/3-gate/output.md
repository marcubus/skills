# Scenario 3: the pre-send check alone

Skill: `skills/productivity/stoneman/SKILL.md`, § Pre-send check (six questions).
User message: `fixtures/main-path/question.md`. Checked reply: `fixtures/gate-alone/reply.md`, then `fixtures/gate-clean/reply.md`.
Nothing rewritten: fixture wording below appears only inside quotes.

## Against the question

Three replicas, pool 20 each, `max_connections` 100, symptom `FATAL: sorry, too many clients already`, metrics ~20 in use per replica, and the explicit statement that the pool is **not** leaking.

## `fixtures/gate-alone/reply.md`

Verdict: **fails** — Floor (three ways, four slips), Preamble, Once, and Facts on the same slips. Escape and two readings pass.

### Floor — FAIL

1. Setting reshaped. `max_conn` is not a Postgres parameter; the source names `max_connections`.
   - Offending text: `Set max_conn to 120`
2. Error string dropped. The user's error string appears nowhere in the reply, so the reply never ties its diagnosis to the symptom.
   - Offending text: absent from the whole reply — `FATAL: sorry, too many clients already` (the reply's nearest line is `Sure! Here is what is eating your connections.`)
3. Negation inverted. The user said the pool is not leaking; the reply asserts the opposite twice.
   - Offending text: `and the pool holds them open after the request returns`
   - Offending text: `In short: the pool is the problem, the fix is a bigger pool and an idle timeout.`
4. Limit invented. The source says `max_connections` is 100; 120 is not in it.
   - Offending text: `Set max_conn to 120`

Minor, not one of the planted set: `conn.` is an invented abbreviation not written out at first use.
   - Offending text: `Three replicas at 20 conn. each is 60 sessions`

### Preamble — FAIL

First line is throat-clearing, not an answer.
   - Offending text: `Sure! Here is what is eating your connections.`

### Once — FAIL

Closing summary restates the paragraph and the list above it.
   - Offending text: `In short: the pool is the problem, the fix is a bigger pool and an idle timeout.`

### Facts — FAIL

Same two slips as the Floor rows, read as a cut that hardened the source: a measured "metrics show around 20 in use" and a checked "not leaking" become a stated cause, and 100 becomes 120.
   - Offending text: `Idle transactions. Three replicas at 20 conn. each is 60 sessions, and the pool holds them open after the request returns.`
   - Offending text: `Set max_conn to 120`

Numbers that do hold: `Three replicas at 20 conn. each is 60 sessions` (3 × 20 = 60).

### Two readings — PASS

Each fragment parses one way in context. Note only: `Idle transactions.` and `holds them open after the request returns` name different mechanisms, which is the Floor inversion above, not an ambiguous cut.

### Escape — PASS

`Restart the replicas` is disruptive but reversible, and the reply asks the user nothing; no security warning and no irreversible step, so no plain-prose conversion is owed. (Separate defect, outside the six: the restart is ordered without saying the pool change needs it first, and `Raise the pool to 30 per replica` contradicts `Set max_conn to 120`.)

## `fixtures/gate-clean/reply.md`

Verdict: **passes all six.**

| Question | Result | Evidence |
|---|---|---|
| Floor | pass | `Not a pool leak.` keeps the negation; `max_connections` and `FATAL: sorry, too many clients already` verbatim; `pg_stat_activity`, `application_name` intact; numbers 20, 60, 100, 40, 10, 30, 70 all check (3 × 20 = 60; 100 − 60 = 40; 3 × 10 = 30; 100 − 30 = 70) |
| Escape | pass | no warning, no irreversible step, no question to the user — nothing to render in prose |
| Preamble | pass | `Not a pool leak.` is the answer on line 1 |
| Facts | pass | states the measured sum (`60 checked-out sockets`) and the unaccounted class as observed, not as a proven cause; `leaves 40 for admin, migrations, monitoring, and replication` keeps the headroom explicit |
| Once | pass | each fact appears once; the closing `Or one pgbouncer in transaction mode with a pool of 20.` is an alternative, not a summary of the lines above |
| Two readings | pass | `a fourth client class takes the last of them` and `Sizing: 10 per replica is 30` each read one way |

No defect invented for this fixture.
