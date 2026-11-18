# Agent notes

Skills live in `skills/productivity/<skill>/SKILL.md`. Each skill is a self-contained folder. `SKILL.md` may point at reference files in the same folder, so install the whole folder.

Install routes:

- `npx skills@latest add marcubus/skills` for any supported agent.
- `.claude-plugin/` for the Claude Code, Codex, and Copilot plugin marketplaces.
- `scripts/install.sh` for a local checkout, into any agent skill directory via one or more `--dest` paths.

## Add or change a skill

1. Create or edit `skills/productivity/<name>/SKILL.md`.
2. Quote the `name` and `description` frontmatter values. An unquoted colon and space breaks YAML parsing, and the installer skips the skill.
3. Add the path to the `skills` array in `.claude-plugin/plugin.json`.
4. Add the skill to `skills/productivity/README.md` and the top-level `README.md`.
5. Add evals under `evals/skills/productivity/<name>/`.
6. Run `npx skills@latest add . --list` and check the skill appears.

## Style

Write plain prose. Keep em dashes out. Use short sentences and active voice.
