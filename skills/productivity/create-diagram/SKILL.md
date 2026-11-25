---
name: "create-diagram"
description: "Draws one Excalidraw diagram that argues a point, simple or technical."
disable-model-invocation: true
---

# Create diagram

A diagram is an argument, not a picture of a list. The **plan** is the drawing: you write the structure, the compiler writes the JSON.

**Input**: a subject, a question it answers, or a source document.
**Output**: brief.txt, `<name>.plan.json`, `<name>.excalidraw`, `<name>.png`, and for a technical diagram ledger.txt, all in `$RUN`.

Set `SKILL` to this skill's folder, `RUN` to the directory that will hold this diagram (create it), and `<name>` to a short slug for the diagram. Run the compiler from the repository root with absolute paths. The compiler is `scripts/diagram`. If that command is not found, the skill was copied without the repository, so install it (`README.md`). Paths that start with `references/` or `examples/` are relative to this folder. `scripts/diagram` is at the repository root, and `GATE.md` gives repository-relative commands.

## Contents

- 1. Classify the depth
- 2. Bind the palette
- 3. Research into a ledger
- 4. Argue it before you draw it
- 5. Write the plan
- 6. Run the gate
- 7. Render once and look
- 8. Deliver
- References

## 1. Classify the depth

**Simple** explains a mental model: few names, abstract shapes, no evidence. **Technical** explains a real system and carries **evidence**: a real payload or code excerpt, quoted from the source.

Technical needs an **owning document** you can quote: a spec, schema, source file, or contract. No document means no technical. Whatever the subject describes. Keep it simple and write the missing source on the claim line. A simple picture still invents no limit, number, or name. If it needs one, it is technical.

Start `$RUN/brief.txt` with a line naming the depth.

**Done when** the first line of brief.txt names the depth and, for technical, names at least one evidence artifact the diagram will show. Step 3 fetches it.

## 2. Bind the palette

```bash
scripts/diagram palette          # source, variant, every role token
scripts/diagram palette --init   # write the canonical file
```

The palette is the only source of colour. The command prints a source, the exact string the compiled file records (`shipped:examples/palette.json`, or a path), and a variant, `light` or `dark`. Leave the user's config alone unless they ask for a canonical file, then run `palette --init`.

A user who names a theme gives you the file: `--source <file>` to `palette`, `--palette <file>` to `layout` and `check`, or `$EXCALIDRAW_PALETTE`. Whatever the source, record its source string and variant in brief.txt. Having used a file, add the same `--palette <file>` to every `layout` and `check` command below.

Colour enters the plan as a **role**, never as hex. Nine roles:

A role is what the element does in the argument, not a taxonomy of the system: `agent` and `external` say who acts, `start` and `outcome` say where the argument begins and ends. A thing that needs two roles is two things, or a `note`.

| Role | Node type | Carries |
|---|---|---|
| `start` | ellipse | an entry point or trigger |
| `process` | rectangle | an action or component |
| `decision` | diamond | a branch |
| `outcome` | ellipse | a result or store |
| `exception` | rectangle | a failure path |
| `warning` | rectangle | a degraded or retry path |
| `agent` | rectangle | an AI, model or autonomous actor |
| `external` | ellipse | something you do not own |
| `neutral` | rectangle | a supporting or unclassified thing |

The compiler resolves each role to `fill`, `stroke`, and `text`. `references/color-system.md` owns those tokens.

**Done when** you have written the palette source and variant into brief.txt.

## 3. Research into a ledger

Skip this step only when step 1 said simple.

Fetch the documents that own the facts: the spec, the API reference, the schema, the changelog. Prefer the primary document over a summary. Save `$RUN/ledger.txt`, one line per fact. A worked ledger is `$SKILL/examples/ledger.txt`:

```
F1  event name is TASK_STARTED            docs.example.com/events
F2  header is X-Api-Version               api.example.com/reference#auth
F3  payload is a JSON Patch array         RFC 6902 section 4
    [{"op": "replace", "path": "/status", "value": "ready"}]
```

A quoted artifact continues on indented lines under its fact.

Use the system's real names, not invented ones. A label with no line is either decoration (cut it) or a fact you have not checked (go and check it).

**Done when** every fact in ledger.txt has a locatable source: a URL or path with the section, and any quoted artifact verbatim.

## 4. Argue it before you draw it

Write six more lines in brief.txt, under the depth and palette lines. A shape to copy is `$SKILL/examples/brief.txt`. Its palette line records that run, so write your own:

1. The claim, in one sentence. If you cannot state it, the diagram is a list. If the subject states none, write the claim you will argue on a line that starts `Claim (mine):`.
2. **Shape**: `stack` when the reader follows the flow down the page, `conveyor` when it is a pipeline that reads left to right on `a4-landscape`.
3. **Tiers** in flow order, every element assigned to one. The ids are yours. `edge`, `public`, `private`, `data` is a common ladder.
4. The **boundary**: the first thing that enters and every thing that leaves, each named. The edges that cross it are among the edges in item 6.
5. One **role** per element. The role fixes its node type.
6. The **relationships**: one edge per relationship, with a kind. End this line with any annotation, quoted. Note content goes on its element line.

A node label, a node note, an edge label or an annotation is **carried text**.

An abstract concept has no tiers until you pick its pattern: choose the dominant one from `references/pattern-library.md` first.

A technical diagram's evidence lives in an `annotations` entry, quoted from the source, or in an element's `note`.

