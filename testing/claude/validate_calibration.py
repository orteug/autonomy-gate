#!/usr/bin/env python3
"""Static regression checks for the Claude-facing Autonomy Gate package."""

from __future__ import annotations

import json
import os
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
GATE = ROOT / "autonomy-gate"
RESULTS = Path(__file__).resolve().parent / "results"

EXPECTED = {
    1: ("AUTONOMOUS", "template-project-setup.md"),
    2: ("SOP_FIRST", "template-stabilization-plan.md"),
    3: ("AUTONOMOUS", "template-automation-architecture.md"),
    4: ("SUPERVISED", "template-control-plan.md"),
    5: ("SUPERVISED", "template-control-plan.md"),
    6: ("AUTONOMOUS", "template-cowork-config.md"),
    7: ("SUPERVISED", "template-control-plan.md"),
    8: ("HUMAN_ONLY", "template-governance-memo.md"),
    9: ("HUMAN_ONLY", "template-governance-memo.md"),
    10: ("SUPERVISED", "template-control-plan.md"),
    11: ("SUPERVISED", "template-control-plan.md"),
    12: ("SUPERVISED", "template-control-plan.md"),
    13: ("SUPERVISED", "template-control-plan.md"),
    14: ("AUTONOMOUS", "template-project-setup.md"),
}


def result(test_id: str, name: str, passed: bool, evidence: str) -> dict:
    return {"id": test_id, "name": name, "status": "PASS" if passed else "FAIL", "evidence": evidence}


def main() -> int:
    results = []
    examples = (GATE / "examples.md").read_text(encoding="utf-8")
    chunks = re.split(r"(?=^## Example \d+)", examples, flags=re.M)
    parsed = {}
    for chunk in chunks:
        match = re.match(r"## Example (\d+)", chunk)
        if match:
            parsed[int(match.group(1))] = chunk

    results.append(result(
        "CLAUDE-CAL-01",
        "All 14 calibration examples remain present",
        set(parsed) == set(EXPECTED),
        f"Found examples: {sorted(parsed)}",
    ))

    mismatches = []
    for number, (autonomy, artifact) in EXPECTED.items():
        chunk = parsed.get(number, "")
        required = [
            f"Autonomy: {autonomy}",
            "Assessment surface:",
            "Execution architecture:",
            "Builder surface:",
            "Terminal action:",
            "Handoff status:",
            f"Artifact required: {artifact}",
        ]
        missing = [token for token in required if token not in chunk]
        if "\nSurface:" in chunk:
            missing.append("legacy Surface field must be absent")
        if missing:
            mismatches.append(f"Example {number}: missing {missing}")
    results.append(result(
        "CLAUDE-CAL-02",
        "Calibration examples use canonical packet fields and approved autonomy mappings",
        not mismatches,
        "All 14 mappings match the approved matrix" if not mismatches else "; ".join(mismatches),
    ))

    identity = (GATE / "identity.md").read_text(encoding="utf-8")
    results.append(result(
        "CLAUDE-PORT-01",
        "Claude Project remains an explicit supported decision surface",
        "including Claude Project and ChatGPT Project" in identity,
        "Platform-neutral authority limit explicitly includes Claude Project",
    ))

    claude_setup = (ROOT / "adapters" / "claude" / "claude-project-setup.md").read_text(encoding="utf-8")
    claude_code = (ROOT / "adapters" / "claude" / "claude-code-CLAUDE.md").read_text(encoding="utf-8")
    cowork = (ROOT / "adapters" / "claude" / "cowork-handoff.md").read_text(encoding="utf-8")
    adapter_checks = {
        "Claude Project": "Claude Project" in claude_setup,
        "Claude Code": "CLAUDE.md" in claude_code,
        "Cowork": "cowork" in cowork.lower(),
    }
    results.append(result(
        "CLAUDE-ADAPT-01",
        "Claude Project, Claude Code, and Cowork adapters remain intact",
        all(adapter_checks.values()),
        json.dumps(adapter_checks, sort_keys=True),
    ))

    enforcement_consistent = "not overridable by user instruction" not in claude_code and "not a security boundary" in claude_code
    results.append(result(
        "CLAUDE-ADAPT-02",
        "Claude Code adapter distinguishes guidance from enforcement",
        enforcement_consistent,
        "CLAUDE.md is described as durable guidance paired with technical controls" if enforcement_consistent else "Claude Code adapter overstates CLAUDE.md enforcement",
    ))

    rules = (GATE / "rules.md").read_text(encoding="utf-8")
    required_rules = [f"RULE-{n:02d}" for n in range(10)] + [f"GATE-{n}" for n in range(1, 6)]
    missing_rules = [token for token in required_rules if token not in rules]
    results.append(result(
        "CLAUDE-RULE-01",
        "Decision-rule and hard-gate identifiers remain available",
        not missing_rules,
        "All RULE-00..09 and GATE-1..5 identifiers present" if not missing_rules else f"Missing: {missing_rules}",
    ))

    summary = {
        "suite": "Autonomy Gate Claude static calibration regression",
        "total": len(results),
        "passed": sum(item["status"] == "PASS" for item in results),
        "failed": sum(item["status"] == "FAIL" for item in results),
        "results": results,
    }
    output = None
    if os.environ.get("AUTONOMY_GATE_READ_ONLY") != "1":
        output = RESULTS / "calibration-results.json"
        try:
            RESULTS.mkdir(parents=True, exist_ok=True)
            output.write_text(json.dumps(summary, indent=2) + "\n", encoding="utf-8")
        except OSError:
            output = None
    print(f"{summary['passed']}/{summary['total']} passed")
    for item in results:
        print(f"{item['status']:4} {item['id']} {item['name']}")
        print(f"     {item['evidence']}")
    print(f"Results: {output}" if output else "Results: not written (read-only validation)")
    return 1 if summary["failed"] else 0


if __name__ == "__main__":
    raise SystemExit(main())
