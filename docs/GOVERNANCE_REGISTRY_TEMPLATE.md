# Governance Registry Template

Use this when running The Autonomy Gate across multiple workflows.

The registry is the portfolio view. Each Gate run produces one row.

---

## Registry Table

| Field | Description |
|---|---|
| Workflow ID | Unique ID, e.g. `WF-001` |
| Workflow name | Plain-language name |
| Business owner | Accountable human |
| Process owner | Person who maintains the workflow |
| Date assessed | Gate run date |
| Autonomy verdict | AUTONOMOUS, SUPERVISED, SOP_FIRST, HUMAN_ONLY |
| Surface verdict | PROJECT, COWORK, CODE_AGENT, NO_AI |
| Confidence | HIGH, MEDIUM, LOW |
| Terminal action | Last thing the workflow executes |
| Gate conditions | GATE-1 through GATE-5 if any |
| Artifact | Link or filename |
| Reviewer | Required for SUPERVISED |
| Controls required | Summary of required controls |
| Evidence gaps | Missing fields |
| Current status | Proposed, approved, active, paused, retired |
| Recertification date | Next required review |
| Expiration triggers | Conditions that invalidate verdict |
| Incident history | Link to incidents or notes |
| Last reviewed by | Human reviewer |
| Notes | Additional context |

---

## Markdown Registry

```markdown
| ID | Workflow | Owner | Verdict | Surface | Confidence | Terminal action | Artifact | Status | Recertification |
|---|---|---|---|---|---|---|---|---|---|
| WF-001 | Weekly KPI Report | Ops Lead | AUTONOMOUS | PROJECT | HIGH | Slack-ready report produced in session | Project Setup Brief | Active | 2026-12-01 |
| WF-002 | Vendor Bank Change | Controller | HUMAN_ONLY | NO_AI | HIGH | Payment routing change authorized | Governance Memo | Human-owned | 2026-12-01 |
| WF-003 | Refund Under $50 | Support Lead | SUPERVISED | CODE_AGENT | MEDIUM | Refund issued | Control Plan | Build pending | 2026-09-01 |
```

---

## CSV Header

```csv
workflow_id,workflow_name,business_owner,process_owner,date_assessed,autonomy_verdict,surface_verdict,confidence,terminal_action,gate_conditions,artifact,reviewer,controls_required,evidence_gaps,current_status,recertification_date,expiration_triggers,incident_history,last_reviewed_by,notes
```

---

## Status Definitions

| Status | Meaning |
|---|---|
| Proposed | Gate run completed but no implementation decision made. |
| Approved | Artifact approved for setup. |
| Active | Workflow is running under the Gate verdict. |
| Paused | Expiration trigger or incident requires reassessment. |
| Blocked | Missing owner, reviewer, evidence, or tool access. |
| Retired | Workflow no longer runs. |

---

## Running An Ops Audit

Use this sequence when assessing a backlog of workflows for the first time.

1. **Submit all candidates first.** Collect all verdicts before building anything. Running the Gate on your full backlog produces the portfolio view — you need that before deciding where to invest implementation effort.
2. **Sort by verdict type.** `HUMAN_ONLY` and `LOW` confidence verdicts go to the top of the priority list for review. These either cannot be automated or lack enough information to govern safely.
3. **SOP_FIRST verdicts form the documentation backlog.** Do not attempt to build these. Assign a process owner and a documentation milestone to each. This queue is the foundation work.
4. **SUPERVISED verdicts are the immediate build queue.** Each requires reviewer designation and checkpoint implementation before deployment.
5. **AUTONOMOUS verdicts are the deployment queue.** Implement controls, then deploy in order of business value.

Recommended columns when tracking the audit:

| Group | Action |
|---|---|
| `HUMAN_ONLY` | Confirm a documented human process exists for each |
| `LOW` confidence | Assign an owner to collect the named evidence gaps |
| `SOP_FIRST` | Assign process owner and documentation deadline |
| `SUPERVISED` | Name reviewer, confirm checkpoint is real, confirm audit trail |
| `AUTONOMOUS` | Implement controls, set recertification date, deploy |

---

## Recertification Cadence By Surface

Set a calendar reminder before deploying any governed workflow.

The intervals below are **illustrative administrative defaults**, not policy requirements. Terminal consequence level, incident history, regulatory requirements, and control strength all affect the appropriate cadence for a specific workflow. The artifact's own AUTONOMY EXPIRES WHEN section takes precedence over these defaults.

| Surface | Illustrative interval |
|---|---|
| `AUTONOMOUS / CODE_AGENT` | Every 6 months |
| `AUTONOMOUS / COWORK` | Every 6 months |
| `AUTONOMOUS / PROJECT` | Annually — lower-risk surface; human-initiated |
| `SUPERVISED` (any surface) | Every 6 months, plus immediately on any reviewer change |
| `SOP_FIRST` | Re-assess when the stabilization checklist is complete |

Adjust to your organization's risk tolerance, the specific failure consequence level named in the artifact, and any applicable policy requirements.

When the recertification date arrives, re-submit the workflow description to the Gate. If nothing material has changed and no incidents have occurred, the verdict will likely be the same. The recertification run produces an updated artifact with an updated expiration date. Replace the old artifact in the registry.

---

## Weekly Review

Each week, review:

- workflows with LOW confidence
- workflows with missing reviewers
- workflows past recertification date
- workflows with incidents
- workflows whose surface is unavailable

---

## Quarterly Review

Each quarter, ask:

1. Are any AUTONOMOUS workflows stale?
2. Are any SUPERVISED reviewers overloaded?
3. Are any SOP_FIRST items stuck?
4. Are HUMAN_ONLY processes documented?
5. Did any model, platform, policy, or system change?
6. Did any workflow drift from its original description?

---

## Registry Rules

- One row per workflow verdict.
- Split workflows get multiple rows.
- HUMAN_ONLY terminal actions stay in the registry.
- Do not delete old verdicts. Mark them retired or superseded.
- Every active workflow needs a recertification date.

