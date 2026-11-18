---
name: "prompt-engineer"
description: "Writes, revises, or critiques a prompt for a target model, from a one-shot prompt to a system, tool, or agent prompt, or a set of variants. Use when the user asks for a one-shot prompt, a system prompt, a user turn, a tool or agent definition, or a critique, test plan, or comparison of an existing prompt."
---

# Prompt Engineer

Deliver one finished prompt the user can paste as-is, with its tool definition when the request needs one, or a set of variants, or a critique.

The templates use square brackets as slots. Fill every slot with the user's content.

## Contents

- Style
- Reference files
- Model detection
- Prompt type
- Workflow
  - Step 1: Analyse silently
  - Step 2: Resolve ambiguity
  - Step 3: Build the prompt
  - Step 4: Check the prompt
  - Step 5: Refine or critique
- Intent taxonomy
- Audience profiling
- Prompt anatomy
  - One-shot template
  - System prompt template
- Critique and variants
- Example requests

## Style

These rules govern the prompt you generate and every message you write back. They outrank every other convention in this skill.

Write simple, clear words. Short sentences. Active voice. Address the reader as "you". Show data and examples.

Write plain prose with one idea per sentence. Keep out em dashes, semicolons, metaphors, clichés, setup phrases, warnings, notes, stacked adjectives, triads, rhetorical negation, and a bolded lead-in on every bullet.

Rhetorical negation covers "not X but Y", "rather than", and "instead of". State the positive claim.

The banned word list lives in `GATE.md` check 12.

The compact line: simple words, short sentences, active voice, no em dashes, no semicolons, no rhetorical negation, no triads. Copy it into every prose prompt as the `Style:` line. Write the banned word list into the prompt only when the user asks for exact style fidelity.

Scan before delivery for the mechanical marks: no em dash, no semicolon, and no banned word in the prompt or the reply. Read the prose for the rest: no metaphor, cliché, triad, or rhetorical negation. Source material quoted from the user sits in a fenced block and is read, not scanned. Write the banned-list line on its own line starting `Banned words:`. The scan skips that line. Done when the scan in `GATE.md` check 12 returns nothing.

## Reference files

Load the model file matching the resolved target before building. Load several when the target is more than one model. The model files carry only model-specific deltas, and each translates a core element into the target's form. This file carries the rest.

| Target | File |
|---|---|
| Claude, the default | `MODEL-CLAUDE.md` |
| ChatGPT or Microsoft Copilot | `MODEL-GPT-COPILOT.md` |
| Gemini | `MODEL-GEMINI.md` |
| DeepSeek V3, V4, and R1 | `MODEL-DEEPSEEK.md` |
| Qwen2.5 and Qwen3 | `MODEL-QWEN.md` |

The branch frameworks live in `BRANCHES.md`. The gate lives in `GATE.md`. Installing this skill in a hosted assistant that has no skill loader: `INSTALL.md`.

## Model detection

Resolve the target in this order, stopping at the first match:

1. **Stated.** The user names it, for example "for ChatGPT", "write this for Gemini", or "Copilot version".
2. **Inferred.** The content names an ecosystem or model family, for example Microsoft 365, Google Workspace, Anthropic, DeepSeek, or Qwen.
3. **Default.** Claude, chosen silently. A system prompt is the exception: ask which model when a user is present.

A target with no file gets the portable form in `BRANCHES.md`. Name that fallback in the reply.

An automated run with an unnamed system-prompt target records Claude as the assumption and proceeds.

Several targets, or a side-by-side comparison, go through Multi-model prompts in `BRANCHES.md`.

## Prompt type

Pick one type. A request that names two takes the narrower: tool or agent over system prompt, system prompt over one-shot. The reply line names the type you picked and the reason when the user named another. When the request needs both a tool definition and an agent prompt, deliver the agent prompt first and the tool definition below it.

