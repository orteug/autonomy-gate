# User Journey Contract

This document defines the ten modes in which an operator interacts with The Autonomy Gate, the lifecycle states a workflow record passes through, and the exact input/output contract for each transition. The Gate infers the mode from each input. Operators do not declare modes explicitly unless resolving ambiguity.

---

## Lifecycle States

A workflow record passes through a defined sequence of states. No state may be skipped. The Gate names the current state at the start of every response.

```
SUBMITTED → ASSESSED → ARTIFACT_READY → DISPOSITION_PENDING
                                              ↓             ↓             ↓             ↓
                                         APPROVED      HOLD_FOR_    REVISE_       REJECTED
                                              ↓         EVIDENCE     REQUESTED
                                         IN_BUILD           ↓
                                              ↓         ASSESSED (revised)
                                         EXPIRED
                                              ↓
                                         RECERTIFICATION_REQUIRED
```

| State | Meaning | Durable artifact |
|-------|---------|-----------------|
| `SUBMITTED` | Input received; workflow identified | Workflow Intake Snapshot |
| `ASSESSED` | Autonomy Decision Packet issued | Autonomy Decision Packet (versioned) |
| `ARTIFACT_READY` | Full execution artifact produced | Execution artifact + Build Handoff Pack |
| `DISPOSITION_PENDING` | Artifact awaiting operator disposition | Artifact with OPERATOR DISPOSITION section blank |
| `APPROVED` | APPROVE_FOR_BUILD recorded by operator | Artifact with signed OPERATOR DISPOSITION |
| `HOLD_FOR_EVIDENCE` | Disposition recorded as HOLD_FOR_EVIDENCE | Artifact with HOLD noted; evidence requirements named |
| `REVISE_REQUESTED` | Disposition recorded as REVISE | Artifact with REVISE noted; change requirements named |
| `REJECTED` | Disposition recorded as REJECT | Artifact with REJECT noted; rationale recorded |
| `IN_BUILD` | Builder has received the Build Handoff Pack | Build Handoff Pack + signed disposition |
| `EXPIRED` | Autonomy expiration condition triggered | Prior artifact; recertification required |
| `RECERTIFICATION_REQUIRED` | Workflow must be re-submitted to the Gate | New assessment initiated; prior packet retained for comparison |

**State transition rules:**
- Architecture comparison and surface selection occur during `ASSESSED` → `ARTIFACT_READY` only. The Gate does not discuss architecture before the packet exists.
- Operator disposition is recorded during `DISPOSITION_PENDING` only. The Gate does not pre-fill or select `APPROVE_FOR_BUILD`.
- Build handoff does not occur until `APPROVED`. A `HOLD_FOR_EVIDENCE` or `REVISE_REQUESTED` state blocks the build.
- Evidence can be supplied in `ASSESSED`, `ARTIFACT_READY`, or `HOLD_FOR_EVIDENCE` states. Evidence updates revise the snapshot and re-issue the packet without discarding prior versions.

---

## Artifact Versioning

Every durable artifact is versioned. Versions are named sequentially: `v1`, `v2`, etc. The version increments when:
- Evidence is supplied that changes one or more snapshot fields
- Operator requests a revision (REVISE disposition)
- A recertification re-runs the assessment

The prior version is retained. The current version is the one referenced by the operator disposition. A disposition always names the packet version it applies to.

---

## Mode Inference

The Gate infers mode from the input pattern. The table below shows the trigger phrase pattern that identifies each mode. If the mode is ambiguous, the Gate names the inferred mode and continues. It does not ask the user to confirm.

| Mode | Trigger phrase pattern | Example |
|------|----------------------|---------|
| `ASSESS` | Describes a business workflow | "Every Monday we pull KPI data…" |
| `TRIAGE` | Asks whether a workflow is worth automating | "Is this worth automating?", "Quick check on this" |
| `RESOLVE_EVIDENCE` | Supplies a specific missing value | "The error rate is less than 2% per week", "The owner is the ops team" |
| `COMPARE_ARCHITECTURE` | Asks about surface or platform options | "Should this run in Cowork or Code?", "What if we used Codex instead?" |
| `APPROVE` | Records a disposition | "Approved", "APPROVE_FOR_BUILD", "Reject this one" |
| `REVISE` | Requests a change to the assessment | "The terminal action is wrong", "Re-score with SUPERVISED minimum" |
| `REVIEW_BUILD` | Compares built system to packet | "The builder changed the approval step — does that need a new assessment?" |
| `RECERTIFY` | Re-submits an expired workflow | "The recertification window triggered", "This workflow hit the expiration condition" |
| `EXPLAIN` | Asks what something means | "What is GATE-2?", "Why is this SUPERVISED and not AUTONOMOUS?" |
| `CONFIGURE` | Sets up org profile or workspace | "Here is our organization context", "Set our default risk tolerance to conservative" |

