# Lesson 11: Multi-Agent Development Workflow

## Purpose and scope

Lesson 11 used four reusable custom agents to separate repository research,
implementation, testing, and review for the Calculator CLI. The workflow was
manual: the human selected the next agent and approved the transition between
planning, implementation, validation, and review. No automatic handoff,
deployment, release, commit, or push was configured.

## Agent configuration

Workspace agents are stored in `.github/agents/`:

| Agent | Purpose | Tools |
|---|---|---|
| `researcher.agent.md` | Analyze architecture, requirements, risks, edge cases, and produce an implementation plan. It must not edit files or run commands. | `read`, `search` |
| `developer.agent.md` | Implement an approved plan, preserve compatibility, add relevant tests, and run focused validation. | `read`, `search`, `edit`, `execute` |
| `tester.agent.md` | Design a test matrix, run authorized local tests, investigate failures, and report exact evidence. It must not edit production code and may not change tests unless authorized. | `read`, `search`, `execute` |
| `reviewer.agent.md` | Independently inspect changes against `main`, assess correctness and maintainability, and rank findings. It must not modify source, tests, or configuration. | `read`, `search`, `execute` |

The repository-wide behavior rules are in `.github/copilot-instructions.md`.
The review guidance used by the reviewer is `.github/skills/review-code/SKILL.md`.
The agents use documented VS Code Copilot tool aliases only; they do not declare
model restrictions or unsupported handoff settings.

## Manual task transfer and approval checkpoints

Tasks were transferred by returning the current agent's findings or plan in
Chat and then explicitly selecting the next custom agent in VS Code. The next
agent re-read the relevant files rather than relying on an implicit shared
workflow state.

The human approval checkpoints were:

1. Approve the researcher's plan to expose the existing `percentage()` API
   function as a CLI operation.
2. Authorize the developer to implement the plan, update tests and README, and
   run the existing tests.
3. Request an independent tester validation with a specified matrix and a full
   suite run.
4. Request an independent review against `main`.
5. Request this documentation after implementation, testing, and review.

These checkpoints are observed process decisions, not automatic features of the
Copilot harness.

## Implementation: percentage CLI operation

The existing `percentage(value, total)` function in `calculator.py` was reused.
The developer made the minimal CLI change in `calculator_cli.py`:

- imported `percentage`;
- added `"percentage": percentage` to `OPERATIONS`.

The existing two-number `argparse` interface and generic dispatch were retained.
The five existing operations (`add`, `subtract`, `multiply`, `divide`, and
`power`) were preserved. The existing exception handling converts a zero total
into exit code `1` with this stderr message:

```text
calculation error: Cannot calculate a percentage of zero.
```

The developer added CLI tests for successful, negative, decimal, help-output,
and zero-total behavior. README and changelog descriptions were updated. No
new dependency or Python API change was introduced.

## Testing strategy and actual results

The tester used two levels of validation:

1. An independent subprocess matrix covering standard percentages, zero
   numerator, zero denominator, negative numbers, decimals, large integers,
   invalid arguments, exit codes, stdout/stderr behavior, and regression cases
   for all five existing operations.
2. The complete existing pytest suite.

Observed results:

- Independent matrix: **19 cases passed, 0 failed**.
- Complete suite: **87 passed, 0 failed**.
- The suite emitted one existing `PytestRemovedIn10Warning` from the installed
  AnyIO pytest plugin. This warning did not fail the tests.

No line or branch coverage report was generated. The validation did not exhaust
all possible numeric inputs, and it did not test every packaging or environment
scenario.

## Review findings

The reviewer compared the current worktree changes with the available `main`
reference. There was no committed branch diff relative to `main`; the
percentage work was uncommitted at review time, so the review covered the
uncommitted source, tests, and documentation changes.

The review found no high- or medium-priority issues. It confirmed that the
implementation was minimal, preserved the Python API and existing operations,
used the existing error path, added relevant tests, and introduced no security
or dependency concerns.

Optional low-priority improvements were recorded:

- add percentage-specific zero-numerator and large-integer test cases;
- test the installed `calculator-cli` entry point directly if that is part of
  the release contract;
- remove or ignore generated `dist/` and `calculator_cli.egg-info/` artifacts
  before committing.

These were recommendations, not unresolved release blockers.

## Implemented features versus future ideas

### Implemented in Lesson 11

- Four workspace custom agents with role-specific tool restrictions.
- Manual researcher-to-developer-to-tester-to-reviewer workflow.
- CLI support for `percentage` using the existing Python function.
- Focused CLI tests, independent validation, and full-suite validation.
- README and changelog updates.
- Independent review against `main`.

### Future ideas, not implemented

- Automatic agent handoffs or workflow orchestration.
- Automated enforcement of the no-commit/no-push boundaries.
- Line and branch coverage thresholds in CI.
- Direct integration tests for the installed console entry point.
- Additional numeric edge-case tests such as non-finite values and extreme
  numeric ranges.

## Limitations of the Copilot harness

- Agent selection and task transfer were manual; no handoff configuration was
  used.
- Tool restrictions guide what each agent can use, but this lesson did not
  establish a separate policy-enforcement mechanism for every prohibition.
- The researcher was restricted to read/search tools and therefore could not
  execute validation itself.
- The tester and reviewer could execute local commands, so their instructions
  explicitly prohibited edits and destructive actions.
- The harness did not automatically provide test coverage measurements,
  release gating, or commit/push protection.
- Review quality still depended on the agent reading repository evidence and on
  human approval of scope and conclusions.

## Lessons learned

- Separate roles reduce context mixing: research produced the plan, development
  changed code, testing gathered evidence, and review challenged the result.
- Minimal tool permissions make role boundaries clearer, especially for research
  and review agents.
- Manual transfer makes approval points explicit, but it requires the next
  agent to re-establish context from files and prior results.
- Exact test commands and outputs are more reliable than claims that behavior
  was tested.
- Documentation must be updated alongside behavior changes so supported CLI
  operations do not diverge from the implementation.
- Independent review is useful even after tests pass: it identified coverage
  and worktree-cleanliness improvements without inventing functional defects.
