#!/usr/bin/env python3
"""
validate_gate_output.py — Autonomy Gate output validator.

Parses a Gate response (Markdown text) and checks for:
  - Presence of the three required sections (Snapshot, Packet, Artifact)
  - Required packet fields with valid mechanism IDs
  - Forbidden placeholders (brackets, TBD, "fill in", "customize")
  - Logical contradictions (HIGH + evidence gaps, AUTONOMOUS + hard gate, etc.)
  - Build Handoff Pack consistency

Usage:
  python3 validate_gate_output.py <output_file.md>
  cat output.md | python3 validate_gate_output.py -
"""

import re
import sys
from dataclasses import dataclass, field
from pathlib import Path


AUTONOMY_VALUES = {"AUTONOMOUS", "SUPERVISED", "SOP_FIRST", "HUMAN_ONLY"}
SURFACE_VALUES = {"PROJECT", "COWORK", "CODE_AGENT", "NO_AI"}
CONFIDENCE_VALUES = {"HIGH", "MEDIUM", "LOW"}
PACK_STATUSES = {"READY", "BLOCKED", "NOT_APPLICABLE"}

PLACEHOLDER_PATTERNS = [
    re.compile(r"\[(?!CONDITIONAL|present when|optional)[^\]]{3,}\]"),  # [fill in], [your value]
    re.compile(r"\bTBD\b", re.IGNORECASE),
    re.compile(r"\bcustomize\b", re.IGNORECASE),
    re.compile(r"fill in", re.IGNORECASE),
    re.compile(r"\byour value\b", re.IGNORECASE),
]

RULE_ID = re.compile(r"\bRULE-\d+\b")
GATE_ID = re.compile(r"\bGATE-[1-5]\b")

SECTION_MARKERS = {
    "snapshot": re.compile(r"WORKFLOW INTAKE SNAPSHOT", re.IGNORECASE),
    "packet": re.compile(r"AUTONOMY DECISION PACKET", re.IGNORECASE),
    "artifact": re.compile(r"BUILD HANDOFF PACK|OPERATOR DISPOSITION", re.IGNORECASE),
}

# Matches full-width box-drawing dashes (━) and regular dashes/underscores
SECTION_BORDER = re.compile(r"[━─=\-_]{4,}")

PACKET_FIELDS = [
    "Autonomy",
    "Surface",
    "Confidence",
    "Terminal action",
    "Justification",
]


@dataclass
class Finding:
    severity: str  # FAIL | WARN
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
        return not any(f.severity == "FAIL" for f in self.findings)


def check_three_sections(text: str, result: ValidationResult) -> dict[str, int]:
    positions = {}
    for name, pattern in SECTION_MARKERS.items():
        m = pattern.search(text)
        if m:
            positions[name] = m.start()
        else:
            result.fail(
                f"STRUCT-{name.upper()}",
                f"Required section not found: {name.upper()}. "
                "Gate must produce Snapshot, Packet, and Artifact in every response.",
            )
    return positions


def extract_packet_blocks(text: str) -> list[str]:
    """Return all packet blocks from the text (one per Gate run)."""
    parts = re.split(r"(?:AUTONOMY DECISION PACKET)", text, flags=re.IGNORECASE)
    blocks = []
    for part in parts[1:]:
        lines = []
        for line in part.splitlines():
            if re.match(r"^\s*#{1,3}\s+", line) and lines:
                break
            lines.append(line)
        block = "\n".join(lines)
        # Only treat as a real packet block if it contains actual packet fields
        if re.search(r"(?m)^[*\s]*Autonomy\s*:", block):
            blocks.append(block)
    return blocks


def extract_packet_block(text: str) -> str:
    """Return the first packet block (backward-compatible)."""
    blocks = extract_packet_blocks(text)
    return blocks[0] if blocks else ""


def parse_packet_fields(packet_block: str) -> dict[str, str]:
    fields = {}
    for line in packet_block.splitlines():
        if ":" in line:
            key, _, value = line.partition(":")
            key = key.strip().lstrip("─- *")
            value = value.strip()
            if key and value:
                fields[key] = value
    return fields


