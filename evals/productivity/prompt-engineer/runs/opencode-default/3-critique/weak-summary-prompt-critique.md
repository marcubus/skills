Model: Claude (default, no target named). Type: critique. Model file: MODEL-CLAUDE.md.
Assumptions: the summary is for a human reader inside the business, the source is a written quarterly supplier review, and no length or format was fixed by the requester.

## Verdict

The prompt is 44 words and carries one of the eleven anatomy elements in usable form. It states a task and a register. Everything else a summarisation prompt needs is absent, so the output would vary by run and by model.

The core defect: the prompt asks for "the important parts" and never says what important means. A model has to invent the criteria, the length, the reader, and the shape. Fix those four and the prompt works.

## Findings

1. Role (check 1). "Helpful assistant" names no expertise. The model has no reason to weigh a price increase against a quality escape.
Fix: "You are a procurement analyst with ten years of experience writing quarterly supplier reviews for a manufacturing business."

2. Audience (check 2). None of the five dimensions appear. The prompt cannot know whether the reader is a buyer, a plant manager, or a finance lead.
Fix: "The audience is the operations director, who reads to approve or end the supply agreement, already knows this supplier and this quarter, cares about cost, delivery, quality, and compliance, and expects a professional register."

3. Context (check 7). The prompt points two ways at once. It says "the document below" and then names "the attached quarterly supplier review". A reader cannot tell where the source sits. It also omits the supplier, the quarter, and what the summary feeds.
Fix: name the supplier and quarter, state the decision the summary supports, and place the review text under a `<document>` tag with a title line.

4. Attachment handling (check 10). The attachment has a label and no extraction instruction.
Fix: "Read the attached review and pull four things: the overall rating, spend and price movement, delivery and quality results against target, and every open corrective action with its owner and due date."

5. Task criteria (check 3). "Summarise" and "covers the important parts" give no test for inclusion. The task sentence passes the letter of check 3 and fails its purpose.
Fix: "Write a five-sentence summary for the operations director. Sentence one gives the overall rating. Sentence two gives spend and price movement. Sentence three gives delivery and quality against target. Sentence four gives the open corrective actions, owners, and due dates. Sentence five gives the decision you recommend."

6. Format (check 5). No length, no structure, no unit. "Concise" is a wish.
Fix: "Output format: five sentences, one per line, under 150 words, no headings, no bullets."

7. Constraints (check 4). Three of the four constraints are bare negatives with no reason, and "make sure the summary is good" cannot be checked.
Fix each as an instruction with its reason:
- "Write in plain business English, because the reader skims on a phone between meetings."
- "Keep supplier terms such as OTIF, NCR, and PPAP, and gloss each in four words or fewer on first use, because the reader knows the terms and the gloss keeps the line readable."
- "Put a figure or a named owner in every sentence, because the reader challenges unsupported claims."
- "Open with the first finding, because the reader sees the first line in a notification preview."

The "no preamble" line earns its place as a default the model would add. Keep it.

8. Self-check (check 4, element 8). Nothing verifies the constraints after writing.
Fix: "Before submitting, check that the summary runs five sentences or fewer, that every sentence carries a figure or a named owner, and that sentence five names one decision."

9. Tone (check 6). "Professional" passes, and it is the strongest part of the prompt. Sharpen it so it directs action.
Fix: "Tone and register: professional and direct, written for a reader who acts on it."

10. Style (check 12). No `Style:` line. Claude mirrors the register of the prompt, and this prompt is written in vague, padded prose, so the summary inherits that.
Fix: add "Style: simple words, short sentences, active voice, no em dashes, no semicolons, no rhetorical negation, no triads."

11. Language (check 9). No language line. Low risk with English source material. Add "Respond in English." when supplier documents may arrive in another language.

12. Economy (check 8). "Helpful assistant" is the one element the task, audience, and format never use. Cut it when you add the role.

## Order of work

Fix the task criteria and format first (findings 5 and 6). They carry most of the gain. Then the audience (finding 2), then the source material and attachment instruction (findings 3 and 4). Add the self-check and the style line last.

## Test plan

Run these three inputs after the fixes.

Typical case. A review with an amber rating, a 6 percent price rise, OTIF at 91 percent against a 95 percent target, and two open NCRs.
Expected: five sentences, a figure in each, one recommendation in sentence five, under 150 words.

Edge case. A review with no quality data for the quarter.
Expected: the summary states the gap and names who will supply the figure. It invents no number.

Missing answer. A review that gives no overall rating.
Expected: the summary says the rating is absent and asks for it. It does not infer one from the other metrics.
