# Composition

The plan's shape and tier order come from brief.txt and the field table in `SKILL.md`. This file covers what happens when the compiled geometry fights back. The model has no nesting: zones are tiers, and a sub-component is an element or a note.

## Siblings

`order` places an element inside its tier; `references/plan-schema.md` owns the field and the rule for choosing it. A wrong order shows up as a crossing, and the fix is the order, not a waypoint.

## Ports

Ports are fixed by shape and never chosen by hand:

| Plan shape | Source side | Target side |
|---|---|---|
| `stack` | Bottom centre | Top centre |
| `conveyor` | Right centre | Left centre |

Parallel arrows leaving one shape are offset by 20px along that side. An arrow that appears to leave the side of a shape is a plan error the gate catches (`C15`).

## Routing

Routes are orthogonal, with as few bends as possible:

- Same column (stack) or row (conveyor): one straight segment.
- Otherwise: a Z through the middle of the gutter, at the largest grid multiple that fits.
- Reverse flow: the arrow leaves the outgoing side, runs to a channel clear of the shapes, climbs the channel, and enters the incoming side from outside the band.

Gutters: 40px between siblings, 80px between tiers. A conveyor shrinks the tier gutter to fit the page, never below 40. Margins are 60px, with a 20px safety pad inside the page box.



## Crossings

The target is zero. In order of preference:

1. Reorder siblings so the lines fan without touching.
2. Move an element to the tier its flow implies.
3. Split one wide tier into two narrower ones.
4. Declare the crossing in `crossings` with a reason, when the diagram's argument needs it.

A declared crossing must be perpendicular (`C18`) and clear of every node (`C16`); step 7 checks it clear of labels.

## Arrows that go back

A cycle is a forward path plus one reverse edge; `references/pattern-library.md` owns the pattern, including where the reverse edge enters. Reverse edges share the channel in 20px lanes, so they stay apart.

## Labels

- Node text: the name of the thing. `note` carries the detail.
- Edge label: the relationship, not the protocol unless the protocol is the point.
- Tier label: a short noun phrase, upper case in the render.
- Annotation: a sentence fragment that belongs to the picture, never inside a box.
- A label can land on a sibling's leg; reorder the sibling pair so each label travels with its edge.

Node width, the 24-character budget and the label-placement rule are in `references/plan-schema.md`.

## Legend

A legend sits bottom left: a swatch and the role name for each role used. It wraps to a second row when the page is narrow.

## Page

| Name | Pixels at 96dpi | Use |
|---|---|---|
| `a4` | 794 × 1123 | Stack |
| `a4-landscape` | 1123 × 794 | Conveyor |
| `none` | content + margins | Patterns that are not page-shaped, and cycles whose return channel leaves the page |

A stack with notes fits four tiers; a conveyor fits five columns of short labels. A one-row conveyor on `a4-landscape` leaves most of the page empty: give a short pattern `page: none` instead. `C23` tells you when the budget is gone, and then it is two diagrams, each its own plan and PNG.

The PNG is the page times the render scale: 1588 × 2246 for A4 at scale 2. A4 is a pixel budget here, not a print pipeline.
