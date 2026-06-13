import json
import re
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


class ReleaseContractTests(unittest.TestCase):
    HISTORICAL_PUBLIC_PATHS = {"examples/trial-audit-output.md"}

    @classmethod
    def normative_paths(cls):
        manifest = (ROOT / "PUBLIC_RELEASE_MANIFEST.txt").read_text(encoding="utf-8").splitlines()
        return [
            ROOT / relative
            for relative in manifest
            if relative.endswith(".md") and relative not in cls.HISTORICAL_PUBLIC_PATHS
        ]

    def test_all_setup_manifests_include_operating_contract(self):
        paths = [
            ROOT / "README.md",
            ROOT / "autonomy-gate" / "README.md",
            ROOT / "adapters" / "claude" / "claude-project-setup.md",
            ROOT / "adapters" / "openai" / "chatgpt-project-setup.md",
            ROOT / "docs" / "PROJECT_WORKSPACE_SETUP.md",
        ]
        for path in paths:
            with self.subTest(path=path):
                self.assertIn("operating-contract.md", path.read_text(encoding="utf-8"))

    def test_claude_project_requires_rendered_artifact_not_raw_html(self):
        paths = [
            ROOT / "adapters" / "claude" / "claude-project-setup.md",
            ROOT / "adapters" / "claude" / "cowork-handoff.md",
            ROOT / "docs" / "OWNER_MANUAL.md",
            ROOT / "docs" / "START_HERE.md",
        ]
        combined = "\n".join(path.read_text(encoding="utf-8") for path in paths)
        lowered = combined.lower()
        self.assertIn("rendered claude artifact", lowered)
        self.assertIn("do not print html source", lowered)
        self.assertNotIn("fenced code block labeled html", lowered)
        self.assertNotIn("save the html block", lowered)

    def test_claude_project_upload_manifest_is_16_runtime_plus_style_reference(self):
        setup = (ROOT / "adapters" / "claude" / "claude-project-setup.md").read_text(
            encoding="utf-8"
        )
        manifest = setup.split("<!-- CLAUDE_UPLOAD_MANIFEST_START -->", 1)[1].split(
            "<!-- CLAUDE_UPLOAD_MANIFEST_END -->", 1
        )[0]
        files = re.findall(r"(?m)^([a-z0-9-]+\.(?:md|html))$", manifest)
        expected_runtime = {
            "identity.md",
            "rules.md",
            "examples.md",
            "autonomy-criteria.md",
            "surface-capability-matrix.md",
            "risk-classification.md",
            "precedents.md",
            "operating-contract.md",
            "operator-disposition.md",
            "tool-selection-rules.md",
            "template-automation-architecture.md",
            "template-project-setup.md",
            "template-cowork-config.md",
            "template-control-plan.md",
            "template-stabilization-plan.md",
            "template-governance-memo.md",
        }
        self.assertEqual(17, len(files))
        self.assertEqual(expected_runtime, set(files) - {"artifact-rendered.html"})
        self.assertIn("artifact-rendered.html", files)

    def test_setup_docs_use_canonical_runtime_and_claude_upload_counts(self):
        paths = [
            ROOT / "README.md",
            ROOT / "docs" / "OWNER_MANUAL.md",
            ROOT / "docs" / "START_HERE.md",
            ROOT / "docs" / "PROJECT_WORKSPACE_SETUP.md",
            ROOT / "adapters" / "claude" / "claude-project-setup.md",
        ]
        for path in paths:
            text = path.read_text(encoding="utf-8")
            with self.subTest(path=path):
                self.assertNotRegex(text, r"\b14(?:-file| files| runtime)")
        claude_setup = paths[-1].read_text(encoding="utf-8")
        self.assertIn("16 runtime Markdown files", claude_setup)
        self.assertIn("17 uploaded files total", claude_setup)

    def test_artifact_rendering_contract_requires_semantic_parity(self):
        setup = (ROOT / "adapters" / "claude" / "claude-project-setup.md").read_text(
            encoding="utf-8"
        )
        lowered = setup.lower()
        for requirement in (
            "presentation may change; meaning may not",
            "do not omit, rename, summarize, or condense",
            "canonical terminal-status tokens",
            "blocked_for_evidence",
            "artifact_rendering_unavailable",
        ):
            self.assertIn(requirement, lowered)

    def test_published_execution_artifacts_include_required_governance_sections(self):
        artifact_dir = ROOT / "examples" / "artifacts"
        for path in artifact_dir.glob("*.html"):
            if path.name == "index.html":
                continue
            text = path.read_text(encoding="utf-8").lower()
            with self.subTest(path=path):
                for required in (
                    "expected outcomes",
                    "autonomy expires",
                    "build handoff pack",
                    "operator disposition",
                    "packet version",
                    "rationale",
                ):
                    self.assertIn(required, text)
                self.assertNotIn("completed_w_warnings", text)

    def test_normative_docs_do_not_use_deployment_pack(self):
        paths = [
            ROOT / "README.md",
            ROOT / "autonomy-gate" / "README.md",
            ROOT / "autonomy-gate" / "rules.md",
            ROOT / "adapters" / "decision-packet-contract.md",
        ]
        for path in paths:
            with self.subTest(path=path):
                self.assertNotIn("DEPLOYMENT PACK", path.read_text(encoding="utf-8").upper())

    def test_decision_packet_schema_uses_three_surface_fields(self):
        schema = json.loads((ROOT / "testing" / "schemas" / "decision-packet.schema.json").read_text())
        required = set(schema["required"])
        self.assertTrue({"assessment_surface", "execution_architecture", "builder_surface"} <= required)
        self.assertNotIn("surface", required)

    def test_registry_uses_canonical_lifecycle_states(self):
        operating = (ROOT / "autonomy-gate" / "reference" / "operating-contract.md").read_text()
        schema = json.loads((ROOT / "docs" / "registry" / "workflow-record.schema.json").read_text())
        states = schema["properties"]["status"]["enum"]
        for state in states:
            self.assertIn(f"`{state}`", operating)

    def test_registry_states_exactly_match_operating_contract_transitions(self):
        operating = (ROOT / "autonomy-gate" / "reference" / "operating-contract.md").read_text()
        schema = json.loads((ROOT / "docs" / "registry" / "workflow-record.schema.json").read_text())
        transition_block = operating.split("```text", 1)[1].split("```", 1)[0]
        transition_states = set(re.findall(r"\b[A-Z][A-Z_]+\b", transition_block))
        schema_states = set(schema["properties"]["status"]["enum"])
        self.assertEqual(schema_states, transition_states)

    def test_material_changes_invalidate_prior_authorization_chain(self):
        paths = [
            ROOT / "autonomy-gate" / "rules.md",
            ROOT / "autonomy-gate" / "reference" / "operating-contract.md",
            ROOT / "autonomy-gate" / "reference" / "build-handoff-contract.md",
            ROOT / "autonomy-gate" / "reference" / "user-journey-contract.md",
        ]
        for path in paths:
            text = path.read_text(encoding="utf-8").lower()
            with self.subTest(path=path):
                self.assertIn("packet version", text)
                self.assertIn("invalidat", text)
                self.assertIn("disposition", text)

    def test_builder_acknowledgement_requires_identity_version_and_scope_evidence(self):
        acknowledgement = (ROOT / "autonomy-gate" / "reference" / "builder-acknowledgement.md").read_text()
        for required in (
            "Packet version",
            "Builder:",
            "Date:",
            "Terminal action (from packet)",
            "Control | Implementation approach",
            "Criterion | Verification method",
            "I accept these constraints",
        ):
            self.assertIn(required, acknowledgement)

    def test_registry_tracks_the_complete_authorization_lifecycle(self):
        schema = json.loads((ROOT / "docs" / "registry" / "workflow-record.schema.json").read_text())
        properties = set(schema["properties"])
        required = {
            "request_record",
            "architecture_options",
            "selected_architecture",
            "builder_acknowledgement",
            "validation_evidence",
            "lifecycle_events",
            "incidents",
            "appeals",
            "change_assessments",
            "precedent_refs",
            "value_metrics",
        }
        self.assertTrue(required <= properties)

    def test_registry_guidance_defines_appeal_change_and_value_routines(self):
        paths = [
            ROOT / "docs" / "registry" / "README.md",
            ROOT / "docs" / "ADOPTION_PLAYBOOK.md",
        ]
        text = "\n".join(path.read_text(encoding="utf-8") for path in paths).lower()
        for term in (
            "appeal",
            "change assessment",
            "precedent",
            "assessment time",
            "unsafe requests rejected",
            "build rework avoided",
            "time to approved handoff",
            "recertification compliance",
        ):
            self.assertIn(term, text)

    def test_owner_manual_uses_only_canonical_terminology(self):
        manual = (ROOT / "docs" / "OWNER_MANUAL.md").read_text(encoding="utf-8")
        retired = re.compile(
            r"\b(?:AUTONOMOUS|SUPERVISED|SOP_FIRST|HUMAN_ONLY)\s*/\s*(?:PROJECT|COWORK|CODE_AGENT|NO_AI)\b",
            re.IGNORECASE,
        )
        self.assertIsNone(retired.search(manual))
        for required in (
            "Assessment surface",
            "Execution architecture",
            "Builder surface",
            "SELECT ARCHITECTURE",
            "Build Handoff Pack",
            "Builder acknowledgement",
            "RECERTIFY",
        ):
            self.assertIn(required, manual)

    def test_print_manual_excludes_retired_document_sources(self):
        builder_path = ROOT / "print-manual" / "build_manual.py"
        if not builder_path.exists():
            self.skipTest("Private print generator is intentionally outside the public release manifest.")
        builder = builder_path.read_text(encoding="utf-8")
        self.assertIn('DOCS / "OWNER_MANUAL.md"', builder)
        for retired in (
            'DOCS / "VERDICT_PLAYBOOK.md"',
            'DOCS / "ARTIFACT_GUIDE.md"',
            'DOCS / "USE_CASE_COOKBOOK.md"',
            'DOCS / "TROUBLESHOOTING.md"',
            'DOCS / "GOVERNANCE_REGISTRY_TEMPLATE.md"',
            'DOCS / "POWER_USER_GUIDE.md"',
        ):
            self.assertNotIn(retired, builder)

    def test_normative_docs_do_not_use_combined_surface_verdicts(self):
        combined_verdict = re.compile(
            r"\b(?:AUTONOMOUS|SUPERVISED|SOP_FIRST|HUMAN_ONLY)\s*/\s*(?:PROJECT|COWORK|CODE_AGENT|NO_AI)\b"
        )
        violations = []
        for path in self.normative_paths():
            for line_number, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
                if combined_verdict.search(line):
                    violations.append(f"{path.relative_to(ROOT)}:{line_number}: {line.strip()}")
        self.assertEqual([], violations, "Retired combined verdicts remain:\n" + "\n".join(violations))

    def test_normative_docs_do_not_treat_implementation_patterns_as_verdicts(self):
        legacy_phrases = (
            "surface verdict",
            "combined autonomy + surface",
            "combined autonomy and surface",
            "assigns a surface verdict",
            "assign execution surfaces",
            "recommended surface",
            "route to code_agent",
            "routes to code_agent",
            "routes to cowork",
        )
        violations = []
        for path in self.normative_paths():
            for line_number, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
                lowered = line.lower()
                if any(phrase in lowered for phrase in legacy_phrases):
                    violations.append(f"{path.relative_to(ROOT)}:{line_number}: {line.strip()}")
        self.assertEqual([], violations, "Legacy surface-verdict language remains:\n" + "\n".join(violations))

    def test_rule_10_selects_artifacts_from_canonical_decision_fields(self):
        rules = (ROOT / "autonomy-gate" / "rules.md").read_text(encoding="utf-8")
        rule_10 = rules.split("### RULE-10", 1)[1].split("### RULE-11", 1)[0]
        self.assertNotIn("combined autonomy + surface verdict", rule_10)
        for required in ("autonomy", "operating pattern", "terminal action", "architecture"):
            self.assertIn(required, rule_10.lower())
        self.assertIn("operator selects", rule_10.lower())
        self.assertIn("BLOCKED_FOR_EVIDENCE", rule_10)

    def test_architecture_contract_defines_enforceable_option_block(self):
        paths = [
            ROOT / "autonomy-gate" / "rules.md",
            ROOT / "autonomy-gate" / "reference" / "workflow-architecture-contract.md",
            ROOT / "docs" / "ARCHITECTURE_OPTIONS_GUIDE.md",
        ]
        required = (
            "ARCHITECTURE OPTIONS",
            "PRIMARY",
            "NATIVE_SUITE",
            "LOW_CODE",
            "CODE_FIRST",
            "VENDOR_NEUTRAL",
            "Execution architecture",
            "Builder surface",
            "Control fit",
            "Implementation effort",
            "Operating cost",
            "Maintenance burden",
            "Security fit",
            "Portability",
            "Skill requirements",
            "Source evidence",
            "Omitted option classes",
            "Selected option",
            "Selection by",
            "Selection date",
        )
        for path in paths:
            text = path.read_text(encoding="utf-8")
            with self.subTest(path=path):
                for item in required:
                    self.assertIn(item, text)

    def test_applicable_templates_put_architecture_options_before_handoff(self):
        template_dir = ROOT / "autonomy-gate" / "reference" / "templates"
        paths = [
            template_dir / "template-automation-architecture.md",
            template_dir / "template-control-plan.md",
            template_dir / "template-cowork-config.md",
            template_dir / "template-project-setup.md",
        ]
        for path in paths:
            text = path.read_text(encoding="utf-8")
            with self.subTest(path=path):
                self.assertIn("ARCHITECTURE OPTIONS", text)
                self.assertLess(text.index("ARCHITECTURE OPTIONS"), text.index("BUILD HANDOFF PACK"))
                self.assertIn("Selected option", text)
                self.assertIn("Selection by", text)
                self.assertIn("Selection date", text)

    def test_all_artifact_templates_require_the_canonical_handoff_contract(self):
        template_dir = ROOT / "autonomy-gate" / "reference" / "templates"
        paths = [
            template_dir / "template-automation-architecture.md",
            template_dir / "template-control-plan.md",
            template_dir / "template-cowork-config.md",
            template_dir / "template-governance-memo.md",
            template_dir / "template-project-setup.md",
            template_dir / "template-stabilization-plan.md",
        ]
        required = (
            "Terminal-action boundary",
            "Architecture decision record",
            "Permissions and credentials",
            "Deterministic controls",
            "Human checkpoints",
            "Prohibited actions",
            "Logging and audit",
            "Failure, rollback, and stop behavior",
            "Deployment sequence",
            "Assumptions",
            "Unresolved dependencies",
            "Expiration and reassessment triggers",
            "Version invalidation triggers",
            "Tool alternatives",
            "Builder acknowledgement",
            "Current state",
            "What the Gate completed",
            "What is blocked",
            "Who acts next",
            "Exact next action",
        )
        for path in paths:
            text = path.read_text(encoding="utf-8")
            with self.subTest(path=path):
                for item in required:
                    self.assertIn(item, text)

        governance = (template_dir / "template-governance-memo.md").read_text(encoding="utf-8")
        self.assertIn("Human operating procedure", governance)
        self.assertIn("Safe decomposition opportunities", governance)


if __name__ == "__main__":
    unittest.main()