The peer-link routes and the `x`/`y` escape hatch are in `references/plan-schema.md`. Edges run between tiers in flow order, except a cycle's one reverse edge. A relationship has an arrow, except where the pattern is the point: a gap or a spine lets an annotation carry it.

If a box adds no meaning, it is an annotation.

**Done when** brief.txt states the claim, the shape and the boundary, names every element, edge, note content and annotation the plan will contain, each element has a tier and a role, each edge has a kind, and, for a technical diagram, every carried text in it has a ledger line.

## 5. Write the plan

| Field | Values | Default |
|---|---|---|
| `title` | any string | none |
| `shape` | `stack`, `conveyor` | `stack` |
| `page` | `a4`, `a4-landscape`, `none` | `a4` for a stack, `a4-landscape` for a conveyor |
| `tiers` | tier ids, or objects with `id` and `label` | required, in flow order |
| `elements` | `id`, `role`, `tier`, `order`, `text`, `note`, `size` (`small`, `normal`, `hero`) | `order` 0, `size` `normal` |
| `edges` | `id`, `from`, `to`, `kind`, `label` | `kind` `primary` |
| `legend` | boolean | on at three or more roles |
| `lines`, `markers`, `annotations` | the structure layer | none |

A plan to copy lives at `$SKILL/examples/plan.json`. Node width and the 24-character budget are in `references/plan-schema.md`. `layout` refuses a structurally invalid plan. Validation in `references/plan-schema.md` is the list. An empty or labelled tier, the structure layer, declarations and the compiled metadata are there too. Read it when you use one.

```bash
scripts/diagram layout $RUN/<name>.plan.json -o $RUN/<name>.excalidraw [--palette <file>]
```

**Done when** the plan has an edge for every boundary entry and exit, `layout` exits 0 and `scripts/diagram check $RUN/<name>.plan.json --only 3,4,5,6` exits 0.

## 6. Run the gate

```bash
scripts/diagram check $RUN/<name>.plan.json --file $RUN/<name>.excalidraw [--palette <file>]
```

Read every finding and fix the plan, not the JSON. Rebuild, rerun. No render until the gate is clean. Step 7 looks for what a check cannot name.

One read the code cannot do, alongside the findings, is check 2 in `GATE.md`.

Six fixes cover most findings:

- **Crossing (`C16`)**: `references/composition.md` ranks the fixes and explains the crossing declaration.
- **Wrong port (`C15`)**. Move the target down a tier, or route a peer pair as a `line`. `references/plan-schema.md` defines this. `references/composition.md` owns the routing of an edge across tiers.
- **Shared run (`C17`)**. Move one edge to a peer `line`, or list the pair in `crossings` with a reason. Port offsets cover a few arrows, not many.
- **Page box (`C23`)**. Shorten labels, use `size: small`, drop a note, drop a tier, move or shorten an annotation, or switch to `page: none` when the pattern is not page-shaped. `references/composition.md` owns the page budget.
- **Hue step (`C12`)**: resolve it in the palette, or declare a substitution.
- **Text in a node (`C21`)**: move or shorten the label or annotation. The compiler avoids node boxes, so a surviving hit is a hand edit.

**Done when** the gate prints `no mechanical findings` and, for a technical diagram, the fact read above passes. A simple diagram has no ledger, so check 2 is not applicable.

## 7. Render once and look

```bash
scripts/diagram setup                                   # once per machine
scripts/diagram render $RUN/<name>.excalidraw --scale 2
```

Then open the PNG with the file-read tool, at full size. Look in this order:

1. **Flow**: does the diagram enter and leave at the boundary you named?
2. **Collision**: any text on a border, arrow through a word, label touching a shape or another label?
3. **Argument**: with the text removed, does the structure still say the claim, and is the page free of dead space?
4. **Evidence**: for a technical diagram, can a reader see one real artifact?

Fix what you saw, rebuild, gate, render once more. Two renders cover most runs. A third is allowed when the second exposed a new defect, and by four the plan, not the pixels, is wrong.

**Done when** you have viewed the PNG, answered the four looks above, every visible defect is either fixed or listed one by one in the reply with a reason, and every accepted declaration is named there.

## 8. Deliver

```bash
scripts/diagram check $RUN/<name>.plan.json --file $RUN/<name>.excalidraw --png $RUN/<name>.png [--palette <file>]
```

This reruns the gate and adds the size check. The one hand-edit branch: a user-supplied `.excalidraw` with no plan is repaired against `references/element-templates.md` and `references/json-schema.md`. With a plan, rebuild it.

**Done when** the gate exits zero, including the size check where the page has one. The delivered PNG is the scale-2 render from step 7. And the reply names every artifact in the Output line and the palette source.

## References

`GATE.md` is read on every run. The rest when their branch fires.

| When | File |
|---|---|
| Every run: the 28 checks, their reads and finding numbers | `GATE.md` |
| An empty or labelled tier, a declaration, the structure layer, or a field outside the table | `references/plan-schema.md` |
| A contrast floor, a hue step, a variant or a token name | `references/color-system.md` |
| Installing the compiler or the renderer | `README.md` |
| A port, gutter, crossing, label or page budget fights the plan | `references/composition.md` |
| The concept is a fan-out, convergence, tree, cycle, cloud, assembly line, side-by-side, gap or spine | `references/pattern-library.md` |
| The canonical palette is in another format | `references/palette-sources.md` |
| Hand-editing an element, or checking what Excalidraw keeps in a file | `references/element-templates.md`, `references/json-schema.md` |
| `render` says the browser or bundle is missing | `references/render-setup.md` |
