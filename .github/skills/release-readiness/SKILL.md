---
name: release-readiness
description: Assess whether a Python repository change is ready for release by checking behavior, tests, documentation, packaging, compatibility, and review findings. Use before release, merge, publish, or final handoff.
---

# Release Readiness

## Triggers

Use this skill for release gates, final change assessment, pre-merge checks, packaging readiness, or a handoff that requires confidence beyond a single passing test.

## Workflow

1. Establish the release scope and inspect the current diff, project instructions, source, tests, documentation, and packaging configuration.
2. Run the focused validation required by the change, then run `python -m pytest -v` when the release scope warrants regression coverage.
3. Check public behavior, error handling, Python version support, package metadata, CLI/API documentation, and generated artifacts.
4. Reuse `.github/skills/review-code/SKILL.md` for the independent correctness, maintainability, and test-coverage review.
5. Confirm the four custom-agent boundaries: Researcher analyzes, Developer implements, Tester validates, and Reviewer assesses independently.
6. Classify the result as ready, not ready, or blocked, with evidence and explicit follow-up items.

## Boundaries

- Do not modify calculator functionality as part of a readiness assessment.
- Do not commit, push, merge, deploy, publish, or silently change release scope.
- Treat warnings, missing coverage, packaging artifacts, and documentation drift as explicit risks rather than silently accepting them.
- A passing pytest suite is necessary evidence, not the only release criterion.

## Expected Output

Return a readiness report containing:

- Scope and validation commands
- Test and review results
- Packaging, compatibility, and documentation checks
- Findings ranked by severity and confidence
- Blocking issues, residual risks, and a clear ready/not-ready/blocked decision
