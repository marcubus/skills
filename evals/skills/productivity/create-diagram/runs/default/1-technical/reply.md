# Reply

The diagram is delivered. It argues the talk's claim left to right: the agent run opens an SSE stream, the stream delivers a `STATE_DELTA` frame, and the A2UI renderer applies it to produce the surface. No poll sits anywhere in the path.

## Artifacts

- `brief.txt` — depth, palette line, claim, shape and page, tiers, inbound/outbound, roles, edges.
- `ledger.txt` — 17 facts, one per line, each with its source. Every node label, note and annotation traces to one.
- `sse-patch.plan.json` — the plan. Five-tier conveyor, A4 landscape, four primary edges, three annotations, legend on.
- `sse-patch.excalidraw` — the compiled scene, 36 elements.
- `sse-patch.png` — the scale-2 render, 2246 × 1588.
- `reply.md` — this file.

## Depth and evidence

Technical. The evidence is the four `data:` frames in order (`RUN_STARTED`, `TEXT_MESSAGE_CONTENT`, `STATE_DELTA`, `RUN_FINISHED`) and the `STATE_DELTA` payload, an RFC 6902 JSON Patch array. The frames come from the AG-UI HTTP+SSE binding example; the patch shape comes from the state pages. The renderer source excerpt is `createA2UIMessageRenderer({ theme })` passed as `renderActivityMessages`.

## Palette

Source: `shipped` (`examples/palette.json`), name `paper`, variant `light`. This machine has no canonical palette file, so I used the skill's shipped fallback rather than running `palette --init`. No hex was written by hand; every colour is a role token.

## Renders

One render at `--scale 2`. The final check added `--png` and exits 0.

```
scripts/diagram check .../sse-patch.plan.json --file .../sse-patch.excalidraw --png .../sse-patch.png
container ratio: 5/18 = 28% (node labels only is the target)
no mechanical findings
EXIT=0
```

## What I saw in the PNG

- Flow enters at `Agent run` and leaves at `Surface`.
- No text on a border, no arrow through a word, no label touching a shape.
- With the text removed the five shapes still read as a single left-to-right path.
- Evidence is readable at full size.

Accepted cosmetic point: the lower right of the A4 sheet is empty because the evidence block is left-aligned. It costs no meaning and is not one of the four looks, so I did not spend a second render on it.
