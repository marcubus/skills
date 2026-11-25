# Excalidraw JSON

The facts the compiler relies on. The file format is Excalidraw's; this page records what it accepts and what it drops.

## Contents

- Scene top level
- Node types used
- Common properties
- Text properties
- Arrows
- Lines
- Roundness
- What Excalidraw changes
- Rendering

## Scene top level

```json
{
  "type": "excalidraw",
  "version": 2,
  "source": "scripts/diagram",
  "elements": [],
  "appState": {"viewBackgroundColor": "<canvas token>", "gridSize": 20},
  "files": {}
}
```

`type` is the literal `excalidraw`; `version` 2 is the current scene schema. `files` holds embedded images and stays empty. `appState` is the view state; only `viewBackgroundColor` and `gridSize` matter here. The compiler adds a `_diagram` key, which Excalidraw ignores and preserves on load in practice; treat it as read-only provenance.

## Node types used

| Type | Notes |
|---|---|
| `rectangle` | node and legend swatch |
| `ellipse` | node and marker |
| `diamond` | decision node |
| `text` | node labels, annotations, tier labels, edge labels, legend labels |
| `arrow` | edges |
| `line` | structural lines |

The role-to-node-type binding is in `SKILL.md`, step 2. 

## Common properties

| Property | Type | Notes |
|---|---|---|
| `id` | string | Unique in the file; the compiler derives it from the plan id |
| `x`, `y` | number | Top-left in scene coordinates |
| `width`, `height` | number | Bounding box; for arrows and lines, the bbox of `points` |
| `strokeColor` | string | Hex, or `"transparent"` |
| `backgroundColor` | string | Hex, or `"transparent"` |
| `fillStyle` | string | `solid` for every filled shape here |
| `strokeWidth` | number | 1, 2 or 4 as drawn by Excalidraw; the compiler uses 2 |
| `strokeStyle` | string | `solid`, `dashed`, `dotted` |
| `roughness` | number | 0 keeps the geometry exact; the compiler always uses 0 |
| `opacity` | number | 100; hierarchy comes from colour and size |
| `angle` | number | Radians; always 0 |
| `seed` | number | Deterministic from the element id, so renders repeat |
| `version`, `versionNonce` | number | Derived, not random, for byte-identical output |
| `isDeleted` | boolean | Always false; deleted elements are removed |
| `groupIds` | array | Empty |
| `boundElements` | array or null | Text and arrows attached to a shape |
| `link` | string or null | Always null |
| `locked` | boolean | False |
| `customData` | object | The skill's `kind`, `role`, `tier`, edge endpoints, or a note's node id |

## Text properties

| Property | Notes |
|---|---|
| `text` | The visible words, including `\n` |
| `originalText` | Same as `text`; Excalidraw keeps the pre-wrap source here |
| `fontSize` | 13 for tier labels, 14 for annotations, 16 for node text, 22 for the title |
| `fontFamily` | 3 (monospace) |
| `textAlign` | `left`, `center`, `right` |
| `verticalAlign` | `top`, `middle`, `bottom` |
| `containerId` | Parent shape id, or null |
| `lineHeight` | 1.25 |

A node's label is a separate element bound both ways: the shape lists it in `boundElements`, the text names the shape in `containerId`. A node's `note` is a second text element at 12px with `containerId: null` and `customData` `{"kind": "node-note", "node": "<id>"}`; it is not bound. Either text is positioned by its own `x`, `y`, not by the container.

## Arrows

| Property | Notes |
|---|---|
| `points` | Array of `[x, y]` relative to the arrow origin; first point is `[0, 0]` |
| `startBinding`, `endBinding` | `{"elementId": "...", "focus": 0, "gap": 2}` or null |
| `startArrowhead` | null |
| `endArrowhead` | `"arrow"` |

Orthogonal routes use two or more segments. Diagonal segments are legal to Excalidraw and rejected by the gate.

## Lines

`points` as for arrows, with no bindings and no arrowheads. Lines are shapes for layout purposes; they do not bind.

## Roundness

```json
"roundness": {"type": 3}
```

Only on rectangles. Omit for diamonds and ellipses.

## What Excalidraw changes

Opening and saving a file in Excalidraw may:

- add default properties (`strokeSharpness`, `frameId`, `index`) to elements;
- reorder elements within a frame, or add `index` ordering;
- drop unknown top-level keys other than `_diagram` in some versions;
- re-measure text if the font is unavailable.

None of that matters for the gate, which runs on the file the compiler wrote. It does mean a file a user has opened and saved is no longer byte-identical.

## Rendering

`exportToSvg` from `@excalidraw/excalidraw` takes `{elements, appState, files}` and returns an SVG at the scene's bounding box. The compiler passes `exportScale: 1` and gives the SVG explicit pixel dimensions; the browser screenshot applies `--scale`. Fonts are embedded as base64 in the SVG, so a render needs no network.
