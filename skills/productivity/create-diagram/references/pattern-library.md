# Pattern library

Nine patterns, each a way of arguing with structure. A plan uses one dominant pattern; a comprehensive diagram may use two. Eight compile as a plan; the spine is a structure fragment you add to one, because a plan needs at least one element and one tier.

## Contents

- 1. Fan-out
- 2. Convergence
- 3. Tree
- 4. Cycle
- 5. Cloud
- 6. Assembly line
- 7. Side by side
- 8. Gap and break
- 9. Spine

## 1. Fan-out

One thing produces many. Use for a single source with many parallel consequences; a sequence of consequences is a chain through later tiers.

```
        ┌── target A
source ─┼── target B
        └── target C
```

```json
"tiers": [{"id": "origin", "label": "Origin"}, {"id": "out", "label": "Fan-out"}],
"elements": [
  {"id": "hub", "role": "start", "tier": "origin", "text": "Webhook"},
  {"id": "a", "role": "process", "tier": "out", "order": 0, "text": "Billing"},
  {"id": "b", "role": "process", "tier": "out", "order": 1, "text": "Search"},
  {"id": "c", "role": "process", "tier": "out", "order": 2, "text": "Audit"}
],
"edges": [
  {"id": "e_hub_a", "from": "hub", "to": "a"},
  {"id": "e_hub_b", "from": "hub", "to": "b"},
  {"id": "e_hub_c", "from": "hub", "to": "c"}
]
```

Gotcha: order the targets by importance, because the middle arrow is the one the eye follows.

## 2. Convergence

Many things become one. Use for a many-into-one step.

```
input A ─┐
input B ─┼─► result
input C ─┘
```

Swap the fan-out's edges. Keep the sources in one tier and the result in the next; the arrows meet at one port with 20px offsets, so the funnel reads without an explicit merge shape.

Gotcha: three sources is the ceiling before the middle one hides the others. Four or more wants a `note` on the result instead.

## 3. Tree

Hierarchy without a flow. Use for a taxonomy.

```
root
├── branch A
│   ├── leaf
│   └── leaf
└── branch B
```

Model it as levels: root in tier 0, branches in tier 1, leaves in tier 2, with one arrow per parent-child link. If the arrows make the tree look like three separate flows, drop the arrows and draw brackets with `lines`, then place the labels as `annotations`.

Gotcha: a tree with arrows claims causality. If the relation is containment, say so with an annotation or use brackets.

## 4. Cycle

A loop with a way back. Use for feedback.

```
  A ──► B
  ▲     │
  └─ C ◄┘
```

Put A, B and C in three consecutive tiers, with the forward edges normal and one reverse edge from C to A. The reverse edge takes the channel beside the bands and enters A from its incoming side.

Gotcha: with four or more nodes, the reverse edge crosses the middle tier. Split it into two diagrams, or declare the crossing and keep it perpendicular. A loop node with a second outbound edge, such as a lockout, cannot route cleanly in either sibling order: split it or list the pair in `crossings` with a reason.

## 5. Cloud

Overlapping shapes for a boundary that has no clean edge.

```json
"page": "none",
"tiers": [{"id": "state", "label": "State"}],
"elements": [
  {"id": "ctx", "role": "agent", "text": "Conversation", "x": 100, "y": 100},
  {"id": "mem", "role": "agent", "text": "Memory", "x": 180, "y": 120},
  {"id": "tool", "role": "external", "text": "Tools", "x": 250, "y": 90}
],
"annotations": [{"text": "shared context", "x": 110, "y": 190}]
```

Ellipses overlap by design; the escape hatch is the point. No arrows, or one labelled arrow to the rest of the diagram.

Gotcha: overlapping boxes hide the labels underneath. Keep the overlap under a third of each shape and put the label in the top shape.

## 6. Assembly line

Input, transformation, output, with the change visible. Use for a conversion.

```
raw ──► [ transform ] ──► shaped
```

Three tiers, three elements: `external` input, `process` middle (the `hero`), `outcome` output. The evidence belongs in the `note` or an adjacent annotation: the actual input shape, the actual output shape.

Gotcha: the middle box is where the argument lives. If it says "process", replace it with the real step.

## 7. Side by side

Two options, or before and after. Use for a comparison.

A conveyor with five columns: option A's two steps, then a gap tier, then option B's two steps. Same roles on both sides so the comparison is about content, not colour.

Gotcha: colour asymmetry reads as a verdict. If one side is the recommendation, say so in an annotation, not with a different role.

## 8. Gap and break

Whitespace as a phase boundary. Use for a phase break.

Declare an empty tier with a label:

```json
"tiers": [
  {"id": "before", "label": "Before"},
  {"id": "break", "label": "Deploy"},
  {"id": "after", "label": "After"}
],
"elements": [
  {"id": "old", "role": "process", "tier": "before", "text": "v1 serving"},
  {"id": "new", "role": "process", "tier": "after", "text": "v2 serving"}
],
"edges": []
```

`break` has no elements. It renders its label and reserves a band, which is the pause. Leave the gap uncrossed; the reader supplies the change.

Gotcha: a gap with no label is just a layout accident. Label it or remove it.

## 9. Spine

Lines as structure. Use for a sequence that matters more than its items.

```json
"lines": [
  {"id": "spine", "x": 120, "y": 300, "points": [[0, 0], [600, 0]], "tone": "muted"}
],
"markers": [
  {"id": "m1", "x": 200, "y": 294, "role": "process"},
  {"id": "m2", "x": 420, "y": 294, "role": "process"}
],
"annotations": [
  {"id": "t1", "text": "TASK_STARTED", "x": 160, "y": 250, "tone": "ink"},
  {"id": "t2", "text": "STEP_UPDATED", "x": 380, "y": 320, "tone": "ink"}
]
```

A spine replaces a row of boxes when the order matters more than each item. Markers sit exactly on the line; annotations alternate above and below so they do not collide.

Gotcha: a spine with too many markers becomes a ruler. Six is a comfortable maximum; beyond that, group into phases and use two spines.
