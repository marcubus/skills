# Evals

Evals are test scenarios that verify each skill works correctly in real use cases. Each eval includes:
- A scenario description with input data
- Expected output or success criteria  
- Recorded run results showing the skill's actual behavior

## Structure

Each skill has its own eval directory mirroring the skill path:

```
evals/skills/productivity/<skill>/
├── README.md          # Eval documentation for this skill
├── fixtures/          # Test input data
│   └── <fixture-name>.<ext>
├── runs/             # Recorded test runs
│   └── default/
│       ├── scenario-1/
│       │   ├── brief.txt
│       │   ├── input.md
│       │   ├── reply.md
│       │   └── output.<ext>
```

## Adding New Evals

To add an eval for a skill:

1. Create the directory structure under `evals/skills/productivity/<skill>/`
2. Add test scenarios in `runs/default/` with descriptive names
3. Include fixtures that represent realistic user inputs
4. Record expected outputs and actual results

## Running Evals

Evals are run manually or as part of a custom CI pipeline. They're not automatically executed by the main check script, but they provide valuable test coverage for skill behavior.

See individual skill eval directories for specific scenarios and how to extend them.
