# Design Dossier — Automation Architecture

**Artifact type:** Automation Architecture  
**Verdict:** AUTONOMOUS  
**Architecture pattern:** Code-first, service, or integration  
**Status:** Undesigned — needs full layout treatment

---

## What This Document Is

The Automation Architecture is the execution artifact the Gate produces when a workflow is implemented as code — a script, a service, an integration, an API-driven pipeline. It tells the builder what to build: the trigger mechanism, the input sources, the step sequence, the output destinations, the error handling, the required controls, and the recommended stack. The operator approves this document to authorize the build.

Like the Cowork Config, the Automation Architecture always carries an AUTONOMOUS verdict. The difference is implementation surface: Cowork is a no-code scheduled tool; Automation Architecture is for anything that requires code or a development environment.

---

## Non-Negotiable Sections (in document order)

### 1. Document Header

Must display at the top:
- Document type label: `AUTOMATION ARCHITECTURE`
- Workflow name
- Verdict: `AUTONOMOUS`
- Architecture pattern: `Code-first architecture`
- Confidence level: `HIGH`, `MEDIUM`, or `LOW`

### 2. Narrative Description

One paragraph. Must state:
- What this workflow does
- Why it qualifies for autonomous execution (all four autonomy criteria passed, no gate triggered)
- What the operator is authorized to do
- The terminal action explicitly named
- The evidence that justifies AUTONOMOUS

### 3. TRIGGER

Single-section callout. Names exactly what initiates execution:
- Schedule (cron expression)
- Event (webhook endpoint, named event type)
- File change (file path pattern)
- API call (endpoint and method)
- System event (named system and condition)

"When needed" or "on demand" are not valid entries. The trigger must be specific enough to implement.

This is functionally the entry point of the pipeline and should receive visual treatment that reflects that — it starts the whole sequence.

### 4. INPUTS

Table. One row per input source. Three columns:
- System name
- Data accessed
- Permission level required

Minimum permission principle applies — only what this specific workflow requires.

### 5. EXECUTION SEQUENCE

Numbered pipeline. Each step must show three things:
1. Action
2. System where the action executes
3. Output produced by that step

The last step is always the terminal action. It must match the terminal action named in the Autonomy Decision Packet. No exceptions.

This is visually similar to the Cowork Config's EXECUTION SEQUENCE but the system column references code environments, APIs, and services rather than local folders.

### 6. OUTPUTS

Required section. Must name:
- Where results go (specific destination: Slack channel, folder path, database table, email address, S3 bucket — not "output location")
- Format of the output
- Naming convention
- Retention period

### 7. ERROR HANDLING

Required section. Not optional even if the workflow description omits it. Must state:
- What happens on failure at each step (or the critical steps)
- Rollback procedure if applicable
- Who is alerted, on what channel, within what timeframe

"Errors are logged" is not a sufficient entry. The section must name where errors are logged and who checks them.

### 8. AUDIT TRAIL

Required fields for every run's log entry:
- Timestamp
- Trigger source
- Input record count
- Output location
- Terminal status
- Any anomalies detected

Plus: where the log is stored, retention period.

### 9. CONTROLS

Bulleted checklist of requirements that must be satisfied before deployment. Always at least:
- Audit log configured and tested
- Rollback procedure documented and tested
- Error alert routed to named owner
- Permission scope limited to minimum required

These are pre-deployment gates, not runtime behavior.

### 10. RECOMMENDED STACK

Single recommendation with rationale. Names the specific tool or technology (e.g., Claude Code / Make / Zapier / n8n / custom Python service) and explains why it fits this workflow. Includes what the operator needs to set up before first run.

This is a callout — one clean recommendation, not a comparison table.

### 11. INFORMATION GAPS *(conditional)*

Same as all other artifact types — present only if more than three fields were inferred.

### 12. EXPECTED OUTCOMES

Five terminal states:
- `Completed`
- `Completed with warnings`
- `Needs review`
- `Blocked`
- `Failed`

Valid terminal status list:
`COMPLETED · COMPLETED_WITH_WARNINGS · NEEDS_REVIEW · BLOCKED · FAILED · SKIPPED · TIMED_OUT`

### 13. AUTONOMY EXPIRES WHEN

Seven checkbox conditions. Each marked applicable or not applicable with rationale.

1. Workflow steps, inputs, or outputs change materially
2. AI surface or tool changes (model upgrade, platform migration)
3. Policy or compliance context changes
4. An incident occurs
5. Error rate exceeds threshold
6. Recertification interval passes
7. Reviewer role changes or becomes vacant *(always Not applicable — AUTONOMOUS has no approval checkpoint)*

### 14. ARCHITECTURE OPTIONS

Same structure as all artifact types. Each option displays 10 fields:
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

Omitted classes listed with reasons. Selection metadata: Selected option / Selection by / Selection date.

### 15. BUILD HANDOFF PACK

Same 20-field structure as all artifact types. For Automation Architecture specifically, this pack must also include:
- Complete `CLAUDE.md` configuration block (for Claude Code workflows)
- Complete `AGENTS.md` configuration block (for Codex workflows)
- Dry-run procedure
- One acceptance test

Fields in order:
1. Handoff status
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

### 16. OPERATOR DISPOSITION

Always last. Always unselected:
- `[ ] APPROVE_FOR_BUILD`
- `[ ] REVISE`
- `[ ] HOLD_FOR_EVIDENCE`
- `[ ] REJECT`

Operator fills: Name / role, Date, Packet version, Rationale.

---

## Structural Notes for Design

- TRIGGER is the entry point of the pipeline — it deserves a distinct visual treatment that reads as "this is where it starts." A single prominent callout or header block, not a field in a table.
- INPUTS is a three-column table — it can be compact since each row is short
- EXECUTION SEQUENCE mirrors the Cowork Config's sequence treatment — numbered rows, three columns (action / system / output). The system column will reference API endpoints, file paths, and code environments rather than local folders.
- OUTPUTS and ERROR HANDLING are prose sections with embedded specifics — no special layout needed beyond clear headers
- CONTROLS reads as a pre-deployment checklist — distinct from the PROHIBITED ACTIONS style because these are setup gates, not runtime prohibitions
- RECOMMENDED STACK is a single-recommendation callout — visually distinct from the architecture options grid. One tool, one rationale, one setup note.
- ARCHITECTURE OPTIONS and BUILD HANDOFF PACK: same layout treatment as the Project Setup Brief

---

## Verdict Color

`AUTONOMOUS` — `#1F6B4A`

All accent elements for this document use this color.
