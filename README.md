# Skills

Agent skills for prompt engineering, deep research, podcast scripting, host personas, privacy review, architecture decisions, fact-checking, and skill improvement. Works in any agent with a skill loader. Maintained by Marcus Ford.

## Skills

### User-invoked

These skills run only when you type the name.

| Skill | Description |
| --- | --- |
| [adr](skills/productivity/adr/SKILL.md) | Writes one architecture decision record as a new record, an in-place edit, an amendment or a successor. Reviews a record against twenty-one checks and fixes only the editorial defects. |
| [bullshit](skills/productivity/bullshit/SKILL.md) | Fact-checks a response claim by claim: a verdict and its evidence for each, then an audit of its own annotations for the same failures. |
| [deep-research](skills/productivity/deep-research/SKILL.md) | Researches a question into one cited report that stands alone. Fans each axis into several queries, keeps an evidence ledger with a quote per source, and names its gaps and conflicts. |
| [podcast-host-personas](skills/productivity/podcast-host-personas/SKILL.md) | Builds one gated, machine-readable host persona. Use it when a show needs a first host, a second host that must not sound like the first, or a revision. |
| [podcast-script](skills/productivity/podcast-script/SKILL.md) | Turns a report or raw notes into a podcast script and the plain text for kokoro-tone, kokoro-fastapi, kokoro-raw, or ElevenLabs. Covers solo, two-host, and panel shows. |
| [policy-review](skills/productivity/policy-review/SKILL.md) | Reads a privacy policy or terms of service against a personal posture. Flags data training, reuse, sharing, and rights gaps in a short summary with recommendations. |
| [prompt-engineer](skills/productivity/prompt-engineer/SKILL.md) | Turns a rough request into one finished prompt for a target AI model. Also critiques, tests, and improves prompts. |
| [skill-improvement](skills/productivity/skill-improvement/SKILL.md) | Reviews an existing agent skill and takes it to a fixed bar: contract, gate, evals, audit. Run it deliberately, not mid-task. |

### Model-invoked

These skills fire on their own when the task fits. Type the name to run one directly.

| Skill | Description |
| --- | --- |
| [prompt-engineer](skills/productivity/prompt-engineer/SKILL.md) | Turns a rough request into one finished prompt for a target AI model. Also critiques, tests, and improves prompts. |

## Install

### Release ZIP (Copilot Chat, Claude Code/Chat, Gemini CLI)

Download the latest release from [GitHub releases](https://github.com/marcubus/skills/releases). The parent ZIP contains individual skill ZIPs in a flat structure:

```
skills-v2026.11.4.zip/
├── adr.zip
├── bullshit.zip
├── deep-research.zip
├── podcast-host-personas.zip
├── podcast-script.zip
├── policy-review.zip
├── prompt-engineer.zip
└── skill-improvement.zip
```

**Install a single skill:**
1. Download the parent ZIP and extract it
2. Drag the relevant skill ZIP (e.g., `prompt-engineer.zip`) into your chat interface's **Skill Create** front end
3. The skill installs immediately

This works in:
- GitHub Copilot Chat
- Claude Code / Claude Chat
- Gemini CLI / Chat Interface

### Any agent, one command

```bash
npx skills@latest add marcubus/skills
```

Omit `-a` to choose from the agents on your machine. Add `-g` for a global install. Add `--skill <name>` for one skill. To update, run `npx skills@latest update`, then re-run `add` for new skills.

Skills live at `skills/productivity/<skill>/`. The `skills.sh` installer reads that layout directly. The `.claude-plugin/` manifests expose the same set to Claude Code, Codex, Copilot, and VS Code as a plugin marketplace.

## Evals

Evals are test scenarios that verify each skill works correctly in real use cases. Each eval includes:
- A scenario description with input data
- Expected output or success criteria  
- Recorded run results showing the skill's actual behavior

Evals live outside the skill folders to keep them versioned separately from the skill code itself. This allows continuous testing without modifying the skills being tested.

See [evals/README.md](evals/README.md) for details on how evals are structured and how to add new ones.

## Rules

Rules are automated checks that ensure each skill meets quality standards before release. Each rule verifies:
- The skill can be executed without errors
- Documentation is complete and consistent
- Style guidelines are followed (no em dashes, semicolons, rhetorical negation)
- All referenced files exist and links work
- No secrets or sensitive data are exposed

Rules run automatically in CI on every commit. They catch issues early so problems don't reach users.

See [scripts/check.py](scripts/check.py) for the full rule set and how to add new ones.

## Attribution

Original concept by Marcubus. This implementation provides a structured skill system with intent-based technique selection, model-specific adaptations, automated validation gates, and eval-driven quality assurance.