def check_packet_fields(text: str, result: ValidationResult) -> list[dict[str, str]]:
    blocks = extract_packet_blocks(text)
    if not blocks:
        for required in PACKET_FIELDS:
            result.fail("PKT-FIELD", f"Required packet field missing: '{required}'")
        return [{}]

    all_fields = []
    for i, block in enumerate(blocks):
        prefix = f"Run {i+1}: " if len(blocks) > 1 else ""
        fields = parse_packet_fields(block)
        all_fields.append(fields)

        for required in PACKET_FIELDS:
            if required not in fields:
                result.fail(
                    "PKT-FIELD",
                    f"{prefix}Required packet field missing: '{required}'",
                )

        autonomy = fields.get("Autonomy", "")
        surface = fields.get("Surface", "")
        confidence = fields.get("Confidence", "")

        for val, valid_set, field_name in [
            (autonomy, AUTONOMY_VALUES, "Autonomy"),
            (surface, SURFACE_VALUES, "Surface"),
            (confidence, CONFIDENCE_VALUES, "Confidence"),
        ]:
            token = val.split()[0].rstrip(".,()").upper() if val else ""
            if token and token not in valid_set:
                result.fail(
                    "PKT-VALUE",
                    f"{prefix}Packet field '{field_name}' has unrecognized value: '{val}'. "
                    f"Expected one of: {', '.join(sorted(valid_set))}",
                )

    return all_fields


def check_justification_citations(fields: dict[str, str], result: ValidationResult) -> None:
    justification = fields.get("Justification", "")
    if not justification:
        return
    has_rule = bool(RULE_ID.search(justification))
    if not has_rule:
        result.warn(
            "PKT-CITE",
            "Justification field does not cite any RULE-NN identifier. "
            "Verdicts should cite the rules that drove them.",
        )


def check_contradictions(fields: dict[str, str], text: str, result: ValidationResult) -> None:
    autonomy_raw = fields.get("Autonomy", "").upper()
    confidence_raw = fields.get("Confidence", "").upper()
    surface_raw = fields.get("Surface", "").upper()
    pack_raw = fields.get("Build Handoff Pack", "").upper()

    autonomy = next((v for v in AUTONOMY_VALUES if v in autonomy_raw), "")
    confidence = next((v for v in CONFIDENCE_VALUES if v in confidence_raw), "")
    surface = next((v for v in SURFACE_VALUES if v in surface_raw), "")

    # HIGH confidence with named evidence gaps — check the packet block only, not full text
    if confidence == "HIGH":
        # Look for evidence gaps line with actual content (not empty or "none")
        gap_match = re.search(r"Evidence gaps?:\s+(?!N/A|None|none|—|$)(.+)", text, re.IGNORECASE | re.MULTILINE)
        if gap_match and gap_match.group(1).strip() not in ("—", "None", "N/A", ""):
            result.fail(
                "CONTRA-HIGH-GAPS",
                "Confidence is HIGH but evidence gaps are named. "
                "HIGH confidence requires all required fields populated and no decision-material gaps. "
                "(RULE-06)",
            )

    # AUTONOMOUS with a hard gate — check the Justification field specifically
    if autonomy == "AUTONOMOUS":
        justification = fields.get("Justification", "")
        gate_hits = GATE_ID.findall(justification)
        critical_gates = [g for g in gate_hits if g in {"GATE-2", "GATE-3"}]
        if critical_gates:
            result.fail(
                "CONTRA-AUTO-GATE",
                f"Autonomy is AUTONOMOUS but {critical_gates} cited in Justification. "
                "GATE-2 and GATE-3 require HUMAN_ONLY regardless of controls. (RULE-06)",
            )

    # NO_AI surface with non-SOP_FIRST / HUMAN_ONLY autonomy
    if "NO_AI" in surface and autonomy not in ("SOP_FIRST", "HUMAN_ONLY", ""):
        result.fail(
            "CONTRA-NO-AI",
            f"Surface is NO_AI but autonomy is '{autonomy}'. "
            "NO_AI pairs only with SOP_FIRST or HUMAN_ONLY. (RULE-06)",
        )

    # NOT_APPLICABLE pack with AUTONOMOUS or SUPERVISED
    if "NOT_APPLICABLE" in pack_raw and autonomy in ("AUTONOMOUS", "SUPERVISED"):
        result.fail(
            "CONTRA-PACK-STATUS",
            f"Build Handoff Pack is NOT_APPLICABLE but autonomy is '{autonomy}'. "
            "NOT_APPLICABLE pairs only with SOP_FIRST and HUMAN_ONLY. (RULE-14)",
        )

    # READY pack with HUMAN_ONLY
    if "READY" in pack_raw and autonomy == "HUMAN_ONLY":
        result.warn(
            "CONTRA-READY-HUMAN",
            "Build Handoff Pack is READY but autonomy is HUMAN_ONLY. "
            "HUMAN_ONLY workflows produce a Governance Memo, not a READY implementation pack. "
            "Expected NOT_APPLICABLE. (RULE-14)",
        )


