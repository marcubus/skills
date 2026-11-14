# Gemini deltas

| Element | In the output |
|---|---|
| Placement | translate: role, context, and source material before the task |
| Opening verb | translate: the task line opens with an action verb |
| System instructions | translate to a separate system field where the surface has one |
| Tool definition schema | translate to `function_declarations` |
| Multimodal attachment | keep, with the modality named |

- Action verbs: open with a direct action verb: summarise, analyse, write, classify, compare, extract, generate, identify, rewrite, create. Pattern: action verb, subject, scope, constraints. Example: "Summarise the key risks in the brief below in five bullet points for a non-technical executive."
- Placement reason: Gemini reads context first, then applies the instruction.
- Multimodal: Gemini reads images, PDFs, audio, and video. State what to extract, analyse, or produce, and state what to do when the content is unclear.
- System instructions: the API and Google AI Studio take system instructions in a separate field. Consumer Gemini and Gemini in Workspace have no separate field. Combine role, context, task, and format in the user message.
- Function calling: `function_declarations` with a name, description, and typed parameters. Write the description as a decision rule. Gemini returns one or more calls and chains calls across turns. State whether parallel calls are wanted. Keep declarations few and non-overlapping.
