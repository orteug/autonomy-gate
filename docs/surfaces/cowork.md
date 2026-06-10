# Surface Guide: Cowork

Use this when the Gate returns:

```text
AUTONOMOUS / COWORK
SUPERVISED / COWORK
```

or when the artifact says Cowork is the ideal surface.

---

## Capability Note

Cowork availability and exact capabilities may vary by account, plan, and product rollout.

Before using this guide operationally, confirm your Cowork environment supports:

- the required folder access
- the required trigger or schedule
- the required connectors
- the required logging method
- the required approval checkpoint

If it does not, use the artifact's fallback path.

---

## What Cowork Is For

Cowork-style workflows are useful when the work needs:

- recurring cadence
- folder-based input/output
- local file handling
- terminal status logs
- multi-step execution
- human-review holds for supervised runs

---

## Standard Folder Structure

```text
[workflow-name]/
├── inputs/
├── outputs/
├── logs/
└── archive/
```

Use the folder names from the artifact when they differ.

---

## Setup Steps

1. Read the Cowork Project Config.
2. Create the folder structure.
3. Add only the folders named in the artifact.
4. Paste the custom instructions.
5. Configure the trigger or schedule.
6. Configure allowed actions.
7. Configure prohibited actions.
8. Configure logging.
9. Run a non-production test.

---

## Required Terminal Status

Every run must end with exactly one:

```text
COMPLETED
COMPLETED_WITH_WARNINGS
NEEDS_REVIEW
BLOCKED
FAILED
SKIPPED
```

Every status must be logged.

If a run does not emit a terminal status, it is not observable.

---

## SUPERVISED / COWORK

For supervised Cowork workflows:

1. Write the output to a review location.
2. Halt before terminal action.
3. Require named reviewer approval.
4. Log approval identity and timestamp.
5. Proceed only after explicit approval.
6. Emit `BLOCKED` if approval is missing or late.

No response is not approval.

---

## Fallback To Project

If Cowork is unavailable:

1. Human starts each run manually.
2. User pastes or uploads input.
3. Project produces output.
4. Human delivers output manually.
5. Human maintains the run log.

The surface changes. The autonomy verdict does not automatically change.

---

## Test Checklist

- [ ] Folders exist.
- [ ] Inputs are scoped.
- [ ] Outputs are scoped.
- [ ] Logs are written.
- [ ] Prohibited actions are visible.
- [ ] Approval checkpoint blocks execution when required.
- [ ] Failed input produces `FAILED` or `BLOCKED`.
- [ ] Recertification trigger is documented.

