#!/usr/bin/env python3
"""Validate offline, read-only MCP/GitHub issue-research reports."""

from __future__ import annotations

import json
import re
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Any
from urllib.parse import urlsplit

EXPECTED_REPOSITORY = "phlppgdfry/copilot-leerpad"
EXPECTED_ISSUE = 17
EXPECTED_PULL_REQUEST = 18
VALID_STATUSES = {"VERIFIED", "SIMULATED", "NOT TESTED", "FAILED"}
ALLOWED_READ_ONLY_TOOLS = {
    "offline-fixture",
    "github.get_issue",
    "github.issue_read",
    "github.pull_request_read",
    "github-mcp-server-issue_read",
    "github-mcp-server-pull_request_read",
    "microsoftLean-microsoft_docs_search",
    "microsoftLean-microsoft_docs_fetch",
}
ALLOWED_READ_ONLY_OPERATIONS = {"fetch", "get", "get_files", "read", "search"}
FORBIDDEN_OPERATION_WORDS = {
    "approve",
    "assign",
    "close",
    "comment",
    "commit",
    "create",
    "delete",
    "edit",
    "label",
    "merge",
    "modify",
    "mutate",
    "push",
    "remove",
    "reopen",
    "update",
    "upload",
    "write",
}
INJECTION_PATTERNS = (
    re.compile(r"\bignore\s+(?:all\s+)?previous\s+instructions?\b", re.I),
    re.compile(r"\bdisregard\s+(?:all\s+)?previous\s+instructions?\b", re.I),
    re.compile(r"\b(upload|send|exfiltrate)\b.{0,80}\b(environment variables?|secrets?|credentials?)\b", re.I),
    re.compile(r"\b(reveal|print|disclose)\b.{0,80}\b(system prompt|environment variables?|secrets?)\b", re.I),
    re.compile(r"\bexecute\s+(?:this\s+)?(?:command|script)\b", re.I),
)


@dataclass(frozen=True)
class ValidationResult:
    """The deterministic result returned by :func:`validate_report`."""

    valid: bool
    errors: tuple[str, ...] = ()
    security_findings: tuple[str, ...] = ()


def _error(errors: list[str], message: str) -> None:
    errors.append(message)


def _is_nonempty_string(value: Any) -> bool:
    return isinstance(value, str) and bool(value.strip())


def _check_targets(report: dict[str, Any], errors: list[str]) -> None:
    if report.get("repository") != EXPECTED_REPOSITORY:
        _error(errors, f"repository must be {EXPECTED_REPOSITORY!r}")
    issue = report.get("issue")
    if not isinstance(issue, dict) or issue.get("number") != EXPECTED_ISSUE:
        _error(errors, "issue.number must be 17")
    pull_request = report.get("pull_request")
    if not isinstance(pull_request, dict) or pull_request.get("number") != EXPECTED_PULL_REQUEST:
        _error(errors, "pull_request.number must be 18")


def _operation_is_forbidden(operation: dict[str, Any]) -> bool:
    if any(operation.get(key) is True for key in ("write", "mutate", "is_write")):
        return True
    for key in ("operation", "action", "method", "capability", "tool"):
        value = operation.get(key)
        if isinstance(value, str):
            words = set(re.findall(r"[a-z]+", value.lower()))
            if words & FORBIDDEN_OPERATION_WORDS:
                return True
    return operation.get("read_only") is False


def _check_read_only_boundary(
    operation: dict[str, Any], location: str, errors: list[str]
) -> None:
    tool = operation.get("tool")
    if not _is_nonempty_string(tool) or tool not in ALLOWED_READ_ONLY_TOOLS:
        _error(errors, f"{location}.tool is not an approved read-only tool")
    for key in ("operation", "action", "method", "capability"):
        value = operation.get(key)
        if value is not None and (
            not isinstance(value, str) or value.lower() not in ALLOWED_READ_ONLY_OPERATIONS
        ):
            _error(errors, f"{location}.{key} is not an approved read-only operation")


def _is_allowed_verified_source(source: Any) -> bool:
    if isinstance(source, dict):
        if "repository" in source and source["repository"] != EXPECTED_REPOSITORY:
            return False
        source = source.get("id")
    if not _is_nonempty_string(source):
        return False

    source = source.strip()
    if source in {"issue:17", "pr:18", "pull_request:18"}:
        return True

    parsed = urlsplit(source)
    return (
        parsed.scheme == "https"
        and parsed.netloc == "github.com"
        and parsed.path in {
            "/phlppgdfry/copilot-leerpad/issues/17",
            "/phlppgdfry/copilot-leerpad/pull/18",
        }
        and not parsed.query
        and not parsed.fragment
    )


