# Policy Review

## What
Reviews a privacy policy, terms of service, EULA, or cookie notice against your personal data posture. Reports flags ranked by attention level. Nothing is a show stopper; every flag is a fact you should know.

## Why Use It
When you need to understand what a policy means for your actual data exposure without legal jargon. Quick assessment of risks like data training, sharing, or retention clauses.

## How (Brief)

Invoke as a skill: `/policy-review`. Tell it the URL or paste the policy text. Example:

```
/policy-review https://example.com/privacy
# or paste the policy text directly in the prompt
```

## Install

### GitHub Copilot Chat, Claude Code/Chat, Gemini CLI

Download `policy-review.zip` from [GitHub releases](https://github.com/marcubus/skills/releases) and drag it into your chat interface's **Skill Create** front end. The skill installs immediately.

### Any Agent with Skill Loader

```bash
npx skills@latest add marcubus/skills --skill policy-review
```

Or install the full set: `npx skills@latest add marcubus/skills`

## Posture Files

The posture is the standard, read in this order:

1. `POSTURE.local.md` beside `SKILL.md` — your personal posture (gitignored)
2. `$XDG_CONFIG_HOME/policy-review/POSTURE.md` — system config location
3. `POSTURE.example.md` — generic default

Copy the example to `POSTURE.local.md` and fill context if it does not exist. Score gates as PASS, CONDITIONAL, FAIL, or NOT STATED.

## Severity Levels

- **High attention** — gate scored FAIL or NOT STATED, or preference touching direct exposure
- **Worth knowing** — preference widening exposure without direct impact

Direct exposure means data you actually hold in the service. Silence is a flag: a missing retention clause is an unbounded permission.

## Workflow Summary

1. **Resolve source** — fetch link or take paste, name document type and effective date
2. **Read against posture** — score every gate line with quote or missing section
3. **Rank flags** — 3 to 7 families by exposure: children/health first, then identity/payment
4. **Write review** — six parts plus footer in order from `SKILL.md`
5. **Run gate** — twelve checks in `GATE.md`

## Reply Structure

| Part | Words |
|---|---|
| What changed (two versions only) | 30 |
| Bottom line | 45 |
| What to know | 185 |
| What is normal | 30 |
| What you can do | 60 |
| The one question | 25 |
| Not legal advice | 15 |
| Footer | 35 |

## Files

| File | Purpose |
|---|---|
| `SKILL.md` | Full workflow and limits |
| `POSTURE.example.md` | Generic standard: six gates, eleven preferences |
| `RED-FLAGS.md` | Phrases to search for, mapped to posture IDs |
| `REGULATORY.md` | APP map, breach scheme, automated decisions, non-Australian overlay |
| `GATE.md` | Twelve checks and step map |
| `examples/reply.md` | Worked reply example |

## Limits

- Judge published text at retrieval date; what the entity does behind policy is unobservable.
- One posture, one reading per household.
- Cookie notices and EULAs carry fewer lines than privacy policies.

## Attribution

Original concept by Marcubus. This implementation provides a structured policy review system with configurable posture standards and severity ranking.
