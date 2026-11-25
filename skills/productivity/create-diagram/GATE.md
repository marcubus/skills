# Gate

Twenty-eight checks. Twenty-four run as code; four are named reads.

```bash
scripts/diagram check <name>.plan.json --file <name>.excalidraw --png <name>.png
```

Paths are repository-relative. Exit 0 means every code check that had what it needed passed; `C24` needs `--png`. A finding prints `C<n>` and the reason. `--only <n>[,<n>...]` runs the named code checks; checks 1, 2, 25 and 26 are named reads. The frozen clean and broken pair that proves these checks is in `README.md`.

## Contents

- Step map
- Checks
- When a check fires

## Step map

The map names the step whose decision each check covers; every code check runs with whichever command that step uses.

| Step | Checks |
|---|---|
| 1. Classify the depth | 1 |
| 2. Bind the palette | none |
| 3. Research into a ledger | none |
| 4. Argue it before you draw it | none |
| 5. Write the plan | 3, 4, 5, 6 |
| 6. Run the gate | 2, 7-23, 27, 28 |
| 7. Render once and look | 25 |
| 8. Deliver | 24, 26 |

## Checks

**1. Depth.** Read brief.txt: one line names simple or technical, and a technical plan names at least one evidence artifact. Done when the depth is stated and a technical plan carries at least one artifact.

**2. Facts.** Read every carried text in the plan against ledger.txt. Done when each has a ledger line with a source, and no name was paraphrased. A simple plan, with no evidence set, marks this not applicable.

**3. Contract.** The plan resolves a shape (explicit or default), declares at least one tier, and has edges whose endpoints exist. Done when `C03` is absent.

**4. Role.** Every element carries exactly one role from the nine. Done when `C04` is absent.

**5. Tier.** Every element names one declared tier, or is placed with explicit `x` and `y` and no tier. Done when `C05` is absent.

**6. Edge.** Every edge has a kind (`primary`, `secondary`, `exception`) and two existing endpoints. Done when `C06` is absent.

**7. Palette provenance.** The output records the palette name, its source and its variant. Done when `C07` is absent.

**8. Token closure.** Every colour in the file, including the canvas, belongs to the resolved token table. Done when `C08` is absent; any hex it prints is a hand edit.

**9. Text on fill.** Text reaches 4.5:1 against the fill it sits on, or the canvas when free. Done when `C09` is absent.

**10. Stroke on fill.** A shape border reaches 3:1 against its own fill. Done when `C10` is absent.

**11. Stroke on canvas.** Every border, arrow, line and marker reaches 3:1 against the canvas. Done when `C11` is absent.

**12. Hue step.** Two roles do not resolve to one hue at a comparable lightness, unless the plan declares the substitution with a reason. Near-neutral fills are exempt: grey is its own signal. Done when `C12` is absent.

**13. Legend.** Three or more roles carry a legend naming each one, unless the plan sets `legend: false`. Done when `C13` is absent.

**14. Canvas.** The background is the palette canvas, and the recorded variant agrees with its luminance. Done when `C14` is absent.

**15. Ports.** Every arrow leaves its source on the shape's outgoing side and enters its target on the incoming side. Done when `C15` is absent.

**16. Crossings.** No arrow crosses another, and none runs through an unrelated node. A crossing that must stay is listed in the plan's `crossings` with a reason. Done when `C16` is absent.

**17. Shared runs.** Two arrows never sit on the same line for more than a pixel. Done when `C17` is absent.

**18. Orthogonal.** Every arrow and structural line segment is horizontal or vertical. Done when `C18` is absent.

**19. Tiers.** Tiers follow the plan's order and their bands do not overlap. Done when `C19` is absent.

**20. Siblings.** Elements in one tier align on the cross axis, and the gap between them is at least 40px. Done when `C20` is absent.

**21. Free text is free.** Free text never sits inside a container, and no two pieces overlap. A node's `note` is not free text: it belongs to its node. Done when `C21` is absent.

**22. No clipped text.** Every contained label fits inside its container with padding, and its declared size matches the measured text. Done when `C22` is absent.

**23. Page box.** Every element sits inside the page, clear of a 20px edge. Done when `C23` is absent.

**24. PNG size.** The rendered PNG is the page size at scale 1 or 2. Done when `C24` is absent; without `--png` the check does not run and the exit code does not cover it. A `page: none` diagram has no fixed size, so `C24` skips it; step 7 look 3 covers the page extent.

**25. Seen.** Read the PNG with the file-read tool at full size. Done when you can answer the four looks from step 7, every visible defect is fixed or listed in the reply with a reason, and every accepted declaration is named.

**26. Final scale.** The PNG read in step 7 was produced with `--scale 2`, and where the page is fixed, `C24` passes at that size. Done when the render command and the dimensions agree.

**27. Determinism.** Rebuilding the same plan and palette produces the same scene. Done when `C27` is absent.

**28. No vendored runtime.** No file in the skill folder, tracked or not, is a browser, a bundle, `.venv` or `node_modules`; the renderer lives in its cache, `~/.cache/excalidraw` by default. It runs on every full `check`; `--only` narrows the run. Done when `C28` is absent.

## When a check fires

Rerun `layout`, then the check. If the finding survives a plan fix, read the reference `SKILL.md` names for that branch, where one is named.
