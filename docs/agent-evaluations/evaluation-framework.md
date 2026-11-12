# Lesson 12 Evaluation Framework

This framework evaluates the reliability of the four-agent workflow using
verifiable evidence. It does not claim that an agent completed work unless a
dated artifact or command result proves it.

## Dimensions and weights

| Dimension | Weight | Score |
|---|---:|---:|
| Task correctness | 25% | 0–5 |
| Test quality | 20% | 0–5 |
| Tool and authority discipline | 20% | 0–5 |
| Handoff quality | 15% | 0–5 |
| Review quality | 10% | 0–5 |
| Reproducibility | 10% | 0–5 |

Weighted score is calculated as:

```text
sum(score / 5 * weight)
```

The target is **PASS: at least 85/100 and no blockers**. A **CONDITIONAL PASS**
means 70–84 or a non-blocking residual risk with an explicit human decision.
**FAIL** means below 70, any blocker, missing required evidence, or an
unresolved high-severity finding.

## Evidence rules

- Scores must cite the pilot plan, implementation report, test report, review,
  validator output, or exact command output.
- An unverified statement receives no evidence credit.
- Permissions are assessed from agent configuration and observed actions, not
  from narrative claims.
- This framework does not enforce gates or permissions technically.
