# Example panel script

Guidance only. An excerpt: three hosts, one moderator, one interjection handoff, one section break. The moderator opens and closes.

## Script

```text
[voice:host_a] The bridge failed on its first day. Not in a storm. Not under a crowd. In a light breeze, while the market below was open. What did the load model assume?

[voice:host_b] A crowd that keeps walking.

[voice:host_c] [rate:1.1] Wait. Nobody stops?

[pause:300ms]

[voice:host_b] [rate:1.0] Nobody stops. And a [sense:bass=base] bass player under the arch, which the model never counted.

[pause:300ms]

[voice:host_a] [emotion:sad] Which is the part that gets me.

[pause:1200ms]

[voice:host_a] [rate:1.0] Local news now. The council has reopened the eastern footpath.

[pause:400ms]

[voice:host_c] Which is the path that runs under the bridge.

[pause:300ms]

[voice:host_a] [rate:0.95] One line. The bridge was checked against a model. Ask who checked the model.
```

## Handoff

Compile with the model file. Write `<source-stem>-tts-<model>.txt`.

Word count: 93. Runtime: about 41 seconds including pauses. Voices: `host_a`, `host_b`, `host_c`. Moderator: `host_a`. Target: `kokoro-tone`. Section break: bridge story to local news at 1200ms.

`[emotion:sad]` is dropped by this model and recorded in the notes. `[sense:bass=base]` is kept as a tag.
