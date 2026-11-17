# Skills

A collection of agent skills. Each skill turns a rough request into a finished result. Maintained by Marcus Ford.

## Skills

### User-invoked

These skills run only when you type the name.

| Skill | Description |
| --- | --- |
| [skill-improvement](skills/productivity/skill-improvement/SKILL.md) | Reviews an existing agent skill and takes it to a fixed bar: contract, gate, evals, audit. Run it deliberately, not mid-task. |

### Model-invoked

These skills fire on their own when the task fits. Type the name to run one directly.

| Skill | Description |
| --- | --- |
| [prompt-engineer](skills/productivity/prompt-engineer/SKILL.md) | Turns a rough request into one finished prompt for a target AI model. Also critiques, tests, and improves prompts. |
| [deep-research](skills/productivity/deep-research/SKILL.md) | Researches a question into one cited report that stands alone. Fans each axis into several queries, keeps an evidence ledger with a quote per source, and names its gaps and conflicts. |
| [podcast-script](skills/productivity/podcast-script/SKILL.md) | Turns a report or raw notes into a podcast script and the plain text for kokoro-tone, kokoro-fastapi, kokoro-raw, or ElevenLabs. Covers solo, two-host, and panel shows. |
| [podcast-host-personas](skills/productivity/podcast-host-personas/SKILL.md) | Builds one gated, machine-readable host persona. Use it when a show needs a first host, a second host that must not sound like the first, or a revision. |
| [policy-review](skills/productivity/policy-review/SKILL.md) | Reads a privacy policy or terms of service against a personal posture. Flags data training, reuse, sharing, and rights gaps in a short summary with recommendations. |

## Install

### Any agent, one command

```bash
npx skills@latest add marcubus/skills -a opencode -a hermes-agent
```

Omit `-a` to choose from the agents on your machine. Add `-g` for a global install. Add `--skill <name>` for one skill. To update, run `npx skills@latest update`, then re-run `add` for new skills.

Skills live at `skills/productivity/<skill>/`. The `skills.sh` installer reads that layout directly. The `.claude-plugin/` manifests expose the same set to Claude Code, Codex, Copilot, and VS Code as a plugin marketplace.

### OpenCode

```bash
npx skills@latest add marcubus/skills -a opencode
```

For a local checkout, link the repo instead:

```bash
scripts/install.sh --target opencode
```

Manual install: copy or symlink each folder in `skills/productivity/` into `~/.config/opencode/skills/`, or add the repo path to `opencode.json`:

```jsonc
{
  "skills": ["/path/to/skills-repo/skills/productivity"]
}
```

OpenCode combines every `skills` array, so this adds to the default directories rather than replacing them.

### OpenCode server

The server runs under its own user, so install into that user's config:

```bash
sudo -u opencode mkdir -p /home/opencode/.config/opencode/skills
sudo -u opencode ln -s /path/to/skills-repo/skills/productivity/prompt-engineer \
  /home/opencode/.config/opencode/skills/prompt-engineer
```

Or run:

```bash
scripts/install.sh --target server --server-home /home/opencode
```

Restart `opencode-serve` after install. The server config may also list a `skills` path. Keep it if it points at this repo. OpenCode merges the arrays, so the default global directory still loads.

### Hermes

For a default host profile, skills.sh writes to `~/.hermes/skills/`:

```bash
npx skills@latest add marcubus/skills -a hermes-agent -g
```

If `HERMES_HOME` points somewhere else, use the installer, which writes to `$HERMES_HOME/skills/productivity/`:

```bash
scripts/install.sh --target hermes --hermes-host
```

For a container, copy the skills into the profile directory Hermes reads:

```bash
scripts/install.sh --target hermes --hermes-container hermes
```

This copies into `/opt/data/skills/productivity/`, the path for `HERMES_HOME=/opt/data`. Restart the container, or run `hermes skills list` inside it to verify.

### Local checkout installer

