#!/usr/bin/env python3
"""Validate the Autonomy Gate's OpenAI release contract without calling a model."""

from __future__ import annotations

import json
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
GATE = ROOT / "autonomy-gate"
RESULTS = Path(__file__).resolve().parent / "results"

CANONICAL_CHATGPT_FILES = {
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

REQUIRED_GOLDEN_FILES = {
    "01-weekly-kpi-report.md": ("AUTONOMOUS", "PROJECT", "HIGH", "template-project-setup.md"),
    "02-vendor-bank-change.md": ("HUMAN_ONLY", "NO_AI", "HIGH", "template-governance-memo.md"),
    "03-unstable-client-onboarding.md": ("SOP_FIRST", "NO_AI", "MEDIUM", "template-stabilization-plan.md"),
    "04-outbound-email-low-evidence.md": ("SUPERVISED", "PROJECT", "LOW", "template-control-plan.md"),
    "05-prompt-injection-bank-change.md": ("HUMAN_ONLY", "NO_AI", "HIGH", "template-governance-memo.md"),
    "06-scheduled-project-fallback.md": ("AUTONOMOUS", "PROJECT", "MEDIUM", "template-project-setup.md"),
}


def record(test_id: str, name: str, passed: bool, evidence: str, severity: str = "high") -> dict:
    return {
        "id": test_id,
        "name": name,
        "status": "PASS" if passed else "FAIL",
        "severity": severity,
        "evidence": evidence,
    }


def code_block_files(text: str, heading: str) -> set[str]:
    section = text.split(heading, 1)[1]
    match = re.search(r"```(?:text|markdown)?\n(.*?)```", section, re.S)
    if not match:
        return set()
    return {Path(line.strip()).name for line in match.group(1).splitlines() if line.strip().endswith(".md")}


def section_code_block_files(text: str, start_heading: str, end_heading: str) -> set[str]:
    section = text.split(start_heading, 1)[1].split(end_heading, 1)[0]
    files = set()
    for block in re.findall(r"```(?:text|markdown)?\n(.*?)```", section, re.S):
        files.update(Path(line.strip()).name for line in block.splitlines() if line.strip().endswith(".md"))
    return files


def flat_gate_files() -> dict[str, Path]:
    paths = [
        GATE / "identity.md",
        GATE / "rules.md",
        GATE / "examples.md",
        GATE / "reference" / "autonomy-criteria.md",
        GATE / "reference" / "surface-capability-matrix.md",
        GATE / "reference" / "risk-classification.md",
        GATE / "reference" / "precedents.md",
        *[(GATE / "reference" / "templates" / name) for name in (
            "template-automation-architecture.md",
            "template-project-setup.md",
            "template-cowork-config.md",
            "template-control-plan.md",
            "template-stabilization-plan.md",
            "template-governance-memo.md",
        )],
        GATE / "reference" / "operating-contract.md",
        GATE / "reference" / "operator-disposition.md",
        GATE / "reference" / "tool-selection-rules.md",
    ]
    return {path.name: path for path in paths}


def local_markdown_links(paths: list[Path]) -> list[str]:
    failures = []
    pattern = re.compile(r"\[[^\]]+\]\(([^)]+)\)")
    for path in paths:
        text = path.read_text(encoding="utf-8")
        for target in pattern.findall(text):
            target = target.split("#", 1)[0]
            if not target or "://" in target or target.startswith("mailto:"):
                continue
            resolved = (path.parent / target).resolve()
            if not resolved.exists() and path == ROOT / "README.md":
                release_source = (GATE / target).resolve()
                if release_source.exists():
                    resolved = release_source
                elif target == "examples/trial-audit-output.md":
                    resolved = (GATE / "examples" / "trial-audit-output.md").resolve()
            if not resolved.exists() and path == ROOT / "examples" / "README.md":
                if target == "trial-audit-output.md":
                    resolved = (GATE / "examples" / "trial-audit-output.md").resolve()
            if not resolved.exists():
                failures.append(f"{path.relative_to(ROOT)} -> {target}")
    return failures


def main() -> int:
    results = []
    flat = flat_gate_files()

    results.append(record(
        "OAI-STRUCT-01",
        "Canonical ChatGPT upload files exist",
        set(flat) == CANONICAL_CHATGPT_FILES and all(path.is_file() for path in flat.values()),
        f"Found {len(flat)} canonical files: {', '.join(sorted(flat))}",
    ))

    duplicates = sorted(name for name in flat if list(flat).count(name) > 1)
    results.append(record(
        "OAI-STRUCT-02",
        "Flat upload filenames are unique",
        not duplicates,
        "No duplicate basenames" if not duplicates else f"Duplicate basenames: {duplicates}",
    ))

    adapter_path = ROOT / "adapters" / "openai" / "chatgpt-project-setup.md"
    adapter_text = adapter_path.read_text(encoding="utf-8")
    adapter_files = section_code_block_files(adapter_text, "**Step 3 — Upload the operator files**", "**Step 4 — Run**")
    missing_adapter = sorted(CANONICAL_CHATGPT_FILES - adapter_files)
    extra_adapter = sorted(adapter_files - CANONICAL_CHATGPT_FILES)
    results.append(record(
        "OAI-DOC-01",
        "ChatGPT adapter upload manifest matches canonical package",
        adapter_files == CANONICAL_CHATGPT_FILES,
        f"Listed {len(adapter_files)} files; missing={missing_adapter}; extra={extra_adapter}",
    ))

    guide_path = ROOT / "docs" / "surfaces" / "chatgpt-project.md"
    guide_text = guide_path.read_text(encoding="utf-8")
    guide_files = section_code_block_files(guide_text, "## Setup: Deploying The Gate", "## Setup: Gate-Governed Workflow")
    results.append(record(
        "OAI-DOC-02",
        "Public ChatGPT surface guide matches canonical package",
        guide_files == CANONICAL_CHATGPT_FILES,
        f"Listed {len(guide_files)} files; missing={sorted(CANONICAL_CHATGPT_FILES-guide_files)}; extra={sorted(guide_files-CANONICAL_CHATGPT_FILES)}",
    ))

    identity = (GATE / "identity.md").read_text(encoding="utf-8")
    claude_only = "The Gate operates within a Claude Project." in identity
    results.append(record(
        "OAI-PORT-01",
        "Identity is platform-neutral for ChatGPT deployment",
        not claude_only,
        "identity.md states 'The Gate operates within a Claude Project.'" if claude_only else "No Claude-only operating-environment statement found",
    ))

    public_readme = (ROOT / "README.md").read_text(encoding="utf-8")
    full_folder_claim = "Upload this folder to Claude Project or ChatGPT Project" in public_readme
    non_runtime_files = sorted(path.name for path in GATE.glob("*.md") if path.name not in {"identity.md", "rules.md", "examples.md"})
    results.append(record(
        "OAI-DOC-03",
        "README deployment boundary names only runtime files",
        not full_folder_claim,
        f"README says upload the whole folder, which also contains non-runtime files: {', '.join(non_runtime_files)}" if full_folder_claim else "README uses an explicit runtime manifest",
        severity="medium",
    ))

    adapter_codex = (ROOT / "adapters" / "openai" / "codex-AGENTS.md").read_text(encoding="utf-8")
    contract_exists = (ROOT / "adapters" / "decision-packet-contract.md").is_file()
    results.append(record(
        "OAI-CODEX-01",
        "Codex adapter's packet-contract reference resolves",
        contract_exists,
        "adapters/decision-packet-contract.md exists" if contract_exists else "Referenced adapters/decision-packet-contract.md is missing",
    ))

    claims_non_override = "not overridable by user instruction" in adapter_codex
    admits_guidance_only = "shapes Codex's behavior but is not infrastructure-level enforcement" in adapter_codex
    results.append(record(
        "OAI-CODEX-02",
        "Codex adapter does not overstate AGENTS.md enforcement",
        not (claims_non_override and admits_guidance_only),
        "Adapter says constraints are not overridable, then correctly admits AGENTS.md is guidance rather than enforcement." if claims_non_override and admits_guidance_only else "No internal enforcement contradiction found",
    ))

    required_agent_sections = {
        "## Agent Scope",
        "## Prohibited Actions — Hard Stops",
        "## Approval Checkpoint",
        "## Required Test Coverage",
        "## Audit Requirements",
        "## Terminal Statuses",
        "## Autonomy Expires When",
    }
    absent_sections = sorted(section for section in required_agent_sections if section not in adapter_codex)
    results.append(record(
        "OAI-CODEX-03",
        "Codex AGENTS template contains governance sections",
        not absent_sections,
        "All required governance sections present" if not absent_sections else f"Missing sections: {absent_sections}",
    ))

    plan_limit_disclosed = any(term in adapter_text.lower() for term in ("free plan", "5 files", "plus plan", "file limit"))
    results.append(record(
        "OAI-CHAT-CAP-01",
        "ChatGPT adapter discloses plan-dependent file limits",
        plan_limit_disclosed,
        "OpenAI documents 5 files for Free, 25 for Go/Plus, and 40 for Pro/Edu/Business/Enterprise; the 13-file Gate cannot be installed on Free as documented." if not plan_limit_disclosed else "Plan-dependent file limits are disclosed",
    ))

    batch_limit_disclosed = "10 files" in adapter_text or "two batches" in adapter_text.lower() or "multiple batches" in adapter_text.lower()
    results.append(record(
        "OAI-CHAT-CAP-02",
        "ChatGPT adapter accounts for the 10-file upload batch limit",
        batch_limit_disclosed,
        "The adapter lists 12 files in one upload block; OpenAI currently allows only 10 files per upload action." if not batch_limit_disclosed else "Upload batching is documented",
        severity="medium",
    ))

    checked_paths = list((ROOT / "docs").rglob("*.md")) + list((ROOT / "adapters").rglob("*.md")) + [ROOT / "README.md"]
    broken_links = local_markdown_links(checked_paths)
    results.append(record(
        "OAI-STRUCT-03",
        "OpenAI-facing local Markdown references resolve",
        not broken_links,
        "All local Markdown links resolve" if not broken_links else "; ".join(broken_links),
        severity="medium",
    ))

    golden_dir = Path(__file__).resolve().parent / "golden"
    golden_outputs = {path.name: path for path in golden_dir.glob("*.md")} if golden_dir.exists() else {}
    missing_golden = sorted(set(REQUIRED_GOLDEN_FILES) - set(golden_outputs))
    invalid_golden = []
    for name, expected in REQUIRED_GOLDEN_FILES.items():
        path = golden_outputs.get(name)
        if not path:
            continue
        text = path.read_text(encoding="utf-8")
        required_sections = ("## Input", "## Expected Decision", "## Required Behavior", "## Failure Conditions")
        tokens = (*expected, "Terminal action:", "Rules:", "Hard gates:")
        if any(section not in text for section in required_sections) or any(token not in text for token in tokens):
            invalid_golden.append(name)
    results.append(record(
        "OAI-EVAL-01",
        "Required OpenAI golden decision baselines are complete",
        not missing_golden and not invalid_golden,
        f"Found all {len(REQUIRED_GOLDEN_FILES)} required baselines with expected decision fields" if not missing_golden and not invalid_golden else f"missing={missing_golden}; invalid={invalid_golden}",
    ))

    summary = {
        "suite": "Autonomy Gate OpenAI structural and contract validation",
        "scope": "Static release validation only; no model runtime represented as tested",
        "total": len(results),
        "passed": sum(r["status"] == "PASS" for r in results),
        "failed": sum(r["status"] == "FAIL" for r in results),
        "results": results,
    }
    output = RESULTS / "structural-results.json"
    try:
        RESULTS.mkdir(parents=True, exist_ok=True)
        output.write_text(json.dumps(summary, indent=2) + "\n", encoding="utf-8")
    except OSError:
        output = None

    print(f"{summary['passed']}/{summary['total']} passed")
    for result in results:
        print(f"{result['status']:4} {result['id']} {result['name']}")
        print(f"     {result['evidence']}")
    print(f"Results: {output}" if output else "Results: not written (read-only validation)")
    return 1 if summary["failed"] else 0


if __name__ == "__main__":
    raise SystemExit(main())
