# Verdict Playbook

Use this after every Gate run.

The question this playbook answers:

```text
The Gate gave me a verdict. What do I do now?
```

---

## Quick Routing Table

| Verdict | Artifact | Next action |
|---|---|---|
| `AUTONOMOUS / PROJECT` | Project Setup Brief | Create a workflow-specific Project. |
| `AUTONOMOUS / COWORK` | Cowork Project Config | Configure folders, schedule, permissions, and logs. |
| `AUTONOMOUS / CODE_AGENT` | Automation Architecture | Build or hand to Claude Code/Codex. |
| `SUPERVISED / PROJECT` | Control Plan | Create Project plus human approval checkpoint. |
| `SUPERVISED / COWORK` | Control Plan | Configure Cowork run plus blocking review step. |
| `SUPERVISED / CODE_AGENT` | Control Plan | Implement approval gate in code before terminal action. |
| `SOP_FIRST / NO_AI` | Stabilization Plan | Document and stabilize the process before automation. |
| `HUMAN_ONLY / NO_AI` | Governance Memo | Keep terminal action human-owned. |

---

## AUTONOMOUS / PROJECT

### Meaning

AI can complete the workflow inside a human-initiated Project session without a human approval checkpoint inside the run.

### Allowed

- Human starts the session.
- User provides needed data or documents.
- AI analyzes, formats, summarizes, compares, or drafts.
- AI produces a document, table, memo, or Slack-ready text.

### Not Allowed

- Self-scheduling
- External API calls
- Direct Slack posting
- Direct CRM updates
- File writes to local disk
- Production system changes

### Required Action

1. Read the Project Setup Brief.
2. Create a new workflow-specific Project.
3. Paste the custom instructions.
4. Upload the named knowledge files.
5. Run one test with non-critical data.
6. Save the output and log the run.

### Expiration Triggers

Re-run the Gate if:

- data sources change
- output format changes
- model or platform changes
- a report error affects a decision
- recertification date arrives

---

## AUTONOMOUS / COWORK

### Meaning

AI can run the workflow without per-run approval on a scheduled or file-based surface, if Cowork is available and configured.

### Allowed

- Scheduled trigger
- Folder-based input/output
- Local file handling inside scoped folders
- Terminal status logging
- Internal reversible outputs

### Not Allowed

- Expanding folder scope without reassessment
- Skipping logs
- Touching systems not listed in the artifact
- Executing any action blocked in the artifact

### Required Action

1. Read the Cowork Project Config.
2. Create the folder structure.
3. Configure run cadence.
4. Set allowed and prohibited actions.
5. Test with non-production inputs.
6. Confirm terminal status is written for every run.

### If Cowork Is Unavailable

Use the fallback note:

- human starts each run manually
- user pastes data or uploads files
- output is delivered manually
- log is maintained manually

The autonomy level may stay the same, but the execution model changes.

---

## AUTONOMOUS / CODE_AGENT

### Meaning

AI can implement or run deterministic code, scripts, APIs, or integration logic without a human approval checkpoint inside the workflow.

### Allowed

- Read-only API calls
- Scripts
- Deterministic classification
- Test suites
- Structured output
- Audit logs
- Dry-run modes

### Not Allowed

- Scope expansion without reassessment
- Unlogged production writes
- Payments unless specifically allowed by verdict and controls
- Access-control changes
- External publication without required gates

### Required Action

1. Read the Automation Architecture.
2. Create or update `CLAUDE.md` for Claude Code or `AGENTS.md` for Codex.
3. Implement dry-run mode first.
4. Implement audit logging.
5. Implement tests for normal and exception paths.
6. Run non-production validation before live use.

### Important

Instruction files guide behavior. They are not hard runtime enforcement by themselves. For high-consequence workflows, implement code-level blocking controls.

---

## SUPERVISED / PROJECT

### Meaning

AI can prepare the work in a Project, but a human must approve before the terminal action.

### Allowed

- Drafting
- Summarizing
- Preparing review packets
- Comparing against criteria
- Recommending next action

### Not Allowed Without Approval

- Sending external messages
- Publishing
- Issuing decisions
- Updating customer records
- Triggering terminal action

### Required Action

