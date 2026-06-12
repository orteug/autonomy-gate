# Workflow Governance Registry

The registry tracks every workflow that has been assessed by The Autonomy Gate. One record per workflow. Each record is a portable JSON file conforming to `workflow-record.schema.json`.

## Purpose

The registry answers the operational question: *"What autonomy have we granted, why, and when does it expire?"*

It is not a database. Each workflow record is a standalone file that can be read by a human, searched by a script, or attached to a governance report.

## File Naming

```
WF-YYYYMMDD-NNN.json
```

Example: `WF-20260611-001.json`

The `workflow_id` in the file must match the filename.

## Status Lifecycle

```
ASSESSED → APPROVED_FOR_BUILD → IN_BUILD → VALIDATING → ACTIVE
    ↓              ↓                                        ↓
 BLOCKED       REJECTED                                  EXPIRED
    ↓
APPROVED_FOR_BUILD
```

| Status | Meaning |
|--------|---------|
| `ASSESSED` | Gate has run; disposition pending |
| `BLOCKED` | HOLD_FOR_EVIDENCE or REVISE recorded; awaiting operator action |
| `APPROVED_FOR_BUILD` | APPROVE_FOR_BUILD recorded; builder may proceed |
| `IN_BUILD` | Builder has received the handoff pack and is implementing |
| `VALIDATING` | Implementation complete; operator verifying acceptance criteria |
| `ACTIVE` | Workflow is running in production under the authorized autonomy level |
| `PAUSED` | Workflow suspended; operator action required before resuming |
| `EXPIRED` | Recertification condition triggered; workflow must not run until recertified |
| `REJECTED` | REJECT disposition recorded; workflow closed |

## Quick Queries

**All active autonomous workflows:**
```bash
jq -r 'select(.verdict == "AUTONOMOUS" and .status == "ACTIVE") | "\(.workflow_id) \(.name)"' *.json
```

**Workflows expiring within 30 days:**
```bash
jq -r --arg cutoff "$(date -v+30d +%Y-%m-%d)" \
  'select(.recertification_due != null and .recertification_due <= $cutoff) | "\(.workflow_id) \(.name) expires \(.recertification_due)"' \
  *.json
```

**All workflows needing operator action (BLOCKED or PENDING):**
```bash
jq -r 'select(.status == "BLOCKED" or .disposition == "PENDING") | "\(.workflow_id) \(.name)"' *.json
```

## Monthly Review Input

Run this query to generate the monthly governance summary:
```bash
echo "=== GOVERNANCE REGISTRY SUMMARY ===" && \
echo "Active autonomous:" && jq -r 'select(.verdict == "AUTONOMOUS" and .status == "ACTIVE") | "  \(.workflow_id) \(.name)"' *.json && \
echo "Active supervised:" && jq -r 'select(.verdict == "SUPERVISED" and .status == "ACTIVE") | "  \(.workflow_id) \(.name)"' *.json && \
echo "In build:" && jq -r 'select(.status == "IN_BUILD") | "  \(.workflow_id) \(.name)"' *.json && \
echo "Blocked:" && jq -r 'select(.status == "BLOCKED") | "  \(.workflow_id) \(.name)"' *.json && \
echo "Expired:" && jq -r 'select(.status == "EXPIRED") | "  \(.workflow_id) \(.name)"' *.json
```
