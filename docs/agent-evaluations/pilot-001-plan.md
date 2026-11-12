# LESSON12-PILOT-001 Research Plan

## Approval status

`approved` for test-only implementation by the human operator. Production
code, packaging, and dependencies are explicitly out of scope.

## Objective

Improve regression coverage for the existing percentage operation without
changing calculator functionality.

## Scope and evidence

The Researcher inspected `calculator.py`, `calculator_cli.py`,
`tests/test_calculator.py`, `tests/test_cli.py`, the repository instructions,
and orchestration documentation. Existing tests cover normal API values,
zero numerator in the API, negative values, decimals, zero totals, CLI error
text, and generic large integers, but do not explicitly cover several
percentage CLI boundaries.

## Planned scenarios

1. Direct API zero-float denominator.
2. CLI zero numerator.
3. CLI negative denominator.
4. CLI scientific notation.
5. CLI large integer operands.

## Acceptance criteria

- Only tests and evaluation documentation change.
- Existing percentage behavior, error text, and exit codes remain unchanged.
- New tests do not duplicate existing cases.
- Full pytest validation passes.
- No commit or push is performed.

## Risks

Very large percentage inputs are converted to floating-point values by the
existing implementation and may lose precision; the test asserts the existing
floating-point result rather than changing that behavior.

## Handoff

The Developer must implement the approved test-only plan and return exact
validation evidence in `pilot-001-implementation.md`.