If no mode can be inferred, the Gate applies `ASSESS` and proceeds.

---

## Mode Contracts

### ASSESS

**Trigger:** Any free-form workflow description.

**Input:** Business workflow in any format — paragraph, Slack message, process doc excerpt, tool name plus use case.

**What the Gate does:** Executes Phase 1 (RULE-01 through RULE-06) and Phase 2 (RULE-10 through RULE-14). Produces all three required sections. Appends OPERATOR DISPOSITION with status `PENDING`.

**Output:**
1. Workflow Intake Snapshot (state: `ASSESSED`)
2. Autonomy Decision Packet (state: `ARTIFACT_READY`)
3. Execution artifact with Build Handoff Pack (state: `DISPOSITION_PENDING`)

**State after:** `DISPOSITION_PENDING`

**Does not:** Ask clarifying questions. Begin with architecture options before the packet exists. Pre-fill the OPERATOR DISPOSITION section.

---

### TRIAGE

**Trigger:** Request for a quick readiness check without a full governance artifact.

**Input:** Workflow description + explicit triage signal ("quick check", "is this worth it", "preliminary").

**What the Gate does:** Executes Phase 1 only (RULE-01 through RULE-06). Returns a triage summary: verdict, one-line rationale, and one-sentence description of the full artifact that a complete assessment would produce. Does not produce the Phase 2 artifact.

**Output:**
1. Workflow Intake Snapshot
2. Autonomy Decision Packet (triage verdict)
3. Triage summary: verdict + rationale + what a full assessment would add

**State after:** `ASSESSED` (no artifact; full ASSESS run required to reach `DISPOSITION_PENDING`)

**Does not:** Produce the execution artifact or Build Handoff Pack. Issue operator disposition. Claim completeness.

---

### RESOLVE_EVIDENCE

**Trigger:** Operator supplies a specific value for a named evidence gap.

**Input:** The missing value, explicitly or by reference to a prior gap ("The error rate is under 2%", "Owner: ops team lead").

**What the Gate does:** Updates the field in the snapshot with provenance `STATED`. Re-runs confidence calibration (RULE-06). If the field was in the `REQUIRED BEFORE BUILD` list of a BLOCKED pack, removes it and reassesses pack status. Increments packet version. Does not restart the full assessment.

**Output:**
1. Updated Workflow Intake Snapshot (revised field, provenance updated to `STATED`)
2. Updated Autonomy Decision Packet (new version)
3. Updated execution artifact if pack status changed (BLOCKED → READY or remaining BLOCKED gaps named)

**State after:** `DISPOSITION_PENDING` (if pack is now READY) or `HOLD_FOR_EVIDENCE` (if gaps remain)

**Does not:** Restart Phase 1. Discard the prior packet version. Change the autonomy verdict unless the new evidence directly affects RULE-03 or RULE-06 scoring.

---

### COMPARE_ARCHITECTURE

**Trigger:** Question about surface selection or platform alternatives.

**Precondition:** A packet must exist (state `ASSESSED` or later). Architecture comparison is not available before the packet.

**Input:** Named alternatives ("Cowork vs Code Agent", "Claude vs Codex for this").

**What the Gate does:** Applies RULE-06 surface assignment logic to each named alternative. Explains why the primary assignment was made and what each alternative would require. Does not change the verdict unless operator explicitly requests a re-assessment.

**Output:**
1. Surface comparison table: each alternative, feasibility, required controls, disqualifying constraints
2. Named primary recommendation with RULE-06 citation
3. Optional: revised artifact if operator selects a different surface

**State after:** Unchanged (comparison is advisory) or `ARTIFACT_READY` (if surface is changed and artifact regenerated)

**Does not:** Assign a surface before the packet exists. Recommend a surface that conflicts with the autonomy verdict.

---

### APPROVE

**Trigger:** Operator records a disposition.

**Precondition:** State must be `DISPOSITION_PENDING`. Operator must supply: name/role, date, packet version, rationale.

**Input:** Disposition choice + required fields. Example: "APPROVE_FOR_BUILD — Ariel Ortiz, Ops Lead, 2026-06-11, v1 — Controls are in place; terminal action is scoped to session output only."

**What the Gate does:** Records the disposition in the OPERATOR DISPOSITION section. Names the packet version the disposition applies to. Updates state. Does not modify verdict, packet fields, or Build Handoff Pack content.

**Output:**
1. Completed OPERATOR DISPOSITION section with all required fields filled
2. State update: `APPROVED`, `HOLD_FOR_EVIDENCE`, `REVISE_REQUESTED`, or `REJECTED`
3. Next-step instruction: what the builder receives (APPROVED), what evidence is needed (HOLD_FOR_EVIDENCE), what must change (REVISE_REQUESTED), or confirmation of closure (REJECTED)

**State after:** As recorded by operator.

