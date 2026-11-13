# Example panel script

Guidance only. Three hosts, one moderator, one interjection handoff, one section break.

## Script

```text
[voice:host_a] [emotion:neutral] The bridge failed on its first day.

[voice:host_b] [emotion:neutral] The load model assumed nobody would ever walk on it.

[voice:host_c] [rate:1.1] Wait. Nobody?

[pause:250ms]

[voice:host_b] [rate:1.0] Nobody.

[voice:host_a] [emotion:neutral] Which is the part that gets me.

[pause:1200ms]

[voice:host_a] [emotion:neutral] Local news now. The council has reopened the eastern footpath.

[voice:host_c] [emotion:neutral] Which is the path that runs under the bridge.

[voice:host_a] [emotion:neutral] [rate:0.95] Naturally.
```

## Request

```json
{
  "model": "kokoro-v1_0",
  "voice": {
    "id": "host_a",
    "host_a": "af_heart",
    "host_b": "am_michael",
    "host_c": "bm_lewis"
  },
  "input": "<script body>",
  "normalise": {"lexicon": true, "acronyms": true, "numbers": true},
  "pronunciations": {"*": {"Lachie": "Locky"}},
  "ambiguity": "error",
  "response_format": "mp3"
}
```

## Handoff

```bash
curl -sS http://kokoro-tone:8000/v1/audio/speech \
  -H "Authorization: Bearer $KOKORO_TONE_API_KEY" \
  -H 'Content-Type: application/json' \
  --data-binary @panel-request.json \
  -o panel.mp3
```

Word count: about 100. Runtime: about 45 seconds at the default baseline. Voices: `host_a` to `af_heart`, `host_b` to `am_michael`, `host_c` to `bm_lewis`. Moderator: `host_a`. Section break: bridge story to local news at 1200ms.
