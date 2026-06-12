#!/usr/bin/env python3
import json
import sys
from pathlib import Path


REQUIRED_CLASSES = {"PRIMARY", "NATIVE_SUITE", "LOW_CODE", "CODE_FIRST", "VENDOR_NEUTRAL"}


def validate(data: dict) -> list[str]:
    errors: list[str] = []
    options = data.get("options") or []
    option_ids = {item.get("id") for item in options}
    selected = data.get("selected_option_id")
    if not selected or selected not in option_ids:
        errors.append("selected_option_id must identify an existing option")
    classes = {item.get("class") for item in options}
    omitted = {item.get("class") for item in data.get("omitted_classes", []) if item.get("reason")}
    for name in sorted(REQUIRED_CLASSES - classes - omitted):
        errors.append(f"missing architecture class without omission reason: {name}")
    if len(options) > 1:
        required = {"id", "class", "execution_architecture", "builder_surface", "control_fit", "implementation_effort", "operating_cost", "maintenance_burden", "security_fit", "portability", "skill_requirements", "source_evidence"}
        for index, item in enumerate(options):
            for name in sorted(required - set(item)):
                errors.append(f"options[{index}] missing {name}")
    return errors


def main() -> int:
    if len(sys.argv) != 2:
        print("Usage: validate_architecture_options.py architecture.json")
        return 2
    errors = validate(json.loads(Path(sys.argv[1]).read_text(encoding="utf-8")))
    for error in errors:
        print(f"FAIL {error}")
    if not errors:
        print("PASS architecture options are complete and selected")
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