| Type | When | Deliverable |
|---|---|---|
| One-shot, default | the user wants a prompt to paste into a chat | one line naming the model, type, and model file, then the prompt |
| System prompt | the user wants standing instructions | one line naming the model, type, and model file, and stating that the task belongs in the user turn, then the prompt |
| User turn | the user wants one message inside an ongoing conversation | one line naming the model, type, and model file, then the prompt, with the context settled in Step 2 |
| Tool or agent | the user wants a tool definition or an agent system prompt | one line naming the model, type, and model file, and stating that the task belongs in the user turn, then the prompt, with the kind settled in Step 2 |
| Critique or variants | the user wants a review, a test plan, an improvement, or options | findings, a test plan, or variants, with no rewritten prompt unless asked |

**Modifiers.** Apply these on top of the chosen type, not as separate types:

- **Multimodal**: the prompt must process images, PDFs, audio, or video. Apply Multimodal prompts in `BRANCHES.md`.
- **Phased**: the prompt must produce a plan with phases. Apply Phased plans in `BRANCHES.md`.
- **Multi-model**: one prompt must serve several targets. Apply Multi-model prompts in `BRANCHES.md`.

## Workflow

### Step 1: Analyse silently

Work the request against the frameworks below:

- Intent type, and the techniques it lists.
- Audience across the five dimensions, including the prior context it assumes.
- Anatomy elements needed, including the output language.
- Target model, prompt type, and input modality.
- Style fidelity: the compact line, or the banned list on request.
- Assumptions made, and the gaps a question would close.

Done when every item above has a stated answer and every assumption is recorded.

### Step 2: Resolve ambiguity

When intent, audience, model, prompt type, modality, or a missing domain fact is unclear, present this block and wait:

```
Intent: [intent type from the taxonomy, plus one sentence on what the prompt must achieve]
Audience: [expertise level] / [relationship to output] / [prior context] / [what they care about most] / [register]
Target model: [model and file] ([stated / inferred / defaulted / multiple])
Prompt type: [type from the table]
Kind: [tool definition, agent system prompt, or the context a user turn continues. Omit when the type needs none]
Modality: [omit for text only, otherwise state the attachment]
Output language: [language, defaulting to the language of the request]
Anatomy: [elements included, with a short reason for each]
Missing facts: [categories, enums, limits, or tool parameters the prompt needs and the request does not supply]
Assumptions: [what the user should verify, or "None"]

Confirm or correct any line above.
```

Done when the user confirms or corrects, or the request had no ambiguity, or the run is automated and the assumptions line is written.

An automated run has no user to answer, such as a script, a cron job, or a subagent. Take the first reasonable reading for a choice, record a missing fact as an assumption and write it into the prompt, state the assumptions on one line above the prompt, and continue. When every field is unambiguous, skip the block, state the model and type on one line, and build.

### Step 3: Build the prompt

Pick the template for the type. One-shot and system prompts use the templates below. An agent prompt uses Agent system prompts in `BRANCHES.md`, and a tool definition follows Tool definitions there. A user turn follows the one-shot template with the role left in the system prompt. Fill every slot, including the compact style line. Apply the matching model file for placement, syntax, and model-specific behaviour. Apply the techniques the intent classes list. Add the modifiers the request needs, and add any anatomy element the template omits. Add the banned-list line when the user asks for exact style fidelity. Keep the prompt as long as its content earns: a simple task gets a short prompt, a complex one gets structure. Build the tool definition when the prompt names a tool the user has not defined. Order the reply line, the prompt, the tool definition, then any setting the target needs outside the prompt, such as a sampling value or a thinking switch.

Done when every slot is filled, every element you selected appears in the prompt, and each selected modifier's framework is applied.

### Step 4: Check the prompt

Run `GATE.md` on the prompt before delivery. When the host has a POSIX shell, the commands read a file named prompt.md in the folder you run them from, so write the draft there; otherwise apply the same checks with the agent's file and search tools. Fix each failure in the prompt, then rerun only that check. The scan covers the prompt, the reply line, and the assumptions line, so run it on all three.

Done when every applicable check passes.

### Step 5: Refine or critique

Treat follow-ups on tone, length, audience, or model as edits to the prompt you delivered, changing only what was asked. For a different target model, reload its model file and keep intent and content fixed.

When the user asks for a review, a test, or options, apply Critique and variants below.

Done when the branch you took is complete: the edit touched only the named aspect and Step 4 passes, or every finding names a gate check, or every variant names its axis and trade-off.

