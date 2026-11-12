#!/usr/bin/env python3
"""Validate the repository's Lesson 12 agent workflow contracts."""

from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
VALID_STATUSES = {"PENDING", "PASS", "FAIL", "BLOCKED", "NOT_APPLICABLE"}
REQUIRED_FILES = (
    ".github/agents/researcher.agent.md",
    ".github/agents/developer.agent.md",
    ".github/agents/tester.agent.md",
    ".github/agents/reviewer.agent.md",
    ".github/agents/orchestrator.agent.md",
    ".github/skills/architecture-analysis/SKILL.md",
    ".github/skills/implementation-planning/SKILL.md",
    ".github/skills/test-engineering/SKILL.md",
    ".github/skills/release-readiness/SKILL.md",
    ".github/skills/review-code/SKILL.md",
    "docs/agent-orchestration.md",
    "docs/quality-gates.md",
)
REQUIRED_CONTRACT_KEYS = {
    "task_id",
    "objective",
    "scope",
    "acceptance_criteria",
    "assigned_agent",
    "workflow_stage",
    "inputs",
    "expected_outputs",
    "required_evidence",
    "approval_status",
    "gate_results",
    "risks",
    "blocking_findings",
}


def fail(message: str) -> None:
    raise ValueError(message)


def validate_contract(path: Path, task_ids: set[str]) -> None:
    try:
        data = json.loads(path.read_text())
    except (OSError, json.JSONDecodeError) as error:
        fail(f"{path}: invalid JSON: {error}")

    missing = REQUIRED_CONTRACT_KEYS - data.keys()
    if missing:
        fail(f"{path}: missing keys: {', '.join(sorted(missing))}")
    task_id = data["task_id"]
    if not isinstance(task_id, str) or not task_id:
        fail(f"{path}: task_id must be a non-empty string")
    if task_id in task_ids:
        fail(f"{path}: duplicate task_id {task_id}")
    task_ids.add(task_id)
    if data["approval_status"] not in VALID_STATUSES:
        fail(f"{path}: invalid approval_status")
    if not isinstance(data["blocking_findings"], list):
        fail(f"{path}: blocking_findings must be a list")
    for gate, status in data["gate_results"].items():
        if status not in VALID_STATUSES:
            fail(f"{path}: invalid status for gate {gate}: {status}")
    if any(status == "PASS" for status in data["gate_results"].values()):
        if not data["required_evidence"]:
            fail(f"{path}: PASS requires required_evidence")
    if data["approval_status"] == "PASS" and data["blocking_findings"]:
        fail(f"{path}: PASS cannot contain blocking_findings")
    evidence = data.get("evidence", [])
    if not isinstance(evidence, list):
        fail(f"{path}: evidence must be a list")
    for reference in data["inputs"] + data["expected_outputs"] + evidence:
        if reference.startswith(("http://", "https://")):
            continue
        candidate = reference.split(":", 1)[0]
        if "/" in candidate and not (ROOT / candidate).exists():
            fail(f"{path}: referenced path does not exist: {candidate}")


def main() -> int:
    errors: list[str] = []
    try:
        for relative in REQUIRED_FILES:
            if not (ROOT / relative).is_file():
                fail(f"required file does not exist: {relative}")
        task_ids: set[str] = set()
        contracts = sorted((ROOT / "docs/agent-contracts").glob("*.json"))
        if not contracts:
            fail("no JSON task contracts found")
        for contract in contracts:
            if contract.name == "task.schema.json":
                continue
            validate_contract(contract, task_ids)
    except ValueError as error:
        errors.append(str(error))

    if errors:
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        return 1
    print("Agent workflow validation passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
