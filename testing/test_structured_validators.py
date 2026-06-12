import json
import subprocess
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def run_script(script: str, payload: dict) -> subprocess.CompletedProcess[str]:
    with tempfile.NamedTemporaryFile("w", suffix=".json", delete=False) as handle:
        json.dump(payload, handle)
        path = handle.name
    return subprocess.run(
        ["python3", str(ROOT / "testing" / script), path],
        text=True,
        capture_output=True,
        check=False,
    )


class StructuredValidatorTests(unittest.TestCase):
    def test_build_ready_requires_complete_manifest_content(self):
        result = run_script("validate_build_handoff.py", {
            "workflow_id": "WF-20260611-001",
            "packet_version": "v1",
            "status": "BUILD_READY",
            "architecture_option_id": "primary",
            "manifest": [{"path": "AGENTS.md", "purpose": "Builder rules", "source_evidence": ["terminal_action"]}],
            "assumptions": [], "unresolved_dependencies": [],
            "prohibited_actions": ["Do not publish externally"],
            "acceptance_tests": [{"setup": "fixture", "input": "run", "expected": "draft", "pass_criterion": "no publish"}],
            "expiration_triggers": ["scope changes"], "stop_conditions": ["permission mismatch"]
        })
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("complete_content", result.stdout)

    def test_architecture_requires_selected_option_to_exist(self):
        result = run_script("validate_architecture_options.py", {
            "options": [{"id": "primary", "class": "PRIMARY"}],
            "selected_option_id": "missing"
        })
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("selected_option_id", result.stdout)

    def test_named_tool_requires_source_and_verification_date(self):
        result = run_script("validate_tool_recommendations.py", {
            "recommendations": [{"tool": "Example Tool", "capability": "approval"}]
        })
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("source_url", result.stdout)


if __name__ == "__main__":
    unittest.main()
