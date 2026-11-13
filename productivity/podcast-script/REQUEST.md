# Request

The kokoro-tone wire contract. The gateway accepts an OpenAI-shaped speech request and translates the text into prosody and mastering. The model is `kokoro-v1_0`.

## Input shapes

A request takes one of two `input` shapes.

- A string with markup. This is the default for a podcast script. It supports `[voice:]`, `[emotion:]`, `[rate:]`, `[pause:]`, and `[sense:]`.
- A turn array. Each turn is an object with `text`, `voice`, `emotion`, `rate`, and `instructions`. The turn array does not parse markup except `[sense:]`.

Use the string form for a script with pauses and sticky tags. Use the turn array only for simple dialogue with no pauses.

## Tags

| Tag | Example | Meaning |
|---|---|---|
| `[voice:name]` | `[voice:host_a]` | Select a voice or alias. Sticky. |
| `[emotion:neutral]` | `[emotion:neutral]` | Clear any emotion override and return to the default. |
| `[rate:1.05]` | `[rate:1.05]` | Multiply the current preset rate. Sticky. `[rate:1.0]` resets. |
| `[pause:800ms]` | `[pause:1.2s]` | Add silence after the previous turn. Replaces the default gap. |
| `[sense:word=sense]` | `[sense:bass=music]` | Choose a heteronym reading. Replaced before synthesis. |

Tags are independent slots. Changing `[voice:]` resets neither emotion nor rate. `[emotion:neutral]` clears only the emotion. Rate has no reset tag because it is a multiplier. `[rate:1.0]` means no change.

`[emotion:]` and `[rate:]` flush the current turn. They are turn boundaries, not inline modifiers. A same-speaker change lands at a sentence boundary and carries an explicit pause. A speaker change uses `[voice:]` as the boundary.

Unknown `[tag:value]` pairs are left in the text and spoken. Use only the five known tags.

Only `neutral` is a valid emotion value on the default deployment. It clears the override. The default baseline is no override at all. Every preset is disabled until the deployment is tuned.

## Instructions

`instructions` is a keyword selector, not a direction field. It maps to one preset for every turn that does not name its own.

| Preset | Keywords include | Status |
|---|---|---|
| default | omit `instructions` | available |
| warm | warm, soft, gentle, kind, friendly, calm, soothing | disabled |
| bright | bright, cheerful, upbeat, happy, lively, sunny | disabled |
| sad | sad, sorrow, melancholy, somber, gloomy, mournful | disabled |
| tired | tired, weary, exhausted, sleepy, drowsy, flat, bored | disabled |
| angry | angry, furious, shout, mad, rage, stern, harsh | disabled |
| whisper | whisper, hushed, quiet, intimate | disabled |
| excited | excited, thrilled, eager, enthusiastic | disabled |

Longest keyword wins. There is no negation. `"not warm"` still selects `warm`. Use one preset word. Do not write a prose direction.

Omit `instructions` for the default baseline. Do not set a preset. Every preset is disabled until the deployment is tuned.

`instructions` sets the file-wide baseline. `[emotion:]` overrides it per turn. `[emotion:neutral]` returns to it.

## Normalise

`normalise` is off unless requested. Use an object to select layers.

```json
"normalise": {"lexicon": true, "acronyms": true, "numbers": true}
```

- `numbers`: Australian English digits. `3,913` becomes "three thousand nine hundred and thirteen". `0.43` becomes "nought point four three". `15%` becomes "fifteen per cent". `10-15` becomes "ten to fifteen". `21st` becomes "twenty-first". Years stay digits. Model names, versions, dates, IPs, and compound tokens are protected.
- `acronyms`: a table entry wins. Otherwise a 2 to 6 letter uppercase token is spelled letter by letter. `HTML` becomes "Aitch Tee Emm Ell".
- `lexicon`: the deployment file's rules, per-voice sets, letters, and locale.

`normalise: true` uses the layer defaults. An object turns on exactly its keys.

## Pronunciations

`pronunciations` maps a written word to the form the engine should say. It applies even when `normalise` is off.

Map form:

```json
"pronunciations": {"Lachie": "Locky", "SQL": "sequel"}
```

List form with context:

```json
"pronunciations": [
  {"match": "bass", "say": "base", "when": {"after": ["band", "music", "plays"]}},
  {"match": "bass", "say": "bas"}
]
```

Each rule takes `match`, `say`, and optional `when`, `case_sensitive`, and `whole_word`. `when` accepts `before`, `after`, and `within`. The replacement is never re-scanned. Brackets are rejected, so a replacement cannot inject markup.

Per-voice maps:

