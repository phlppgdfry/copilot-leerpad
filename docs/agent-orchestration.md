# Agent Orchestration Workflow

## Purpose and scope

This workflow coordinates repository research, implementation, testing, and
review for the Calculator CLI without changing the calculator's behavior or
automating irreversible Git or release actions. It uses the four existing
workspace agents and the four existing Agent Skills.

The workflow is controlled and resumable: every transition carries a
structured handoff, every quality gate has evidence, and a human approves
scope-sensitive transitions.

## Participants and responsibilities

| Role | Agent | Primary skills | Responsibilities | Prohibited actions |
|---|---|---|---|---|
| Research | [Repository Researcher](../.github/agents/researcher.agent.md) | [architecture-analysis](../.github/skills/architecture-analysis/SKILL.md), [implementation-planning](../.github/skills/implementation-planning/SKILL.md) | Inspect architecture, requirements, dependencies, risks, edge cases, and produce a plan. | Edit files, run commands, tests, or builds. |
| Implementation | [Repository Developer](../.github/agents/developer.agent.md) | [implementation-planning](../.github/skills/implementation-planning/SKILL.md) | Implement an approved plan, preserve compatibility, update relevant tests/docs, and run focused validation. | Commit, push, merge, deploy, publish, or expand scope without approval. |
| Testing | [Repository Tester](../.github/agents/tester.agent.md) | [test-engineering](../.github/skills/test-engineering/SKILL.md) | Define the test matrix, run authorized local checks, investigate failures, and report exact evidence. | Modify production code or tests unless explicitly authorized; commit or release. |
| Review | [Repository Reviewer](../.github/agents/reviewer.agent.md) | [review-code](../.github/skills/review-code/SKILL.md), [release-readiness](../.github/skills/release-readiness/SKILL.md) | Independently assess correctness, security, maintainability, compatibility, coverage, and readiness. | Modify source, tests, configuration, commit, push, merge, or release. |
| Coordination | [Lesson 12 Orchestrator](../.github/agents/orchestrator.agent.md) | All four workflow skills as delegated context | Pass structured contracts between the four specialist agents, enforce evidence gates, and halt on blockers. | Edit files directly, invent delegation APIs, approve human gates, or perform Git/release actions. |

Repository-wide rules remain in
[`copilot-instructions.md`](../.github/copilot-instructions.md).

## Execution order

```text
Research -> human plan approval -> Implementation -> Tester
    ^                                              |
    |                                              v
    +------- failure or requested correction <- Review
                                                   |
                                                   v
                              human merge/release approval -> CI -> release
```

1. **Research:** create a research handoff using
   [`research-handoff.md`](task-templates/research-handoff.md).
2. **Plan approval:** a human confirms objective, scope, acceptance criteria,
   risks, and files before implementation starts.
3. **Implementation:** the Developer consumes the approved handoff and returns
   an implementation handoff using
   [`implementation-handoff.md`](task-templates/implementation-handoff.md).
4. **Testing:** the Tester consumes the implementation handoff and returns
   [`test-report.md`](task-templates/test-report.md).
5. **Review:** only after tests pass, the Reviewer returns
   [`review-report.md`](task-templates/review-report.md), using
   `review-code` and `release-readiness` where applicable.
6. **Correction loop:** high or medium findings, failed tests, or scope
   mismatches return to the Developer with a new evidence-bearing handoff.
7. **Final gate:** CI must pass and a human must explicitly authorize commit,
   push, merge, or release. Agents do not perform those actions automatically.

## Task contract

Every handoff and report must contain these fields:

| Field | Required content |
|---|---|
| Task ID | Stable identifier, for example `calc-2026-001`. |
| Objective | One measurable outcome. |
| Scope | In-scope work and explicit non-goals. |
| Acceptance criteria | Observable conditions for completion. |
| Files involved | Existing and expected paths; use `none` when applicable. |
| Risks | Technical, compatibility, security, and process risks. |
| Evidence | Repository paths, commands, outputs, or review observations. |
| Approval status | `pending`, `approved`, `rejected`, `blocked`, or `complete`, with approver and date when known. |

