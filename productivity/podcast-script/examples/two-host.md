# Example two-host script

Guidance only. An excerpt: two hosts, one section break, one interjection handoff.

## Script

```text
[voice:host_a] The bridge failed on its first day. Not in a storm. Not under a crowd or a truck. In a light breeze, on a Tuesday, while the market below it was open.

[voice:host_b] [rate:1.1] Wait. A light breeze?

[pause:250ms]

[voice:host_a] [rate:1.0] A light breeze.

[pause:400ms]

[voice:host_b] The load model assumed nobody would ever walk on it.

[pause:400ms]

[voice:host_a] Right. And the engineer who signed the drawing assumed the same thing.

[pause:1000ms]

[voice:host_a] Local news now. The council has reopened the eastern footpath.

[pause:400ms]

[voice:host_b] Which is the path that runs under the bridge.

[pause:300ms]

[voice:host_a] [rate:0.95] Naturally.

[pause:600ms]

[voice:host_b] [rate:0.9] One line. Ask who signed the drawing before you ask who built the bridge.
```

## Handoff

Compile with the model file. Write `<source-stem>-tts-<model>.txt`.

Word count: 95. Runtime: about 42 seconds including pauses. Voices: `host_a`, `host_b`. Target: `kokoro-tone`. Baseline: 145 wpm. Section break: bridge story to local news at 1000ms.