1. Read the Control Plan.
2. Confirm the reviewer is named.
3. Confirm the reviewer has blocking authority.
4. Define approval format.
5. Define timeout behavior.
6. Test with one sample before operational use.

### Failure Mode To Watch

Human-in-the-loop theater.

If the reviewer cannot realistically review or block, the workflow is not supervised. It is uncontrolled.

The four conditions that produce theater:

1. **The reviewer lacks time.** The workflow runs 200 times a week; the reviewer has 4 hours. The checkpoint will be bypassed in practice.
2. **The reviewer lacks criteria.** There is no defined approval standard, so "review" means glancing at it.
3. **The reviewer lacks authority.** The reviewer can flag concerns but cannot actually stop execution.
4. **The reviewer is unavailable.** The named reviewer is on leave, has changed roles, or the role is vacant.

If any of these apply, the checkpoint does not exist. Remedies before deployment:

- Route only exceptions to review — let standard cases proceed, flag borderline ones
- Designate a second reviewer to split the load
- Reduce run cadence until review capacity matches
- Re-scope the workflow so fewer terminal actions require approval

Do not deploy a SUPERVISED workflow without a functioning checkpoint.

---

## SUPERVISED / COWORK

### Meaning

Cowork may prepare or route work, but the terminal action waits for a human approval checkpoint.

### Required Action

1. Configure the Cowork folders.
2. Write outputs to a review folder.
3. Block terminal action until approval is logged.
4. Require reviewer identity in the log.
5. Emit `BLOCKED` if approval is not received in time.

### Not Allowed

- Treating no response as approval
- Letting the workflow continue after timeout
- Burying warnings in logs only

---

## SUPERVISED / CODE_AGENT

### Meaning

A code agent can prepare, validate, or stage work, but execution waits for a human checkpoint.

### Required Action

1. Add the packet to `CLAUDE.md` or `AGENTS.md`.
2. Implement a blocking approval state.
3. Require explicit approval artifact.
4. Add tests proving terminal action cannot execute before approval.
5. Log approval identity, timestamp, and decision.

### Approval Examples

- A file appears in `/approvals/approved-[run-id].json`
- A PR comment from named reviewer says `APPROVED FOR EXECUTION`
- A signed internal ticket is moved to approved status

Approval must be explicit.

---

## SOP_FIRST / NO_AI

### Meaning

The workflow is not ready for AI authority.

This is not a failure. It is the correct automation decision when process knowledge is missing.

### Required Action

1. Assign a process owner.
2. Complete the Stabilization Plan.
3. Document standard path.
4. Document exception paths.
5. Define failure handling.
6. Run manual cycles to establish baseline.
7. Re-run the Gate.

### Not Allowed

- Automating only the "happy path" while ignoring exceptions
- Treating undocumented judgment as model judgment
- Creating an automation before the team can explain the process

---

## HUMAN_ONLY / NO_AI

### Meaning

The terminal action cannot be delegated to AI.

Common reasons:

- irreversible external commitment
- access control change
- unbounded consequence
- required human legal/financial/security authority

### Required Action

1. Read the Governance Memo.
2. Keep the terminal action human-owned.
3. Document the human review process.
4. Identify whether preparation steps can be split into a separate workflow.
5. Re-submit only the preparation phase if appropriate.

### Important

HUMAN_ONLY does not always mean AI cannot assist.

It means AI cannot own the terminal action.

Example:

```text
AI may prepare a vendor verification packet.
AI may not authorize the payment routing change.
```

### The Decomposition Pattern

Most HUMAN_ONLY workflows contain a preparation phase that can receive a different verdict when submitted separately.

The split:

- **Phase 1 — Preparation:** compile data, analyze, format, flag anomalies, produce a review-ready package. Re-submit this as its own workflow. It will likely receive `SUPERVISED / PROJECT` or `SUPERVISED / CODE_AGENT`.
- **Phase 2 — Terminal action:** the specific step that triggered GATE-2 or GATE-3. This stays HUMAN_ONLY. It is not submitted again — it is implemented as a human process with the Governance Memo as the SOP.

The two phases are implemented separately. The higher-restriction verdict governs only the terminal action of its phase. AI can own Phase 1. A human owns Phase 2.

