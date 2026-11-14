---
name: meeting-summary
description: Turns a meeting transcript into decisions, actions, and dates. Use when a transcript or rough meeting notes need a summary someone can act on.
---

# Meeting summary

Turn a transcript into a summary someone can act on. The summary carries three things: what was decided, who owes what, and when.

## Steps

1. Read the transcript. Done when every speaker is identified or marked unknown.
2. Extract decisions. Done when every decision names what was decided and who agreed.
3. Extract actions. Done when every action has an owner and a date, or is marked unassigned.
4. Write the summary. Done when every sentence is a decision, an action, or a stated fact.
5. Check the summary. Done when all five checks pass.

## Checks

1. Every decision names the person who made it.
2. Every action has an owner or is marked unassigned.
3. Every date is absolute, never "next week".
4. No sentence restates another.
5. The summary is under 400 words.

## Output

Write `<transcript-stem>-summary.md` beside the transcript, with three headings: Decisions, Actions, Notes.

A decision is a line the group agreed to. A proposal nobody agreed to belongs under Notes, marked proposed.

## Voice

Plain prose. The summary is read by someone who was not in the room, so it names people and dates rather than referring to "the team" or "last week".
