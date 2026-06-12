#!/usr/bin/env python3
import json
import sys
from pathlib import Path


def validate(data: dict) -> list[str]:
    errors: list[str] = []
    required = ["workflow_id", "packet_version", "status", "assumptions", "prohibited_actions", "acceptance_tests", "expiration_triggers", "stop_conditions"]
    errors.extend(f"missing field: {name}" for name in required if name not in data)
    status = data.get("status")
    if status not in {"BUILD_READY", "BLOCKED_FOR_EVIDENCE", "NOT_APPLICABLE"}:
        errors.append("status must be BUILD_READY, BLOCKED_FOR_EVIDENCE, or NOT_APPLICABLE")
    if status == "BUILD_READY":
        if not data.get("architecture_option_id"):
            errors.append("BUILD_READY requires architecture_option_id")
        manifest = data.get("manifest") or []
        if not manifest:
            errors.append("BUILD_READY requires a non-empty manifest")
        for index, entry in enumerate(manifest):
            for name in ("path", "purpose", "complete_content", "source_evidence"):
                if not entry.get(name):
                    errors.append(f"manifest[{index}] missing {name}")
        if data.get("unresolved_dependencies"):
            errors.append("BUILD_READY cannot contain unresolved_dependencies")
    if status == "BLOCKED_FOR_EVIDENCE" and not data.get("unresolved_dependencies"):
        errors.append("BLOCKED_FOR_EVIDENCE requires unresolved_dependencies")
    for index, case in enumerate(data.get("acceptance_tests") or []):
        for name in ("setup", "input", "expected", "pass_criterion"):
            if not case.get(name):
                errors.append(f"acceptance_tests[{index}] missing {name}")
    return errors


def main() -> int:
    if len(sys.argv) != 2:
        print("Usage: validate_build_handoff.py handoff.json")
        return 2
    data = json.loads(Path(sys.argv[1]).read_text(encoding="utf-8"))
    errors = validate(data)
    for error in errors:
        print(f"FAIL {error}")
    if not errors:
        print("PASS build handoff is structurally complete")
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
