# Install

Every route installs the same skills from `skills/productivity/`. Pick the route that matches your agent. Do not install the same skill twice through two routes, because the agent will list it twice.

Hosted assistants without a skill loader need the manual paste steps at the end. The same pattern works for each skill: paste its `SKILL.md` body, then upload its reference files.

## Platforms

The skills are text and folders, so they work on Linux, macOS, and Windows. The local installer needs bash: use Linux, macOS, WSL, or Git Bash. On Windows, pass `--copy` when symlinks are unavailable.

The gate blocks use a POSIX shell with `awk`, `grep`, and `sed`. On native Windows, run them in WSL or Git Bash. Each gate also carries a table that names the file or search operation and the pass condition for every command check, so an agent with no shell can run the same gate with its own tools. The hashing and timestamp checks name a macOS and Python alternative where the Linux command differs.

## Paths by agent

| Agent | Scope | Path |
| --- | --- | --- |
| OpenCode | Global | `~/.config/opencode/skills/` |
| OpenCode | Project | `<project>/.opencode/skills/` |
| OpenCode | Compatibility | `~/.agents/skills/`, `.agents/skills/` |
| Claude Code | Global | `~/.claude/skills/` |
| Codex, Cursor, Amp, Pi | Global | `~/.agents/skills/` |
| Codex, Cursor, Amp, Pi | Project | `.agents/skills/` |

## skills.sh, any agent

```bash
npx skills@latest add marcubus/skills
```

Omit `-a` to choose from the agents detected on your machine. Add `-a opencode` or `-a claude-code` to preselect. Add `-g` for a global install. Add `--skill prompt-engineer` for one skill.

The installer discovers `skills/productivity/<skill>/SKILL.md`, links the folders into each agent's skill directory, and records them in `skills-lock.json`.

Update with:

```bash
npx skills@latest update
```

Then re-run `add` to pick up skills added upstream.

## Local checkout, any agent

`scripts/install.sh` links the repo into any directory an agent reads skills from. Pass one or more destinations:

```bash
scripts/install.sh --dest ~/.config/opencode/skills
scripts/install.sh --dest ~/.claude/skills --dest ~/.agents/skills
scripts/install.sh --dest ~/.agents/skills --copy
```

The installer does not assume an agent name or a global layout. Use the destination that your agent documents. It expands `~`, `%USERPROFILE%`, `%APPDATA%`, and `%LOCALAPPDATA%`, and normalises backslashes in a Windows path. `--copy` copies instead of linking, `--dry-run` prints the plan, and `--force` replaces existing folders.

## OpenCode

```bash
npx skills@latest add marcubus/skills -a opencode
```

For a local checkout:

```bash
scripts/install.sh --dest ~/.config/opencode/skills
```

Manual install:

1. Copy or symlink each folder in `skills/productivity/` into `~/.config/opencode/skills/`.
2. Keep each folder intact, so `SKILL.md` and its reference files stay together.
3. Start a new session so OpenCode discovers the skill.
4. Ask in plain language, for example: write me a prompt for a non-technical executive summary, targeting ChatGPT.

You can also point OpenCode at the repo without copying:

```jsonc
{
  "skills": ["/path/to/skills-repo/skills/productivity"]
}
```

OpenCode combines every `skills` array, so the entry adds to the default directories.

Verify: the session lists `prompt-engineer` among available skills.

## Claude Code

```bash
claude plugin marketplace add marcubus/skills
claude plugin install marcubus-skills@marcubus
```

The plugin updates when the `version` in `.claude-plugin/plugin.json` changes.

Or use skills.sh:

```bash
npx skills@latest add marcubus/skills -a claude-code
```

## Codex

```bash
codex plugin marketplace add marcubus/skills
codex plugin add marcubus-skills@marcubus
```

Codex updates the plugin at startup.

Or use skills.sh:

```bash
npx skills@latest add marcubus/skills -a codex
```

## GitHub Copilot CLI and VS Code

