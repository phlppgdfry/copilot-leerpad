# Lesson 12 Quality Gates

These gates describe the controlled workflow; documentation and JSON contracts
do not independently enforce permissions or human decisions.

| Gate | Required condition | Evidence | Blocking status |
|---|---|---|---|
| 1. Plan approval | Research handoff is complete and human-approved. | `pilot-001-plan.md` and approval record. | `FAIL` or `BLOCKED` stops implementation. |
| 2. Implementation complete | Developer reports scope, changed files, deviations, and focused checks. | `pilot-001-implementation.md`. | Missing evidence blocks testing. |
| 3. Tests pass | Tester runs the required matrix and full pytest suite successfully. | `pilot-001-test-report.md`. | Any failed required test blocks review completion. |
| 4. Review approved | No unresolved blocker or major correctness finding. | `pilot-001-review.md`. | Blocker/major blocks merge approval. |
| 5. CI verified | Required CI checks pass on supported Python versions and workflow validation. | GitHub Actions run linked by a human. | Failed or unavailable CI blocks release. |
| 6. Human action approval | Human explicitly approves commit, push, merge, deploy, or release. | Recorded approval status and GitHub audit trail. | Agents must not infer approval. |

## Status vocabulary

Contracts use only `PENDING`, `PASS`, `FAIL`, `BLOCKED`, and `NOT_APPLICABLE`.
`PASS` requires evidence. `PENDING` means work is not complete. `FAIL` means
the condition was checked and not met. `BLOCKED` means it could not be
checked. `NOT_APPLICABLE` requires an explanation.

## Correction loop

Failed gates return to the responsible role with the original Task ID and
preserved evidence. High-severity review findings must be resolved before
merge. A human must approve any scope change or exception.
