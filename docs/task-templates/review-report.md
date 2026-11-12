# Review Report Template

```yaml
task_id: "<same task id as test report>"
objective: "<review objective>"
scope:
  in_scope:
    - "<diff, source, tests, docs, or packaging reviewed>"
  out_of_scope:
    - "<unavailable or intentionally excluded area>"
acceptance_criteria:
  - criterion: "<condition>"
    status: "passed"
files_involved:
  - "<reviewed path>"
risks:
  - "<accepted residual risk or none>"
evidence:
  - "<diff, path, command, or review observation>"
approval_status: "pending"
```

## Findings

| Severity | Confidence | File/line | Evidence and impact | Recommendation | Status |
|---|---|---|---|---|---|
| `<critical/high/medium/low>` | `<high/medium/low>` | `<path:line>` | `<confirmed finding>` | `<minimal fix>` | `<open/resolved/accepted>` |

## Review output

- Review base or diff scope:
- Tests and checks considered:
- High-severity findings:
- Medium-severity findings:
- Low-priority suggestions:
- Release readiness decision: `ready`, `not-ready`, or `blocked`
- Human approval required for: commit, push, merge, deploy, or release

Reuse [review-code](../../.github/skills/review-code/SKILL.md) for Python review
guidance and [release-readiness](../../.github/skills/release-readiness/SKILL.md)
for final readiness checks. High-severity findings must be resolved before
merge approval.
