# Workflow Lifecycle

A workflow record passes through defined states from first submission to build authorization. This document shows what happens at each stage, what the operator does, and what the Gate returns.

---

## The Full Lifecycle — One Page

```
Operator submits workflow description
         ↓
    [Gate: Phase 1]
  Workflow Intake Snapshot
  Autonomy Decision Packet
         ↓
    [Gate: Phase 2]
  Execution Artifact
  Build Handoff Pack
  OPERATOR DISPOSITION (blank)
         ↓
  Operator reviews artifact
         ↓
     ┌─────────────────────────────────────────┐
     │ Pack is READY?                          │
     │ → Record APPROVE_FOR_BUILD              │
     │                                         │
     │ Pack is BLOCKED?                        │
     │ → Supply missing values → Re-issue pack │
     │ → Then record disposition               │
     │                                         │
     │ Verdict is wrong?                       │
     │ → Record REVISE → Gate re-assesses      │
     │                                         │
     │ Workflow should not be built?           │
     │ → Record REJECT → workflow closed       │
     └─────────────────────────────────────────┘
         ↓ (APPROVE_FOR_BUILD only)
  Builder receives Build Handoff Pack
         ↓
  Builder implements
         ↓
  [Expiration condition triggers]
         ↓
  Operator submits for recertification
         ↓
  New packet → New disposition required
```

---

## Stage-by-Stage

### Stage 1: Submit

**What you do:** Describe the workflow. Include what triggers it, what it does, what it touches, what happens if it fails, and whether the output can be undone.

**What the Gate does:** Runs Phase 1 (assessment) and Phase 2 (artifact generation). Delivers all three required sections in one response.

**What you have:** A complete execution artifact with a blank OPERATOR DISPOSITION section. The workflow is now in state `DISPOSITION_PENDING`.

**If confidence is LOW:** The Gate routed conservatively. This is correct. Supply missing evidence using Mode 3 (RESOLVE_EVIDENCE) to upgrade confidence before disposition.

---

### Stage 2: Review

**What you do:** Read the artifact. Check the verdict, the terminal action boundary, the controls, and the Build Handoff Pack status.

**Key questions to answer before disposition:**
1. Is the terminal action correctly identified?
2. Is the verdict (AUTONOMOUS/SUPERVISED/SOP_FIRST/HUMAN_ONLY) appropriate given what the workflow does?
3. Is the assigned surface (PROJECT/COWORK/CODE_AGENT/NO_AI) the right one?
4. Is the Build Handoff Pack READY or BLOCKED?
5. If BLOCKED: can you supply the missing values now?

**If the terminal action is wrong:** Use REVISE mode. Correcting the terminal action re-triggers RULE-04 and RULE-06. The verdict may change.

**If the verdict seems too conservative:** Check if LOW confidence is driving it. Supply the missing evidence first — the verdict may upgrade on its own.

---

### Stage 3: Resolve Blocks (if BLOCKED)

**What you do:** Submit the missing values using RESOLVE_EVIDENCE mode.

**What the Gate does:** Updates the snapshot field with provenance `STATED`. Removes the field from the BLOCKED list. If all BLOCKED items are resolved, issues a new READY pack (v2).

**What you have:** Updated artifact with READY pack. Return to Stage 2 review.

---

### Stage 4: Record Disposition

**What you do:** Choose one of four dispositions and supply the required fields.

**Required fields for APPROVE_FOR_BUILD:**
- Your name and role
- Today's date
- Packet version (e.g., v1, v2)
- Rationale (one or more sentences)

**What the Gate does:** Records the disposition in the OPERATOR DISPOSITION section. Names the next step.

**What you have:**
- `APPROVE_FOR_BUILD` → Completed artifact ready for builder handoff. State: `APPROVED`.
- `HOLD_FOR_EVIDENCE` → Artifact on hold. State: `HOLD_FOR_EVIDENCE`. Return to Stage 3.
- `REVISE` → Artifact sent back for revision. State: `REVISE_REQUESTED`. Gate re-assesses.
- `REJECT` → Workflow closed. State: `REJECTED`. No further action.

---

### Stage 5: Builder Handoff

**What you do:** Send the completed artifact (with signed disposition) to the builder.

**Builder receives:**
- The full execution artifact
- The Build Handoff Pack with all required files
- The OPERATOR DISPOSITION record

**Builder's obligations:**
- Do not modify verdict fields, terminal action, or controls
- Do not cross the terminal action boundary
- If a scope change is required: stop, return to operator, new Gate assessment before proceeding
- Acknowledge receipt (if builder acknowledgement is required per the organization profile)

---

### Stage 6: Monitor and Expire

**What you do:** Monitor for the expiration conditions listed in the artifact's AUTONOMY EXPIRES WHEN section.

**Common expiration conditions:**
- Workflow has run for the recertification interval (e.g., 12 months)
- Error rate exceeded the stated threshold
- A system or integration changed materially
- A regulation affecting the workflow changed

**What happens when an expiration condition triggers:**

Submit the workflow for recertification (RECERTIFY mode). The Gate runs a new full assessment. The new packet is independent — it receives its own version number and requires its own operator disposition. The prior packet and disposition are retained as historical record.

---

## Example Conversation — Weekly KPI Report

### Turn 1 — ASSESS

**Operator:**
> We generate a weekly KPI report every Monday morning. A team member exports stable CRM and analytics data, pastes it into the Project, and needs a standardized Slack-ready narrative. If the report has a mistake, it gets caught in review before we post it — and since it's just an internal Slack message, the worst case is we post a correction. Nothing irreversible happens.

**Gate returns:**
> [Three sections]
> State: `DISPOSITION_PENDING`
> Verdict: `AUTONOMOUS / PROJECT · HIGH`
> Build Handoff Pack: BLOCKED (missing: error-rate threshold, recertification interval)

---

### Turn 2 — RESOLVE_EVIDENCE

**Operator:**
> Evidence update for Weekly KPI Report:
> - Error rate: under 2% per weekly run
> - Recertification interval: 12 months

**Gate returns:**
> Updated packet v2. Build Handoff Pack: READY.
> State: `DISPOSITION_PENDING`

---

### Turn 3 — APPROVE

**Operator:**
> APPROVE_FOR_BUILD — Ariel Ortiz, Ops Lead — 2026-06-11 — v2
> Rationale: Controls are in place. Terminal action is scoped to session output only. The operator posts to Slack; the Gate does not. Error rate threshold and recertification interval are now specified.

**Gate returns:**
> OPERATOR DISPOSITION recorded: APPROVE_FOR_BUILD
> State: `APPROVED`
> Next: Send the Build Handoff Pack to the builder.

---

## Lifecycle Anti-Patterns

**Do not record disposition on a BLOCKED pack without resolving the blocks first.** A BLOCKED pack means the builder cannot proceed — they are missing required configuration values. Record HOLD_FOR_EVIDENCE and supply the missing values first.

**Do not ask the Gate to approve on your behalf.** The Gate may recommend a disposition but cannot select `APPROVE_FOR_BUILD`. That decision requires a human operator who accepts accountability.

**Do not let a builder proceed without a disposition.** A `PENDING` disposition means no build is authorized. The builder must not start until `APPROVE_FOR_BUILD` is recorded.

**Do not skip recertification.** When an expiration condition triggers, the workflow must be re-submitted. Running an expired workflow without recertification means operating outside the authorized scope.
