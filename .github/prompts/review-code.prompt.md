
---
name: review-code
description: Review Python code for correctness, quality and maintainability
---

# Professional Python Code Review

Act as a senior Python engineer and code reviewer.

Review the selected code or attached files.

## Review criteria

1. Functional correctness
2. Edge cases
3. Error handling
4. Readability and maintainability
5. Type hints
6. Test coverage
7. Documentation accuracy
8. Unnecessary complexity

## Output format

Return a table containing:

| Priority | File/Line | Finding | Evidence | Recommendation |
|----------|-----------|---------|----------|----------------|

Priority levels:
- High: confirmed bug or significant correctness issue
- Medium: meaningful quality or maintainability issue
- Low: optional improvement

## Rules

- Do not change any files.
- Do not invent bugs.
- Do not confuse style preferences with functional defects.
- Identify up to five meaningful findings.
- Explain each finding clearly for a beginner.
- State when no meaningful issues are found.
- Finish with an overall code quality assessment.
