# Workflow Governance Registry

The registry stores one portable JSON record per governed workflow, validated against `workflow-record.schema.json`. It answers: what autonomy was granted, which architecture was selected, who authorized it, what is running, and when must it stop?

It is the persistent system of record for the request, packet versions, architecture options and selection, disposition, builder acknowledgement, validation evidence, lifecycle events, incidents, expiration, recertification, appeals, change assessments, precedents, and value metrics. Conversation memory is never authoritative.

## File Naming

Use `WF-YYYYMMDD-NNN.json`; the filename and `workflow_id` must match.

## Canonical Lifecycle

The registry uses the exact states from `autonomy-gate/reference/operating-contract.md`:

`SUBMITTED`, `ASSESSED`, `ARCHITECTURE_SELECTED`, `HANDOFF_BLOCKED`, `DISPOSITION_PENDING`, `APPROVED_FOR_BUILD`, `IN_BUILD`, `VALIDATING`, `ACTIVE`, `PAUSED`, `EXPIRED`, `RECERTIFICATION_REQUIRED`, and `REJECTED`.

Handoff readiness is a separate field: `BUILD_READY`, `BLOCKED_FOR_EVIDENCE`, or `NOT_APPLICABLE`.

## Appeal Path

An appeal challenges a field or conclusion with evidence; it does not override a hard gate. Record who raised it, the claim, evidence, resolution, and any new packet version. If evidence changes a material field, issue a new packet and invalidate the prior selection, disposition, and acknowledgement.

## Change Assessment

Record proposed changes to tools, policies, terminal actions, controls, permissions, credentials, or data flows before implementation. Classify each as `IN_SCOPE`, `OUT_OF_SCOPE`, or `RECERTIFICATION_REQUIRED`. Builders may not self-authorize an out-of-scope change.

## Precedent Retrieval

Use `precedent_refs` to link materially similar prior records. Similarity requires comparable terminal action, hard-gate exposure, data sensitivity, reversibility, and control pattern. A precedent informs consistency but never overrides current evidence.

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

# Appeals and material change assessments
jq -r 'select((.appeals | length) > 0 or (.change_assessments | length) > 0) | "\(.workflow_id) appeals=\(.appeals|length) changes=\(.change_assessments|length)"' *.json

# Value metrics
jq -r '"\(.workflow_id) assessment_min=\(.value_metrics.assessment_minutes) handoff_hours=\(.value_metrics.time_to_approved_handoff_hours) recertification=\(.value_metrics.recertification_compliant)"' *.json
```

Do not delete prior packet versions or dispositions. Append history and retain records according to the organization's stated policy.
