# DeepSeek deltas

DeepSeek has two families. V3 and V4 chat models answer directly. R1 reasoning models reason before the answer and may show the reasoning block. Identify the family before writing.

| Element | In the output |
|---|---|
| Chain-of-thought instruction | drop for R1, keep for V3 and V4 |
| Plain labelled sections | keep: `TASK`, `CONTEXT`, `SOURCE`, `OUTPUT FORMAT` |
| Few-shot examples | keep for V3 and V4, drop for R1 |
| JSON output | translate to an explicit schema |
| Tool definition schema | translate to the OpenAI-compatible `tools` interface |
| Image input | drop: V3, V4, and R1 read text only, so route to DeepSeek-VL |

- R1 reasoning: R1 reasons internally. Give one self-contained user message with the final-answer format. Use zero-shot. Extra CoT duplicates the work and lowers quality. If the deployment echoes the trace, add "Return only the final answer, without the reasoning."
- V3 and V4 chat: chain-of-thought helps on analytical and decisioning tasks. The system role works normally. Few-shot examples work for format and style.
- Sampling: set it in the API config, on the line below the prompt.
- JSON and code: V3 and V4 support JSON output and function calling. State the schema and add "Return only valid JSON, with no surrounding text." For code, name the language, version, framework, and style.
- Function calling: V3 and V4 expose an OpenAI-compatible `tools` interface. Validate returned arguments before use. R1 is less reliable at tool calling. Prefer V3 or V4 for agent loops.
