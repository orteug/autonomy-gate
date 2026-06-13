#!/usr/bin/env python3
"""Validate a saved Autonomy Gate Markdown response."""

from __future__ import annotations

import re
import sys
from dataclasses import dataclass, field
from pathlib import Path


AUTONOMY_VALUES = {"AUTONOMOUS", "SUPERVISED", "SOP_FIRST", "HUMAN_ONLY"}
CONFIDENCE_VALUES = {"HIGH", "MEDIUM", "LOW"}
HANDOFF_STATUSES = {"BUILD_READY", "BLOCKED_FOR_EVIDENCE", "NOT_APPLICABLE"}
ARCHITECTURE_CLASSES = {"PRIMARY", "NATIVE_SUITE", "LOW_CODE", "CODE_FIRST", "VENDOR_NEUTRAL"}
HANDOFF_HEADING = r"^\s*(?:#{1,4}\s*)?(?:━━\s*)?BUILD HANDOFF PACK(?:\s*━━+)?\s*$"
ARCHITECTURE_HEADING = r"^\s*(?:#{1,4}\s*)?(?:━━\s*)?ARCHITECTURE OPTIONS(?:\s*━━+)?\s*$"
PACKET_FIELDS = [
    "Autonomy",
    "Assessment surface",
    "Execution architecture",
    "Builder surface",
    "Confidence",
    "Terminal action",
    "Justification",
]
PLACEHOLDER_PATTERNS = [
    re.compile(r"\[(?!x\]| \]|CONDITIONAL|present when|optional)[^\]]{3,}\]", re.IGNORECASE),
    re.compile(r"\bTBD\b", re.IGNORECASE),
    re.compile(r"\bcustomize\b", re.IGNORECASE),
    re.compile(r"fill in", re.IGNORECASE),
    re.compile(r"\byour value\b", re.IGNORECASE),
]


@dataclass
class Finding:
    severity: str
    code: str
    message: str
    line: int = 0


@dataclass
class ValidationResult:
    findings: list[Finding] = field(default_factory=list)

    def fail(self, code: str, message: str, line: int = 0) -> None:
        self.findings.append(Finding("FAIL", code, message, line))

    def warn(self, code: str, message: str, line: int = 0) -> None:
        self.findings.append(Finding("WARN", code, message, line))

    @property
    def passed(self) -> bool:
        return not any(item.severity == "FAIL" for item in self.findings)


def section(text: str, start: str, end: str | None = None) -> str:
    match = re.search(start, text, re.IGNORECASE | re.MULTILINE)
    if not match:
        return ""
    tail = text[match.end():]
    if end:
        stop = re.search(end, tail, re.IGNORECASE | re.MULTILINE)
        if stop:
            tail = tail[:stop.start()]
    return tail


def parse_fields(block: str) -> dict[str, str]:
    fields: dict[str, str] = {}
    for line in block.splitlines():
        line = line.strip().replace("**", "")
        match = re.match(r"^\s*(?:[-*]\s*)?([A-Za-z][A-Za-z /_-]+?)\s*:\s*(.+?)\s*$", line)
        if match:
            fields[match.group(1).strip()] = match.group(2).strip().strip("`*")
    return fields


def packet_blocks(text: str) -> list[str]:
    starts = list(re.finditer(r"AUTONOMY DECISION PACKET", text, re.IGNORECASE))
    blocks: list[str] = []
    for index, start in enumerate(starts):
        tail_end = starts[index + 1].start() if index + 1 < len(starts) else len(text)
        tail = text[start.end():tail_end]
        boundary = re.search(r"\n\s*(?:━━|#{1,3}\s+)(?!AUTONOMY DECISION PACKET)", tail, re.IGNORECASE)
        blocks.append(tail[:boundary.start()] if boundary else tail)
    return blocks


def check_structure(text: str, result: ValidationResult) -> None:
    for code, marker in (
        ("STRUCT-SNAPSHOT", "WORKFLOW INTAKE SNAPSHOT"),
        ("STRUCT-PACKET", "AUTONOMY DECISION PACKET"),
        ("STRUCT-ARTIFACT", "OPERATOR DISPOSITION"),
    ):
        if not re.search(marker, text, re.IGNORECASE):
            result.fail(code, f"Required section not found: {marker}.")
    if not re.search(HANDOFF_HEADING, text, re.IGNORECASE | re.MULTILINE):
        result.fail("PACK-MISSING", "BUILD HANDOFF PACK section not found.")
    next_action_fields = (
        "Current state",
        "What the Gate completed",
        "What is blocked",
        "Who acts next",
        "Exact next action",
    )
    missing = [
        field
        for field in next_action_fields
        if not re.search(rf"^\s*{re.escape(field)}\s*:\s*\S", text, re.IGNORECASE | re.MULTILINE)
    ]
    if missing:
        result.fail("NEXT-ACTION", "State-aware next action is missing: " + ", ".join(missing) + ".")


