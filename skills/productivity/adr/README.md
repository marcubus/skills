# Architecture Decision Records (ADR)

## What
Writes one architecture decision record as a new record, in-place edit, amendment, or successor. Also reviews an existing ADR against twenty-one checks for quality and consistency.

## Why Use It
When you need to document technical decisions with context, alternatives considered, trade-offs, and consequences. Ensures decisions are auditable and future-proof without making the decision itself.

## How (Brief)

Invoke as a skill: `/adr`. Tell it your action and decision. Example:

```
/adr new use Redis for session storage
# or /adr review ADR-001 to check it against the gate
```

## Install

### GitHub Copilot Chat, Claude Code/Chat, Gemini CLI

Download `adr.zip` from [GitHub releases](https://github.com/marcubus/skills/releases) and drag it into your chat interface's **Skill Create** front end. The skill installs immediately.

### Any Agent with Skill Loader

```bash
npx skills@latest add marcubus/skills --skill adr
```

Or install the full set: `npx skills@latest add marcubus/skills`

## Actions

| Action | When | Output |
|---|---|---|
| `new` | Writing a fresh ADR | New record file in `decisions/` |
| `edit` | Modifying an existing ADR | Updated record with version bump |
| `amend` | Adding to an incomplete or outdated decision | Amendment appended to original |
| `supersede` | Replacing a decision with a better one | New record with supersedes link |
| `review` | Checking an ADR against quality gates | Review report with findings |

## ADR Structure

Every ADR follows the standard format:

- **Number** — unique identifier (e.g., 001, 002)
- **Status** — proposal, accepted, rejected, superseded
- **Context** — why this decision was needed
- **Decision** — what was decided
- **Consequences** — short-term and long-term impacts

## Workflow Summary

1. **Resolve the action** — determine if new, edit, amend, or supersedes
2. **Gather context** — technical constraints, alternatives considered, stakeholders
3. **Write the record** — follow ADR template with all required sections
4. **Run checks** — apply twenty-one quality gates in `GATE.md`
5. **Index and link** — update `decisions/index.jsonl`, add supersedes links

## Files

| File | Purpose |
|---|---|
| `SKILL.md` | Full workflow, ADR lifecycle, review process |
| `GATE.md` | Twenty-one checks for quality and consistency |
| `examples/adr-template.md` | Blank ADR template with all sections |
| `decisions/index.jsonl` | Index of all decisions (auto-generated) |

## Review Process

The review applies twenty-one checks across five categories:

- **Structure** — required fields present, correct order
- **Clarity** — unambiguous language, no jargon without definition
- **Completeness** — alternatives considered, trade-offs documented
- **Consistency** — links to related decisions, version tracking
- **Quality** — prose rules followed, no banned words or em dashes

## Limits

- One ADR per decision. Split complex topics into multiple records.
- Status is immutable once accepted; use amendments for updates.
- Superseded decisions remain in the index with links to successors.

## Attribution

Original concept by Marcubus. This implementation provides a structured ADR system with automated quality gates and lifecycle management.
