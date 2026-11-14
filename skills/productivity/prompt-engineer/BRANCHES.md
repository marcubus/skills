# Branch frameworks

Four frameworks `SKILL.md` points at. Load the framework the request reaches before building.

## Contents

- Multimodal prompts
- Tool and agent prompts
  - Tool definitions
  - Agent system prompts
- Multi-model prompts
- Phased plans
  - Every phase carries a validation criterion
  - Sample questions
  - How the prompt requests this

## Multimodal prompts

Apply this when the task involves images, PDFs, audio, or video. The job stays the same: direct attention, then specify the output. The source material is non-text, so address it by name.

**Name the modality and the attachment.** Refer to the content by what it is and, when there is more than one, by label: "the attached screenshot", "Image 2, the org chart", "the contract PDF". A model given several images will guess which matters. A label removes the guess.

**Separate reading from reasoning.** Instruct what to extract first, then the task that uses the extraction. Read the chart first, then answer the question.

**Match the extraction instruction to the content type.**

- **Images with text** (screenshots, scans, whiteboards): instruct transcription, and ask the model to flag anything illegible.
- **Charts and diagrams**: ask for structured extraction of axis labels, series, values, and node or edge relationships before any interpretation.
- **Documents and PDFs with layout**: state the reading order, or which pages, tables, or sections matter.
- **Audio and video**: state the unit of output: full transcript, timestamped summary, or segment-by-segment breakdown.

**Give a fallback for illegible content.** "If any label is unreadable, write [ILLEGIBLE] in its place." Invented values in the extraction step poison every downstream step.

**Label multi-item inputs.** For more than one image or file, number them and refer to them by number throughout the prompt.

```
You are [specific role].

Image 1: [what it is].
[Image 2: what it is, if any.]

Step 1: Extract [what to transcribe or read from the attached content. State how to handle illegible or missing parts.]
Step 2: [The task using the extraction.]

Output format: [structure, length, format.]
Tone and register: [specify].
Style: [compact line]

Respond in [language]. Begin your response directly with the output.
```

## Tool and agent prompts

Apply this when the target is not a single text response but a model that selects tools or runs in an act-observe loop. Two artefacts exist and are built differently: the tool definition, and the agent system prompt. When the agent prompt names a tool the user has not defined, deliver its definition below the prompt.

### Tool definitions

The description field is what the model reads when deciding to call the tool. Write it as an instruction to the model.

**Each tool definition states:**
- **Name**: `verb_noun`, snake_case, unambiguous, for example `search_docs`, `create_ticket`, `send_email`.
- **Description**: what the tool does, when to use it, and what it returns. State when to skip it when a second tool exists. Put the trigger conditions here: "Use this when the user asks about existing content. Skip it when the user wants to create new content."
- **Parameters**: every parameter with its type, meaning, constraints, and one concrete example. Mark required versus optional and give defaults.

**Design the set as well as the items.** Keep tools few and non-overlapping. Near-duplicate tools cause wrong selection. Prefer explicit enum values over free text when the domain is fixed. Express parameters as JSON Schema when the target takes a schema, and as typed name and description pairs when it does not. The example below uses the typed form. Wrap the parameter object in the target's schema form when it takes one.

```
{
  "name": "search_docs",
  "description": "Search the internal document store for passages matching a query. Use this when the user asks about information already present in company documents. Skip this tool when the user wants to create or edit documents. Returns up to 5 ranked passages with source IDs.",
  "parameters": {
    "query": "string: the search phrase, in natural language. Example: 'remote work policy 2026'.",
    "top_k": "integer, optional, default 5: maximum number of passages to return."
  }
}
```

### Agent system prompts

An agent system prompt governs a model that plans, calls tools, observes results, and repeats. It carries the standing policy. The task belongs in the user turn. A capability the agent exercises on every request is standing policy. A single instance of work is a task.