Reports may add role-specific fields, but must not remove these contract
fields. Handoffs should be passed as plain Markdown or pasted into the next
agent's prompt so the next agent can re-read the repository evidence.

## Quality gates

1. **Plan gate:** the Researcher has produced a complete plan and a human has
   approved it before the Developer edits anything.
2. **Implementation gate:** the Developer records changed files, non-goals,
   compatibility impact, and focused validation results.
3. **Test gate:** the Tester runs the required matrix; tests must pass before
   the Reviewer can mark review complete.
4. **Review gate:** high-severity findings must be resolved and medium-severity
   findings must be accepted or resolved before merge approval.
5. **CI gate:** required CI checks must pass before release.
6. **Human action gate:** a human must approve commit, push, merge, deploy, or
   release. No agent is authorized to infer that approval from a passing test.

## Human approval checkpoints

Human approval is required:

1. Before implementation begins.
2. Before widening scope or changing acceptance criteria.
3. Before accepting a test exception, review finding, or known risk.
4. Before commit, push, merge, deploy, or release.

The approval should be recorded in the handoff's `Approval status` field.

## Failure handling

- **Research incomplete:** keep status `blocked`; identify missing evidence and
  return to research. Do not start implementation.
- **Implementation failure:** return the Developer's evidence and failed
  acceptance criteria to the Developer; do not ask the Tester to validate an
  unknown state.
- **Test failure:** classify as product, test, or environment failure. Fix the
  cause, rerun the affected tests, and preserve the original evidence.
- **Review finding:** create a correction handoff referencing the finding and
  acceptance criteria. High-severity findings block merge.
- **CI failure:** treat CI as authoritative for release readiness; investigate
  and rerun after correction.
- **Tool or agent failure:** preserve the last valid handoff, mark the task
  blocked, and resume with the same Task ID after the environment is restored.

No broad catches, silent defaults, weakened tests, or success-shaped fallback
reports are permitted.

## Rollback approach

Before implementation, record the baseline commit or worktree state and the
files in scope. Prefer small, isolated changes. If a change must be rolled
back:

1. Stop the workflow and mark the current handoff `blocked`.
2. Ask a human to approve the rollback action.
3. Revert only the approved files or commit; do not use destructive resets or
   discard unrelated worktree changes.
4. Rerun the relevant tests and record the rollback evidence.
5. Reopen research with the original Task ID or create a linked follow-up ID.

Agents must not commit, push, merge, deploy, publish, or execute rollback
actions automatically.

## Native delegation support

The repository uses documented VS Code custom-agent primitives: workspace
agents, role-specific `tools`, and the `agents` frontmatter field. The active
harness has also successfully invoked the Researcher, Tester, and Reviewer as
subagents for this lesson. The new Orchestrator configuration restricts its
delegation list to the four existing specialist agents.

Delegation is therefore **supported but gate-controlled**, not an unattended
pipeline. The Orchestrator may delegate focused work and return results, while
plan approval, scope changes, and Git/release actions remain manual. If the
active harness does not expose the `agent` tool, use the manual workflow above;
do not simulate delegation or claim it occurred.

## Automation versus manual control

| Concern | Automated | Manual |
|---|---|---|
| Role-specific tool restrictions | Agent configuration guides available tools. | Human selects the correct agent. |
| Architecture and plan content | Skills provide repeatable instructions. | Research and approval are human-supervised. |
| Tests | Tester/Developer can run pytest when authorized. | Test scope, interpretation, and exceptions require judgment. |
| Review | Reviewer can use the review skill and local checks. | Findings and their resolution require human acceptance. |
| Quality gates | Templates make required evidence explicit. | Gate decisions are not enforced by this repository. |
| CI and release | Existing repository/CI systems, when configured, provide checks. | Human authorizes commit, push, merge, and release. |

## Reusable templates

- [Research handoff](task-templates/research-handoff.md)
- [Implementation handoff](task-templates/implementation-handoff.md)
- [Test report](task-templates/test-report.md)
- [Review report](task-templates/review-report.md)
