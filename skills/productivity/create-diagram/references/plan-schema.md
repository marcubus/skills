# Plan schema

The field table lives in `SKILL.md`, step 5, because every run reads it. This file owns the rules behind those fields: tiers, sizing, routing constraints, the structure layer, declarations, validation and metadata.

## Contents

- Tiers
- Elements
- Edges
- Structure layer
- Declarations
- Validation
- Output metadata

## Tiers

A **tier** is one rung of the flow: a trust boundary, a phase or a depth. Its drawn region is a **band**: a row in a stack, a column in a conveyor. The list order is the flow order, outermost first.

```json
"tiers": [
  {"id": "outside", "label": "Outside"},
  {"id": "public", "label": "Public"},
  {"id": "private", "label": "Private network"}
]
```

A bare string works: `"tiers": ["outside", "public", "private"]`. Its label is the id, title-cased. Ids are unique. A label is optional except for an empty break tier.

A tier with no members but a label renders its label and reserves a 100px band. That is the gap/break pattern.


## Elements

An **element** is one entry in the plan; the box it compiles to is a **node**. An element's width is measured from its text in the monospace face and rounded up to the 20px grid, clamped to 120..480. A label longer than about 24 characters makes a wide box; shorten it or move detail to `note`. The compiler does not wrap.

`note` renders as a second line inside the same box, in smaller type. `size` sets the height: `small` 50px, `normal` 60px, `hero` 90px.

`order` places an element inside its tier. Lower goes first: left to right in a stack band, top to bottom in a conveyor column. Ties keep plan order. Order siblings by where their connections land in the next tier; a swap produces a crossing.

Siblings in one tier read as parallel. For a sequential disposition, chain the steps through later tiers instead of fanning them: `send -> retry -> support`, not both out of `send`.

`x` and `y` replace `tier` and `order` together, though the plan still declares at least one tier. The element keeps its role, shape and token colours, and the page check still applies. Use it for a cloud of overlapping shapes or a deliberately irregular composition. Escaped elements do not join a tier, so the sibling checks skip them; arrows to them still use the fixed ports, so place the box where that port makes sense.

## Edges

An edge joins two different tiers. Two elements in one tier is a peer link: move one into the next tier, or place both with explicit `x` and `y` and join them with a `line`. A line is a plain connector, so label it with an annotation. Do not invent a tier to order peers. The compiler refuses the plan rather than inventing a route.

`kind` colours and styles the arrow:

| Kind | Meaning | Render |
|---|---|---|
| `primary` | the main path | solid, process stroke |
| `secondary` | a side path, retry or async | dashed, muted |
| `exception` | a failure path | solid, exception stroke, listed for review |

`label` sits on the longest segment, above a horizontal run or beside a vertical one. A label wider than its run moves beside the route's vertical leg, or above the band when there is none. Keep a label near 24 characters, the element budget. A longer one is measured at 14px and placed on the side its edge is heading, so two long labels from one source sit on opposite sides rather than on each other.

## Structure layer

Use it when the drawing needs a spine, a bracket, a timeline or a label that belongs to no box.

| Kind | Fields | Notes |
|---|---|---|
| `lines` | `id`, `x`, `y`, `points`, `tone`, `strokeStyle`, `strokeWidth` | Points are relative to `x`, `y`; segments must be orthogonal; tone is `muted`, `border`, `ink` or `title` |
| `markers` | `id`, `x`, `y`, `role` | A 12px ellipse in the role stroke colour |
| `annotations` | `id`, `text`, `x`, `y`, `fontSize`, `tone`, `align` | 14px by default; never contained |

```json
"lines": [
  {"id": "spine", "x": 120, "y": 300, "points": [[0, 0], [600, 0]], "tone": "muted"}
],
"markers": [
  {"id": "m1", "x": 200, "y": 294, "role": "process"}
],
"annotations": [
  {"id": "n1", "text": "one batch per hour", "x": 120, "y": 320, "tone": "muted"}
]
```

Annotations are measured at their `fontSize` (14 by default) and do not wrap; about 50 characters fits from x 60 on A4, and `C23` fails one that crosses the page box. Coordinates are absolute from the page's top-left. With a title the first band starts at y 116; without one, y 80; the left margin is x 60. A tier label sits at its band's top left, so keep hand-placed structure clear of it.

In a stack, a node sits 40px below its band top and is 60px tall (`small` 50, `hero` 90); a `note` adds 20px. A band is the tallest node in the tier plus 80px, and bands are 80px apart, so band tops advance by that node height + 160. The last node's bottom is the content bottom; place a below-content annotation just under it and clear of the legend. There is no separate content-height read: use this arithmetic. On `page: none` the page grows to include the annotation, so a y that is too high lands it in a node rather than enlarging the page. The worked example is one such placement. An empty tier with a label is 100px tall and advances 180px. In a conveyor, columns advance by the widest node plus the tier gutter, which `references/composition.md` owns. A stack reserves a left gutter as wide as its longest tier label plus 40px, so tier labels never meet an inbound arrow. The page box and the content-sized page both account for structure elements.

## Declarations

```json
"crossings": [{"a": "e1", "b": "e2", "reason": "the retry path must cross the commit path"}],
"substitutions": [{"roles": ["warning", "external"], "reason": "the palette gives both the orange slot"}]
```

Both are **declarations**: the plan admits the crossing or the collision and gives the reason. A declaration is not a fix. The gate accepts one because the plan states why; the review still names it.

## Validation

`layout` stops with a message when:

- the plan has no elements;
- an unknown field appears on the plan, an element or an edge;
- an id repeats, or an element, tier or endpoint is missing;
- a role is not one of the nine;
- an element has both a tier and `x`/`y`, or neither;
- an edge joins two elements in the same tier, or has an unknown kind;
- the shape or page name is unknown.

## Output metadata

The compiled file keeps the provenance under `_diagram`:

```json
"_diagram": {
  "schema": 1,
  "shape": "stack",
  "page": {"name": "a4", "width": 794, "height": 1123},
  "palette": {"name": "<name>", "source": "<source>", "variant": "<light|dark>"},
  "tokens": {"canvas": "<hex>", "process.fill": "<hex>"},
  "planSha": "…"
}
```

`check` reads it. Excalidraw ignores it.
