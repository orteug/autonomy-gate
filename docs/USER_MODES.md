# User Modes

Use five primary commands for normal work. Describe facts in plain language; do not choose a template or translate packet fields.

## 1. ASSESS

Use for a new workflow.

```text
ASSESS
Every Monday an operations analyst exports CRM and analytics data, checks that both exports cover the same reporting period, and produces an internal KPI narrative. A human reviews and posts it. If the narrative is wrong, it can be corrected before posting. The workflow has no system write access.
```

The Gate returns the intake snapshot, autonomy decision, architecture options, completed artifact, handoff status, and exact next action.

## 2. RESOLVE EVIDENCE

Use when the pack names missing organizational facts.

```text
RESOLVE EVIDENCE for Weekly KPI Narrative, packet v1
The output owner is the operations lead. The approved retention policy is 12 months. The error-rate threshold is 2 percent per monthly review.
```

The Gate records the facts as `STATED`, creates a new packet version, reruns affected rules, and invalidates any stale selection or disposition when material content changes.

## 3. SELECT ARCHITECTURE

Use after the Gate generates architecture options. This is the operator-facing selection action within the `COMPARE_ARCHITECTURE` lifecycle mode.

```text
SELECT ARCHITECTURE for Weekly KPI Narrative, packet v1
Select OPT-1. Selected by Operations owner on 2026-06-12. We accept the stated operating and maintenance burden.
```

The option ID must already exist. The Gate does not select on the operator's behalf. A material tool substitution later triggers review and may invalidate this selection.

## 4. APPROVE

Use only after the selected architecture and Build Handoff Pack are `BUILD_READY`.

```text
APPROVE_FOR_BUILD for Weekly KPI Narrative, packet v1
Approved by Operations owner on 2026-06-12. The terminal action, controls, selected architecture, complete files, and acceptance tests match the intended workflow.
```

To hold, revise, or reject, begin with `HOLD_FOR_EVIDENCE`, `REVISE`, or `REJECT` and state the packet version, identity or role, date, and rationale. The Gate never records approval without those facts.

## 5. REVIEW BUILD

Use when implementation differs from the approved pack or before activation.

```text
REVIEW BUILD for Weekly KPI Narrative, packet v1
The builder added direct Slack posting. Compare this change with the authorized terminal action and controls.
```

The Gate returns `IN_SCOPE` or `OUT_OF_SCOPE`, identifies the boundary crossed, and states whether a new packet version and disposition are required.

## Advanced Modes

These remain available without expanding the first-use path:

| Mode | Use |
|---|---|
| `TRIAGE` | Preliminary assessment without a full handoff pack |
| `REVISE` | Correct a specific packet field or assessment conclusion |
| `RECERTIFY` | Reassess after an expiration trigger |
| `EXPLAIN` | Explain a rule, gate, verdict, or status without changing state |
| `CONFIGURE` | Supply attributable organization or technology-stack facts |

## Every State-Changing Response

The artifact always states:

```text
Current state
What the Gate completed
What is blocked
Who acts next
Exact next action
```

The durable workflow record, not conversation memory, remains the source of truth.
