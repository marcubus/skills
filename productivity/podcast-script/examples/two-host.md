# Example two-host script

Guidance only. Two hosts, one section break, one interjection handoff.

## Script

```text
[voice:host_a] [emotion:neutral] The bridge failed on its first day. Not in a storm. In a light breeze.

[voice:host_b] [rate:1.1] Wait. A light breeze?

[pause:250ms]

[voice:host_a] [rate:1.0] A light breeze.

[pause:400ms]

[voice:host_b] [emotion:neutral] The load model assumed nobody would ever walk on it.

[voice:host_a] [emotion:neutral] And the engineer who signed the drawing assumed the same thing.

[pause:1000ms]

[voice:host_a] [emotion:neutral] Local news now. The council has reopened the eastern footpath.

[voice:host_b] [emotion:neutral] Which is the path that runs under the bridge.

[voice:host_a] [emotion:neutral] [rate:0.95] Naturally.

[pause:600ms]

[voice:host_a] [emotion:neutral] [rate:0.9] One line. Ask who signed the drawing before you ask who built the bridge.
```

## Request

```json
{
  "model": "kokoro-v1_0",
  "voice": {"id": "host_a", "host_a": "af_heart", "host_b": "am_michael"},
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
  --data-binary @two-host-request.json \
  -o two-host.mp3
```

Word count: about 130. Runtime: about 55 seconds at the default baseline. Voices: `host_a` to `af_heart`, `host_b` to `am_michael`. Baseline: default. Section break: bridge story to local news at 1000ms.
