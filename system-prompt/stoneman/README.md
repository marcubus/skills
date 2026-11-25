# stoneman System Prompt

A toggleable style constraint that compresses output to payload-only fragments while preserving all technical facts. Platform-agnostic: paste into any LLM chat interface's system prompt field.

## What it does

**Normal mode (default):** Full prose responses with standard formatting, articles and copulas included.

**Stoneman mode:** Fragment-only responses that drop articles and copulas, keep code/numbers/negations verbatim, answer-first without preamble, under 150 words as single paragraph without headings or bullets.

## How to use (platform-agnostic)

### Step 1: Configure system prompt

Paste the entire contents of `SYSTEM-PROMPT.md` into your LLM chat interface's **system prompt** field. This applies before every message in a session.

### Step 2: Toggle mode during chat

Type these commands in your messages to switch modes:
- `/stoneman` - Activate fragment-only responses
- `/normal` - Return to full prose

The model will acknowledge the toggle and maintain that mode until you change it again.

## Key rules (when stoneman is active)

### Floor (never cut these):
- Code, commands, paths, API names, error strings verbatim
- Negations including contractions (not, don't, won't)
- Numbers and units
- User's language

### Escape to plain prose (always use full sentences for):
- Security warnings
- Irreversible actions before confirmation
- Ambiguous fragments that could be misread
- Confused users (asked again or answer didn't help)
- Questions with options
- Anything persisted outside chat
- Harness status lines

### Thinking rules (when active):
- One-step tasks: decide once, answer in fragments
- Multi-step tasks (arithmetic, file changes, audits, negations, numbers to preserve): reason fully before compressing output
- Unclear shape: take multi-step path

## Example transformation

**Normal mode:** "The component re-renders because an inline object prop creates a new reference each render, which you can prevent using useMemo."

**Stoneman mode:** "Inline object prop, new ref, re-render. `useMemo`."

## Platform compatibility

This system prompt works with any LLM chat interface that supports:
- System prompt configuration (static text applied before every message)
- User messages that the model reads and responds to
- Context tracking of previous turns in a session

Tested/compatible with:
- LM Studio
- OpenCode/Hermes
- Any custom LLM client supporting system prompts

## Maintenance notes

- This is a **style constraint**, not a skill. It changes formatting, doesn't perform work.
- Mode toggles persist across messages until changed again.
- No external dependencies or configuration files required beyond the system prompt text itself.
