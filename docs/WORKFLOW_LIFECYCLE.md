# Workflow Lifecycle

The canonical lifecycle is owned by `autonomy-gate/reference/operating-contract.md`.

```text
SUBMITTED -> ASSESSED -> ARCHITECTURE_SELECTED -> DISPOSITION_PENDING
                    \-> HANDOFF_BLOCKED --------/
DISPOSITION_PENDING -> APPROVED_FOR_BUILD | HANDOFF_BLOCKED | ASSESSED | REJECTED
APPROVED_FOR_BUILD -> IN_BUILD -> VALIDATING -> ACTIVE
ACTIVE -> PAUSED | EXPIRED
EXPIRED -> RECERTIFICATION_REQUIRED -> SUBMITTED
```

## Stage 1: Assess

Submit a free-form workflow description. The Gate returns the snapshot and decision packet, including autonomy, terminal action, controls, confidence, and evidence gaps. Architecture is not selected before assessment.

## Stage 2: Select Architecture

Compare primary, native-suite, low-code, code-first, and vendor-neutral options where viable. Confirm stack constraints and record the operator-selected option. Missing evidence moves the record to `HANDOFF_BLOCKED`.

## Stage 3: Resolve Evidence

Supply only the named missing organizational values. The Gate increments packet version and reruns every affected rule. A prior disposition is invalidated if verdict, terminal action, controls, architecture, or handoff contents change.

## Stage 4: Review and Disposition

Review the complete artifact and Build Handoff Pack. `BUILD_READY` means the architecture is selected and no required content is missing. Approval requires operator name and role, date, packet version, and rationale. Other choices are `HOLD_FOR_EVIDENCE`, `REVISE`, and `REJECT`.

## Stage 5: Build

The builder completes the Builder Acknowledgement before implementation. The builder may not broaden scope, weaken controls, or substitute a materially different tool without returning to the operator.

## Stage 6: Validate and Activate

Map every acceptance criterion to test, log, screenshot, or observable evidence. Only validated implementation moves to `ACTIVE`.

## Stage 7: Monitor and Recertify

Monitor incidents, error thresholds, material system changes, policy changes, model changes, and time-based expiration conditions. Pause expired autonomy immediately. Recertification creates a new packet and requires a new disposition.
