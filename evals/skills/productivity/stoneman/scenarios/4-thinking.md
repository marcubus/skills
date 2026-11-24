# Scenario 4: thinking

## Prompt, run A

> Read `skills/productivity/stoneman/SKILL.md` and follow it for this reply. Answer this task: `fixtures/thinking/task.md`. Write your answer to `output.md` in this folder and nothing else.

## Prompt, run B, the control

> Read `skills/productivity/stoneman/SKILL.md` and follow it for this reply, except that the Thinking section does not apply: treat every task as one-step, decide in one pass, and do not reason through the steps. Answer this task: `fixtures/thinking/task.md`. Write your answer to `output.md` in this folder and nothing else.

## Fixture

`fixtures/thinking/task.md`. 4 workers on a 4-core VM, SQLite in WAL, writes serialized by the writer lock, throughput flat at 90 rps, a proposal to go to 16 workers, and the instruction not to change the journal mode.

## Expectations, in `output.md`

- Answers no: 16 workers on 4 cores with a serialized writer does not raise throughput.
- Names the mechanism: worker count above core count adds contention, and the writer lock caps write throughput regardless.
- Keeps `4`, `16`, `90`, and `4-core` unchanged.
- Does not propose changing the journal mode, because the fixture forbids it.
- Run A is correct on the first four bullets; run B is recorded whatever it says, and a difference between them is the measured cost of the one-step rule.

## Runs

`runs/default/4-thinking/output.md`, `runs/control/4-thinking/output.md`
