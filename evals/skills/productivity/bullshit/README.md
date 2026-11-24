# Evals: bullshit

Three scenarios for `skills/productivity/bullshit`. The skill never reads this folder.

## Layout

| Path | Holds |
|---|---|
| `scenarios/` | one file per scenario: the prompt, the fixture, the expectations |
| `fixtures/main-path/response.md` | five claims across four verdicts, one fabricated quote |
| `fixtures/hostile/response.md` | four judgments, nothing checkable |
| `fixtures/gate-clean/reply.md` | an annotation that passes every gate check a frozen file can pass |
| `fixtures/gate-broken/reply.md` | the same shape with seven planted defects |
| `runs/<run>/<scenario>/` | the recorded output of one run |

## Scenarios

| # | Scenario | Proves |
|---|---|---|
| 1 | A paragraph of five claims, one fabricated | the main path: verdicts below `✅`, quotes, tally, audit line |
| 2 | Four judgments and a forecast | the branch where nothing is checkable: no accusation, opinions listed |
| 3 | The gate against `gate-clean` and `gate-broken` | the gate checks work it did not produce, and rewrites nothing |

## Running

Scenario 3, from this folder:

```bash
for f in fixtures/gate-clean/reply.md fixtures/gate-broken/reply.md; do
  echo "== $f"
  grep -oE '^C[0-9]+' "$f" | sed 's/^C//' | awk 'NR != $1 {print "gap at " NR ": got C" $1}'
  grep -E '^C[0-9]+ ' "$f" | grep -oE '(✅|❓|⚠️|❌|🤷)' | sort | uniq -c
  grep -c '^> '
  grep -c '^Self-audit:'
done
```

Run the gate's own command blocks from `GATE.md` against each fixture; the clean file prints nothing and the broken file complains at checks 1, 2, 4, 7, 8, 12 and 14.

Scenarios 1 and 2 name the real skill folder and no fixture beyond the paragraph. Recorded runs sit under `runs/default/`.

## Regression list

Run before a report:

- a change to `GATE.md` keeps all three scenarios passing, and keeps the broken fixture at exactly seven complaining checks;
- a change to `fixtures/main-path/response.md` changes only scenario 1;
- a change to `fixtures/hostile/response.md` changes only scenario 2;
- a change to `SKILL.md` keeps the annotation shape, the five markers and the audit line stable;
- adding a sixth marker changes every scenario, because the enum is single-sourced in `SKILL.md` § 4.
