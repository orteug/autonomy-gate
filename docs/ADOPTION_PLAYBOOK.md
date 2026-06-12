# Adoption Playbook — Operator Routines

The Gate becomes useful when it is part of a recurring cadence, not an occasional tool. This playbook defines three routines: daily intake, weekly review, and monthly audit. Each routine takes under 30 minutes and produces a specific output.

---

## Daily Intake Routine

**When:** Any day a new workflow automation request arrives.

**Trigger:** Someone says "can we automate this?" — in a meeting, Slack message, email, or ticket.

**Steps:**

1. **Collect the workflow description.** Ask the requestor: what initiates it, what it does step by step, what systems it touches, what happens if it's wrong, and whether the output can be undone. Encourage 2-3 paragraphs. Do not require a form.

2. **Submit to the Gate (ASSESS mode).** Paste the description into your Gate workspace. Receive the three-section output in one response.

3. **Review the packet.** Check: Is the terminal action correctly identified? Is the verdict reasonable? Is the pack READY or BLOCKED?

4. **Act on the result:**
   - **READY + convinced:** Record `APPROVE_FOR_BUILD`. Forward the Build Handoff Pack to the builder.
   - **BLOCKED:** Submit missing values using RESOLVE_EVIDENCE. Then reassess disposition.
   - **Not convinced:** Record `REVISE`. Specify what needs to change.
   - **HUMAN_ONLY:** Document the decision. Share the Governance Memo with the requestor. Close the automation request.

5. **Save the artifact.** Name it `[WorkflowName]-[YYYY-MM-DD]-v1.md`. File it in your workflow record folder.

**Time budget:** 20-30 minutes for a standard workflow. 45-60 minutes for complex workflows with multiple evidence gaps.

**Output:** A filed governance artifact with operator disposition recorded.

---

## Weekly Review Routine

**When:** Every week, same day (suggested: Friday afternoon or Monday morning).

**Trigger:** Calendar event or weekly team standup.

**Agenda:**

**1. Blocked assessments (5 min)**
- List all workflows in `HOLD_FOR_EVIDENCE` or `REVISE_REQUESTED` state
- For each: is the blocking evidence now available? Who owns it?
- Action: submit evidence updates or escalate to the owner

**2. In-build handoffs (10 min)**
- List all workflows in `IN_BUILD` state
- For each: has the builder submitted a Builder Acknowledgement? Have they encountered any scope changes?
- Action: confirm acknowledgement received; review any scope change requests

**3. Upcoming expirations (5 min)**
- Check AUTONOMY EXPIRES WHEN sections for workflows approaching their recertification interval
- Action: schedule recertification 2 weeks before expiration triggers

**4. New requests in queue (5 min)**
- Triage any workflow descriptions that arrived during the week but haven't been assessed yet
- Action: schedule assessment for each, or decline with rationale

**Time budget:** 20-30 minutes.

**Output:** Updated status for all open workflow records. Any new assessments scheduled.

---

## Monthly Audit Routine

**When:** Last business day of each month.

**Trigger:** Calendar event.

**Agenda:**

**1. Active workflow review (15 min)**
- List all workflows with `ACTIVE` or `IN_BUILD` status
- For each: are the stated controls still in place? Has the workflow operated within the stated exception rate?
- Action: flag any that need recertification or controls review

**2. Incident review (10 min)**
- Were there any errors, unexpected outputs, or near-misses from autonomous workflows this month?
- For each incident: what happened, what workflow was involved, what control failed or was absent?
- Action: determine if a recertification or control update is required

**3. Expired autonomy (5 min)**
- Have any AUTONOMY EXPIRES WHEN conditions triggered?
- Action: initiate recertification for each expired workflow; suspend autonomous operation until recertification is complete

**4. Governance drift check (10 min)**
- Have any builders reported scope changes they handled without returning to the Gate?
- Have any workflows been modified in ways that weren't assessed?
- Action: require new assessments for any unauthorized scope expansions

**5. Monthly summary (5 min)**
- How many workflows were assessed this month?
- How many reached APPROVE_FOR_BUILD?
- How many were rejected or held?
- What is the current count of active autonomous and supervised workflows?

**Time budget:** 40-50 minutes.

**Output:** Monthly governance summary. Any remediation actions assigned.

---

## Meeting-Ready Review Formats

### For Leadership (2-3 minutes)

> "This month we assessed [N] workflow automation requests. [N] were approved for build, [N] were rejected or are on hold for evidence, and [N] are in active development. We currently have [N] autonomous workflows running and [N] supervised workflows. The Gate blocked [N] requests that would have bypassed [GATE type — e.g., irreversible financial commitments]. [N] workflows are approaching their recertification interval."

### For Implementation Teams (5-10 minutes)

Present the Build Handoff Pack directly. Walk through:
1. Terminal action — what the implementation may and may not do
2. Required controls — what must be in place before the workflow runs
3. Acceptance criteria — how we verify it works correctly
4. Expiration triggers — when they must stop and return to the Gate

### For Requestors Who Were Declined (2 minutes)

> "The Gate assessed this workflow and found [HUMAN_ONLY: the terminal action cannot be delegated to AI regardless of controls / SOP_FIRST: the process isn't stable enough to automate yet]. The Governance Memo explains the specific reasons. Here's what would need to change for this to be reassessable in the future."

---

## Sample Language

**Asking for complete evidence:**
> "Before I submit this to the Gate, I need to know: what happens if the output is wrong — specifically, can it be corrected and how? And how often do exceptions occur in this workflow?"

**Recording a HOLD_FOR_EVIDENCE:**
> "The verdict is sound, but I need the error-rate threshold and recertification interval before I can authorize the build. HOLD_FOR_EVIDENCE pending those values from [team/owner]."

**Declining an automation request:**
> "The Gate flagged this as HUMAN_ONLY under GATE-2 — the terminal action is an irreversible financial commitment that can't be delegated regardless of what controls we add. I can share the Governance Memo with the rationale if helpful."

**Responding to a scope change from a builder:**
> "If the approval step changed materially, that requires a new Gate assessment before you can proceed. Please pause and send me the specifics of what changed — I'll run it through the Gate and get you an updated authorization."

---

## Quick Reference Card

| Situation | Mode | Time | Output |
|-----------|------|------|--------|
| New automation request arrives | ASSESS | 20-30 min | Governance artifact with disposition |
| Evidence needed from requestor | RESOLVE_EVIDENCE | 10 min | Updated packet + disposition |
| Builder found a scope issue | REVIEW_BUILD | 10 min | IN_SCOPE or OUT_OF_SCOPE determination |
| Recertification window triggered | RECERTIFY | 20-30 min | New packet + new disposition |
| Someone asks why a decision was made | EXPLAIN | 5 min | Rule citations |
| New team member needs org context loaded | CONFIGURE | 10 min | Workspace ready for assessments |
