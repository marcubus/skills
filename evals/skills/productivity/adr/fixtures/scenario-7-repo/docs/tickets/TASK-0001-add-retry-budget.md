# Add a retry budget to the webhook sender

**Type:** TASK
**Status:** open
**Record:** none

## Scope

Cap the outbound sender at three retries per delivery, with exponential backoff, before the queue work starts.
