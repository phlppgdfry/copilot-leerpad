---
name: architecture-analysis
description: Analyze a repository's architecture, requirements, dependencies, risks, and compatibility boundaries before implementation. Use when exploring an unfamiliar codebase, assessing a change, or preparing research for the Repository Researcher.
---

# Architecture Analysis

## Triggers

Use this skill when a task needs repository discovery, architecture mapping, requirements analysis, dependency tracing, risk identification, or compatibility assessment before code is changed.

## Workflow

1. Read `.github/copilot-instructions.md` and the relevant project documentation.
2. Inspect the source, tests, configuration, and existing customizations related to the request.
3. Trace public APIs, callers, data flow, error paths, and user-facing behavior.
4. Record confirmed constraints, assumptions, edge cases, dependencies, and regression risks.
5. Separate facts supported by repository evidence from open questions.
6. Produce an ordered implementation plan for the Repository Developer.

## Boundaries

- Prefer the Repository Researcher for read-only architecture work.
- Do not edit files, run commands, or change calculator behavior during analysis.
- Preserve existing role boundaries: research informs implementation; it does not perform implementation or testing.

## Expected Output

Return:

- Architecture summary with relevant file paths
- Requirements and compatibility constraints
- Risks, edge cases, and assumptions
- Ordered implementation steps
- Focused validation commands for the Repository Tester or Developer
