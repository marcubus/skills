# Scenario 2: palette binding

One plan, two palettes, from the repository root.

```bash
R=evals/skills/productivity/create-diagram/runs/default/2-palette
P=evals/skills/productivity/create-diagram/fixtures

EXCALIDRAW_PALETTE=$P/palette-paper.json \
  scripts/diagram layout $R/plan.json --palette $P/palette-paper.json -o $R/paper.excalidraw
# paper.excalidraw · 36 elements · paper (light)

EXCALIDRAW_PALETTE=$P/palette-slate.json \
  scripts/diagram layout $R/plan.json --palette $P/palette-slate.json -o $R/slate.excalidraw
# slate.excalidraw · 36 elements · slate (light)

scripts/diagram check $R/plan.json --palette $P/palette-paper.json --file $R/paper.excalidraw
# no mechanical findings, exit 0

scripts/diagram check $R/plan.json --palette $P/palette-slate.json --file $R/slate.excalidraw
# no mechanical findings, exit 0
```

## Comparison

Comparing `id`, `type`, `x`, `y`, `width`, `height`, `text` and `points` element for element:

- 36 elements in each file.
- 0 geometry differences.
- 36 of 36 elements differ in stroke or fill, which is the palette and nothing else.
- Canvas: `#fbfaf7` under paper, `#f7f8fa` under slate.

The plan, the text, the roles and the positions are identical. Only colour bytes differ, and the canvas moved with them.

## What this proves

The palette is a file, not a preference inside the skill. Swapping it re-colours the diagram without touching the argument. Passing `--palette` to `check` matters: without it the check resolves the shipped palette and reports `C08` and `C14` against a scene drawn with the user's theme.
