---
name: implementation-planning
description: Turn approved repository research into a precise, minimal implementation plan with file-level changes, tests, documentation, and validation. Use before implementing a feature, bug fix, refactor, or configuration change.
---

# Implementation Planning

## Triggers

Use this skill when a research result must be converted into an actionable plan, when a change spans source and tests, or when scope and compatibility need to be explicit before editing.

## Workflow

1. Confirm the request and approval status; stop if the proposed change is not approved or is materially ambiguous.
2. Re-read the relevant source, tests, documentation, instructions, and configuration rather than relying on an unverified summary.
3. Define the smallest set of files to create or modify and explain each file's purpose.
4. Describe behavior, interfaces, error handling, compatibility requirements, and documentation updates.
5. Define focused tests and the narrowest validation command, with escalation criteria for broader checks.
6. Hand the plan to the Repository Developer and retain unresolved questions as explicit risks.

## Boundaries

- The Repository Researcher supplies evidence and architecture analysis.
- The Repository Developer performs edits and authorized validation.
- The Repository Tester independently verifies behavior; the Repository Reviewer independently reviews changes.
- Do not commit, push, merge, deploy, publish, or modify unrelated calculator functionality.

## Expected Output

Return an implementation plan containing:

- Objective and non-goals
- Ordered file-level changes
- API, compatibility, and error-handling considerations
- Test cases and validation commands
- Documentation impact
- Risks, assumptions, and completion criteria
