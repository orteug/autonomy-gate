# Workflow Governance Registry

The registry stores one portable JSON record per governed workflow, validated against `workflow-record.schema.json`. It answers: what autonomy was granted, which architecture was selected, who authorized it, what is running, and when must it stop?

## File Naming

Use `WF-YYYYMMDD-NNN.json`; the filename and `workflow_id` must match.

## Canonical Lifecycle

The registry uses the exact states from `autonomy-gate/reference/operating-contract.md`:

`SUBMITTED`, `ASSESSED`, `ARCHITECTURE_SELECTED`, `HANDOFF_BLOCKED`, `DISPOSITION_PENDING`, `APPROVED_FOR_BUILD`, `IN_BUILD`, `VALIDATING`, `ACTIVE`, `PAUSED`, `EXPIRED`, `RECERTIFICATION_REQUIRED`, and `REJECTED`.

Handoff readiness is a separate field: `BUILD_READY`, `BLOCKED_FOR_EVIDENCE`, or `NOT_APPLICABLE`.

## Useful Queries

```bash
# Active autonomous workflows
jq -r 'select(.autonomy == "AUTONOMOUS" and .status == "ACTIVE") | "\(.workflow_id) \(.name)"' *.json

# Work requiring operator action
jq -r 'select(.status == "HANDOFF_BLOCKED" or .status == "DISPOSITION_PENDING" or .status == "RECERTIFICATION_REQUIRED") | "\(.workflow_id) \(.name) \(.status)"' *.json

# Work in implementation or validation
jq -r 'select(.status == "IN_BUILD" or .status == "VALIDATING") | "\(.workflow_id) \(.name) \(.status)"' *.json

# Expired or paused workflows
jq -r 'select(.status == "EXPIRED" or .status == "PAUSED") | "\(.workflow_id) \(.name) \(.status)"' *.json
```

Do not delete prior packet versions or dispositions. Append history and retain records according to the organization's stated policy.
