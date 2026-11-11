
# GitHub Copilot Repository Instructions

## Project context

This repository is a beginner-friendly Python calculator project.
Its purpose is to teach professional AI-assisted software development,
testing, debugging, documentation, and Git workflows.

## Python standards

- Support Python 3.11 or newer.
- Use clear English function and variable names.
- Use descriptive type hints for public functions.
- Follow the existing code style and PEP 8 conventions.
- Prefer simple, maintainable solutions over unnecessary abstractions.
- Preserve existing behavior unless explicitly asked to change it.

## Testing

- Use pytest for automated testing.
- Add tests for meaningful new functionality or bug fixes.
- For numeric functions, check the relevant cases from this checklist:
  negative values, zero values, mixed `int`/`float` inputs, floating-point
  precision, and division-by-zero paths.
- Handle division by zero explicitly and consistently.
- Use pytest.approx where floating-point precision matters.
- Run `python -m pytest -v` after code changes.
- No linter or static type checker is configured currently; review PEP 8 and
  public type hints manually unless a tool is added deliberately.
- Never claim tests passed unless they were actually executed.

## Change management

- Inspect relevant files before modifying them.
- Explain the intended changes before implementation.
- Keep changes limited to the requested scope.
- Do not introduce external dependencies without explaining why.
- Do not overwrite unrelated user changes.
- Do not commit, push, merge, open or update pull requests, modify issues,
  respond to reviews, or resolve review threads without explicit authorization.
- Report modified files and verification results.

## Documentation

- Keep README instructions consistent with actual project behavior.
- Include executable examples when appropriate.
- Do not invent functionality or test results.

## Communication

- Explain complex concepts in beginner-friendly language.
- Distinguish confirmed bugs from potential improvements.
- State assumptions and uncertainties.
- Prefer precise, actionable explanations.

## Instruction priority

When instructions conflict, apply this order:

1. The current user request and explicit constraints.
2. These repository instructions.
3. Existing project conventions and documentation.

If a conflict remains ambiguous, state it instead of silently choosing.
