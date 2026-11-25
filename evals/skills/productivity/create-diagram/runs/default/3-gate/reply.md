# Scenario 3: gate alone

Run from the repository root against the frozen scenes, pinned to their own palette. The gate checks work it did not produce and rewrites nothing.

## Broken

```
C08 gateway.backgroundColor = #dee4ec is not in the token table
C15 e_db: enters db on the wrong side, want top
C15 e_service: first segment does not leave bottom
C15 e_service: leaves gateway on the wrong side, want bottom
C16 e_client crosses trap_cross; reroute or list the crossing
C18 e_db: segment ((355.5, 706), (372.5, 797)) is diagonal
C18 e_db: segment ((372.5, 797), (355.5, 780)) is diagonal
C22 db_n: text starts outside db
C22 gateway_t: text is wider than gateway
C23 db sits outside the page box
C23 db_t sits outside the page box
C27 the delivered file differs from a rebuild of the plan

12 finding(s)
exit=1
```

## Clean

```
no mechanical findings
exit=0
```
