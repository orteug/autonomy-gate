#!/usr/bin/env python3
from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def run(name: str, command: list[str]) -> bool:
    result = subprocess.run(command, cwd=ROOT, text=True, capture_output=True, check=False)
    print(f"{'PASS' if result.returncode == 0 else 'FAIL'} {name}")
    if result.stdout:
        print(result.stdout.rstrip())
    if result.stderr:
        print(result.stderr.rstrip())
    return result.returncode == 0


def main() -> int:
    checks = [
        ("unit tests", [sys.executable, "-m", "unittest", "testing.test_validate_gate_output", "testing.test_release_contract", "testing.test_structured_validators", "-v"]),
        ("adoption contract", [sys.executable, "testing/validate_adoption.py"]),
        ("OpenAI static package", [sys.executable, "testing/openai/validate_release.py"]),
        ("Claude static calibration", [sys.executable, "testing/claude/validate_calibration.py"]),
        ("public release manifest", [sys.executable, "testing/validate_competition_package.py", "."]),
        ("fixture consistency", [sys.executable, "testing/validate_fixture_consistency.py"]),
        ("valid build handoff", [sys.executable, "testing/validate_build_handoff.py", "testing/fixtures/productization/build-handoff-valid.json"]),
        ("valid architecture options", [sys.executable, "testing/validate_architecture_options.py", "testing/fixtures/productization/architecture-valid.json"]),
        ("valid tool recommendation", [sys.executable, "testing/validate_tool_recommendations.py", "testing/fixtures/productization/tool-recommendations-valid.json"]),
    ]
    for receipt in sorted((ROOT / "examples" / "receipts").glob("*.md")):
        checks.append((f"receipt {receipt.name}", [sys.executable, "testing/validate_gate_output.py", str(receipt.relative_to(ROOT))]))
    results = [run(name, command) for name, command in checks]
    ok = all(results)
    schema_errors = []
    for path in sorted((ROOT / "testing" / "schemas").glob("*.json")) + [ROOT / "docs" / "registry" / "workflow-record.schema.json"]:
        try:
            json.loads(path.read_text(encoding="utf-8"))
        except Exception as exc:
            schema_errors.append(f"{path.relative_to(ROOT)}: {exc}")
    print(f"{'PASS' if not schema_errors else 'FAIL'} JSON schema syntax")
    for error in schema_errors:
        print(error)
    ok = ok and not schema_errors
    print(f"RELEASE SUITE: {'PASS' if ok else 'FAIL'}")
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