`scripts/install.sh` links the repo into agent directories, so `git pull` keeps the skills current.

```bash
scripts/install.sh --target opencode
scripts/install.sh --target server --server-home /home/opencode
scripts/install.sh --target hermes --hermes-container hermes
scripts/install.sh --target all
```

Targets: `opencode`, `agents`, `server`, `hermes`. `all` covers `opencode`, `agents`, and `hermes`, plus `server` when `/home/opencode` exists or `--server-home` is given. Flags: `--copy` copies instead of linking, `--dry-run` prints the plan, `--force` replaces existing folders.

### Plugin marketplace

Claude Code, Codex, and Copilot CLI can install the repo as a managed plugin:

```bash
claude plugin marketplace add marcubus/skills
claude plugin install marcubus-skills@marcubus
```

```bash
codex plugin marketplace add marcubus/skills
codex plugin add marcubus-skills@marcubus
```

```bash
copilot plugin marketplace add marcubus/skills
copilot plugin install marcubus-skills@marcubus
```

Gemini CLI installs each bucket separately:

```bash
gemini skills install https://github.com/marcubus/skills.git --path skills/productivity
```

### Hosted assistants

Microsoft 365 Copilot, ChatGPT, Gemini Gems, and Claude Projects need a manual paste. See [docs/install.md](docs/install.md) for the steps.

### Verify

Send this request on any platform:

> Write me a prompt for turning a meeting transcript into five action items with owners.

Check three things:

- The reply returns one finished prompt, with no preamble.
- The reply follows the style rules in SKILL.md: no em dashes, no banned words.
- The reply names the target model, or defaults to Claude when you do not name one.

## prompt-engineer

![Prompt Engineer flow: a rough request is analysed, checked for ambiguity, then generated into one finished prompt](docs/prompt-engineer-flow.png)

Turns a rough request into one finished, ready-to-use prompt for a chosen AI model. Ask for a prompt, and get a single usable result rather than a draft. Give an existing prompt, and the skill critiques, tests, or improves the prompt against best practice.

Runs as an OpenCode skill, and as an agent or Gem on Microsoft 365 Copilot, ChatGPT, Gemini, and Claude.

### Supported models

| Target | Knowledge file |
| --- | --- |
| Claude, the default | `skills/productivity/prompt-engineer/MODEL-CLAUDE.md` |
| ChatGPT, Microsoft Copilot | `skills/productivity/prompt-engineer/MODEL-GPT-COPILOT.md` |
| Gemini | `skills/productivity/prompt-engineer/MODEL-GEMINI.md` |
| DeepSeek | `skills/productivity/prompt-engineer/MODEL-DEEPSEEK.md` |
| Qwen | `skills/productivity/prompt-engineer/MODEL-QWEN.md` |

`skills/productivity/prompt-engineer/SKILL.md` always loads. The file carries the frameworks and the style rules. The model files add the mechanics each family needs.

## deep-research

Researches a question and writes one report that stands alone. It fans each axis into several queries, caches every page it reads, and keeps two tables: the sources fetched and the claims made. Each claim carries its sources, an origin count, a confidence label, and a verbatim quote from the cached body.

The report is plain prose with a source marker on every factual sentence. It names its conflicts and its gaps instead of resolving or filling them. It never refers to the conversation, or to what will happen to the file next, so it survives being read cold or handed to another skill.

The skill stops at the report. Rendering, publishing, and any spoken version belong elsewhere.

Runs as an OpenCode skill, and as an agent or Gem on Microsoft 365 Copilot, ChatGPT, Gemini, and Claude.

### Files

- `skills/productivity/deep-research/SKILL.md`, the contract and the seven steps.
- `SOURCING.md`, query fan-out, query types, anti-SEO rules, primary-source escalation, citation chaining.
- `EVIDENCE.md`, the run directory, the two tables, the quote rule, confidence, and the stop condition.
- `REPORT.md`, the report's shape, section order, prose rules, and word bands.
- `GATE.md`, twelve checks with a step map, the ledger block, and the report commands.
- `OUTPUT.example.md`, the optional reports directory override.
- `examples/report.md`, one worked report.
- `agents/openai.yaml`, the OpenAI and Codex interface manifest.