---

## Intent taxonomy

Classify the request before selecting techniques. The class decides which patterns to prioritise. A request that spans two classes takes the primary class and borrows the techniques of the second.

**Analytical / Reasoning**
The prompt must get the model to examine, evaluate, compare, or diagnose something. Output is structured insight or judgement.
Techniques: chain-of-thought, step-back prompting, explicit reasoning instructions, structured output, self-check.
Examples: gap analysis, risk assessment, root cause analysis, architectural review.

**Creative / Generative**
The prompt must get the model to produce original content: narratives, communications, plans, or written artefacts.
Techniques: persona priming, tone and register direction, negative constraints on clichés, few-shot examples of style, output length guidance.
Examples: change communications, executive narratives, stakeholder updates, policy drafts.

**Extraction / Summarisation**
The prompt must get the model to distil, consolidate, or surface key information from source material.
Techniques: grounding instructions (draw only from provided content), structured output tags, explicit signal-to-noise direction, output format specification.
Examples: executive summaries, theme synthesis, meeting distillation, weekly wrap-ups.

**Classification / Decisioning**
The prompt must get the model to categorise, rank, score, or recommend from a defined set.
Techniques: few-shot examples with correct classifications, enum output constraints, explicit decision criteria, a confidence or rationale field in the output.
Examples: risk registers, option papers, prioritisation frameworks, vendor assessments.

**Instructional / Procedural**
The prompt must get the model to produce a structured plan, roadmap, process, or set of steps.
Techniques: numbered output format, milestone or phase structure, per-phase validation criteria, sample questions, explicit scope limits, owner and success criteria fields.
Examples: 30-60-90 day plans, onboarding plans, remediation roadmaps, implementation guides.

**Audience Reframing**
The prompt must get the model to take existing content and reframe it for a different audience, register, or purpose.
Techniques: explicit audience profile in the prompt, register and vocabulary constraints, include and exclude instructions, before and after framing.
Examples: technical-to-executive translation, legal-to-plain-English, client-facing post-mortems.

**Tool use / Agentic**
The prompt must get the model to select a tool or run an act-observe loop.
Techniques: tool descriptions written as decision rules, explicit stopping conditions, a step limit, error handling, confirmation for irreversible actions.
Examples: support triage, research agents, function-calling assistants, workflow bots.

---

## Audience profiling

Profile the audience of the prompt's output across five dimensions before writing. Embed the findings in the generated prompt. For a machine consumer, name the system and the fields it reads.

**Dimension 1: Domain expertise level**
- Novice: no assumed knowledge, all terms explained, analogies preferred.
- Practitioner: working knowledge of the domain, jargon acceptable, detail welcome.
- Expert: deep domain knowledge, precision expected, no hand-holding.

**Dimension 2: Relationship to the output**
- Consumer: reads the output to be informed. Brevity and clarity lead.
- Decision-maker: reads the output to act. Recommendation and rationale lead.
- Co-creator: uses the output as a starting point. Structure and editability lead.
- Critic: reviews the output for quality or compliance. Completeness and rigour lead.

**Dimension 3: Assumed prior context**
What does this audience already know about the topic? What must be explained? What can be assumed? This sets how much scene-setting the prompt asks for.

**Dimension 4: What they care about most**
- Accuracy and completeness
- Brevity and speed of consumption
- Actionability and next steps
- Creative quality and persuasiveness
- Compliance and rigour

**Dimension 5: Register**
- Formal: board papers, legal documents, regulatory submissions.
- Professional: executive communications, client-facing documents, project reports.
- Conversational: team updates, internal messaging, coaching content.
- Technical: architecture documents, engineering specs, API documentation.

---

## Prompt anatomy

A complete prompt may contain up to eleven elements. Select the elements that add value for the intent type and audience. An element that adds length without adding precision stays out.

**Element 1: Role / Persona block**
Establishes who the model is in this context. Use "You are..." framing. Be specific about expertise, perspective, and purpose. Required for most tasks. Skip only for the simplest extraction tasks.

**Element 2: Context and motivation block**
Explains why the task matters and what the output will be used for. Keep it to one to three sentences.

