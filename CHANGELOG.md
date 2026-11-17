# Changelog

All notable changes to this repository are recorded here.

Versions use CalVer in the form `YYYY.MM.MICRO`. `MICRO` starts at `0` each
month and increments per release; tags are prefixed with `v`. `VERSION` holds
the current release, and the release workflow refuses a tag that disagrees with
it.

## [Unreleased]

## [2026.11.1] - 2026-11-17

### Added

- `deep-research`: researches a question into one cited report that stands
  alone. Seven steps, two evidence tables with a verbatim quote per claim,
  query fan-out with intent routing, anti-SEO and primary-source rules, a
  twelve-check gate with a shell ledger block, and an output path override
  that stays local.
- `policy-review`: reads a privacy policy, terms of service, EULA, or cookie
  notice against a personal data posture. Six gates and eleven preferences,
  a phrase catalogue mapped to posture IDs, an Australian regulatory map, and a
  reply that names the worst flag and calls nothing a show
  stopper. The posture lives in a gitignored `POSTURE.local.md`, so personal
  detail never reaches the repository.
- `skill-improvement`: a fourth gauntlet reviewer for voice (R10 to R14), R14
  for an idea that should collapse to one leading word, audits A20 and A21,
  laws 9 and 10, and a lens pass after the gauntlet exits.

### Changed

- `podcast-script`: kokoro-tone renders a long episode in capped requests,
  breaking at pauses then turn boundaries, repeating the sticky voice and rate
  at every seam, and recording the split in the notes.

## [2026.11.0] - 2026-11-14

First tagged release. The repository is now four skills with evals, a single
installer, and plugin manifests for the Claude Code, Codex, and Copilot
marketplaces.

### Added

- `podcast-host-personas`: builds one gated, machine-readable host persona per
  show. A 29-check gate, a persona schema with 35 rules, a generator procedure,
  four worked examples, and a local gitignored persona store.
- `podcast-script`: turns a report or raw notes into a spoken script and the
  plain text a text-to-speech model reads, for solo, two-host and panel shows,
  targeting kokoro-tone, kokoro-fastapi, kokoro-raw and ElevenLabs.
- `prompt-engineer`: writes, revises, or critiques a prompt for a resolved
  target model, with per-model mechanics for Claude, GPT/Copilot, Gemini,
  DeepSeek and Qwen.
- `skill-improvement`: reviews an existing skill and takes it to a fixed bar
  through three reviewer rounds, a numbered gate, and an eval suite.
- Evals for every skill under `evals/skills/productivity/`, outside the skill
  folders, with fixtures and recorded runs.
- `scripts/install.sh`, with targets for OpenCode, the OpenCode server user,
  Hermes, and shared agent directories.
- `.claude-plugin/` manifests so the repository installs as a plugin in the
  Claude Code, Codex, and Copilot marketplaces.
- `scripts/check.py` and `make check`: frontmatter, manifest, link, version,
  secret and local-only checks, run in CI on every push and pull request.
- CalVer release flow: `VERSION`, this changelog, an annotated `vYYYY.MM.MICRO`
  tag, and a release workflow that verifies the tag and publishes notes.

### Changed

- Skills moved to `skills/productivity/<skill>/` and evals to
  `evals/skills/productivity/<skill>/`, so the skill folder holds only what the
  agent reads.
- Review reports are local and gitignored. They are a snapshot of one audit and
  go stale as the skill moves.

### Removed

- The root `productivity` compatibility symlink and the `CLAUDE.md` symlink.
  `AGENTS.md` is the one agent-notes file.