def check_packets(text: str, result: ValidationResult) -> None:
    blocks = packet_blocks(text)
    if not blocks:
        for name in PACKET_FIELDS:
            result.fail("PKT-FIELD", f"Required packet field missing: '{name}'")
        return
    for run_number, block in enumerate(blocks, 1):
        fields = parse_fields(block)
        prefix = f"Run {run_number}: " if len(blocks) > 1 else ""
        for name in PACKET_FIELDS:
            if not fields.get(name):
                result.fail("PKT-FIELD", f"{prefix}Required packet field missing: '{name}'")
        if "Surface" in fields:
            result.fail("PKT-SURFACE", f"{prefix}Legacy overloaded 'Surface' field is forbidden.")
        autonomy_parts = fields.get("Autonomy", "").split()
        confidence_parts = fields.get("Confidence", "").split()
        autonomy = autonomy_parts[0].strip("`.,()") if autonomy_parts else ""
        confidence = confidence_parts[0].strip("`.,()") if confidence_parts else ""
        if autonomy and autonomy not in AUTONOMY_VALUES:
            result.fail("PKT-VALUE", f"{prefix}Invalid autonomy value: {autonomy}")
        if confidence and confidence not in CONFIDENCE_VALUES:
            result.fail("PKT-VALUE", f"{prefix}Invalid confidence value: {confidence}")
        justification = fields.get("Justification", "")
        if justification and not re.search(r"\bRULE-\d+\b", justification):
            result.warn("PKT-CITE", f"{prefix}Justification does not cite a RULE-NN identifier.")
        gaps = fields.get("Evidence gaps", "").strip().rstrip(".,;")
        if confidence == "HIGH" and gaps and gaps.lower() not in {"none", "n/a", "not applicable", "—"}:
            result.fail("CONTRA-HIGH-GAPS", f"{prefix}HIGH confidence cannot include decision-material evidence gaps.")
        if autonomy == "AUTONOMOUS" and re.search(r"\bGATE-[23]\b", justification):
            result.fail("CONTRA-AUTO-GATE", f"{prefix}AUTONOMOUS conflicts with GATE-2 or GATE-3.")


def architecture_block(text: str) -> str:
    return section(text, ARCHITECTURE_HEADING, HANDOFF_HEADING)


