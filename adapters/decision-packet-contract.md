# Decision Packet Contract

The Autonomy Decision Packet is the provider-neutral interface between assessment, architecture selection, operator disposition, and implementation. It follows `autonomy-gate/reference/operating-contract.md`.

## Required Packet Fields

```text
Workflow ID:            WF-YYYYMMDD-NNN
Packet version:         vN
Autonomy:               AUTONOMOUS | SUPERVISED | SOP_FIRST | HUMAN_ONLY
Assessment surface:     Where the Gate assessment ran
Execution architecture: Technology-neutral design or operator-selected named stack
Builder surface:        Internal engineering | platform administrator | low-code specialist | Claude Code | Codex | other
Confidence:             HIGH | MEDIUM | LOW
Terminal action:        Last action the workflow executes
Justification:          RULE-NN and GATE-NN citations
Controls required:      Deterministic controls required by the verdict
Evidence gaps:          Decision-material gaps or None
Artifact required:      Execution artifact type
Handoff status:         BUILD_READY | BLOCKED_FOR_EVIDENCE | NOT_APPLICABLE
Operator disposition:   PENDING | APPROVE_FOR_BUILD | REVISE | HOLD_FOR_EVIDENCE | REJECT
```

## Role Separation

- `Assessment surface` never determines production architecture.
- `Execution architecture` names production capabilities and components. It remains technology-neutral when the stack is unknown.
- `Builder surface` names the implementer and may differ from both assessment and execution environments.
- `PROJECT`, `COWORK`, and `CODE_AGENT` are implementation patterns, not universal production verdicts.

## Confidence and Handoff

Confidence concerns the autonomy decision. Handoff status concerns implementation completeness.

| Handoff status | Meaning |
|---|---|
| `BUILD_READY` | Architecture selected; every manifest file, control, and acceptance test is complete; no unresolved input remains. |
| `BLOCKED_FOR_EVIDENCE` | All generatable content exists, but named organizational evidence is missing. Affected rules rerun when evidence arrives. |
| `NOT_APPLICABLE` | No implementation is authorized. |

## Disposition

The Gate issues `PENDING`. `APPROVE_FOR_BUILD` is valid only when the operator records name and role, date, packet version, and rationale against a `BUILD_READY` pack. Any change to verdict, terminal action, controls, selected architecture, or handoff contents invalidates the prior disposition.

## Consumer Rules

1. Do not modify verdict fields.
2. Do not broaden the terminal action.
3. Do not replace deterministic controls with prompt instructions.
4. Do not begin implementation without `BUILD_READY` and `APPROVE_FOR_BUILD`.
5. Complete the Builder Acknowledgement before changing code or configuration.
6. Stop and return to the operator when a tool substitution changes permissions, controls, data handling, or audit behavior.
7. Halt operation when an expiration trigger fires and move the workflow to `RECERTIFICATION_REQUIRED`.