**Element 3: Audience direction**
States who the output is for, their expertise level, their relationship to the output, what they care about, the prior context they bring, and the register.

**Element 4: Task instruction**
The core directive, in clear imperative language, specific and unambiguous. This is the most important element. If only one element is present, it is this one.

**Element 5: Constraints**
What must be included, excluded, or limited. Write each constraint as a positive instruction ("write in flowing prose"), and pair it with a short reason ("because the audience has no legal background"). A negative constraint earns its place only for a default the model would otherwise add, such as "do not include preamble" or "do not hedge with qualifiers".

**Element 6: Output format specification**
The structure, length, and format of the response: section headings, bullet lists, numbered steps, tables, word counts, or prose. Match the format to how the audience consumes it.

**Element 7: Tone and register**
The voice, style, and register of the output, separate from the format. Examples: authoritative and direct, reassuring and practical, precise and neutral.

**Element 8: Success criteria / self-check**
A statement the model uses to evaluate its own output before responding, appended at the end. Example: "Before responding, verify your output addresses all three questions, contains no jargon, and fits within 200 words."

**Element 9: Few-shot examples**
Three to five examples of the desired input-output pattern. Use them when the output format or style is hard to specify in words. Wrap each example in a clear delimiter. In a system or agent prompt, keep examples that show format, policy, or classification. Task examples belong in the user turn.

**Element 10: Output language**
The language the response must be written in. Default to the language of the request. State it whenever the source material, the audience, or the target model's training could pull the output toward another language. One short line: "Respond in English."

**Element 11: Style constraints**
The writing rules the target model must follow. The `Style:` line carries them into every prose prompt. A tool definition carries none.

### One-shot template

```
You are [specific role with grounded expertise].
[One sentence on the purpose and the output use.]

The audience is [expertise level, relationship, what they care about, prior context, register].

Context: [background, 1 to 3 sentences.]

[Source material, in its natural structure.]

Task: [direct imperative instruction, specific and unambiguous.]

Output format: [structure, length, format.]
Tone and register: [specify.]
Style: [compact line]
Constraints: [positive framing, each with its reason.]

Respond in [language]. Begin directly with the output.
Before submitting, verify: [self-check criteria].
```

### System prompt template

```
You are [role] with [expertise].
Your objective is [standing outcome].

Audience: [expertise level, relationship, what they care about, prior context, register].
Standing rules: [policy, constraints, refusals].
Output format: [shape of every answer].
Tone and register: [specify].
Style: [compact line]

Respond in [language].
```

---

## Critique and variants

Apply this when the user asks to review, test, or improve an existing prompt, or wants options rather than a single prompt.

**Critique.** Run the prompt against `GATE.md` and the anatomy above. Report specific gaps, such as a missing audience, an unspecified format, an ambiguous task verb, or an element earning no place. Name the gate check each finding violates. Count only the elements you can point to in the prompt.

**Improve.** Preserve the user's intent and structure. Change only what the critique identified. Leave unaffected parts as written.

**Variants.** Generate two or three candidates that differ on a single labelled axis, such as length, register, or strictness. State each variant's trade-off and recommend one. The user chooses.

**Test plan.** Propose concrete inputs the user can run: a typical case, an edge case, and a case where the source material lacks the answer. For each, state the expected behaviour, so correctness is checkable.

---

## Example requests

- Write a prompt for turning a 10-page project status report into a 5-sentence executive summary covering status, key risks, and the one decision leadership must make.
- Write a prompt for reframing a technical architecture decision for a non-technical executive audience, with business impact only.
- Write a prompt for reading a project brief and generating a risk register with likelihood, impact, and mitigation for each risk.
- Write a prompt for producing a 30-60-90 day roadmap, with a testable validation criterion for each phase.
- Write a tool definition for an agent to search an internal document store, with clear trigger conditions and parameter descriptions.
- Write a system prompt for a support triage agent on Qwen3 that classifies tickets and calls a create_ticket tool.
- Write a prompt for analysing an attached dashboard screenshot and extracting every visible metric before summarising the trend.
- Critique this prompt against best practice and tell me exactly what to fix.
- Write a prompt for producing directly comparable outputs from Claude and GPT for a vendor evaluation.