**Every agent system prompt states:**
- **Role and objective**: who the agent is and the single outcome it exists to produce.
- **The loop**: plan, act, observe, decide, and how the agent knows the work is finished.
- **Tool-use policy**: when to call a tool versus answer from knowledge. Prefer retrieval over memory for factual claims.
- **Stopping conditions**: when to stop, the step limit, and when to ask the user instead of continuing.
- **Error handling**: what to do when a tool fails, times out, or returns empty.
- **Output contract**: the shape of the final answer the user sees.
- **Safety constraints**: the actions that need confirmation before they run.

State the step limit as a number. Use ten when the user gives none. An action that deletes, pays, or messages a person outside the team counts as irreversible. A record the agent creates inside its own system does not. Drop the skip sentence when the tool is the only one. Drop the confirmation sentence when no action is irreversible. Drop the prohibited-action sentence when no action is prohibited. Use one paragraph for the final answer when the user gives no length.

```
You are [role] with [expertise], and your objective is [single outcome].

Audience: [expertise level, relationship, what they care about, prior context, register].
Work in a loop: plan the next step, call a tool when needed, evaluate the result, then decide
whether the objective is met. Stop when [stopping condition], and never exceed [N] tool calls.

Use [tool] when [trigger]. Skip it when [skip condition]. Answer from your own knowledge only for [safe categories].
If a tool fails or returns nothing useful, [fallback behaviour]. Ask the user before [irreversible action].

Return your final answer as [structure, length, format]. For [prohibited action], refuse and name the policy.
Tone and register: [specify].
Constraints: [positive framing, each with its reason.]
Style: [compact line]

Respond in [language].
```

## Multi-model prompts

Apply this when one prompt must serve several target models, or when the user wants to optimise across a set.

**Build on the intersection.** Use the most conservative positioning rule among the targets. A prompt that leads with the task, carries the source in the middle, and restates the instruction at the end satisfies both instruction-first and context-first models. Keep two model files' contradictory placement rules out of one prompt.

**Keep syntax portable.** Model-specific syntax, such as XML tags and output priming cues, stays out unless every target supports it. Fall back to plain labelled sections (`TASK`, `CONTEXT`, `SOURCE`, `OUTPUT FORMAT`) when portability matters.

**State the format directly.** Explicit specification reaches every target. Style mirroring exploits one model's property and leaves the rest behind.

**To compare models,** give each the identical, self-contained prompt and demand the same structured output, so the results are directly comparable. Vary nothing but the model.

**To optimise for one target,** load that model's file and adapt the structure.

**Portable form.** For a target with no model file, use plain labelled sections `TASK`, `CONTEXT`, `SOURCE`, `OUTPUT FORMAT`, with the conservative placement of task first and restated last.

## Phased plans

Apply this when the prompt must produce a plan with phases: a roadmap, an implementation plan, a rollout, a learning path, or any multi-stage objective. The phases belong to the prompt's output, so the prompt asks the target model for them.

### Every phase carries a validation criterion

Each phase states how the user confirms the phase succeeded. A validation criterion names an observable, binary, testable state.

- Weak: phase one lays the groundwork.
- Strong: phase one closes when all five onboarding accounts are active and the first staging deploy runs green.

Structure every phase with four parts:

- Objective: the outcome the phase produces.
- Steps: the actions that reach the objective.
- Validation criteria: the checks that prove the objective was met.
- Sample questions: questions the user asks to test the phase.

### Sample questions

Ask the target model for sample questions alongside the plan. They serve two purposes:

- Exercise the plan. Questions a user asks to confirm a phase delivered, for example: what is the rollback step if the deploy fails.
- Seed the test plan. Questions that reveal whether the prompt itself works, at least one per phase plus one edge case.

Pair each sample question with its expected answer, or with the expected behaviour when no single answer exists. A question without an expected result proves nothing.

### How the prompt requests this

Instruct the target model to deliver the plan with the four parts per phase, and to append a sample-questions list. Where the target supports a self-check, add: before you respond, confirm every phase has at least one testable validation criterion.
