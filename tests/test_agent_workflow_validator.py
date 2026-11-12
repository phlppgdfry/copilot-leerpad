import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).parents[1]
VALIDATOR = ROOT / "scripts/validate_agent_workflow.py"


def test_agent_workflow_validator_passes():
    result = subprocess.run(
        [sys.executable, str(VALIDATOR)],
        cwd=ROOT,
        capture_output=True,
        text=True,
        check=False,
    )

    assert result.returncode == 0
    assert "passed" in result.stdout.lower()
    assert result.stderr == ""


def test_pilot_contract_is_valid_json():
    contract = json.loads(
        (ROOT / "docs/agent-contracts/pilot-001.json").read_text()
    )

    assert contract["task_id"] == "LESSON12-PILOT-001"
    assert contract["approval_status"] == "PASS"
    assert set(contract["gate_results"].values()) <= {
        "PENDING",
        "PASS",
        "FAIL",
        "BLOCKED",
        "NOT_APPLICABLE",
    }


def test_task_schema_requires_evidence():
    schema = json.loads(
        (ROOT / "docs/agent-contracts/task.schema.json").read_text()
    )

    assert "evidence" in schema["required"]
