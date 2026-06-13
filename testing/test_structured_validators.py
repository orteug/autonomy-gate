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
    def complete_handoff(self, *, status="BUILD_READY"):
        return {
            "workflow_id": "WF-20260611-001",
            "packet_version": "v1",
            "status": status,
            "architecture_option_id": "OPT-1",
            "terminal_action_boundary": "Produce an internal review document without external action",
            "architecture_decision_record": {
                "selected_option_id": "OPT-1",
                "selected_by": "Operations owner",
                "selection_date": "2026-06-12",
                "rejected_or_omitted_options": ["CODE_FIRST: unnecessary operating burden"],
            },
            "manifest": [{
                "path": "instructions.md",
                "purpose": "Bound the workflow",
                "complete_content": "Use supplied evidence and produce only the internal review document.",
                "source_evidence": ["packet.terminal_action"],
            }],
            "permissions_credentials_contract": ["Read supplied files only; no production credentials"],
            "deterministic_controls": ["Reject missing source evidence before model invocation"],
            "human_checkpoints": [],
            "prohibited_actions": ["Do not publish or modify source systems"],
            "logging_audit_requirements": ["Record packet version, input hash, status, and output location"],
            "failure_rollback_stop_behavior": ["Stop before output when validation fails"],
            "acceptance_tests": [{
                "setup": "Valid source data",
                "input": "One workflow run",
                "expected": "Internal review document",
                "pass_criterion": "No external action occurs",
            }],
            "deployment_sequence": ["Create instructions", "Run acceptance tests", "Record acknowledgement"],
            "assumptions": [],
            "unresolved_dependencies": [],
            "expiration_triggers": ["Terminal action, controls, tools, permissions, or policy changes"],
            "version_invalidation_triggers": ["Any material change creates a new packet version and invalidates prior approval"],
            "tool_alternatives": ["Use any approved workspace preserving the same controls"],
            "builder_acknowledgement": "Required before implementation begins",
            "stop_conditions": ["Permission mismatch"],
        }

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

    def test_build_ready_requires_full_build_contract(self):
        payload = self.complete_handoff()
        del payload["permissions_credentials_contract"]
        result = run_script("validate_build_handoff.py", payload)
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("permissions_credentials_contract", result.stdout)

    def test_blocked_pack_still_requires_generatable_contract_sections(self):
        payload = self.complete_handoff(status="BLOCKED_FOR_EVIDENCE")
        payload["architecture_option_id"] = "NOT_SELECTED"
        payload["architecture_decision_record"]["selected_option_id"] = "NOT_SELECTED"
        payload["unresolved_dependencies"] = ["Operator must select a generated architecture option"]
        del payload["deployment_sequence"]
        result = run_script("validate_build_handoff.py", payload)
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("deployment_sequence", result.stdout)

    def test_not_applicable_requires_human_procedure_and_safe_decomposition(self):
        payload = self.complete_handoff(status="NOT_APPLICABLE")
        payload["architecture_option_id"] = "NOT_APPLICABLE"
        payload["manifest"] = []
        payload["acceptance_tests"] = []
        payload["unresolved_dependencies"] = []
        result = run_script("validate_build_handoff.py", payload)
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("human_operating_procedure", result.stdout)
        self.assertIn("safe_decomposition_opportunities", result.stdout)


if __name__ == "__main__":
    unittest.main()
