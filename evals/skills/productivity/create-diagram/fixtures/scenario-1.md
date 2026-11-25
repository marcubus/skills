# Scenario 1: technical brief

Draw one diagram for a conference talk that explains how a streamed agent event reaches a React frontend.

The talk's claim: the frontend does not poll; each event is a state patch, and the patch is what the renderer applies.

Facts the diagram must show by name:

- The transport is Server-Sent Events.
- The events are `RUN_STARTED`, `TEXT_MESSAGE_CONTENT`, `STATE_DELTA` and `RUN_FINISHED`.
- The frontend applies `STATE_DELTA` with `createA2UIMessageRenderer()`.

Evidence in the diagram: the actual `STATE_DELTA` payload shape, and the actual event names in order.

Constraints:

- Conveyor shape, A4 landscape.
- One palette, bound from the user's theme.
- At most two renders.
- Every label traces to a fetched source, recorded in the agent's ledger.

Expected result: a three-to-five column conveyor, an evidence annotation holding the payload, a legend at three or more roles, and a gate that exits 0.
