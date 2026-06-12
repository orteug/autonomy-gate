#!/usr/bin/env python3
import argparse
import sys
from pathlib import Path

from validate_gate_output import validate


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate and optionally emit an approved builder handoff.")
    parser.add_argument("input")
    parser.add_argument("--output")
    args = parser.parse_args()
    source = Path(args.input)
    text = source.read_text(encoding="utf-8")
    result = validate(text)
    for finding in result.findings:
        print(f"{finding.severity} [{finding.code}] {finding.message}")
    if not result.passed:
        print("FAIL handoff not emitted")
        return 1
    if "Disposition: APPROVE_FOR_BUILD" not in text:
        print("FAIL operator approval record is not present")
        return 1
    if args.output:
        Path(args.output).write_text(text, encoding="utf-8")
        print(f"PASS clean handoff written to {args.output}")
    else:
        print("PASS handoff is eligible for builder delivery")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
