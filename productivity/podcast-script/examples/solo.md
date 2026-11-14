# Example solo script

Guidance only. An excerpt: a full episode runs 8 to 12 minutes. The body shows the marker mechanics.

## Script

```text
[voice:host_a] The bridge failed on its first day. Not in a storm. Not under a crowd, or a truck, or a flood. In a light breeze, on a Tuesday, while the market below it was open and the second staircase was empty.

[pause:400ms]

The load model assumed nobody would ever walk on it. The engineer who signed the drawing assumed the same thing.

[pause:600ms]

[rate:0.95] The second staircase is the one that tells you whether anybody read the drawings.

[pause:1000ms]

[rate:1.0] Local news now. The council has reopened the eastern footpath.

[pause:600ms]

[rate:0.9] One line. Ask who signed the drawing before you ask who built the bridge.
```

## Handoff

Compile with the model file. Write `<source-stem>-tts-<model>.txt`.

Word count: 99. Runtime: about 44 seconds including pauses. Voices: `host_a`. Target: `kokoro-tone`. Baseline: 145 wpm. Section break: bridge story to local news at 1000ms.
