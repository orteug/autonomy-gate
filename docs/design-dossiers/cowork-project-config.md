# Design Dossier — Cowork Project Config

**Artifact type:** Cowork Project Config  
**Verdict:** AUTONOMOUS  
**Architecture pattern:** Scheduled local-file or connector workflow  
**Status:** Undesigned — needs full layout treatment

---

## What This Document Is

The Cowork Project Config is the execution artifact the Gate produces when a workflow runs on a scheduled, unattended basis using Claude Cowork. It tells the builder exactly how to configure the Cowork project: what folders to create, what the run schedule is, what the step sequence is, and what controls apply. The operator approves this document to authorize the build.

It is always AUTONOMOUS verdict — if human approval is required before execution, the document type switches to a Control Plan.

---

## Non-Negotiable Sections (in document order)

### 1. Document Header

Must display at the top of the document:
- Document type label: `COWORK PROJECT CONFIG`
- Workflow name
- Verdict: `AUTONOMOUS`
- Architecture pattern: `Scheduled workflow architecture`
- Confidence level: `HIGH`, `MEDIUM`, or `LOW`

The verdict and document type must be immediately identifiable.

### 2. Narrative Description

One paragraph. Must state:
- What this workflow does inside Cowork
- What it reads and what it writes
- How it runs on schedule without human initiation
- The terminal action explicitly named
- Why no GATE conditions trigger (i.e., why AUTONOMOUS is correct)
- If Cowork is unavailable, the fallback surface named

### 3. LOCAL FOLDER STRUCTURE

A visual folder tree showing the required directory layout. Must show:
- `/inputs` — what lands here and from where (source system, file format, naming convention)
- `/outputs` — what the operator writes (format, naming, retention period)
- `/logs` — what is recorded on every run (minimum: timestamp, run ID, terminal status, input count, output location, errors)

This section must be visually distinct — it is a technical spec a builder copies verbatim.

### 4. SCHEDULED TASK

Four required fields displayed together as a compact block:
- `Frequency` — e.g., Daily / Weekly / specific schedule
- `Trigger condition` — cron expression or event trigger
- `Expected runtime` — approximate duration per run
- `Run window` — time of day or day of week acceptable for execution

### 5. EXECUTION SEQUENCE

Numbered list. Each item must show three things:
1. Action
2. System or folder where the action executes
3. Output produced by that step

The last item in the list is always the terminal action. It must match the terminal action stated in the Autonomy Decision Packet. No exceptions.

### 6. AUTHORIZED ACTIONS

Bulleted list. What the operator is explicitly authorized to do. Every bullet is specific — not goals, not outcomes, but specific permitted actions. Minimum permission principle applies.

### 7. PROHIBITED ACTIONS

Bulleted list. What the operator may not do under any condition. Every Cowork Config must list at least three prohibited actions. This list is a hard stop — not guidelines.

### 8. FALLBACK IF COWORK IS UNAVAILABLE

Required section. Names:
- The nearest alternative surface (typically Claude Project)
- The specific adjustments required to run manually on that fallback surface (at least three adjustments)

### 9. INFORMATION GAPS *(conditional)*

Present only if more than three fields were inferred rather than stated in the operator's workflow description. Shows: field name, what was inferred, what evidence would confirm it. May be omitted if gaps are three or fewer.

### 10. EXPECTED OUTCOMES

Five terminal states, each with a specific description for this workflow:
- `Completed`
- `Completed with warnings`
- `Needs review`
- `Blocked`
- `Failed`

Plus the valid terminal status list:
`COMPLETED · COMPLETED_WITH_WARNINGS · NEEDS_REVIEW · BLOCKED · FAILED · SKIPPED · TIMED_OUT`

### 11. AUTONOMY EXPIRES WHEN

Seven checkbox conditions. Must be presented as a checklist. Each condition is marked applicable or not applicable with rationale. Do not omit any condition.

1. Workflow steps, inputs, or outputs change materially
2. AI surface or tool changes (Cowork version, model, connector)
3. Policy or compliance context changes
4. An incident occurs
5. Error rate exceeds threshold
6. Recertification interval passes
7. Reviewer role changes or becomes vacant *(always Not applicable for AUTONOMOUS — no reviewer)*

### 12. ARCHITECTURE OPTIONS

Required block showing all evaluated implementation options. Each option (`OPT-1`, `OPT-2`, etc.) must display these ten fields:
1. Execution architecture
2. Builder surface
3. Control fit
4. Implementation effort
5. Operating cost
6. Maintenance burden
7. Security fit
8. Portability
9. Skill requirements
10. Source evidence

Options not presented must be listed under `Omitted option classes` with an evidence-based reason.

After all options, three selection fields:
- `Selected option`
- `Selection by`
- `Selection date`

### 13. BUILD HANDOFF PACK

Contains these 20 fields in order. Every field must be present — no omissions:

1. Handoff status *(BUILD_READY or BLOCKED_FOR_EVIDENCE)*
2. Terminal-action boundary
3. Architecture decision record
4. Permissions and credentials
5. Deterministic controls
6. Human checkpoints
7. Prohibited actions
8. Logging and audit
9. Failure, rollback, and stop behavior
10. Deployment sequence
11. Assumptions
12. Unresolved dependencies
13. Expiration and reassessment triggers
14. Version invalidation triggers
15. Tool alternatives
16. Builder acknowledgement
17. Current state
18. What the Gate completed
19. What is blocked
20. Who acts next + Exact next action

Must also include: complete folder tree, complete project instructions, run trigger, terminal-status log format, failure behavior, and one non-production acceptance run. No brackets or placeholders in the final output.

### 14. OPERATOR DISPOSITION

Always the last section. Always four unselected checkboxes:
- `[ ] APPROVE_FOR_BUILD`
- `[ ] REVISE`
- `[ ] HOLD_FOR_EVIDENCE`
- `[ ] REJECT`

Gate may recommend but may never pre-select `APPROVE_FOR_BUILD`.

Four operator-filled fields: Name / role, Date, Packet version, Rationale.

---

## Structural Notes for Design

- The folder tree in LOCAL FOLDER STRUCTURE is a technical element — it must render in a fixed-width / monospace treatment
- SCHEDULED TASK reads as a compact key-value grid (4 rows, 2 columns)
- EXECUTION SEQUENCE is a numbered pipeline — each row has three columns (action / system / output)
- AUTHORIZED ACTIONS and PROHIBITED ACTIONS are visually parallel bullet lists — consider adjacent or sequential layout so the contrast between permitted and prohibited is immediate
- ARCHITECTURE OPTIONS is the longest section — each OPT-N block has 10 fields. The selected option needs a clear visual indicator (the primary option treatment from the existing artifact design applies here)
- BUILD HANDOFF PACK is 20 fields — same structure as the Project Setup Brief handoff pack; same layout treatment applies

---

## Verdict Color

`AUTONOMOUS` — `#1F6B4A`

All accent elements for this document use this color.