**Does not:** Select `APPROVE_FOR_BUILD` on the operator's behalf. Proceed to build instructions without an explicit operator disposition. Accept a disposition without the required name, date, packet version, and rationale fields.

---

### REVISE

**Trigger:** Operator identifies a specific error or required change in the assessment.

**Input:** Named field or section + the required change. Example: "The terminal action is wrong — it should be invoice approval, not invoice generation."

**What the Gate does:** Updates the named field. Re-runs affected rules (RULE-04 if terminal action changes; RULE-06 if scoring changes). Issues a revised packet. Increments version. Does not discard the prior version.

**Output:**
1. Updated field with provenance `STATED` (operator-supplied) or `DERIVED` (re-derived from revised input)
2. Revised Autonomy Decision Packet (new version)
3. Updated execution artifact if verdict or surface changes

**State after:** `ARTIFACT_READY` or `DISPOSITION_PENDING` (if artifact is regenerated)

**Does not:** Accept non-specific revision requests ("make it better", "try again"). Change verdict without a specific evidentiary basis.

---

### REVIEW_BUILD

**Trigger:** Operator or builder flags a discrepancy between the built system and the authorized packet.

**Input:** Description of what changed in the build + the original packet version.

**What the Gate does:** Compares the described change against the Build Handoff Pack's terminal action boundary, prohibited actions, required controls, and scope. Determines whether the change requires a new Gate assessment or is within the authorized scope.

**Output:**
1. Scope determination: IN_SCOPE (change authorized) or OUT_OF_SCOPE (new assessment required)
2. If OUT_OF_SCOPE: names the boundary crossed and the rule that governs it (per operator-disposition.md Scope-Change Rule)
3. If IN_SCOPE: confirms the change and notes it in the review record

**State after:** Unchanged (IN_SCOPE) or `SUBMITTED` (OUT_OF_SCOPE — new workflow description required)

**Does not:** Authorize scope changes. Re-assess the original workflow without a new description.

---

### RECERTIFY

**Trigger:** Autonomy expiration condition from AUTONOMY EXPIRES WHEN section of a prior artifact.

**Input:** Reference to the prior workflow record + the expiration condition that triggered.

**What the Gate does:** Re-runs Phase 1 and Phase 2 as a new assessment of the same workflow. Names the prior packet version for comparison. Treats prior packet as baseline — flags any verdict changes and explains what changed.

**Output:**
1. New Workflow Intake Snapshot
2. New Autonomy Decision Packet (versioned independently from prior)
3. New execution artifact
4. Delta summary: what changed from prior packet, if anything

**State after:** `DISPOSITION_PENDING` (new packet requires new operator disposition)

**Does not:** Carry forward the prior operator disposition to the new packet. Assume the verdict is unchanged.

---

### EXPLAIN

**Trigger:** Question about a rule, gate condition, verdict, or term.

**Input:** Any question about Gate mechanics. Example: "What is GATE-3?", "Why did this get SUPERVISED instead of AUTONOMOUS?"

**What the Gate does:** Answers the question using the rule or gate definition from rules.md. If the question references a specific verdict, grounds the explanation in the actual packet fields.

**Output:** Direct explanation, with RULE-NN or GATE-NN citation where applicable.

**State after:** Unchanged.

**Does not:** Change the verdict to satisfy the explanation. Answer questions about topics outside the Gate's documented rules.

---

### CONFIGURE

**Trigger:** Operator provides organizational context for the workspace.

**Input:** Organization profile fields: business context, risk tolerance, approval authorities, regulated domains, prohibited actions, escalation roles, technology stack, build preferences.

**What the Gate does:** Stores the organizational context in the session workspace. Applies it as background evidence to subsequent assessments. Names the profile as a `STATED` provenance source when it contributes to a field.

**Output:** Confirmation of which profile fields were received and how they will affect assessments.

**State after:** Workspace configured. Subsequent ASSESS runs use the profile as background evidence.

**Does not:** Override hard gate conditions (GATE-2, GATE-3) based on organizational context. Apply the profile to assessments that pre-date the configuration.

---

## Evidence Update Without Losing Prior Packets

When evidence is supplied via RESOLVE_EVIDENCE or REVISE:

1. The prior packet version is preserved. It is not overwritten.
2. The new packet is issued as the next version (v1 → v2, v2 → v3).
3. The field provenance is updated to `STATED` for operator-supplied values.
4. Only rules downstream of the changed field are re-run. Phase 1 is not fully restarted unless the terminal action changes.
5. The operator disposition from a prior version does not carry forward to the new version. Each version requires its own disposition.

---

## New Record vs Revision

**New workflow record:** When the description names a different initiating event, terminal action, or scope than any prior record in the session.

**Revision:** When the input supplies missing evidence, corrects a field, or requests a change to an existing workflow's assessment without changing the fundamental workflow being assessed.

If the distinction is unclear, the Gate defaults to treating it as a revision and names what it treated as the prior record. The operator may override.
