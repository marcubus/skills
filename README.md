# Skills Repository

A collection of agent skills for OpenCode, each implementing a specific productivity workflow.

## Skills (Alphabetical Order)

| # | Skill | Description |
|---|-------|-------------|
| 1 | **adr** | Record architecture decisions as ADRs |
| 2 | **bullshit** | Fact-check claims claim by claim |
| 3 | **create-diagram** | Draw Excalidraw diagrams that argue a point |
| 4 | **deep-research** | Research questions into cited reports |
| 5 | **podcast-host-personas** | Create machine-readable host personas |
| 6 | **podcast-script** | Turn documents into spoken scripts |
| 7 | **policy-review** | Review policies against personal data posture |
| 8 | **prompt-engineer** | Write/review prompts for LLMs |
| 9 | **skill-improvement** | Improve agent skills to fixed bar |
| 10 | **stoneman** | Compress responses to payload only, keep facts |

## Quick Start

```bash
# Clone repository
git clone git@github.com:marcubus/skills.git
cd skills

# Use with OpenCode agents
npx skills@latest add . --list
```

## Skill Details

### create-diagram (Position 3)

Draws Excalidraw diagrams that argue a point, simple or technical.

**Features:**
- Generates `.excalidraw` JSON from plan files
- Validates and auto-fixes diagrams before output
- Supports SVG and PNG output
- Agent-callable with no interactive prompts

**Usage:**
```bash
# Generate diagram from plan
python scripts/diagram layout test-diagram/plan.json -o test-diagram/diagram.excalidraw

# Render with Excalidraw renderer (requires Playwright setup)
cd skills/productivity/create-diagram/references
uv sync
uv run playwright install chromium
python render_excalidraw.py diagram.excalidraw --output output.png
```

**See:** `skills/productivity/create-diagram/README.md` for full documentation.

### Other Skills

Each skill has its own folder with:
- `SKILL.md` - Main documentation and workflow
- Reference files in subdirectories as needed

## License

MIT, © 2026 Marcus Ford. See the repository LICENSE.
