# Example solo script

Guidance only. The script body is the text between the markers. The request is the handoff.

## Script

```text
[voice:narrator] [emotion:neutral] The bridge failed on its first day. Not in a storm. In a light breeze.

[pause:400ms]

[emotion:neutral] The load model assumed nobody would ever walk on it. The engineer who signed the drawing assumed the same thing.

[pause:600ms]

[emotion:neutral] [rate:0.95] The second staircase is the one that tells you whether anybody read the drawings.

[pause:1000ms]

[emotion:neutral] Local news now. The council has reopened the eastern footpath.

[pause:600ms]

[emotion:neutral] [rate:0.9] One line. Ask who signed the drawing before you ask who built the bridge.
```

## Request

```json
{
  "model": "kokoro-v1_0",
  "voice": {"id": "narrator", "narrator": "bm_lewis"},
  "input": "<script body>",
  "normalise": {"lexicon": true, "acronyms": true, "numbers": true},
  "pronunciations": {"Lachie": "Locky"},
  "ambiguity": "error",
  "response_format": "mp3"
}
```

## Handoff

```bash
curl -sS http://kokoro-tone:8000/v1/audio/speech \
  -H "Authorization: Bearer $KOKORO_TONE_API_KEY" \
  -H 'Content-Type: application/json' \
  --data-binary @solo-request.json \
  -o solo.mp3
```

Word count: about 110. Runtime: about 45 seconds at the default baseline. Voices: `narrator` to `bm_lewis`. Baseline: default. Section break: weather to local news at 1000ms.
