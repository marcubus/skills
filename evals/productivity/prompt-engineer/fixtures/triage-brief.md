# Triage agent brief

Request from the support operations team:

> Write a system prompt for a support triage agent running on Qwen3 that classifies tickets and calls a create_ticket tool.

What the requester supplied:

- The agent runs inside the helpdesk product.
- The agent reads an incoming ticket and either classifies it or creates a ticket record.
- The team uses a ticket system that reads a JSON payload.

What the requester did not supply:

- The ticket category list.
- The priority scale.
- The `create_ticket` parameter names, types, or defaults.
- Whether the agent replies to the customer or only writes the record.
- The step limit.
