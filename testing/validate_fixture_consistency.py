#!/usr/bin/env python3
import json
import sys
from pathlib import Path


def main() -> int:
    path = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(__file__).parent / "fixtures" / "productization" / "fixture-bank.json"
    fixtures = json.loads(path.read_text(encoding="utf-8"))
    errors = []
    if len(fixtures) < 20:
        errors.append(f"fixture bank has {len(fixtures)} entries; at least 20 required")
    ids = [item.get("id") for item in fixtures]
    if len(ids) != len(set(ids)):
        errors.append("fixture ids must be unique")
    required = {"id", "input", "expected_autonomy", "expected_handoff_status", "required_behavior", "prohibited_behavior"}
    for index, item in enumerate(fixtures):
        missing = required - set(item)
        if missing:
            errors.append(f"fixture[{index}] missing {', '.join(sorted(missing))}")
    for error in errors:
        print(f"FAIL {error}")
    if not errors:
        print(f"PASS {len(fixtures)} fixtures are structurally consistent")
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
