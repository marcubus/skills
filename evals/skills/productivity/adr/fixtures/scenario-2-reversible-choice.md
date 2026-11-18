# Brief: formatting tool for the `ledger` CLI

We switched the project from autopep8 to `ruff format` last week. It is a one-line change in `pyproject.toml` and a single commit that reformatted 14 files.

Anyone reading the code would not ask why: both tools produce the same style. There was no alternative worth weighing, because ruff was already installed for linting.

Record this as an ADR.
