# Example panel script

Guidance only. An excerpt: three hosts, one moderator, one interjection handoff, one section break.

## Script

```text
[voice:host_a] The bridge failed on its first day. Not in a storm. Not under a crowd. In a light breeze, while the market below was open. What did the load model assume?

[voice:host_b] Nobody would ever walk on it.

[voice:host_c] [rate:1.1] Wait. Nobody?

[pause:300ms]

[voice:host_b] [rate:1.0] Nobody.

[pause:300ms]

[voice:host_a] Which is the part that gets me.

[pause:1200ms]

[voice:host_a] Local news now. The council has reopened the eastern footpath.

[pause:400ms]

[voice:host_c] Which is the path that runs under the bridge.

[pause:300ms]

[voice:host_a] [rate:0.95] Naturally.
```

## Handoff

Compile with the model file. Write `<source-stem>-tts-<model>.txt`.

Word count: 67. Runtime: about 30 seconds including pauses. Voices: `host_a`, `host_b`, `host_c`. Moderator: `host_a`. Target: `kokoro-tone`. Section break: bridge story to local news at 1200ms.
