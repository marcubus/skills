# Project Atlas status report, week 32

Reporting period: 4 August to 8 August 2026.
Owner: Priya Raman, programme director.
Audience for this report: the steering committee.

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
