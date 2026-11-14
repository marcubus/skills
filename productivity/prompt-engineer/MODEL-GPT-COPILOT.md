# GPT and Copilot deltas

| Element | In the output |
|---|---|
| Placement | translate: task first, context and source next, key instruction restated last |
| Plain labelled sections | keep, separated by `---` with uppercase labels |
| Output priming | translate to the first words or the first row of the output |
| Tool definition schema | translate to a strict JSON schema with `tool_choice` |
| Vision input | translate to an `image_url` content part with `detail` |

- Recency: later content carries more weight, so the restatement at the end holds the instruction.
- Sections: separate with `---` and uppercase labels `TASK`, `CONTEXT`, `SOURCE`, `OUTPUT FORMAT`. Markdown and XML both work.
- Output priming: end the prompt with the first few words or the first row of the output. Use priming when the output must start in a fixed shape and few-shot examples would run long. Examples: `Key points:` then a new line and `-`. `30-60-90 Day Plan:` then `**Days 1-30:**`. A table header row then the separator row.
- Fallback: "If the source material does not contain enough information, write 'Insufficient information provided' rather than inferring or fabricating."
- Vision: current GPT chat models read images. Pass each image as an `image_url` content part. Set `detail: "high"` when small text or fine detail matters. Label multiple images.
- Function calling: `name`, `description`, parameter schema. `strict: true` guarantees valid arguments. `tool_choice` controls whether and which tool runs. The model returns `tool_calls` with JSON arguments.
- Copilot: name the work context, the open email, document, meeting, or SharePoint folder. Copilot otherwise falls back to general knowledge. Keep one-shot prompts under 400 words. State length and depth when a longer answer is needed. Match the surface: Word drafts and rewrites, Outlook replies and thread summaries, Teams meeting summaries and action items, Copilot Chat for broader questions. Copilot Studio bots take the system prompt in bot settings.
