# Scenario 2 links

Two URLs, both expected to fail retrieval. Neither resolves to a policy.

1. `https://northwind.example/privacy` returns no DNS record.
2. `https://ledger.example/privacy?login=1` returns a login wall.

The skill must name the fetch route, report the failure, and ask for a paste. It must not search for the policy, use a cached summary, or review from memory.
