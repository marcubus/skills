# Element templates

These are the element shapes the compiler writes, for the two cases where a hand edit is legitimate: repairing a file a user sent, and adding one shape the schema cannot express. The block below is one real compile of `gateway`; your ids, text and geometry will differ. The gate reports a hand-edited scene as drift (`C27`); that is the point of the check.

The placeholders below (`$role.fill`, `$canvas`, `$ink`) stand for the hex values in the resolved token table. Write the table's hex; a literal hex outside the table is a gate failure (`C08`).

## Contents

- Common fields
- Rectangle, ellipse, diamond
- Node label
- Node note
- Free text
- Arrow
- Structural line
- Marker
- Bindings
- When to edit by hand

## Common fields

Every element carries:

```json
"id": "gateway",
"type": "rectangle",
"x": 345.5,
"y": 386,
"width": 260,
"height": 80,
"strokeColor": "$process.stroke",
"backgroundColor": "$process.fill",
"strokeWidth": 2,
"strokeStyle": "solid",
"fillStyle": "solid",
"roughness": 0,
"opacity": 100,
"angle": 0,
"seed": "<from the id>",
"version": 1,
"versionNonce": "<from the id>",
"isDeleted": false,
"groupIds": [],
"boundElements": [{"id": "gateway_t", "type": "text"}],
"link": null,
"locked": false,
"customData": {"kind": "node", "role": "process", "tier": "public"}
```

`customData` is the skill's provenance. Excalidraw keeps it; the gate reads it. Use one of the kinds below.

## Rectangle, ellipse, diamond

The only difference is `type` and, for a rectangle, `roundness`:

```json
"type": "rectangle",
"roundness": {"type": 3}
```

The node type follows the role table in `SKILL.md`, step 2.

## Node label

```json
{
  "id": "gateway_t",
  "type": "text",
  "x": 422.7,
  "y": 406.5,
  "width": 105.6,
  "height": 20,
  "text": "API gateway",
  "originalText": "API gateway",
  "fontSize": 16,
  "fontFamily": 3,
  "textAlign": "center",
  "verticalAlign": "middle",
  "strokeColor": "$process.text",
  "backgroundColor": "transparent",
  "strokeWidth": 1,
  "containerId": "gateway",
  "lineHeight": 1.25,
  "customData": {"kind": "node-label", "role": "process", "tier": "public"}
}
```

`fontFamily` 3 is the monospace face. Width and height come from measuring the text at `0.6 × fontSize` per character and `1.25 × fontSize` per line. A hand edit that changes the text must change the geometry too, or `C22` fires.

## Node note

A `note` is its own unbound text element, at 12px, below the label:

```json
{
  "id": "gateway_n",
  "type": "text",
  "x": 414.3,
  "y": 430.5,
  "width": 122.4,
  "height": 15,
  "text": "auth + rate limit",
  "fontSize": 12,
  "fontFamily": 3,
  "textAlign": "center",
  "verticalAlign": "top",
  "containerId": null,
  "lineHeight": 1.25,
  "customData": {"kind": "node-note", "role": "process", "tier": "public", "node": "gateway"}
}
```

It names its node in `customData.node` instead of binding through `containerId`; the node's `boundElements` does not list it. `C22` measures it against that node.

## Free text

Same as above, with `containerId: null`, no `boundElements`, and `verticalAlign: "top"`. Its colour is `$ink`, `$muted` or `$title`. Its `customData.kind` is `annotation`, `tier-label`, `edge-label`, `legend-label` or `title`.

## Arrow

```json
{
  "id": "e_queue",
  "type": "arrow",
  "x": 465.5,
  "y": 466,
  "width": 130,
  "height": 160,
  "strokeColor": "$muted",
  "backgroundColor": "transparent",
  "strokeWidth": 2,
  "strokeStyle": "dashed",
  "points": [[0, 0], [0, 54], [130, 54], [130, 160]],
  "startBinding": {"elementId": "gateway", "focus": 0, "gap": 2},
  "endBinding": {"elementId": "queue", "focus": 0, "gap": 2},
  "startArrowhead": null,
  "endArrowhead": "arrow",
  "customData": {"kind": "edge", "kind_name": "secondary", "source": "gateway", "target": "queue"}
}
```

`points` are relative to the arrow's `x`, `y`; `width` and `height` are the bounding box of those points. Every segment is horizontal or vertical. Both bindings point at real element ids, and each bound shape lists the arrow in `boundElements`.

## Structural line

```json
{
  "id": "spine",
  "type": "line",
  "x": 120,
  "y": 300,
  "width": 600,
  "height": 0,
  "strokeColor": "$muted",
  "backgroundColor": "transparent",
  "strokeWidth": 2,
  "strokeStyle": "solid",
  "points": [[0, 0], [600, 0]],
  "customData": {"kind": "line"}
}
```

## Marker

A 12px ellipse, stroke and fill the same token:

```json
"type": "ellipse",
"width": 12,
"height": 12,
"strokeColor": "$process.stroke",
"backgroundColor": "$process.stroke",
"customData": {"kind": "marker", "role": "process"}
```

## Bindings

A shape that receives or sends an arrow lists it:

```json
"boundElements": [
  {"id": "gateway_t", "type": "text"},
  {"id": "e_queue", "type": "arrow"}
]
```

An arrow with a binding to an element that does not exist is a broken file even when it renders. `C15` checks the arrow's geometry against the named endpoint, not only the binding.

## When to edit by hand

- Adding one shape the schema cannot express; the gate will report the drift.
- Repairing a file a user sent you, before deciding whether to rebuild it as a plan.

Anything larger goes back into the plan.
