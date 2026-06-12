# Workflow Architecture Contract

The Workflow Architecture Contract defines the structure a workflow specification must satisfy before a Build Handoff Pack is issued. It is a technology-neutral blueprint: it names required capability categories and specifies what each must cover, without depending on any named vendor.

The Gate produces architecture specifications that conform to this contract. Builders implement the specification using tools from the organization's technology stack.

---

## Contract Structure

A complete workflow architecture specification covers seven sections. All seven must be present in a `BUILD_READY` Build Handoff Pack. An unanswered required field produces `BLOCKED_FOR_EVIDENCE`.

---

### Section 1 — Workflow Identity

```
Workflow name:          [human-readable name]
Workflow ID:            [identifier for version tracking — format: WF-YYYYMMDD-NNN]
Packet version:         [v1, v2, ... — matches the Autonomy Decision Packet version]
Autonomy verdict:       [AUTONOMOUS / SUPERVISED / SOP_FIRST / HUMAN_ONLY]
Assessment surface:     [where the Gate ran — Claude Project | ChatGPT Project | other]
Execution architecture: [how the workflow runs in production — technology-neutral description]
Builder surface:        [who implements this — Claude Code | Codex | internal engineering | low-code specialist | platform administrator]
```

**Assessment surface** is where the Gate decision was made. **Execution architecture** is how the workflow runs in production. **Builder surface** is who receives this handoff pack and implements it. These are three distinct roles that may or may not share a platform.

---

### Section 2 — Workflow Mechanics

```
Trigger:                [what initiates the workflow — schedule, event, webhook, human request, API call]
Actors:                 [who or what participates — AI, human approver, system, scheduler]
Inputs:
  - Source:             [where data comes from]
  - Format:             [structure, schema, or format of input data]
  - Data classification:[public | internal | confidential | regulated | PII]
  - System of record:   [which system owns this data]
Transformations:
  - Deterministic rules:[logic that must not depend on model judgment — validation, routing, thresholds]
  - AI reasoning steps: [where model judgment is applied — analysis, summarization, classification]
Outputs:
  - Format:             [structure, schema, or format of output]
  - Destination:        [where output is delivered]
  - Terminal action:    [the last thing that executes — matches packet terminal action field]
```

**Deterministic rules must be implemented as code or configuration, not model prompts.** Controls — approval thresholds, prohibited action lists, schema validation — are not trusted to model judgment.

---

### Section 3 — Autonomy Operating Pattern

The autonomy operating pattern names how AI authority and human authority are divided across the workflow's steps.

**For AUTONOMOUS workflows:**

```
Pattern:               FULLY_AUTONOMOUS
Human involvement:     Initiation only (or scheduled — no human in the run)
AI authority:          Full execution authority within stated scope
Boundaries:            [what the AI may and may not do — named explicitly]
Terminal action:       [executed without human checkpoint]
```

**For SUPERVISED workflows:**

```
Pattern:               HUMAN_IN_THE_LOOP
Human involvement:     Review and approval before terminal action
AI authority:          Preparation only — AI does not execute the terminal action
Approval checkpoint:   [blocking step — workflow halts here until human approves]
Approval method:       [how the human approves — reply, button, form, signature]
Approval timeout:      [what happens if no response — escalate, cancel, alert]
```

**For SOP_FIRST or HUMAN_ONLY workflows:**

```
Pattern:               HUMAN_ONLY
Human involvement:     All steps
AI authority:          None (SOP_FIRST: pending documentation) or None (HUMAN_ONLY: permanent)
Gate recommendation:   [what the operator should do before reconsidering automation]
```

---

### Section 4 — Control Architecture

Controls are the conditions under which the verdict was issued. They are not optional. If a listed control cannot be implemented, the workflow should not run at the current verdict level.

```
Required controls:
  - [Control 1]: [implementation requirement]
  - [Control 2]: [implementation requirement]
  ...

Prohibited actions:
  - [The workflow may not ...]
  - [The workflow may not ...]

Approval checkpoint (if SUPERVISED):
  - Trigger:            [when checkpoint activates]
  - Blocking mechanism: [how the workflow halts]
  - Approver:           [role or system that approves]
  - Approval criteria:  [what the approver evaluates]
  - Rejection handling: [what happens if rejected]

Audit requirements:
  - Log each:           [events that must be logged]
  - Retain for:         [retention period]
  - Access:             [who can review logs]

Error handling:
  - On validation failure: [halt | escalate | retry with backoff]
  - On AI output failure:  [halt | fallback | escalate]
  - On timeout:            [cancel | escalate | alert]
  - On partial failure:    [rollback | compensate | halt and alert]
```

**Deterministic enforcement:** Controls that the organization relies on for governance must be implemented in deterministic code or configuration — not in a model prompt. A model prompt is guidance, not enforcement.

---

### Section 5 — Execution Paths

```
Standard path:
  Step 1: [description — actor, action, output]
  Step 2: [description — actor, action, output]
  ...
  Terminal: [final action]

Exception paths:
  - [Exception condition]: [handling — escalate | halt | retry | fallback]
  - [Exception condition]: [handling]

Idempotency:
  - Duplicate prevention: [how duplicate triggers are detected and handled]
  - Retry safety:         [whether steps are safe to retry; which are not]

Rollback:
  - Trigger condition:    [when rollback is initiated]
  - Rollback steps:       [what is undone and in what order]
  - Rollback limit:       [what cannot be rolled back — named explicitly]
```

