I didn't write the record. The switch to `ruff format` fails all three triage conditions, so it doesn't earn an ADR — and I've stopped rather than write one because you asked.

## Why it fails triage

| Condition | Verdict | Evidence from your brief |
|---|---|---|
| Hard to reverse | **No** | Reverting is one line in `pyproject.toml` and one reformat commit. Changing your mind costs a line edit, not real work. |
| Surprising without context | **No** | You say it plainly: anyone reading the code would not ask why, because both tools produce the same style. |
| A real trade-off | **No** | No alternative was weighed. `ruff` was already installed for linting, so `ruff format` added no dependency and displaced nothing. |

A record is for a choice a future reader would otherwise have to reverse-engineer. This one is invisible in the code, and there is nothing to reconstruct.

## Where it belongs instead

The **commit message on the reformat commit** is the right home. That commit already touches 14 files, so it is the one place a reader might stop and wonder, and the message is where they will look. Say what replaced what and why:

```
style: format with ruff instead of autopep8

ruff was already installed for linting, so this drops autopep8 as a
second formatter and removes a dependency. Both tools produce the same
style, so the reformatted files carry no behaviour change.
```

If you want it to survive the commit log, one line in `README.md` (or a `CONTRIBUTING.md` if you have one) under a development section is enough — "Format with `ruff format`; `ruff` is configured in `pyproject.toml`." No ADR file, no index row.

## What I checked

- `docs/adrs/` does not exist in this repository, so there was no index to read and no earlier record to compare against. Had the decision earned a record, it would have been `0001-...` in the default house shape from `FORMAT.md`.
- I did not search for a record covering this decision, because with no `docs/adrs/` directory there are no records to search.

If I've misread the situation — for example, if `ruff format` and `autopep8` do *not* agree on some construct you rely on, or if a downstream tool pins autopep8's exact output — tell me and the trade-off condition flips. That would make it a real decision and I'd write it up.
