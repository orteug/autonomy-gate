# Autonomy Decision Packet — Contract Specification

This document defines the Autonomy Decision Packet as a portable interface. The packet is produced by The Autonomy Gate (Decision Layer) and consumed by any execution surface (Cowork, Claude Code, Codex, or a human reviewer). The packet is platform-agnostic. Every adapter in this folder reads the same fields.

---

## Packet Structure

Every Gate run produces a packet with the following fields. All fields are always present. Fields marked REQUIRED must be populated for HIGH confidence. Fields marked CONDITIONAL appear only when the condition applies.

Snapshot fields carry provenance states from RULE-01: `STATED` (explicit in input), `DERIVED` (produced by a named Gate rule), `UNKNOWN` (cannot be populated; recorded as evidence gap), `NOT_APPLICABLE` (field does not apply). Only `STATED` and `DERIVED` values count as populated. `UNKNOWN` fields always become evidence gaps.

```
AUTONOMY DECISION PACKET

Autonomy:             [AUT-1 AUTONOMOUS | AUT-2 SUPERVISED | AUT-3 SOP_FIRST | AUT-4 HUMAN_ONLY]
Surface:              [SURFACE-1 PROJECT | SURFACE-2 COWORK | SURFACE-3 CODE_AGENT | SURFACE-4 NO_AI]
Confidence:           [HIGH | MEDIUM | LOW]
Terminal action:      [The last thing that executes — not the workflow label]
Justification:        [RULE-NN and GATE-NN citations that drove the verdict]
Controls required:    [List of controls that must be in place before the workflow runs]
Evidence gaps:        [CONDITIONAL — present when confidence is MEDIUM or LOW]
Conservative route:   [CONDITIONAL — present when adversarial check revised the base verdict]
Artifact required:    [template filename — the execution document produced in Phase 2]
Build Handoff Pack:   [READY | BLOCKED | NOT_APPLICABLE — status of the generated handoff pack]
Operator Disposition: [PENDING — always unselected by the Gate; operator fills before build]
```

---

## Field Definitions

### Autonomy

The level of authority the workflow is permitted to execute without a human approval checkpoint.

| Value | Meaning | Execution implication |
|-------|---------|----------------------|
| AUTONOMOUS | No approval checkpoint required inside the run | Surface executes end-to-end; human may initiate but does not approve mid-run |
| SUPERVISED | AI prepares; human approves before terminal action executes | Approval checkpoint must be implemented as a blocking step |
| SOP_FIRST | Process documentation must precede any automation | Do not route to any execution surface; return to process owner |
| HUMAN_ONLY | Terminal action cannot be delegated regardless of controls | No surface assignment; governance memo governs the human process |

---

### Surface

The platform where the workflow should run.

| Value | Platform | What it can do |
|-------|----------|---------------|
| PROJECT | Claude Project / ChatGPT Project | Human-initiated sessions, document and analysis outputs |
| COWORK | Claude Cowork | Scheduled/unattended execution, local file access, folder I/O |
| CODE_AGENT | Claude Code / Codex | Code execution, API integration, deterministic logic, scheduling |
| NO_AI | None | Human process only; pairs with SOP_FIRST and HUMAN_ONLY |

---

### Confidence

The completeness of the decision evidence at the time of assessment. Confidence reflects the quality of the autonomy verdict — not the completeness of the Build Handoff Pack. A governance value gap (missing error-rate threshold, recertification interval) affects pack status, not decision confidence.

| Value | Meaning | How to act |
|-------|---------|-----------|
| HIGH | All required fields populated; no decision-material evidence gaps; adversarial check passed | Proceed to artifact implementation |
| MEDIUM | Minor gaps present; verdict is defensible but not fully evidenced | Implement with gaps acknowledged; re-run when gaps are resolved |
| LOW | Significant gaps; conservative route applied | Implement conservatively; gather missing evidence and re-run |

---

### Terminal Action

The last thing that executes in the workflow — not the label applied to it. This is the field the Gate's gate conditions are applied to. Every execution surface must know the terminal action before running. If the surface's scope expands beyond the terminal action stated in the packet, halt and re-submit.

