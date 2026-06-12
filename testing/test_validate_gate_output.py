import importlib.util
import sys
import unittest
from pathlib import Path


MODULE_PATH = Path(__file__).with_name("validate_gate_output.py")
SPEC = importlib.util.spec_from_file_location("validate_gate_output", MODULE_PATH)
validator = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
sys.modules[SPEC.name] = validator
SPEC.loader.exec_module(validator)


def gate_output(*, pack: str, disposition: str = "Disposition: PENDING", confidence: str = "HIGH", gaps: str = "None") -> str:
    return f"""━━ WORKFLOW INTAKE SNAPSHOT ━━━
Name: Test workflow
Evidence gaps: {gaps}

━━ AUTONOMY DECISION PACKET ━━━
Autonomy: AUTONOMOUS
Assessment surface: ChatGPT Project
Execution architecture: Human-triggered model workspace producing an internal document
Builder surface: Platform administrator
Confidence: {confidence}
Terminal action: Produce an internal review document
Justification: RULE-03 and RULE-06 support bounded document production
Controls required: Source validation and retained output
Evidence gaps: {gaps}
Build Handoff Pack: BUILD_READY

━━ PROJECT SETUP BRIEF ━━━
Purpose: Produce an internal review document.
{pack}

━━ OPERATOR DISPOSITION ━━━
{disposition}
"""


class GateOutputValidatorTests(unittest.TestCase):
    def assert_fails_with(self, text: str, code: str) -> None:
        result = validator.validate(text)
        self.assertIn(code, {finding.code for finding in result.findings})
        self.assertFalse(result.passed)

    def test_rejects_output_without_build_handoff_pack(self):
        self.assert_fails_with(gate_output(pack="No implementation package was generated."), "PACK-MISSING")

    def test_rejects_build_ready_manifest_without_complete_content(self):
        pack = """BUILD HANDOFF PACK
Handoff status: BUILD_READY
Manifest:
- Path: instructions.md
  Purpose: Runtime instructions
  Source evidence: packet terminal action
"""
        self.assert_fails_with(gate_output(pack=pack), "PACK-CONTENT")

    def test_rejects_model_selected_approval_in_prose(self):
        pack = """BUILD HANDOFF PACK
Handoff status: BLOCKED_FOR_EVIDENCE
Required before build: Operator retention policy
"""
        self.assert_fails_with(
            gate_output(pack=pack, disposition="Disposition: APPROVE_FOR_BUILD"),
            "DISP-PRESELECTED",
        )

    def test_rejects_approval_without_required_metadata(self):
        pack = """BUILD HANDOFF PACK
Handoff status: BUILD_READY
Manifest:
- Path: instructions.md
  Purpose: Runtime instructions
  Source evidence: packet terminal action
  Complete content: Use only supplied source data and produce the named internal document.
Acceptance tests:
- Setup: Valid source data
  Input: One workflow run
  Expected: Internal review document
  Pass criterion: No external action occurs
"""
        self.assert_fails_with(
            gate_output(pack=pack, disposition="Disposition: APPROVE_FOR_BUILD\nName / role: Operator"),
            "DISP-METADATA",
        )

    def test_rejects_high_confidence_with_decision_evidence_gaps(self):
        pack = """BUILD HANDOFF PACK
Handoff status: BLOCKED_FOR_EVIDENCE
Required before build: Retention policy
"""
        self.assert_fails_with(
            gate_output(pack=pack, confidence="HIGH", gaps="Terminal-action authority is unknown"),
            "CONTRA-HIGH-GAPS",
        )

    def test_rejects_legacy_overloaded_surface_field(self):
        text = gate_output(
            pack="BUILD HANDOFF PACK\nHandoff status: BLOCKED_FOR_EVIDENCE\nRequired before build: Retention policy"
        ).replace(
            "Assessment surface: ChatGPT Project\nExecution architecture: Human-triggered model workspace producing an internal document\nBuilder surface: Platform administrator",
            "Surface: PROJECT",
        )
        self.assert_fails_with(text, "PKT-FIELD")

    def test_accepts_bold_markdown_packet_fields_without_crashing(self):
        text = gate_output(
            pack="BUILD HANDOFF PACK\nHandoff status: BLOCKED_FOR_EVIDENCE\nRequired before build: Retention policy",
            confidence="MEDIUM",
            gaps="Retention policy is unknown",
        )
        for field in ("Autonomy", "Assessment surface", "Execution architecture", "Builder surface", "Confidence", "Terminal action", "Justification", "Controls required", "Evidence gaps"):
            text = text.replace(f"{field}:", f"**{field}:**")
        result = validator.validate(text)
        self.assertNotIn("PKT-FIELD", {finding.code for finding in result.findings})

    def test_accepts_bold_markdown_handoff_status(self):
        text = gate_output(
            pack="BUILD HANDOFF PACK\n**Handoff status:** `BLOCKED_FOR_EVIDENCE`\nRequired before build: Retention policy",
            confidence="MEDIUM",
            gaps="Retention policy is unknown",
        )
        result = validator.validate(text)
        self.assertNotIn("PACK-STATUS", {finding.code for finding in result.findings})


if __name__ == "__main__":
    unittest.main()
