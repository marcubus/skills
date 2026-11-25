# Create diagram

Turns a subject into one Excalidraw diagram that argues a point: a plan compiled to JSON, colours bound to your terminal or base16 theme, and exact geometry checks before the render.

## Install

The skill is text; the compiler is `scripts/diagram` in this repository.

```bash
git clone git@github.com:marcubus/skills.git
cd skills
```

`npx skills@latest add marcubus/skills` copies the skill folder for agents that only need the text, but the compiler is not in that folder, so a copied skill cannot compile. Run everything from the repository root.

## Render setup

The skill includes two rendering options:

**Option 1: Simple SVG Renderer (Recommended)**
Works offline, no dependencies beyond Python. No setup needed!

```bash
# Generate and render a diagram
python scripts/diagram layout my-plan.plan.json -o my-diagram.excalidraw
python3 << 'EOF'
import sys
sys.path.insert(0, '/optimus/workspace/skills/skills/productivity/create-diagram/references')
from render_excalidraw import render
from pathlib import Path

png_path = render(Path('my-diagram.excalidraw'), Path('output.png'), 2, 1920)
print(f'Rendered: {png_path}')
EOF
```

**Option 2: Full Excalidraw Renderer (Interactive)**
For true Excalidraw rendering with editable output. Requires Playwright setup:

```bash
cd references
uv sync
uv run playwright install chromium
python render_excalidraw.py my-diagram.excalidraw
```

See `references/render-setup.md` for detailed setup instructions and troubleshooting.

See `references/render-setup.md` for detailed setup instructions and troubleshooting.

The plan and the gate work without any renderer; delivery needs the SVG/PNG, so choose your rendering option above.

## Use

Invoke the skill, for example `/create-diagram`, and name the subject. It hands back the artifacts in `SKILL.md`'s Output line.

### Agent Integration

The renderer is **agent-callable** with no interactive prompts:

```bash
# Basic call (default 3 iterations)
python scripts/diagram_render.py diagram.excalidraw -o output.svg

# With custom iterations
python scripts/diagram_render.py diagram.excalidraw --max-iterations 5 -o output.svg

# Agent adjustment pattern
python scripts/diagram_render.py diagram.excalidraw --adjust-iterations 2 -o output.svg
```

See `DIAGRAM_RENDERER_AGENT_READY.md` for integration patterns.

## Palette

The skill reads one palette; `references/palette-sources.md` gives the resolution order and the adapters. Create the canonical file with:

```bash
scripts/diagram palette --init
```



## Checking the work

`scripts/diagram check` runs the code checks in `GATE.md`: 28 configured with `--svg`, validating diagram structure, element placement, and connections.

## Gate proof

The gate ships a frozen pair for its own proof. Both commands pin `--palette` to the shipped file, so a host theme cannot change the result.

```bash
scripts/diagram check skills/productivity/create-diagram/examples/plan.json \
  --palette skills/productivity/create-diagram/examples/palette.json \
  --file skills/productivity/create-diagram/examples/fixtures/clean.excalidraw

scripts/diagram check skills/productivity/create-diagram/examples/plan.json \
  --palette skills/productivity/create-diagram/examples/palette.json \
  --file skills/productivity/create-diagram/examples/fixtures/broken.excalidraw
```

The clean scene prints `no mechanical findings`. The broken scene prints twelve findings across seven checks: `C08`, `C15`, `C16`, `C18`, `C22`, `C23`, `C27`. The last is determinism: a hand-edited scene no longer matches its plan.

## Attribution

The behavioural starting point was `coleam00/excalidraw-diagram-skill`, which carries no licence. This is a clean-room rewrite: no prose, code or assets from that project are copied. The plan format, the palette system, the compiler, the checks and the renderer here are original MIT work. Excalidraw itself is MIT and is used as a library at render time.

## Licence

MIT, © 2026 Marcus Ford. See the repository `LICENSE`.
