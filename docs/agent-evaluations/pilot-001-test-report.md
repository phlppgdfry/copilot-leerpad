# LESSON12-PILOT-001 Test Report

## Contract

- Task ID: `LESSON12-PILOT-001`
- Objective: Independently validate the test-only percentage regression
  changes and workflow artifacts.
- Approval status: `PASS`

## Matrix

| Area | Coverage |
|---|---|
| API | Normal, negative, decimal, zero, and floating-point zero denominator |
| CLI | Standard, zero numerator, negative denominator, scientific notation, large integers |
| Error paths | Zero denominator, exit code, stderr, no traceback |
| Regression | Complete existing pytest suite |
| Workflow | JSON parsing, contract validation, duplicate/status checks |
| Hygiene | `git diff --check`, no production-code changes |

## Commands and results

```text
python scripts/validate_agent_workflow.py
Agent workflow validation passed.

python -m pytest -q
95 passed, 1 warning

python -m pytest -q tests/test_calculator.py tests/test_cli.py
92 passed, 1 warning

python -m json.tool docs/agent-contracts/task.schema.json
python -m json.tool docs/agent-contracts/pilot-001.json
git diff --check
all passed
```

The warning is the existing AnyIO `PytestRemovedIn10Warning`; it does not fail
the suite.

## Findings and residual risks

- No test failures remain.
- The large-integer percentage assertion verifies the existing floating-point
  behavior; it does not claim arbitrary-precision percentage output.
- The validator intentionally provides limited standard-library checks rather
  than full JSON Schema validation.
- CI status is pending until the workflow runs on GitHub.
