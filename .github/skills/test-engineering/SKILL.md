---
name: test-engineering
description: Design and execute evidence-based pytest validation for Python changes, including regression, boundary, invalid-input, integration, and failure-path coverage. Use when testing a change or investigating test failures.
---

# Test Engineering

## Triggers

Use this skill when a change needs a test matrix, focused pytest execution, regression validation, failure investigation, or an exact pass/fail report.

## Workflow

1. Read `.github/copilot-instructions.md`, the implementation, tests, and relevant configuration.
2. Define a matrix covering normal behavior, boundaries, invalid inputs, compatibility, and relevant error paths.
3. Run the smallest authorized pytest command that covers the change.
4. Expand to `python -m pytest -v` when the change is cross-cutting, targeted tests pass but regression risk remains, or the task requires the full suite.
5. Investigate failures using repository evidence and distinguish product defects, test defects, and environment issues.
6. Report exact commands, outcomes, warnings, failures, coverage gaps, and residual risks.

## Boundaries

- Prefer the Repository Tester for independent validation.
- Do not edit production code, tests, or configuration unless explicitly authorized.
- Do not weaken, replace, or hide failing tests; do not claim success without execution.
- Preserve existing calculator functionality and test expectations.
- Use `.github/skills/review-code/SKILL.md` only for review concerns, not as a substitute for test execution.

## Expected Output

Return:

- Test matrix and rationale
- Exact commands executed
- Pass/fail/blocked result with observed evidence
- Failure diagnosis and affected files
- Coverage gaps and residual risks
