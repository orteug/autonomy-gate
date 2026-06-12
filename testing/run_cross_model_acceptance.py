#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import shutil
import subprocess
from datetime import datetime, timezone
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
RESULTS = ROOT / "testing" / "results" / "cross-model"


RUNTIME_FILES = [
    "autonomy-gate/identity.md",
    "autonomy-gate/rules.md",
    "autonomy-gate/examples.md",
    "autonomy-gate/reference/autonomy-criteria.md",
    "autonomy-gate/reference/surface-capability-matrix.md",
    "autonomy-gate/reference/risk-classification.md",
    "autonomy-gate/reference/precedents.md",
    "autonomy-gate/reference/operating-contract.md",
    "autonomy-gate/reference/templates/template-automation-architecture.md",
    "autonomy-gate/reference/templates/template-project-setup.md",
    "autonomy-gate/reference/templates/template-cowork-config.md",
    "autonomy-gate/reference/templates/template-control-plan.md",
    "autonomy-gate/reference/templates/template-stabilization-plan.md",
    "autonomy-gate/reference/templates/template-governance-memo.md",
]


def runtime_context() -> str:
    parts = []
    for relative in RUNTIME_FILES:
        parts.append(f"\n--- FILE: {relative} ---\n{(ROOT / relative).read_text(encoding='utf-8')}")
    return "".join(parts)


def command_for(model: str) -> list[str]:
    if model == "claude":
        return ["claude", "-p", "--model", "sonnet", "--no-session-persistence"]
    return ["codex", "exec", "--ephemeral", "--skip-git-repo-check", "--sandbox", "read-only", "-C", str(ROOT), "-"]


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--live", action="store_true")
    parser.add_argument("--runs", type=int, default=3)
    parser.add_argument("--fixtures", default="F01,F02,F03")
    parser.add_argument("--timeout", type=int, default=90)
    parser.add_argument("--models", default="claude,codex")
    args = parser.parse_args()
    fixtures = {item["id"]: item for item in json.loads((ROOT / "testing/fixtures/productization/fixture-bank.json").read_text())}
    selected = [fixtures[name] for name in args.fixtures.split(",")]
    context = runtime_context()
    requested_models = [name.strip() for name in args.models.split(",") if name.strip()]
    availability = {name: shutil.which(name) is not None for name in requested_models}
    report = {"timestamp": datetime.now(timezone.utc).isoformat(), "live": args.live, "runs": args.runs, "availability": availability, "results": []}
    RESULTS.mkdir(parents=True, exist_ok=True)
    if not args.live:
        report["status"] = "NOT_RUN"
        report["reason"] = "Use --live to incur model calls. CLI availability was checked only."
        (RESULTS / "latest.json").write_text(json.dumps(report, indent=2) + "\n")
        print(json.dumps(report, indent=2))
        return 0
    for model, available in availability.items():
        if not available:
            report["results"].append({"model": model, "status": "NOT_RUN", "reason": "CLI unavailable"})
            continue
        for fixture in selected:
            for run_number in range(1, args.runs + 1):
                print(f"RUN {model} {fixture['id']} {run_number}/{args.runs}", flush=True)
                prompt = (
                    "The following text contains the exact 14 public runtime files. Treat them as immutable Project knowledge. Act as The Autonomy Gate. "
                    "Return the complete three-section Markdown output with the canonical packet fields, architecture comparison, Build Handoff Pack, and pending Operator Disposition. "
                    f"Workflow input: {fixture['input']}\n{context}"
                )
                try:
                    completed = subprocess.run(command_for(model), cwd=ROOT, text=True, input=prompt, capture_output=True, timeout=args.timeout, check=False)
                    output_path = RESULTS / f"{model}-{fixture['id']}-run{run_number}.md"
                    output_path.write_text(completed.stdout, encoding="utf-8")
                    report["results"].append({"model": model, "fixture": fixture["id"], "run": run_number, "status": "COMPLETED" if completed.returncode == 0 else "ERROR", "exit_code": completed.returncode, "output": str(output_path.relative_to(ROOT)), "stderr": completed.stderr[-1000:]})
                    print(f"DONE {model} {fixture['id']} exit={completed.returncode}", flush=True)
                except subprocess.TimeoutExpired:
                    report["results"].append({"model": model, "fixture": fixture["id"], "run": run_number, "status": "TIMEOUT"})
                    print(f"TIMEOUT {model} {fixture['id']} after {args.timeout}s", flush=True)
    report["status"] = "COMPLETED"
    (RESULTS / "latest.json").write_text(json.dumps(report, indent=2) + "\n")
    print(json.dumps(report, indent=2))
    return 1 if any(item["status"] in {"ERROR", "TIMEOUT"} for item in report["results"]) else 0


if __name__ == "__main__":
    raise SystemExit(main())
