# Voice

Casting, presets, rate, and pause. The gateway passes voice names through to the engine. The engine owns the voice inventory.

## Available presets

The default deployment renders only the baseline. No emotion preset is enabled by default.

- The default is the baseline. It is no override at all.
- `[emotion:neutral]` clears any override and returns to the default.

Every preset is disabled until the deployment is tuned. Do not write `warm`, `bright`, `sad`, `tired`, `angry`, `whisper`, or `excited`. They are listed at the bottom for later.

Variety comes from rate, pause, sentence length, and word choice.

## Casting

- Run `GET /v1/audio/voices` for the authoritative list.
- Use an alias map in the request so the script is portable.

```json
"voice": {"id": "host_a", "host_a": "af_heart", "host_b": "am_michael"}
```

- The script uses the alias: `[voice:host_a]`.
- `id` sets the default voice when a turn has no voice.
- A voice may be a single name, a blend, or an OpenAI alias.

Examples for casting:

| Role | Example voices | Character |
|---|---|---|
| Narrator or host A | `af_heart`, `bm_lewis`, `bf_emma` | clear, steady |
| Host B | `am_michael`, `af_bella`, `bm_fable` | distinct from host A |
| Guest or panelist | `am_puck`, `bf_isabella`, `am_onyx` | contrast |

These are examples. Verify against the live inventory.

## Blends

```text
af_bella                      single voice
af_bella+af_sky               equal weights
af_bella(2)+af_sky(1)         2:1 blend
af_bella(3)-af_sky(1)         subtractive
```

A blend moves timbre, not prosody. Weights must be positive. Use a blend only when a single voice does not fit. Test a short sample.

## Levelling

Every voice is levelled to a common pre-master loudness before mastering. A blend interpolates its members' gains by weight. The gateway makes the file correct. It does not equalise voices. Choose voices for timbre, not loudness.

## Presets

| Preset | Rate | Pitch | Gain | EQ | Intent |
|---|---|---|---|---|---|
| default | 1.0 | 0 st | 0 dB | flat | baseline, explanation, evidence, close |

`neutral` is the reset. It clears the turn override and returns to the file-wide baseline, which is the default.

## Emotion guidance

- The default is the baseline. Use it for the whole episode.
- The words carry the emotion. The rate only moves pace.
- If a passage needs more weight, slow the rate and shorten the sentence. Do not reach for a disabled preset.

## Rate

- `[rate:]` multiplies the preset rate. Bounds are 0.75 to 1.3.
- `[rate:1.0]` means no change. Use it to reset a sticky rate.
- Rate is sticky across voice changes. Reset it at the next speaker's first turn.
- Do not stack `speed` and `[rate:]`. Leave `speed` at 1.0.
- A same-speaker rate change lands at a sentence boundary and carries an explicit pause.
- Useful bands: `0.9` for a close or a warning, `0.95` for evidence, `1.0` for explanation, `1.05` for a build or a list.

## Pause

- `[pause:800ms]` or `[pause:1.2s]` adds silence after the previous turn.
- An explicit pause replaces the default 350ms gap.
- One pause may be up to 30 seconds. The total is capped at 60 seconds by default.
- Use pauses for beats and section breaks, not for pace.
- A logical section boundary gets 800 to 1200ms.
- A same-speaker tone change gets 300 to 600ms.
- An interjection handoff gets 200 to 300ms after the interjection.
- A panel section break gets 1000 to 1200ms.

## Voice changes

Changing `[voice:]` resets neither emotion nor rate. If the new speaker should not inherit the previous rate, add `[rate:1.0]`.

A voice change is a speaker change. It needs a pause, a question, or an interjection. See `MULTIHOST.md` and `PANEL.md`.

## Disabled presets

These exist in the engine and are documented for later. The deployment needs tuning before they render correctly. Do not use them.

| Preset | Rate | Pitch | Gain | EQ |
|---|---|---|---|---|
| warm | 0.95 | -1.2 st | +1 dB | low-shelf +1 dB at 250 Hz, high-shelf -1 dB at 6 kHz |
| bright | 1.036 | +1.1 st | +1 dB | high-shelf +5 dB at 6 kHz, low-shelf -1 dB at 600 Hz |
| sad | 0.88 | -2 st | -3 dB | lowpass 6 kHz |
| tired | 0.90 | -1 st | -2 dB | lowpass 8 kHz |
| angry | 1.15 | +1 st | +4 dB | treble +2 dB, compression 3:1 |
| whisper | 0.85 | 0 st | -8 dB | highpass 300 Hz, lowpass 8 kHz |
| excited | 1.12 | +2 st | +2 dB | high-shelf +9 dB at 6 kHz, low-shelf -1 dB at 600 Hz |