```bash
copilot plugin marketplace add marcubus/skills
copilot plugin install marcubus-skills@marcubus
```

Then, once, add the marketplace to `~/.copilot/settings.json`:

```json
{
  "extraKnownMarketplaces": {
    "marcubus": {
      "source": { "source": "github", "repo": "marcubus/skills" },
      "autoUpdate": true
    }
  }
}
```

In VS Code, run **Chat: Install Plugin From Source** and enter `https://github.com/marcubus/skills`.

## Gemini CLI

Gemini installs one bucket at a time:

```bash
gemini skills install https://github.com/marcubus/skills.git --path skills/productivity
```

Re-run the command to update.

## Microsoft 365 Copilot

Regular Microsoft 365 Copilot Chat, not Copilot Studio.

1. Sign in at <https://m365.cloud.microsoft/chat>, or open Copilot in Teams.
2. Choose Create an agent, or open the Agents area and pick New agent.
3. Name the agent Prompt Engineer and give the agent a short description.
4. Paste the body of `skills/productivity/prompt-engineer/SKILL.md` into the Instructions box. Start at the `# Prompt Engineer` heading. The front matter is for skill loaders; the body is what the hosted assistant needs.
5. Under Knowledge, add the five model knowledge files from the same folder. Upload them from OneDrive or SharePoint, since Copilot grounds agents on Microsoft 365 content.
6. Save, then open the agent from Copilot Chat and describe the prompt you want.

If the tenant does not show the agent builder, start a Copilot chat, paste the SKILL.md body, then add the request on the next line.

## ChatGPT

Two options. Custom GPTs support knowledge files. Custom instructions apply to every chat.

### Custom GPT, knowledge files supported

1. Open ChatGPT and go to Explore GPTs, then Create.
2. Switch to the Configure tab.
3. Set the name to Prompt Engineer and add a short description.
4. Paste the body of `skills/productivity/prompt-engineer/SKILL.md` into the Instructions box.
5. Under Knowledge, upload the five model knowledge files.
6. Save, then set the access level for the GPT. Open the GPT and describe the prompt you want.

### Custom instructions, no files

1. Open Settings, then Personalization, then Custom instructions.
2. Paste the SKILL.md body into the field about how ChatGPT should respond.
3. Save. Start a new chat and describe the prompt you want.

Custom instructions have a length limit. If the body does not fit, paste the framework section and trim the model list.

## Gemini Gems

1. Open <https://gemini.google.com> and choose Gems in the sidebar.
2. Choose New Gem.
3. Name the Gem Prompt Engineer and add a short description.
4. Paste the SKILL.md body into the instructions field.
5. Attach the five model knowledge files if the plan allows uploads.
6. Save, then open the Gem and describe the prompt you want.

File attachments in Gems need a paid Google plan. Without uploads, paste the SKILL.md body into the first message of a chat and keep the Gem open.

## Claude Projects

1. Open <https://claude.ai> and go to Projects.
2. Choose New Project and name the project Prompt Engineer.
3. Open the project instructions and paste the SKILL.md body.
4. Add the five model knowledge files to the project knowledge.
5. Start a chat inside the project and describe the prompt you want.

Alternative without a Project: open Settings, then Profile, and paste the SKILL.md body into the custom instructions field. This applies to every chat and carries no knowledge files.

## Verify

Send this request on any platform:

> Write me a prompt for turning a meeting transcript into five action items with owners.

Check three things:

- The reply returns one finished prompt, with no preamble.
- The reply follows the style rules in SKILL.md: no em dashes, no banned words.
- The reply names the target model, or defaults to Claude when you do not name one.

## Tips

- Name the target model every time. Each model family has its own prompt mechanics.
- Say what the audience cares about. Non-technical executives beats general audience.
- Ask for a system prompt explicitly when you configure a bot.
- For images and documents, say what is attached and what to extract.
- Refine in place. Follow-ups adjust the same prompt rather than starting over.
