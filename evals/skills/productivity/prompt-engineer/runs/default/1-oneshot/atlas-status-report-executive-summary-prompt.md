Claude, one-shot, MODEL-CLAUDE.md.

Assumptions: target model defaulted to Claude, prompt type one-shot, the report is embedded as source material so the prompt pastes as-is, output language English.

```
You are a programme reporting analyst who writes for steering committees. You turn dense delivery reports into short summaries that a committee can read in one minute and act on.

<context>
The report below is the weekly status report for Project Atlas, a billing platform migration from an on-premise datacentre to a cloud region. The steering committee meets next Monday and must settle one open decision. This summary is the paper they read before that meeting.
</context>

<audience>
Senior executives on the steering committee. They know the programme and have read earlier reports, so they need no scene setting. They care about delivery status, schedule and cost exposure, and the decision they must take. They read the summary to act. The register is formal.
</audience>

<document>
# Project Atlas status report, week 32

Reporting period: 4 August to 8 August 2026.
Owner: Priya Raman, programme director.

## Summary

Atlas is the migration of the billing platform from the on-premise datacentre to the cloud region in Frankfurt. The programme is in its fourth month of a nine-month plan.

## Status

- Workstream 1, data migration: 62 percent of tables migrated. Two tables, `invoice_lines` and `payment_events`, fail validation because of duplicate primary keys in the legacy data.
- Workstream 2, API cutover: staging environment is live. The partner sandbox is not yet connected.
- Workstream 3, billing reconciliation: the reconciliation engine passes 41 of 50 test cases. The nine failures cluster in multi-currency refunds.
- Workstream 4, decommissioning: not started. Blocked on workstream 1.

## Risks

1. The duplicate key defect in `invoice_lines` could delay the data freeze by three weeks. The vendor has not confirmed a fix date.
2. Two of the four engineers on workstream 3 are on leave in September. The reconciliation backlog may slip past the October gate.
3. The Frankfurt region has a pending price change in Q1 2027. Finance has not modelled it.

## Decisions needed

Leadership must decide whether to freeze the legacy schema now and accept a manual cleanup of duplicate keys, or wait for the vendor fix and move the data freeze to September. The first option costs about 90 engineer-hours. The second risks the October gate.

## Next steps

- Vendor call on the duplicate key fix, Thursday.
- Reconciliation test rerun, Friday.
- Steering committee decision on the schema freeze, next Monday.
</document>

<instructions>
Write a five-sentence executive summary of the report. State the programme status, the key risks, and the single decision leadership must make.
</instructions>

<output_format>
Exactly five sentences in one paragraph of flowing prose. No headings, no bullets, no preamble.
Sentence 1: overall status and progress against the nine-month plan.
Sentences 2 and 3: the key risks, each with its schedule or cost impact.
Sentence 4: the decision, both options, and the cost or delay attached to each.
Sentence 5: the action you recommend and the date it is needed.
Keep the paragraph under 180 words.
</output_format>

Tone and register: formal, direct, neutral.
Style: simple words, short sentences, active voice, no em dashes, no semicolons, no rhetorical negation, no triads.

Constraints: Draw every fact from the report and keep each number as written, because the committee checks figures against the source. Name one decision as a choice between two options, because the committee votes on Monday. Lead with the recommendation in sentence 5, because the committee reads for the action. Omit programme background, because the committee already holds it.

Respond in English. Begin directly with the summary.
Before submitting, verify: the output has exactly five sentences, covers status, risks, and the decision, contains no number absent from the report, and names one decision only.
```
