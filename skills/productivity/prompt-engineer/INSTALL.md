# Prompt Engineer: hosted assistant install

This skill loads itself in any agent with a skill loader. Such an agent needs only the routes in [`docs/install.md`](../../../docs/install.md).

This page covers the other case. A hosted assistant has no skill loader, so the files go in by hand. The route mechanics live in `docs/install.md`. What follows is the part specific to this skill: which files to load, what goes in the instruction box, and how to tell it works.

## What to load

Load eight files: `SKILL.md`, `GATE.md`, `BRANCHES.md`, and the five `MODEL-*.md` files.

| File | Role |
|---|---|
| `SKILL.md` | The instructions. Style, model detection, prompt anatomy, the five workflow steps. |
| `GATE.md` | The checks that run before delivery, including the banned word list. |
| `BRANCHES.md` | Branch frameworks for analytical, creative, extraction and instruction prompts. |
| `MODEL-CLAUDE.md` | Claude, the default target. |
| `MODEL-GPT-COPILOT.md` | ChatGPT and Microsoft Copilot. |
| `MODEL-GEMINI.md` | Gemini. |
| `MODEL-DEEPSEEK.md` | DeepSeek V3, V4 and R1. |
| `MODEL-QWEN.md` | Qwen2.5 and Qwen3. |

Every file earns its place. The model files carry only the deltas for their model, so a platform with a small file limit still fits the whole skill.

## The instruction box

When the platform accepts files, upload all eight and put this in the instructions box:

```text
You are a prompt engineer. The attached files are your instructions and your knowledge base.

Follow SKILL.md exactly. Before you build a prompt, load GATE.md and the MODEL-*.md file
that matches the target model, and apply the branch framework from BRANCHES.md.

Apply every check in GATE.md before you deliver. Deliver one finished prompt with no
preamble and no commentary.

Write plain prose. No em dashes, no semicolons, no banned words.
```

The block points at the files rather than restating them. Restating them would give you two copies to keep in step, and the copy in the box is the one that would go stale.

When the platform has no file upload, paste the body of `SKILL.md` into the instructions box or the first message, then paste `GATE.md` and the matching model file, then your request.

## Platform notes

Each platform has its own steps in `docs/install.md`. The notes below are the constraints that matter for this skill.

| Platform | Route | Constraint |
|---|---|---|
| Microsoft 365 Copilot | [Agent builder](../../../docs/install.md#microsoft-365-copilot) | Knowledge grounds on Microsoft 365 content, so the eight files come from OneDrive or SharePoint. Without the agent builder, paste `SKILL.md` into a chat and add the request on the next line. |
| ChatGPT | [Custom GPT or custom instructions](../../../docs/install.md#chatgpt) | A Custom GPT takes the eight knowledge files. Custom instructions have a length limit, so paste `SKILL.md` and let the request name the target model. |
| Gemini | [Gems](../../../docs/install.md#gemini-gems) | File attachments need a paid Google plan. Without uploads, paste `SKILL.md` into the first message and keep the Gem open. |
| Claude | [Projects](../../../docs/install.md#claude-projects) | Project knowledge holds all eight files. The custom instructions field applies to every chat and carries no knowledge files. |

## Verify

Send this request after install:

> Write me a prompt that turns a meeting transcript into five action items with owners.

Check the reply against four things:

- It returns one finished prompt, with no preamble and no commentary.
- It follows the house style: plain prose, no markdown, no em dashes, no semicolons.
- It names the target model, or defaults to Claude when you name none.
- It opens with a short confirmation block only when the request is ambiguous. This request is clear, so it should build the prompt directly.

Then ask for a system prompt for a support bot. A working install states the loop, the tool-use policy and the stopping conditions, because `BRANCHES.md` requires those for an agent prompt.

## Tips

- Name the target model. Each model family has its own prompt mechanics and the model files assume you know which one you want.
- Say what the audience cares about. "Non-technical executives" beats "general audience".
- Ask for a system prompt when you configure a bot, and ask for a tool definition when the bot calls tools.
- Refine in place. Follow-ups adjust the same prompt, so the assistant keeps one version rather than starting over.
