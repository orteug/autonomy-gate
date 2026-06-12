#!/usr/bin/env python3
import json
import sys
from pathlib import Path
from urllib.parse import urlparse


def validate(data: dict) -> list[str]:
    errors: list[str] = []
    for index, item in enumerate(data.get("recommendations") or []):
        if not item.get("capability"):
            errors.append(f"recommendations[{index}] missing capability")
        if item.get("tool"):
            for name in ("source_url", "verified_date", "constraint_fit", "capability_to_control"):
                if not item.get(name):
                    errors.append(f"recommendations[{index}] missing {name}")
            url = item.get("source_url", "")
            if url and urlparse(url).scheme != "https":
                errors.append(f"recommendations[{index}] source_url must use https")
    return errors


def main() -> int:
    if len(sys.argv) != 2:
        print("Usage: validate_tool_recommendations.py recommendations.json")
        return 2
    errors = validate(json.loads(Path(sys.argv[1]).read_text(encoding="utf-8")))
    for error in errors:
        print(f"FAIL {error}")
    if not errors:
        print("PASS tool recommendations are sourced and constraint-aware")
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
