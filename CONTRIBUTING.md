# Contributing

Thanks for taking a look. This repository is a set of agent skills, so most
changes are prose, and the bar is that the prose is executable: an agent reads
it and does the right thing without asking a question the skill should have
answered.

## Before you start

- Open an issue for a new skill, or for a change that alters what a skill
  refuses or requires. Small fixes can go straight to a pull request.
- Read `AGENTS.md` for the layout and the house style.
- Read the skill you are changing, and its `GATE.md` if it has one. The gate is
  the contract, not a suggestion.

## Add or change a skill

1. Create or edit `skills/productivity/<name>/SKILL.md`.
2. Quote the `name` and `description` frontmatter values. An unquoted colon and
   space breaks YAML parsing, and the installer silently skips the skill.
3. Add the skill path to the `skills` array in `.claude-plugin/plugin.json`.
4. Add the skill to `skills/productivity/README.md` and the top-level
   `README.md`.
5. Add evals under `evals/skills/productivity/<name>/`. A scenario needs a
   brief, the expected result, and a recorded run.
6. Run `make check`, or `python3 scripts/check.py` plus `bash -n
   scripts/install.sh`, and check both pass. On Windows, use `python` or
   `py -3` in place of `python3`.

A skill folder holds only what the agent reads at run time: `SKILL.md`, its
reference files, examples, and an `agents/openai.yaml` manifest. Evals live
outside it on purpose, because the skill never reads them and only the tester
does.

## Style

Write plain prose. Keep em dashes out. Use short sentences and active voice.
Prefer a table when the reader will scan, and a numbered list when the order
matters. Do not write "simply", "just", or "obviously".

A rule that cannot be checked is a wish. If you add a requirement, say where it
is verified: a gate check, an eval, or `scripts/check.py`.

## Commits and pull requests

- One change per commit, in the imperative mood: `Add podcast-host-personas`,
  not `Added ...` or `Fixes ...`.
- Fill in the pull request template, including the test plan.
- `make check` must pass before review.
- Do not commit a generated persona, a review report, or a secret. All three are
  gitignored, and `scripts/check.py` fails the build if one slips in.

## Versioning and releases

Versions use CalVer, `YYYY.MM.MICRO`. `MICRO` starts at `0` each month and
increments per release. Tags are `vYYYY.MM.MICRO`.

To release:

1. Move the entries under `## [Unreleased]` in `CHANGELOG.md` into a new
   `## [YYYY.MM.MICRO] - YYYY-MM-DD` section.
2. Write the same version to `VERSION`.
3. Commit, then `make tag`. It refuses a dirty tree or a tag that already
   exists.
4. `git push origin main --follow-tags`.

The release workflow checks that the tag matches `VERSION`, that the changelog
has an entry for it, and then publishes a GitHub release with generated notes.

## Reporting a bug

Use the bug report template. Include the skill, the model or agent you ran it
in, the brief you gave, and what came back. If the output is a persona or a
script, paste the profile or the compiled text, not a screenshot.

For a security issue, follow `SECURITY.md` instead of opening an issue.
