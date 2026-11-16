# Changelog

All notable changes to this repository are recorded here.

Versions use CalVer in the form `YYYY.MM.MICRO`. `MICRO` starts at `0` each
month and increments per release; tags are prefixed with `v`. `VERSION` holds
the current release, and the release workflow refuses a tag that disagrees with
it.

## [Unreleased]

### Added

- `policy-review`: reads a privacy policy, terms of service, EULA, or cookie
  notice against a personal data posture. Six gates and eleven preferences,
  a phrase catalogue mapped to posture IDs, an Australian regulatory map, and a
  reply that names the worst flag and calls nothing a show
  stopper. The posture lives in a gitignored `POSTURE.local.md`, so personal
  detail never reaches the repository.

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
