import json
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


class ReleaseContractTests(unittest.TestCase):
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


if __name__ == "__main__":
    unittest.main()
