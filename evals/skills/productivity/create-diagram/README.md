# Create diagram evals

Three scenarios. Scenario 1 needs an agent; scenarios 2 and 3 are reproducible from the command line and a run of each is recorded under `runs/default/`.

## Scenarios

| # | Input | Exercises | Passes when |
|---|---|---|---|
| 1 | `fixtures/scenario-1.md`, a technical brief | The main path: ledger, plan, gate, one render | The .excalidraw and .png exist; the gate exits 0; the PNG was viewed; at most two renders ran; every label traces to a ledger line |
| 2 | `fixtures/plan.json` with `palette-paper.json`, then `palette-slate.json` via `$EXCALIDRAW_PALETTE` | Palette binding | Layout, text, roles and positions are identical between runs; only colour bytes differ; both gates exit 0 |
| 3 | `fixtures/broken.excalidraw` against `fixtures/plan.json` | The gate's trap detectors plus drift | Seven checks fire: `C08`, `C15`, `C16`, `C18`, `C22`, `C23`, `C27`; the clean fixture reports nothing |

## Fixtures

| File | What it is |
|---|---|
| `scenario-1.md` | The technical brief for scenario 1 |
| `plan.json` | A worked stack plan, the same one as `examples/plan.json` |
| `clean.excalidraw` | That plan compiled, passing every mechanical check |
| `broken.excalidraw` | The clean file with six planted defects and the drift they cause |
| `palette-paper.json` | The seed palette, light variant |
| `palette-slate.json` | A second light palette with the same slot count |

The broken file carries one defect per check:

| Check | Defect |
|---|---|
| `C08` | `gateway.backgroundColor` is `#dee4ec`, one digit off a token |
| `C15` | `e_service` leaves its source inside the shape, and `e_db` enters its target on the wrong side |
| `C16` | `trap_cross` runs through `e_client` in the gutter |
| `C18` | A waypoint in `e_db` makes two diagonal segments |
| `C22` | `gateway_t` is 400px wide inside a 240px box |
| `C23` | `db` is moved to the right edge of the page |
| `C27` | Every hand edit above makes the scene differ from a rebuild |

## Expectations

Scenario 1, every bullet naming its file:

- `1-technical/brief.txt` opens with a depth line naming technical, and names at least one evidence artifact.
- `1-technical/ledger.txt` carries one line per label, and each line names its source.
- `1-technical/sse-patch.plan.json` compiles, and the gate exits 0 on `1-technical/sse-patch.excalidraw`.
- `1-technical/sse-patch.png` is 2246 × 1588 (A4 landscape at scale 2), and the reply shows it was viewed.
- `1-technical/reply.md` names the brief, the ledger, the plan, the scene, the PNG and the palette source, and records at most two renders.

Scenario 2, every bullet naming its file:

- `2-palette/paper.excalidraw` and `2-palette/slate.excalidraw` hold the same number of elements.
- `id`, `type`, `x`, `y`, `width`, `height`, `text` and `points` match element for element across the pair.
- Every `strokeColor` and `backgroundColor` is a token from its own run's palette.
- `2-palette/reply.md` records the comparison.

Scenario 3, every bullet naming its file:

- `3-gate/reply.md` shows exit 0 and `no mechanical findings` for `3-gate/clean.excalidraw`.
- `3-gate/reply.md` shows exit 1 for `3-gate/broken.excalidraw`, with `C08`, `C15`, `C16`, `C18`, `C22`, `C23` and `C27` each present.
- The six fixture files are byte-identical before and after the run.

## Running

From the repository root:

```bash
scripts/diagram check evals/skills/productivity/create-diagram/fixtures/plan.json \
  --palette evals/skills/productivity/create-diagram/fixtures/palette-paper.json \
  --file evals/skills/productivity/create-diagram/fixtures/clean.excalidraw

scripts/diagram check evals/skills/productivity/create-diagram/fixtures/plan.json \
  --palette evals/skills/productivity/create-diagram/fixtures/palette-paper.json \
  --file evals/skills/productivity/create-diagram/fixtures/broken.excalidraw
```

The clean run exits 0 with `no mechanical findings`. The broken run exits 1 and names each of the seven checks at least once, twelve findings in all. A check that goes silent is a regression in the gate.

Scenario 2:

```bash
EXCALIDRAW_PALETTE=evals/skills/productivity/create-diagram/fixtures/palette-paper.json \
  scripts/diagram layout evals/skills/productivity/create-diagram/fixtures/plan.json -o paper.excalidraw
EXCALIDRAW_PALETTE=evals/skills/productivity/create-diagram/fixtures/palette-slate.json \
  scripts/diagram layout evals/skills/productivity/create-diagram/fixtures/plan.json -o slate.excalidraw
```

Compare the two files with colours stripped: `id`, `type`, `x`, `y`, `width`, `height`, `text`, `points` must match element for element.

## Recorded runs

Each scenario has its own folder under `runs/default/`, with a copy of the fixture it used.

- `1-technical/`: the agent's brief, ledger, plan, scene, PNG and reply.
- `2-palette/`: both palettes, both scenes, and `reply.md` with the comparison.
- `3-gate/`: the clean and broken scenes, and `reply.md` with the gate output.

Scenario 1 is recorded only when an agent has actually drawn the diagram; a fabricated reply is worse than a missing run.
