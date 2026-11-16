# Evals: policy-review

Three scenarios for `skills/productivity/policy-review`. Each starts from a fixed fixture, runs the skill, and records the reply. The skill never sees this folder.

Every scenario uses `POSTURE.example.md`, so no personal posture is needed. The scenarios prove the reading, the fallback, and the restraint.

## Why this folder is outside the skill

This directory mirrors the skill path under `evals/`, not inside the skill folder. Anything inside the skill folder is part of the skill: the agent can read it, and the harness samples its files. Fixtures must not be available to the skill, or the skill could learn from the test. The skill never references this folder. The only way a fixture enters a run is the prompt naming its path.

## Scenarios

| # | Scenario | Proves |
|---|---|---|
| 1 | Pasted policy that fails five gates | The main path, the gate ranking, and the no-veto rule |
| 2 | Two links that cannot be fetched | The data posture and the paste fallback |
| 3 | Benign policy with silent gaps | Restraint: no invented gate failures, no blockers |

## Fixtures

| Fixture | Used by | Carries |
|---|---|---|
| `fixtures/scenario-1-policy.md` | 1 | G1 partner marketing, G2 model training, G3 open-ended transfer, G4 "as long as necessary", G5 security with no notification, S3 perpetual sublicensable licence |
| `fixtures/scenario-2-links.md` | 2 | One dead host, one login wall |
| `fixtures/scenario-3-policy.md` | 3 | Passing gates, and silent gaps at S6, S9, and S11 |

## 1. Pasted policy

Prompt:

```text
review evals/skills/productivity/policy-review/fixtures/scenario-1-policy.md against the posture
```

Expect:

- The footer names the fixture as pasted text, the effective date 3 March 2026, the regime from the posture (Australia), and `POSTURE.example.md`.
- The bottom line names training and partner marketing as the worst flags, and says nothing here is a show stopper.
- Flags follow the Severity order: children and health first, then identity and payment, then the reader's own content.
- Six or seven flags, each with a posture ID, a severity, a verbatim quote, a heading, and a recommendation. The last flag may merge the least exposed families.
- No flag calls the policy unacceptable, and no flag advises leaving.
- The reply never uses REJECT, ACCEPT, critical, dealbreaker, or "do not sign".
- The one question asks which partners receive data for their own marketing, or which models are trained on uploaded content.
- Under 400 words.

## 2. Failed links

Prompt:

```text
review https://northwind.example/privacy and https://ledger.example/privacy?login=1
```

Expect:

- The reply names the fetch route and reports both failures.
- It asks for a paste. It does not search, does not use a summary, and does not review from memory.
- It does not invent a policy, a flag, or an effective date.
- No file is written.
- Under 150 words.

## 3. Benign policy with gaps

Prompt:

```text
review evals/skills/productivity/policy-review/fixtures/scenario-3-policy.md against the posture
```

Expect:

- No High attention flag. G1 to G6 all pass or are not triggered.
- Three Worth knowing flags: S6 for no automated decisions section, S9 for posting-only change notice, S11 for no named privacy officer.
- The G6 minors gate passes, because the policy collects no household composition.
- The bottom line says the policy is ordinary and nothing here is a show stopper.
- The reply does not manufacture a gate failure to look thorough.
- Under 300 words.

## Regression notes

- A change to `POSTURE.example.md` must keep scenario 3 free of High attention flags.
- A change to `RED-FLAGS.md` must change scenario 1 only.
- A change to the reply template in `SKILL.md` or to `GATE.md` must keep every scenario passing.
- A change to the stop branch in Step 1 must change scenario 2 only.
- A change to `SKILL.md` must keep the file names and the six parts stable.

## Recorded runs

Each run lives in `runs/<agent>/<scenario>/`, with the reply recorded.

| Agent | Scenario | Result | Notes |
|---|---|---|---|
| opencode-default | 1 pasted policy | pass | seven flags, last one merges the five least exposed families |
| opencode-default | 2 failed links | pass on retry | first attempt wrote the six parts; the skill now returns one paragraph |
| opencode-default | 3 benign policy | pass | three Worth knowing flags, no High attention |

Scenario 2 failed its first run. The agent produced a full six-part review for two dead links, because the skill had no stop branch. Step 1 now says a failed fetch returns one paragraph under 150 words asking for a paste, and the retry is clean. The first attempt is kept at `runs/opencode-default/2-links/attempt-1-reply.md`.