def check_architecture(text: str, result: ValidationResult) -> None:
    packets = packet_blocks(text)
    fields = parse_fields(packets[0]) if packets else {}
    autonomy_parts = fields.get("Autonomy", "").split()
    autonomy = autonomy_parts[0].strip("`.,()") if autonomy_parts else ""
    if autonomy not in {"AUTONOMOUS", "SUPERVISED"}:
        return

    block = architecture_block(text)
    if not block:
        result.fail("ARCH-MISSING", "AUTONOMOUS and SUPERVISED outputs require an ARCHITECTURE OPTIONS section.")
        return

    option_matches = list(
        re.finditer(
            r"^\s*#{2,4}\s+(OPT-[A-Z0-9_-]+)\s+[—-]\s+(PRIMARY|NATIVE_SUITE|LOW_CODE|CODE_FIRST|VENDOR_NEUTRAL)\s*$",
            block,
            re.IGNORECASE | re.MULTILINE,
        )
    )
    option_ids = {match.group(1).upper() for match in option_matches}
    option_classes = {match.group(2).upper() for match in option_matches}
    required_labels = (
        "Execution architecture",
        "Builder surface",
        "Control fit",
        "Implementation effort",
        "Operating cost",
        "Maintenance burden",
        "Security fit",
        "Portability",
        "Skill requirements",
        "Source evidence",
    )
    for index, match in enumerate(option_matches):
        end = option_matches[index + 1].start() if index + 1 < len(option_matches) else len(block)
        option = block[match.end():end]
        for label in required_labels:
            if not re.search(rf"\*{{0,2}}{re.escape(label)}:\*{{0,2}}\s*\S", option, re.IGNORECASE):
                result.fail("ARCH-OPTION", f"{match.group(1)} is missing required field '{label}'.")

    omitted = {
        match.group(1).upper()
        for match in re.finditer(
            r"^\s*-\s*(PRIMARY|NATIVE_SUITE|LOW_CODE|CODE_FIRST|VENDOR_NEUTRAL)\s+[—-]\s+\S",
            block,
            re.IGNORECASE | re.MULTILINE,
        )
    }
    for missing in sorted(ARCHITECTURE_CLASSES - option_classes - omitted):
        result.fail("ARCH-CLASS", f"Architecture class {missing} is neither generated nor omitted with a reason.")

    selection_match = re.search(r"^\s*Selected option\s*:\s*(\S+)", block, re.IGNORECASE | re.MULTILINE)
    selected = selection_match.group(1).strip("`*.,").upper() if selection_match else ""
    unselected_values = {"", "NONE", "NOT_SELECTED", "PENDING", "UNKNOWN"}
    if selected not in unselected_values and selected not in option_ids:
        result.fail("ARCH-SELECTION", f"Selected architecture option '{selected}' was not generated.")

    handoff_fields = parse_fields(handoff_block(text))
    handoff_status = (handoff_fields.get("Handoff status") or "").strip(" `*").replace(" ", "_").upper()
    if handoff_status == "BUILD_READY":
        if selected in unselected_values or selected not in option_ids:
            result.fail("ARCH-SELECTION", "BUILD_READY requires an operator-selected generated architecture option.")
        if not re.search(r"^\s*Selection by\s*:\s*\S", block, re.IGNORECASE | re.MULTILINE):
            result.fail("ARCH-METADATA", "BUILD_READY architecture selection requires the selector identity or role.")
        if not re.search(r"^\s*Selection date\s*:\s*\d{4}-\d{2}-\d{2}\s*$", block, re.IGNORECASE | re.MULTILINE):
            result.fail("ARCH-METADATA", "BUILD_READY architecture selection requires an ISO selection date.")


def handoff_block(text: str) -> str:
    return section(
        text,
        HANDOFF_HEADING,
        r"^\s*(?:#{1,4}\s*)?(?:━━\s*)?OPERATOR DISPOSITION(?:\s*━━+)?\s*$",
    )


def check_handoff(text: str, result: ValidationResult) -> None:
    block = handoff_block(text)
    if not block:
        return
    fields = parse_fields(block)
    raw_status = (
        fields.get("Handoff status")
        or fields.get("Build Handoff Pack")
        or fields.get("Deployment status")
    )
    if not raw_status:
        result.fail("PACK-STATUS", "Handoff status is missing.")
        return
    status = raw_status.strip(" `*").replace(" ", "_").upper()
    if status not in HANDOFF_STATUSES:
        result.fail("PACK-STATUS", f"Invalid handoff status '{status}'.")
        return
    required_contract_labels = (
        "Terminal-action boundary",
        "Architecture decision record",
        "Permissions and credentials",
        "Deterministic controls",
        "Human checkpoints",
        "Prohibited actions",
        "Logging and audit",
        "Failure, rollback, and stop behavior",
        "Deployment sequence",
        "Assumptions",
        "Unresolved dependencies",
        "Expiration and reassessment triggers",
        "Version invalidation triggers",
        "Tool alternatives",
        "Builder acknowledgement",
    )
    missing_contract = [
        label
        for label in required_contract_labels
        if not re.search(rf"^\s*(?:#{1,4}\s*)?(?:\*+)?{re.escape(label)}\s*:(?:\*+)?", block, re.IGNORECASE | re.MULTILINE)
    ]
    if missing_contract:
        result.fail("PACK-CONTRACT", "Build Handoff Pack is missing contract fields: " + ", ".join(missing_contract) + ".")
    if status == "BUILD_READY":
        if not re.search(r"\bManifest\s*:", block, re.IGNORECASE):
            result.fail("PACK-MANIFEST", "BUILD_READY requires an artifact manifest.")
        entries = re.split(r"(?=^\s*-?\s*Path\s*:)", block, flags=re.IGNORECASE | re.MULTILINE)[1:]
        if not entries:
            result.fail("PACK-MANIFEST", "BUILD_READY manifest contains no file entries.")
        for entry in entries:
            if not re.search(r"^\s*(?:-\s*)?Complete content\s*:\s*\S", entry, re.IGNORECASE | re.MULTILINE):
                result.fail("PACK-CONTENT", "Every BUILD_READY manifest entry requires complete content.")
            if not re.search(r"^\s*(?:-\s*)?Source evidence\s*:\s*\S", entry, re.IGNORECASE | re.MULTILINE):
                result.fail("PACK-SOURCE", "Every BUILD_READY manifest entry requires source evidence.")
        if not re.search(r"Acceptance tests?\s*:", block, re.IGNORECASE):
            result.fail("PACK-TESTS", "BUILD_READY requires complete acceptance tests.")
        if re.search(r"Required before build\s*:\s*\S", block, re.IGNORECASE):
            result.fail("PACK-READY-BLOCKERS", "BUILD_READY cannot contain unresolved required inputs.")
    elif status == "BLOCKED_FOR_EVIDENCE":
        if not re.search(r"Required before build\s*:\s*\S", block, re.IGNORECASE):
            result.fail("PACK-BLOCKERS", "BLOCKED_FOR_EVIDENCE requires named missing evidence.")
    elif status == "NOT_APPLICABLE":
        missing_human = [
            label
            for label in ("Human operating procedure", "Safe decomposition opportunities")
            if not re.search(rf"^\s*(?:#{1,4}\s*)?{re.escape(label)}\s*:", block, re.IGNORECASE | re.MULTILINE)
        ]
        if missing_human:
            result.fail("PACK-HUMAN", "NOT_APPLICABLE is missing: " + ", ".join(missing_human) + ".")