```json
"voice": {"id": "host_a", "host_a": "bm_lewis", "host_b": "am_michael"},
"pronunciations": {
  "*": {"Lachie": "Locky"},
  "host_a": [{"match": "bass", "say": "base"}],
  "host_b": [{"match": "bass", "say": "bas"}]
}
```

Request rules beat deployment rules, the acronym table, and number normalisation.

## Ambiguity

Heteronyms can be guessed, ignored, or rejected.

| Value | Behaviour |
|---|---|
| `guess` | First candidate, render, `X-Kokoro-Tone-Guessed` header. |
| `ignore` | Leave the engine default, no header. |
| `error` | 400 with the tags to choose from. Nothing rendered. |

Use `guess` and read the `X-Kokoro-Tone-Guessed` header. An absent header means nothing was guessed. The header names every assumption, so the check is exact.

`error` is documented in ADR 0012. Some gateway versions reject it with `ambiguity must be 'guess' or 'ignore'`, so use `error` only where the deployment implements it. Otherwise `guess` plus the header is the production preflight.

## Solo request

```json
{
  "model": "kokoro-v1_0",
  "voice": {"id": "narrator", "narrator": "bm_lewis"},
  "input": "[voice:narrator] Cold open. ...",
  "normalise": {"lexicon": true, "acronyms": true, "numbers": true},
  "pronunciations": {"Lachie": "Locky", "SQL": "sequel"},
  "ambiguity": "guess",
  "response_format": "mp3"
}
```

## Two-host request

```json
{
  "model": "kokoro-v1_0",
  "voice": {"id": "host_a", "host_a": "af_heart", "host_b": "am_michael"},
  "input": "[voice:host_a] ...\n[voice:host_b] [emotion:neutral] ...",
  "normalise": {"lexicon": true, "acronyms": true, "numbers": true},
  "pronunciations": {"*": {"Lachie": "Locky"}},
  "ambiguity": "guess",
  "response_format": "mp3"
}
```

## Panel request

```json
{
  "model": "kokoro-v1_0",
  "voice": {
    "id": "host_a",
    "host_a": "af_heart",
    "host_b": "am_michael",
    "host_c": "bm_lewis"
  },
  "input": "[voice:host_a] ...\n[voice:host_b] ...\n[voice:host_c] ...",
  "normalise": {"lexicon": true, "acronyms": true, "numbers": true},
  "pronunciations": {"*": {"Lachie": "Locky"}},
  "ambiguity": "guess",
  "response_format": "mp3"
}
```

## Limits

| Variable | Default | What it means for a script |
|---|---|---|
| `MAX_INPUT_CHARS` | 4096 | Total input characters. Raise it for a full episode. |
| `MAX_TURNS` | 100 | Tag-delimited turns. Raise it for a panel. |
| `MAX_PAUSE_MS` | 30000 | One `[pause:]`. |
| `MAX_TOTAL_PAUSE_MS` | 60000 | Sum of explicit pauses. |
| `MIN_RATE` / `MAX_RATE` | 0.75 / 1.3 | `[rate:]` bounds. |
| `TURN_GAP_MS` | 350 | Default gap between turns. An explicit pause replaces it. |
| `SEGMENT_CHARS` | 1000 | Long turns split internally at sentence boundaries. |
| `MAX_ALIASES` | 64 | Aliases a request may add. |
| `MAX_BODY_BYTES` | 1048576 | Whole JSON body. |

Raise `MAX_INPUT_CHARS` and `MAX_TURNS` in `.env` before a full episode. A 10-minute script is roughly 8500 characters before tags. A panel can exceed 100 turns.

## Handoff

```bash
curl -sS http://kokoro-tone:8000/v1/audio/speech \
  -H "Authorization: Bearer $KOKORO_TONE_API_KEY" \
  -H 'Content-Type: application/json' \
  --data-binary @episode-request.json \
  -o episode.mp3
```

The project's compose file publishes no host port by default. Run the curl from another container on that network, or add a port mapping for your setup.

`make narrate` is the simple path. It sends the file as `input` with a default voice and optional instructions. It does not send `pronunciations`, `normalise`, `ambiguity`, an alias map, or a turn array. Use the request JSON for a real episode.

## One master per file

The gateway masters the whole request once. Do not split an episode into multiple requests and stitch. Each request is mastered separately. If the deployment cannot raise the limits, split at act boundaries and accept that the master is per request.

## Voice and speed

Leave `speed` at 1.0. The preset already sets the rate. Do not stack `speed: 0.95` on top of the default. Use `[rate:]` for local pace changes.

Voice names and blends are passed through. OpenAI names resolve in the engine. `alloy` is `am_adam`, `echo` is `af_bella`, `shimmer` is `af_sky`, and so on.