def _check_no_write_evidence(report: dict[str, Any], errors: list[str]) -> None:
    evidence = report.get("no_write_evidence")
    if not isinstance(evidence, dict):
        _error(errors, "no_write_evidence is required")
        return
    if evidence.get("asserted") is not True:
        _error(errors, "no_write_evidence.asserted must be true")
    if not _is_nonempty_string(evidence.get("statement")):
        _error(errors, "no_write_evidence.statement is required")
    operations = evidence.get("operations")
    if not isinstance(operations, list) or not operations:
        _error(errors, "no_write_evidence.operations must be a non-empty list")
        return
    for index, operation in enumerate(operations):
        if not isinstance(operation, dict):
            _error(errors, f"no_write_evidence.operations[{index}] must be an object")
        else:
            location = f"no_write_evidence.operations[{index}]"
            _check_read_only_boundary(operation, location, errors)
            if _operation_is_forbidden(operation):
                _error(errors, f"{location} claims a write-capable operation")


def _check_result(result: Any, index: int, errors: list[str]) -> None:
    if not isinstance(result, dict):
        _error(errors, f"results[{index}] must be an object")
        return
    status = result.get("status")
    if status not in VALID_STATUSES:
        _error(errors, f"results[{index}].status is not allowed")
    if not _is_nonempty_string(result.get("finding")):
        _error(errors, f"results[{index}].finding is required")
    if status != "VERIFIED":
        return

    source = result.get("source")
    if not _is_allowed_verified_source(source):
        _error(
            errors,
            f"results[{index}] VERIFIED finding requires source attribution; "
            "source must be an allowed Issue 17 or PR 18 source",
        )
    tool_evidence = result.get("tool_evidence")
    if not isinstance(tool_evidence, dict):
        _error(errors, f"results[{index}] VERIFIED finding requires tool_evidence")
        return
    if not _is_nonempty_string(tool_evidence.get("tool")):
        _error(errors, f"results[{index}].tool_evidence.tool is required")
    if tool_evidence.get("read_only") is not True:
        _error(errors, f"results[{index}].tool_evidence.read_only must be true")
    if not _is_nonempty_string(tool_evidence.get("response")):
        _error(errors, f"results[{index}] requires returned tool response evidence")
    _check_read_only_boundary(tool_evidence, f"results[{index}].tool_evidence", errors)
    if _operation_is_forbidden(tool_evidence):
        _error(errors, f"results[{index}] tool_evidence claims a write-capable operation")


def _strings(value: Any) -> list[str]:
    if isinstance(value, str):
        return [value]
    if isinstance(value, dict):
        return [text for item in value.values() for text in _strings(item)]
    if isinstance(value, (list, tuple)):
        return [text for item in value for text in _strings(item)]
    return []


def _security_findings(report: dict[str, Any]) -> tuple[str, ...]:
    findings: list[str] = []
    untrusted_data = (
        report.get("results", []),
        report.get("no_write_evidence", {}),
    )
    for text in _strings(untrusted_data):
        for pattern in INJECTION_PATTERNS:
            if pattern.search(text):
                finding = "Prompt-injection-like text detected in retrieved report data"
                if finding not in findings:
                    findings.append(finding)
                break
    return tuple(findings)


def validate_report(report: Any) -> ValidationResult:
    """Validate a parsed report without contacting any external service."""
    errors: list[str] = []
    if not isinstance(report, dict):
        return ValidationResult(False, ("report must be a JSON object",))
    _check_targets(report, errors)
    _check_no_write_evidence(report, errors)
    results = report.get("results")
    if not isinstance(results, list) or not results:
        _error(errors, "results must be a non-empty list")
    else:
        for index, result in enumerate(results):
            _check_result(result, index, errors)
    security_findings = _security_findings(report)
    return ValidationResult(
        valid=not errors and not security_findings,
        errors=tuple(errors),
        security_findings=security_findings,
    )


def validate_file(path: Path) -> ValidationResult:
    """Read and validate one JSON report, returning explicit file errors."""
    try:
        text = path.read_text(encoding="utf-8")
    except OSError as error:
        return ValidationResult(False, (f"could not read {path}: {error}",))
    try:
        report = json.loads(text)
    except json.JSONDecodeError as error:
        return ValidationResult(False, (f"invalid JSON in {path}: {error}",))
    return validate_report(report)


def main(argv: list[str] | None = None) -> int:
    arguments = sys.argv[1:] if argv is None else argv
    if len(arguments) != 1:
        print("Usage: validate_mcp_research.py REPORT.json", file=sys.stderr)
        return 2
    result = validate_file(Path(arguments[0]))
    if result.valid:
        print("MCP research report is valid and read-only.")
        return 0
    print("MCP research report is invalid or unsafe.")
    for message in (*result.errors, *result.security_findings):
        print(f"ERROR: {message}")
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
