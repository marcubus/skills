# Qwen deltas

| Element | In the output |
|---|---|
| Thinking mode | translate to `/think` or `/no_think`, or `enable_thinking` in the API |
| Chat template | keep: system role for standing rules, user role for the task |
| Few-shot examples | keep, three to five diverse pairs |
| Structured output | translate to an exact schema |
| Tool definition schema | translate to the OpenAI-compatible `tools` interface |
| Image and video input | drop: route to Qwen2.5-VL or Qwen3-VL |

- Thinking switch: Qwen3 has two modes. Thinking reasons before answering. Non-thinking answers fast. Use thinking for maths, code, logic, and multi-step analysis. Use non-thinking for chat, classification, extraction, formatting, and simple instruction. For an agent loop, use thinking when the loop plans and non-thinking when it only classifies. When the loop does both, keep thinking on. Append `/think` or `/no_think` in the message. For a system or agent prompt, put the switch on the line below the prompt and its tool definition. Set `enable_thinking` true or false in the API or chat template. Thinking stays on in Qwen3-Thinking. Qwen2.5 has no thinking mode.
- Sampling: set it in the API or chat template, on the line below the prompt. Use sampled decoding with Qwen3, because greedy decoding risks repetition.
- Chat template: let the runtime apply the Qwen chat template. Keep the system role for standing role and format. Keep the user role for the task.
- Structured output and coding: give input tables as markdown and state the output schema exactly: columns, JSON keys, enum values. For strict JSON, add "Return only valid JSON, with no surrounding text." Qwen3-Coder is the code specialist. Name the language, version, framework, and style.
- Vision: images and video need a vision variant, Qwen2.5-VL or Qwen3-VL. These read images, documents, and video and return bounding boxes. State the unit of output for video: transcript, timestamped summary, or per-scene analysis.
- Function calling: Qwen2.5 and Qwen3 expose an OpenAI-compatible `tools` interface and the Qwen-Agent framework. Qwen supports tool use in both modes. Constrain parameters with the schema the target takes, and use enums where the domain is fixed.
