# Deep Research

## What
Turns a topic or question into one cited report that stands alone. Every claim traces to a source with tier and date, or is labelled an inference. The report exits at step 3 if the answer fits in chat; otherwise it writes to disk.

## Why Use It
When you need research-backed answers with evidence tracking, not just search snippets. Ideal for topics requiring multiple perspectives, conflicting sources, or verified claims with citations.

## How (Brief)

Invoke as a skill: `/deep-research`. Tell it your topic or question. Example:

```
/deep-research grid-scale sodium-ion battery economics
```

## Install

### GitHub Copilot Chat, Claude Code/Chat, Gemini CLI

Download `deep-research.zip` from [GitHub releases](https://github.com/marcubus/skills/releases) and drag it into your chat interface's **Skill Create** front end. The skill installs immediately.

### Any Agent with Skill Loader

```bash
npx skills@latest add marcubus/skills --skill deep-research
```

Or install the full set: `npx skills@latest add marcubus/skills`

## Workflow Summary

1. **Frame the question** — pick 3 to 6 axes from the axis list in `SKILL.md`.
2. **Open the run** — create the evidence directory and report skeleton.
3. **Search in waves** — five queries per axis across three waves, plus blindspots.
4. **Validate** — apply sourcing rules, tier caps, coverage bar.
5. **Write the report** — fill the skeleton from `REPORT.md`.
6. **Run the gate** — twelve checks in `GATE.md`.
7. **Deliver** — handoff with key findings and gaps.

## Output

One markdown file at `<reports-dir>/YYYY-MM-DD-<slug>-report.md`. The reports directory resolves in this order: user path, `$XDG_CONFIG_HOME/deep-research/OUTPUT.md`, `OUTPUT.local.md`, or `reports/` in the working directory.

## Files

| File | Purpose |
|---|---|
| `SKILL.md` | Full workflow and rules |
| `SOURCING.md` | Finding and judging sources, tiers, anti-SEO rules |
| `EVIDENCE.md` | Run directory structure, two tables, truth discipline |
| `REPORT.md` | Report shape, prose rules, word band |
| `GATE.md` | Twelve checks for the final report |
| `examples/report.md` | Worked example of a complete report |

## Limits

- Research is bounded: the report cites what supports and contradicts rather than everything published.
- Paywalled origins are cited as secondary with the gap named in WHAT COULD NOT BE VERIFIED.

## Attribution

Original concept by Marcubus. This implementation adds structured evidence tracking, tiered sourcing, and automated validation gates.
