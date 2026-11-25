# Colour system

One palette, sixteen slots, nine roles. You pick roles; the compiler picks hex.

## Contents

- Slots
- Roles
- Derivation
- Floors
- Variant
- Token names
- Hue steps and declarations
- Editing the palette

## Slots

The palette is a base16 scheme: `base00` to `base0F`. The names are the contract. A terminal theme, a base16 scheme, pywal and our own JSON all translate into these sixteen before anything else happens.

| Slot | Usual job | Used here for |
|---|---|---|
| `base00` | background | canvas |
| `base01` | raised background | panel (unused by default) |
| `base02` | selection | palette only |
| `base03` | comments | neutral role, borders |
| `base04` | dark foreground | muted text |
| `base05` | foreground | body text |
| `base06` | light foreground | title |
| `base07` | lightest | text on a dark fill |
| `base08` | red | exception |
| `base09` | orange | warning |
| `base0A` | yellow | decision |
| `base0B` | green | outcome |
| `base0C` | cyan | start |
| `base0D` | blue | process |
| `base0E` | magenta | agent |
| `base0F` | brown | external |

The binding is fixed in `scripts/diagram` (`ROLE_SLOTS`). A palette swap changes colour, never meaning.

## Roles

The nine roles and their node types are in `SKILL.md`, step 2; this file owns the tokens behind them.

## Derivation

For each role, from its slot colour and the canvas:

1. **Fill** = the slot mixed 14% into the canvas on a light palette, 26% on a dark one. The neutral role uses 10% / 16%. The fill is a tint of the canvas, never a saturated block.
2. **Stroke** = the slot darkened (light palette) or lightened (dark palette) in 5% steps until it reaches 3:1 against both the fill and the canvas. Hue is preserved; the stroke stays recognisably the slot.
3. **Text** = the first of ink, `base07`, canvas that reaches 4.5:1 on the fill. A palette that fails all three gets black or white, and `C09` reports it.

Derivation happens once, at compile time. The resolved values become the **token table**, and the file may only use values from it. `palette` prints the table; read it when a check complains.

## Floors

| Pair | Floor | Check |
|---|---|---|
| Text on the fill it sits on | 4.5:1 | `C09` |
| Border on its own fill | 3:1 | `C10` |
| Border, arrow, line or marker on the canvas | 3:1 | `C11` |
| Two role fills | A hue step apart | `C12` |

## Variant

The variant is inferred from the canvas: luminance under 0.4 is dark. Dark palettes lighten fills and strokes; light palettes darken them. A palette file may declare `"variant"` and the gate checks that the declaration agrees with the canvas, because a wrong variant is a whole diagram of unreadable text.

## Token names

```
canvas  panel  ink  muted  title  border  lightest
<role>.fill  <role>.stroke  <role>.text
```

An element never carries a raw colour; it carries a role, and the token follows. When you hand-edit, use a token value from the table.

## Hue steps and declarations

A **hue step** is two roles landing on one hue at a comparable lightness; `C12` catches it. It happens most often to `warning` and `external`, because base16 gives brown and orange the same family. A substitution is a declaration that admits the collision; its shape is in `references/plan-schema.md`.


## Editing the palette

Edit the file at the canonical path, not the output. `references/palette-sources.md` owns the path, `--init` and the adapters.