---

### Section 6 — Data and Security

```
Data flows:
  - [System A] → [System B]: [data type, classification, volume]

Credentials and access:
  - [System]: [access pattern — OAuth, API key, service account]
  - Minimum permissions: [least-privilege principle — named permissions only]
  - Secrets storage:     [approved secrets management mechanism]

Data handling:
  - PII/regulated data:  [how it is handled, masked, or excluded]
  - Retention:           [how long data is held at each stage]
  - Deletion:            [when and how data is purged]

Observability:
  - Logs:                [what is logged at each step]
  - Metrics:             [what is measured — latency, error rate, volume]
  - Alerts:              [conditions that trigger operator notification]
  - Incident response:   [who to notify and how if the workflow produces an unexpected outcome]
```

---

### Section 7 — Acceptance Criteria

```
Functional acceptance:
  - Given [normal inputs], the workflow produces [expected output]
  - Given [edge case], the workflow [correct behavior]

Failure injection:
  - Given [invalid input], the workflow [rejects or halts correctly]
  - Given [system unavailable], the workflow [fails safely]

Security tests:
  - Verify prohibited actions cannot be triggered by any input
  - Verify approval checkpoint cannot be bypassed
  - Verify credentials are not exposed in logs

Operator acceptance:
  - The terminal action is identical to the packet terminal action
  - The approval checkpoint (if SUPERVISED) is blocking and cannot be skipped
  - All required controls from the packet are implemented and verifiable
  - The workflow halts within stated error conditions
  - Audit log is generated and retained per requirements
```

---

## Architecture-First Rule

The workflow architecture is agreed before tool selection. The Gate produces architecture specifications in technology-neutral terms first. Tool selection occurs after:
1. The operator confirms the architecture is correct
2. The organization's technology stack profile is applied
3. Tools are matched to required capabilities

A workflow specification that names a specific product before the architecture is agreed is incomplete. Product names are implementation details — capabilities are the contract.

## Required Alternatives

Before selection, compare five option classes when viable: primary, native-suite, low-code, code-first, and vendor-neutral. Each option states execution architecture, builder surface, control fit, implementation effort, operating cost, maintenance burden, security/compliance fit, portability, skill requirements, and source evidence. An option class may be omitted only with an evidence-based reason. The operator records the selected option; no pack is `BUILD_READY` before that selection.

### Canonical Architecture Options Block

Every `AUTONOMOUS` and `SUPERVISED` artifact places this block immediately before `BUILD HANDOFF PACK`. Repeat the option section for every viable class. Account for every absent class under `Omitted option classes` with an evidence-based reason.

```
ARCHITECTURE OPTIONS
### OPT-1 — PRIMARY
**Execution architecture:** [capability-first production design]
**Builder surface:** [implementation owner or builder]
**Control fit:** [deterministic enforcement of required controls]
**Implementation effort:** [relative effort and dependencies]
**Operating cost:** [grounded cost information or named evidence gap]
**Maintenance burden:** [ownership and recurring operational work]
**Security fit:** [identity, permissions, data, and compliance fit]
**Portability:** [switching constraints and export path]
**Skill requirements:** [build and operating skills]
**Source evidence:** [official source and verification date for named-tool claims, or technology-neutral basis]

Omitted option classes:
- NATIVE_SUITE — [evidence-based reason, when omitted]
- LOW_CODE — [evidence-based reason, when omitted]
- CODE_FIRST — [evidence-based reason, when omitted]
- VENDOR_NEUTRAL — [evidence-based reason, when omitted]

Selected option: [generated option ID or NOT_SELECTED]
Selection by: [operator identity or role, or NOT_RECORDED]
Selection date: [ISO date or NOT_RECORDED]
```

The canonical classes are `PRIMARY`, `NATIVE_SUITE`, `LOW_CODE`, `CODE_FIRST`, and `VENDOR_NEUTRAL`. Every generated option includes all ten labeled comparison fields. The Gate may recommend `PRIMARY`, but only the operator may record `Selected option`, `Selection by`, and `Selection date`. Until a generated option is selected, the handoff is `BLOCKED_FOR_EVIDENCE`.

Tool substitution preserves the autonomy verdict and terminal-action boundary. A substitute is acceptable only when verified capabilities satisfy the same controls and organizational constraints. A change to permissions, data flow, approval enforcement, audit behavior, rollback, security posture, or operating burden requires operator review and reassessment under `tool-selection-rules.md`.

---

## Technology-Neutral Architecture Descriptions

When the technology stack profile is absent or incomplete, architecture components are described by required capability, not by product name:

| Instead of | Write |
|-----------|-------|
| "Use GitHub Actions for scheduling" | "A scheduler that triggers the workflow at the defined interval" |
| "Use Workato to move data from Salesforce to Slack" | "An integration mechanism that reads from the CRM system and delivers to the messaging platform" |
| "Use OpenAI GPT-4 for analysis" | "A language model capable of the named reasoning task, accessed via the organization's approved AI provider" |
| "Use Postgres for the audit log" | "A persistent data store for audit records, retained for the defined period" |

When the stack profile is present, the Gate substitutes named tools where they satisfy the required capability and are within the approved set.
