# Palette sources

The palette is a file, not a preference inside the skill. Point the skill at one theme and every diagram follows it.

## Contents

- Resolution order
- Our palette file
- Adapters
- The pywal caveat
- Not supported
- Troubleshooting

## Resolution order

`scripts/diagram palette` and `layout` look in this order and stop at the first hit:

1. `--source <file>` to `palette`, or `--palette <file>` to `layout` and `check`, when you pass one.
2. `$EXCALIDRAW_PALETTE`, when set.
3. `$XDG_CONFIG_HOME/excalidraw/palette.json`, or `~/.config/excalidraw/palette.json` when `XDG_CONFIG_HOME` is unset.
4. A terminal config file the compiler finds: alacritty, kitty, wezterm, ghostty, foot, `.Xresources` or `.minttyrc`; or pywal's colors.json.
5. The shipped `examples/palette.json`, recorded as `shipped:examples/palette.json`.

A missing canonical file is normal on a fresh machine. `palette --init` writes the example palette there; `--force` replaces an existing one. The command prints the source it used, and the compiled file records it, so a diagram never hides which theme produced it.

## Our palette file

The shape is the worked example at `examples/palette.json`: `name`, an optional `variant`, and a `slots` object with the sixteen `baseXX` keys.

`variant` is optional; the canvas luminance decides when it is absent. `name` is a label, not an identity.

## Adapters

| Source | Detection | Parse rule |
|---|---|---|
| Our JSON | `.json` with a `slots` object | Read the sixteen `slots` |
| base16 JSON | `.json` with sixteen `baseXX` keys, flat or under `colors`/`palette` | Read the sixteen keys |
| base16 scheme | `.yaml` or text with `baseXX:` lines | First quoted or bare hex after each key |
| alacritty | `.toml` with `[colors.*]` | `normal`/`bright` names map to ANSI 0..15, `primary.background`/`foreground` |
| kitty | `kitty.conf` with `colorN` | The hex on each `colorN`, plus `background`/`foreground` |
| wezterm | `.lua`-style text with `colorN =` | The hex after each `colorN`, plus background/foreground |
| ghostty | `config` with `palette = N=#…` | The hex after each `palette = N` |
| foot | `foot.ini` with `regularN=` / `brightN=` | The hex after each numbered key |
| `.Xresources` | `*.colorN:` lines | The hex after each numbered resource |
| mintty | `.minttyrc` with `Black=` / `Red=` | The hex after each named key, `Bright…` for 8..15 |
| pywal JSON | a pywal JSON file with `special` and `colors` | `special.background`/`foreground`, `colorN` for ANSI 0..15 |
| pywal `colors` | A file named `colors`, sixteen bare hex lines | Line N is ANSI N; canvas is ANSI 0 |

ANSI to slots:

| ANSI | Slot |
|---|---|
| background | `base00` |
| black | `base01` |
| bright black | `base03` |
| foreground | `base05` |
| bright foreground | `base07` |
| red / bright red | `base08` / `base09` |
| yellow | `base0A` |
| green | `base0B` |
| cyan | `base0C` |
| blue | `base0D` |
| magenta | `base0E` |
| bright yellow | `base0F` |

Missing ANSI colours fall back to a shipped value, so a partial theme still resolves. `base01`, `base02`, `base04`, `base06` and `base07` are synthesised from the foreground and background; `base03` uses bright black when the theme has one, otherwise a mix; `base00`, `base05` and the ANSI slots pass through.

## The pywal caveat

A pywal colors file has no background; the canvas becomes ANSI 0 (black), which produces a dark palette. When `special.background` exists in the pywal JSON, that is used instead. If the result looks wrong, pass the theme's own background as `base00` in a small JSON file rather than editing the terminal config.

## Not supported

A live OSC query of the running terminal is not implemented. The renderer and the palette both read files, so a diagram is reproducible after the terminal closes. To use a terminal theme that has no config file, export it to one of the formats above, or write a palette file.

## Troubleshooting

| Symptom | Cause | Fix |
|---|---|---|
| `palette` prints `shipped` | No canonical file | Proceed, or `palette --init` to make it canonical |
| `no 16 base16 slots found` | JSON is a theme file, not a base16 scheme | Pass the base16 export, or adapt it |
| `no 16-colour theme found` | Text format not recognised | Check the key names against the adapter table |
| Colours look washed out | Light theme with pale slots | Pick a theme with stronger chroma, or darken `base03`..`base0E` |
| Text is black everywhere | Palette too pale for ink at 4.5:1 | Replace the slot colours, not the output |
