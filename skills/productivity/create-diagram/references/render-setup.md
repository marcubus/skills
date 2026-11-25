# Render setup

The renderer is real Excalidraw code in a headless browser, cached outside the skill. Setup runs once; renders are offline after it.

## Install the renderer

```bash
scripts/diagram setup
```

It does three things:

1. Creates a virtual environment at `~/.cache/excalidraw/venv` and installs `playwright` into it with `uv`.
2. Installs Playwright's Chromium build (skipped when it is already cached).
3. Bundles `@excalidraw/excalidraw@0.18.0`, React and React DOM with esbuild into `~/.cache/excalidraw/build/excalidraw.js`.

`uv` and `npm` are the only prerequisites, plus network access on the first run. The browser, the virtual environment and the bundle all live in the user's cache, outside the repository. Check 28 scans the skill folder, tracked or not, and fails if a runtime is vendored there.

Override the cache with `$EXCALIDRAW_CACHE` when the default home cache is not writable.

## Render

```bash
scripts/diagram render out.excalidraw                  # scale 2, page from the plan
scripts/diagram render out.excalidraw --scale 1
scripts/diagram render out.excalidraw --page a4-landscape
```

The PNG sits beside the `.excalidraw` file unless `-o` names another path. The command prints the path and the pixel dimensions.

`--page` crops to that page even when the plan used `none`: the content is drawn at its own coordinates and the page box decides the crop. `--scale` multiplies both dimensions; the delivered PNG is scale 2.

## How it renders

- The plan's elements go through `exportToSvg`, which returns an SVG with fonts embedded as base64.
- The SVG is placed on a white or dark page at the plan's coordinates, with the page size as the viewport.
- The browser screenshots the viewport at `device_scale_factor = scale`.
- No network request happens during a render. Chromium is launched from the Playwright cache.

## Failure modes

| Message | Meaning | Fix |
|---|---|---|
| `playwright is not installed` | The cached venv is missing | `scripts/diagram setup` |
| `renderer bundle missing` | Cache was cleared or built elsewhere | `scripts/diagram setup` |
| `Executable doesn't exist` at launch | Chromium was removed | `python -m playwright install chromium` in the venv |
| PNG is blank | The page is smaller than the content | `C23` should have caught it; recheck the plan |
| Text is 90° rotated | A hand edit changed `angle` | Revert the file and rebuild |

## What setup does not do

- No dark-mode-aware syntax colours. Evidence text uses the palette's ink and muted tokens.
- Animation and interactivity belong to the consuming app; the output is a scene and a still.
- No licence vendoring in the repository: the bundle carries Excalidraw's MIT licence into the cache, and the repository stays MIT.

## Checking a render

```bash
scripts/diagram check plan.json --file out.excalidraw --png out.png
```

This adds `C24`: the PNG signature and its dimensions against the page times the scale. A PNG of the wrong size means the render did not use the page the plan declared. Then read the image: the gate can measure it, only you can look at it.