def disposition_block(text: str) -> str:
    matches = list(re.finditer(r"OPERATOR DISPOSITION", text, re.IGNORECASE))
    if not matches:
        return ""
    return text[matches[-1].end():]


def check_disposition(text: str, result: ValidationResult) -> None:
    block = disposition_block(text)
    if not block:
        result.fail("DISP-MISSING", "OPERATOR DISPOSITION section not found.")
        return
    checked_approval = bool(re.search(r"\[x\]\s*APPROVE_FOR_BUILD", block, re.IGNORECASE))
    field_approval = bool(re.search(r"Disposition\s*:\s*APPROVE_FOR_BUILD", block, re.IGNORECASE))
    if checked_approval:
        result.fail("DISP-PRESELECTED", "The Gate may not pre-select APPROVE_FOR_BUILD.")
    if field_approval or checked_approval:
        required = {
            "Name / role": r"Name\s*/\s*role\s*:\s*\S",
            "Date": r"Date\s*:\s*\d{4}-\d{2}-\d{2}",
            "Packet version": r"Packet version\s*:\s*v\d+(?:[.\-]\d+)*\s*$",
            "Rationale": r"Rationale\s*:\s*\S",
        }
        missing = [name for name, pattern in required.items() if not re.search(pattern, block, re.IGNORECASE)]
        if missing:
            result.fail("DISP-PRESELECTED", "APPROVE_FOR_BUILD appears without a complete operator record.")
            result.fail("DISP-METADATA", f"Approval is missing required metadata: {', '.join(missing)}.")


def check_placeholders(text: str, result: ValidationResult) -> None:
    checkable = re.sub(r"OPERATOR DISPOSITION.*\Z", "", text, flags=re.IGNORECASE | re.DOTALL)
    for line_number, line in enumerate(checkable.splitlines(), 1):
        for pattern in PLACEHOLDER_PATTERNS:
            if pattern.search(line):
                result.fail("PLACEHOLDER", f"Forbidden placeholder at line {line_number}: {line.strip()[:80]}", line_number)
                break


def validate(text: str) -> ValidationResult:
    result = ValidationResult()
    check_structure(text, result)
    check_packets(text, result)
    check_architecture(text, result)
    check_handoff(text, result)
    check_placeholders(text, result)
    check_disposition(text, result)
    return result


def main() -> int:
    if len(sys.argv) != 2:
        print("Usage: validate_gate_output.py <output_file.md> OR -")
        return 2
    source = sys.argv[1]
    text = sys.stdin.read() if source == "-" else Path(source).read_text(encoding="utf-8")
    result = validate(text)
    print(f"Gate Output Validator — {source}")
    print("─" * 60)
    if not result.findings:
        print("PASS  No issues found.")
    for item in result.findings:
        location = f" (line {item.line})" if item.line else ""
        print(f"{item.severity:4}  [{item.code}]{location} {item.message}")
    failures = sum(item.severity == "FAIL" for item in result.findings)
    warnings = sum(item.severity == "WARN" for item in result.findings)
    print(f"Result: {'PASS' if failures == 0 else 'FAIL'} — {failures} failure(s), {warnings} warning(s)")
    return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
