# Prompt Engineer

## What
Writes, revises, or critiques a prompt for a target model: one-shot prompts, system prompts, tool definitions, agent prompts, or sets of variants. Also provides test plans and comparisons.

## Why Use It
When you need production-ready prompts that work reliably across different AI models. Ensures prompts follow best practices with intent-based technique selection and model-specific adaptations.

## How (Brief)

Invoke as a skill: `/prompt-engineer`. Tell it what you want the prompt to do. Example:

```
/prompt-engineer write a system prompt for an agent that searches internal docs and calls create_ticket when issues are found
```

## Prompt Types

| Type | When | Deliverable |
|---|---|---|
| One-shot (default) | User wants a prompt to paste into chat | Model line, type, file, then prompt |
| System prompt | User wants standing instructions | Model line, type, file, task in user turn note |
| User turn | User wants one message in ongoing conversation | Prompt with context settled |
| Tool or agent | User wants tool definition or agent system prompt | Agent prompt first, tool definition below |
| Critique or variants | User wants review, test plan, improvement, options | Findings, test plan, or variants only |

## Model Detection

Resolves target in this order:

1. **Stated** — user names it explicitly
2. **Inferred** — content names ecosystem (Microsoft 365, Google Workspace, Anthropic, DeepSeek, Qwen)
3. **Default** — Claude, unless system prompt with user present

Model files carry only model-specific deltas: `MODEL-CLAUDE.md`, `MODEL-GPT-COPILOT.md`, `MODEL-GEMINI.md`, `MODEL-DEEPSEEK.md`, `MODEL-QWEN.md`.

## Workflow Summary

1. **Analyse silently** — intent, audience, anatomy elements, target model, style fidelity
2. **Resolve ambiguity** — present clarification block if needed, or proceed with assumptions for automated runs
3. **Build the prompt** — fill template slots, apply techniques and modifiers
4. **Check the prompt** — run GATE.md checks before delivery
5. **Refine or critique** — edits on tone/length/audience, or full critique with test plan

## Intent Taxonomy

Seven intent classes that select techniques:

- **Analytical / Reasoning** — chain-of-thought, step-back prompting, self-check
- **Creative / Generative** — persona priming, tone direction, few-shot style examples
- **Extraction / Summarisation** — grounding instructions, structured output tags
- **Classification / Decisioning** — few-shot classifications, enum constraints
- **Instructional / Procedural** — numbered format, milestone structure, validation criteria
- **Audience Reframing** — explicit audience profile, register constraints
- **Tool use / Agentic** — tool descriptions as decision rules, stopping conditions

## Prompt Anatomy

Eleven elements selected for intent and audience:

1. Role / Persona block
2. Context and motivation block
3. Audience direction
4. Task instruction (most important)
5. Constraints
6. Output format specification
7. Tone and register
8. Success criteria / self-check
9. Few-shot examples
10. Output language
11. Style constraints

## Files

| File | Purpose |
|---|---|
| `SKILL.md` | Full workflow, intent taxonomy, prompt anatomy |
| `MODEL-CLAUDE.md` | Claude-specific deltas and syntax |
| `MODEL-GPT-COPILOT.md` | ChatGPT/Copilot deltas |
| `MODEL-GEMINI.md` | Gemini deltas |
| `MODEL-DEEPSEEK.md` | DeepSeek V3/V4/R1 deltas |
| `MODEL-QWEN.md` | Qwen2.5/Qwen3 deltas |
| `BRANCHES.md` | Multi-model, multimodal, phased prompts |
| `GATE.md` | Checks for prompt quality and style compliance |

## Style Rules

- Simple words, short sentences, active voice
- No em dashes, semicolons, rhetorical negation, triads
- Compact line in every prose prompt: "simple words, short sentences, active voice"
- Banned word list on request only

## Attribution

Original concept by Marcubus. This implementation provides a structured prompt engineering system with intent-based technique selection and model-specific adaptations.