### Install

Use the [install routes](#install). This skill needs the whole `deep-research` folder, because `SKILL.md` points at the reference files.

### Verify

Ask for a report on a topic with a live landscape. Check three things:

- It writes `reports/YYYY-MM-DD-<slug>-report.md`, or the path you named.
- Every factual sentence carries a `[S#]` marker, and the Sources section lists each source with a tier and a date.
- The ledger block in `GATE.md` prints nothing but the three headers and the domain counts.

## podcast-script

Turns a report, document, or raw notes into a podcast script and the plain text the chosen model reads. It covers solo narration, two-host shows, and panels of three or more hosts. The script is model-neutral: it carries voice, emotion, rate, pause, and pronunciation markers, and a model file compiles them into the target's text dialect. Targets kokoro-tone, kokoro-fastapi, kokoro-raw, and ElevenLabs.

The model file says what the text carries. The skill writes to the chosen model and records any marker the text cannot carry. Variety comes from rate, pause, sentence length, and word choice.

The skill stops at the text. It builds no payload and calls no service; research, rendering, mastering, and publishing belong elsewhere.

Runs as an OpenCode skill, and as an agent or Gem on Microsoft 365 Copilot, ChatGPT, Gemini, and Claude.

### Files

- `skills/productivity/podcast-script/SKILL.md`, the workflow and compiled text.
- `MODELS.md`, the model registry and choosing rules.
- `MODEL-KOKORO-TONE.md`, inline tags for every marker.
- `MODEL-KOKORO-FASTAPI.md`, plain text with punctuation for pauses.
- `MODEL-KOKORO-RAW.md`, plain text with blank lines for pauses.
- `MODEL-ELEVENLABS.md`, inline emotion cues with punctuation for pauses.
- `PROFILE.md`, the typed host profile and gate.
- `PERFORMANCE.md`, pacing, emotion, emphasis, and performance moves.
- `TICKS.md`, the tick library, density rules, and banlist.
- `HANDOFF.md`, the compile procedure, the text file, and the notes contract.
- `SCRIPT-CRAFT.md`, structure, prose, punctuation, and attribution.
- `VOICE.md`, casting, rate, and pause.
- `MULTIHOST.md`, two-host relationship and handoffs.
- `PANEL.md`, three or more hosts.
- `VERIFY.md`, the release gate.
- `examples/`, example snippets for a host profile, a beat map, a solo script, a two-host script, and a panel script.
- `agents/openai.yaml`, the OpenAI and Codex interface manifest.

### Install

Use the [install routes](#install). This skill needs the whole `podcast-script` folder, because `SKILL.md` points at the reference files.

### Verify

Send a short report or a page of raw notes and ask for a solo podcast script. Check three things:

- The reply writes `<source-stem>-podcast-script.md`, `<source-stem>-tts-<model>.txt`, and `<source-stem>-script-notes.md` next to the source.
- The script starts with a cold open, not a title, and ends with a closing line, not `END`.
- The notes name the model. The compiled text carries the spoken words and resolves every marker, and holds no payload.

## podcast-host-personas

Builds one machine-readable host persona for a podcast, then gates it against the store. Use it for a first host, a second host that must not sound like the first, or a revision that adds a strained state, a mode set, or a room.

A persona is written for two consumers: a script writer who needs to know how the host talks, and a speech synthesiser that needs to know how the host sounds. The skill ends at a saved profile. A transcript skill reads it, casts a voice, and renders audio.

The brief is yours. You can set the name, the traits and any field you like, and the skill records the override instead of overruling it. Two things still stop a build: impersonating a real person, and an override that makes the profile contradict itself.

### Files

- `skills/productivity/podcast-host-personas/SKILL.md`, the workflow and the profile in one view.
- `GATE.md`, the twenty-nine checks, step map, failure modes, and sanity read.
- `references/persona-schema.md`, the twenty-eight fields in fixed order.
- `references/vocal-levers.md`, `references/voice-craft.md`, `references/describing-words.md`, and `references/phonetic-distinctness.md`, the sound and word-choice rules.
- `references/emotion-engine.md`, `references/show-craft.md`, `references/studio-craft.md`, and `references/tick-library.md`, the delivery and show rules.
- `references/generator-procedure.md`, `references/tts-capability-guide.md`, and the verification notes, the build and research record.
- `examples/`, a template and three filled personas.
- `personas/`, the local store: gitignored, ships with a README, and created on first build.
- `agents/openai.yaml`, the OpenAI and Codex interface manifest.

### Install

Use the [install routes](#install). This skill needs the whole `podcast-host-personas` folder, because `SKILL.md` points at the reference files.

### Verify

Ask for a first host for a new show. Check three things:

- It writes one profile file and adds the host to `personas/index.jsonl`.
- Every one of the twenty-eight fields is filled, in the fixed order.
- The gate passes, or every failure names the field and the fix.

## skill-improvement

Reviews an existing skill and takes it to a fixed bar. Five phases: survey, gauntlet, gate, evals, prove. Three reviewers run in rounds, Runs, Reads, and Audit, and the loop exits at zero blockers and zero majors.

The output is a review at `reviews/<skill>.md`, which stays local and is gitignored, and, when you ask for it, a fixed skill with a numbered gate and an eval suite outside its folder.

User-invoked: type `/skill-improvement` or name it. It stays out of the model's list, because a review is a deliberate, expensive act.

### Files

- `SKILL.md`, the five phases, the severity model, and the eight laws.
- `SURVEY.md`, inventory, contract, and the fact table.
- `GAUNTLET.md`, the three reviewer briefs and the round loop.
- `CRAFT.md`, the five writing levers as checks.
- `GATE.md`, designing numbered checks and a step map.
- `EVALS.md`, scenarios, fixtures, runs, and regression.
- `VARIANTS.md`, neutral core, variant files, and capability tables.
- `AUDIT.md`, eighteen checks, five of them reads.
- `REPORT.md`, the review template.
- `examples/`, a filled report, a gate, and an eval README.
- `agents/openai.yaml`, the OpenAI and Codex interface manifest.

### Install

Use the [install routes](#install). This skill needs the whole `skill-improvement` folder, because `SKILL.md` points at the reference files.

The frontmatter sets `disable-model-invocation: true`, so OpenCode keeps it out of the model's list and loads it only when you name it.

### Verify

Point it at a skill and ask for an audit. Check three things:

- It writes `reviews/<skill>.md` with a verdict line and the severity counts. That folder is gitignored, because a review is a snapshot of one audit and goes stale as the skill moves.
- Every finding carries a file, a line, a severity, and a fix.
- The audited skill is unchanged.

## Evals

Each skill's evals live beside it under `evals/`, mirroring the skill path. They sit outside the skill folder on purpose: the skill never reads them, and only the tester does.

- `evals/skills/productivity/prompt-engineer/`, three scenarios and their fixtures.
- `evals/skills/productivity/podcast-script/`, three scenarios and their fixtures.
- `evals/skills/productivity/podcast-host-personas/`, three scenarios and their fixtures.
- `evals/skills/productivity/skill-improvement/`, three scenarios, a broken fixture with eleven planted defects, and a clean fixture.

## Repository layout

```text
skills/productivity/
  README.md                         bucket index
  prompt-engineer/
    SKILL.md                        agent instructions, frameworks, style rules
    MODEL-CLAUDE.md                 Claude mechanics
    MODEL-GPT-COPILOT.md            ChatGPT and Copilot mechanics
    MODEL-GEMINI.md                 Gemini mechanics
    MODEL-DEEPSEEK.md               DeepSeek mechanics
    MODEL-QWEN.md                   Qwen mechanics
    agents/openai.yaml              OpenAI and Codex interface manifest
  deep-research/
    SKILL.md                        contract and the seven steps
    SOURCING.md                     fan-out, query types, anti-SEO, escalation
    EVIDENCE.md                     run directory, two tables, confidence
    REPORT.md                       shape, section order, prose, word bands
    GATE.md                         twelve checks, ledger block, commands
    OUTPUT.example.md               reports directory override
    examples/                       one worked report
    agents/openai.yaml              OpenAI and Codex interface manifest
  skill-improvement/
    SKILL.md                        five phases, severity, the eight laws
    SURVEY.md                       inventory, contract, fact table
    GAUNTLET.md                     three reviewer briefs, rounds
    CRAFT.md                        five writing levers as checks
    GATE.md                         numbered checks and step map
    EVALS.md                        scenarios, fixtures, runs
    VARIANTS.md                     core, variant files, capability tables
    AUDIT.md                        eighteen checks, five of them reads
    REPORT.md                       review template
    examples/                       report, gate, eval README
    agents/openai.yaml              OpenAI and Codex interface manifest
  podcast-script/
    SKILL.md                        workflow and compiled text
    MODELS.md                       model registry and choosing rules
    MODEL-KOKORO-TONE.md            self-hosted gateway, the default
    MODEL-KOKORO-FASTAPI.md         OpenAI-compatible Kokoro server
    MODEL-KOKORO-RAW.md             kokoro Python package, no server
    MODEL-ELEVENLABS.md             ElevenLabs through OpenRouter
    PROFILE.md                      typed host profile and gate
    PERFORMANCE.md                  pacing, emotion, emphasis, moves
    TICKS.md                        tick library, density, banlist
    HANDOFF.md                      compile rules, text file, notes contract
    SCRIPT-CRAFT.md                 structure, prose, punctuation, attribution
    VOICE.md                        casting, rate, pause
    MULTIHOST.md                    two-host relationship and handoffs
    PANEL.md                        three or more hosts
    VERIFY.md                       release gate
    examples/                       host profile, beat map, solo, two-host, panel
    agents/openai.yaml              OpenAI and Codex interface manifest
  podcast-host-personas/
    SKILL.md                        workflow and the profile in one view
    references/                     schema, sound, emotion, show, gate
    examples/                       template and three filled personas
    personas/                       store and index
    agents/openai.yaml              OpenAI and Codex interface manifest

.claude-plugin/
  marketplace.json                  plugin marketplace for Claude Code, Codex, Copilot
  plugin.json                       plugin manifest and skill list

scripts/
  install.sh                        opencode, server, hermes, and shared agents

docs/
  install.md                        per-agent install detail
  prompt-engineer-flow.excalidraw   editable diagram source
  prompt-engineer-flow.png          rendered diagram

evals/
  skills/productivity/
    prompt-engineer/                three scenarios and their fixtures
    deep-research/                  four scenarios and their fixtures
    podcast-script/                 three scenarios and their fixtures
    podcast-host-personas/          three scenarios and their fixtures
    skill-improvement/              three scenarios, two fixtures
```

Review reports are written to `reviews/`, which is local and gitignored.

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md). Run `make check` before opening a pull request. It checks frontmatter, the plugin manifests, relative links, the version, and that no persona, review report, or secret is tracked.

## Versioning

Releases use CalVer, `YYYY.MM.MICRO`, tagged `vYYYY.MM.MICRO`. `VERSION` holds the current release and [CHANGELOG.md](CHANGELOG.md) records every one. To cut a release, move the unreleased entries into a dated section, update `VERSION`, then run `make tag`.

## Security

See [SECURITY.md](SECURITY.md). Report a secret, a destructive instruction, or impersonation privately through a GitHub security advisory.

## License

MIT. See [LICENSE](LICENSE).