---

### Controls Required

The controls that must be in place before the workflow executes. These are not optional — they are the conditions under which the verdict was issued. If a listed control cannot be implemented, the workflow should not run at the current verdict level.

---

### Evidence Gaps

Present when confidence is MEDIUM or LOW. Names the specific fields that could not be populated from the workflow description. Each gap is a specific piece of information, not a vague request for more detail. Fill the gaps and re-run to upgrade confidence.

---

### Build Handoff Pack

The status of the implementation-ready specification generated in Phase 2.

| Value | Meaning |
|-------|---------|
| READY | All required files are fully generated as paste-ready content; no operator input required before implementation |
| BLOCKED | Required governance values (error-rate threshold, recertification interval, owner assignment, etc.) are missing and must be supplied by the operator before the builder can proceed |
| NOT_APPLICABLE | Pairs with HUMAN_ONLY / NO_AI; no implementation artifact is generated |

A BLOCKED pack is not a failed assessment. The verdict is valid; the operator must supply the missing values. Once supplied, the builder may proceed without re-running the Gate.

---

### Operator Disposition

The human release gate. A Build Handoff Pack is not authorized for implementation until an accountable operator records a disposition. The Gate may recommend a disposition but may not select `APPROVE_FOR_BUILD` on the operator's behalf.

| Value | Meaning |
|-------|---------|
| APPROVE_FOR_BUILD | Operator authorizes the build; scope, architecture, and controls are accepted |
| REVISE | Assessment or architecture requires changes before authorization |
| HOLD_FOR_EVIDENCE | Assessment is sound but required governance values are missing |
| REJECT | Workflow should not be built at this time |

The `Operator Disposition` field in the packet is always `PENDING` when the Gate issues it. The operator fills this field in the artifact's OPERATOR DISPOSITION section before build handoff.

Governed by RULE-15. See `autonomy-gate/reference/operator-disposition.md`.

---

## How Each Surface Consumes the Packet

```
Claude Project / ChatGPT Project
  → Receives: identity.md + rules.md + examples.md + reference files
  → Produces: Workflow Intake Snapshot + Autonomy Decision Packet + Artifact
  → Does not execute the workflow — produces the governed work order

Claude Cowork
  → Receives: Autonomy Decision Packet + Cowork Project Config artifact
  → Executes: Scheduled or unattended workflow within named constraints
  → Emits: Terminal status per run; log retained per AUDIT REQUIREMENTS

Claude Code / Codex
  → Receives: CLAUDE.md or AGENTS.md containing the packet fields
  → Executes: Code, scripts, integrations, deterministic logic
  → Blocked by: Prohibited actions list; approval checkpoint (if SUPERVISED)

Human reviewer
  → Receives: Governance Memo (HUMAN_ONLY) or Control Plan (SUPERVISED)
  → Executes: Review, approval, or rejection per APPROVAL CHECKPOINT
  → Documents: Decision with timestamp in audit trail
```

---

## Packet Integrity Rules

1. **Do not modify verdict fields.** The autonomy level, surface, confidence, and justification are issued by the Gate. They are not editable by the execution surface.
2. **Do not strip the terminal action field.** Every surface must know what it is and is not permitted to cross.
3. **Do not suppress evidence gaps.** If gaps are present, they must be visible in the implementation artifact.
4. **Prohibited actions are hard stops.** They cannot be overridden by user instruction, operator context, or workflow urgency.
5. **Autonomy expires.** Every packet has an AUTONOMY EXPIRES WHEN section in its artifact. When any condition is met, the surface must halt and the workflow must be re-submitted to the Gate.
6. **Build Handoff Pack status is independent of confidence.** A BLOCKED pack does not lower the verdict's confidence level. The operator supplies missing governance values; the builder does not re-assess.
7. **No build without operator disposition.** A `PENDING` Operator Disposition field means no implementation has been authorized. The builder must not proceed until the operator records `APPROVE_FOR_BUILD` in the artifact.
