# Test Report Template

```yaml
task_id: "<same task id as implementation>"
objective: "<validation objective>"
scope:
  in_scope:
    - "<behavior and regression area tested>"
  out_of_scope:
    - "<untested area>"
acceptance_criteria:
  - criterion: "<condition>"
    status: "passed"
files_involved:
  - "<implementation or test path>"
risks:
  - "<coverage gap or environment risk>"
evidence:
  - command: "<exact command>"
    result: "<passed, failed, or blocked with counts>"
approval_status: "pending"
```

## Test output

- Test matrix:
- Commands executed:
- Exact results:
- Failure classification:
- Warnings:
- Coverage gaps:
- Residual risks:
- Requested next role: `Repository Reviewer`

The Tester must not weaken tests or claim a pass without executing the command.
Tests must pass before the Reviewer can complete review.