def strip_operator_section(text: str) -> str:
    """Remove OPERATOR DISPOSITION sections — their blanks are intentional."""
    return re.sub(
        r"OPERATOR DISPOSITION.*?(?=\n#{1,3}\s|\Z)",
        "",
        text,
        flags=re.DOTALL | re.IGNORECASE,
    )


def check_placeholders(text: str, result: ValidationResult) -> None:
    # Exclude the OPERATOR DISPOSITION section — blanks there are by design (RULE-15)
    checkable = strip_operator_section(text)
    lines = checkable.splitlines()
    for lineno, line in enumerate(lines, 1):
        for pattern in PLACEHOLDER_PATTERNS:
            if pattern.search(line):
                snippet = line.strip()[:80]
                result.fail(
                    "PLACEHOLDER",
                    f"Forbidden placeholder at line {lineno}: {snippet!r}",
                    line=lineno,
                )
                break  # one finding per line


def check_operator_disposition(text: str, result: ValidationResult) -> None:
    if not re.search(r"OPERATOR DISPOSITION", text, re.IGNORECASE):
        result.fail(
            "DISP-MISSING",
            "OPERATOR DISPOSITION section not found. Required by RULE-15 and RULE-12.",
        )
        return

    if re.search(r"\[x\]\s*APPROVE_FOR_BUILD", text, re.IGNORECASE):
        result.fail(
            "DISP-PRESELECTED",
            "APPROVE_FOR_BUILD is pre-selected in the OPERATOR DISPOSITION section. "
            "The Gate may not select APPROVE_FOR_BUILD on the operator's behalf. (RULE-15)",
        )


def validate(text: str) -> ValidationResult:
    result = ValidationResult()

    check_three_sections(text, result)
    all_fields = check_packet_fields(text, result)
    for fields in all_fields:
        check_justification_citations(fields, result)
        check_contradictions(fields, text, result)
    check_placeholders(text, result)
    check_operator_disposition(text, result)

    return result


def main() -> int:
    if len(sys.argv) < 2:
        print("Usage: validate_gate_output.py <file.md> OR cat output.md | validate_gate_output.py -")
        return 2

    path = sys.argv[1]
    if path == "-":
        text = sys.stdin.read()
        source = "<stdin>"
    else:
        p = Path(path)
        if not p.exists():
            print(f"File not found: {path}")
            return 2
        text = p.read_text(encoding="utf-8")
        source = path

    result = validate(text)

    print(f"Gate Output Validator — {source}")
    print("─" * 60)

    if not result.findings:
        print("PASS  No issues found.")
    else:
        failures = 0
        warnings = 0
        for f in result.findings:
            loc = f" (line {f.line})" if f.line else ""
            print(f"{f.severity:4}  [{f.code}]{loc} {f.message}")
            if f.severity == "FAIL":
                failures += 1
            else:
                warnings += 1
        print("─" * 60)
        print(f"{failures} failure(s), {warnings} warning(s)")

    return 0 if result.passed else 1


if __name__ == "__main__":
    raise SystemExit(main())
