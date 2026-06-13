# Design Dossier — Control Plan

**Artifact type:** Control Plan  
**Verdict:** SUPERVISED  
**Architecture pattern:** Any surface (PROJECT, COWORK, or CODE) with a blocking human checkpoint  
**Status:** Undesigned — needs full layout treatment

---

## What This Document Is

The Control Plan is the execution artifact the Gate produces when a workflow requires a human to review and approve AI output before the terminal action executes. It is the only artifact that carries a SUPERVISED verdict. The entire document is organized around one structural reality: something cannot proceed without a human saying yes.

The APPROVAL CHECKPOINT is not one section among many — it is the architectural backbone of this document. Everything before it describes what AI prepares. Everything after it describes what happens once the human approves. The design must reflect this: the checkpoint is the dominant visual element.

---

## Non-Negotiable Sections (in document order)

### 1. Document Header

Must display:
- Document type label: `CONTROL PLAN`
- Workflow name
- Verdict: `SUPERVISED`
- Surface (e.g., `PROJECT surface`, `COWORK surface`, `CODE surface`)
- Confidence level: `HIGH`, `MEDIUM`, or `LOW`

### 2. Narrative Description

One paragraph. Must state:
- What AI prepares
- What the human reviews
- Why this workflow requires a checkpoint before execution proceeds
- The specific gate condition or criterion that produced the SUPERVISED verdict (named, not paraphrased)
- The terminal action explicitly named
- Why the terminal action requires human authorization

### 3. WHAT AI PREPARES

Specific description of the output AI produces before reaching the checkpoint. Must include:
- What file, document, or record is produced
- Where it is placed for the reviewer (destination)
- Naming convention so the reviewer can find it

"The output" is not a valid entry — the actual artifact name must be stated.

### 4. APPROVAL CHECKPOINT

This is the document's central section. It must be the most visually prominent block on the page. Five required fields:

- **Reviewer** — Named role. Not "a manager" or "someone on the team." If unknown, it is stated as an evidence gap and confidence is LOW.
- **Reviews** — Exactly what the reviewer evaluates. Not "the output." Specific criteria: what they check, what tolerances apply, what lists they consult.
- **Approves when** — The conditions under which execution proceeds. Specific and measurable.
- **Rejects when** — The conditions under which execution is blocked. Must also state what happens to the rejected item.
- **Turnaround** — Expected timeframe in business hours. Not "as soon as possible."

Design requirement: this block must read as a contract, not a description. It should be visually heavier or more contained than surrounding sections — bordered, elevated, or otherwise distinguished to signal that this is where decisions are made.

### 5. POST-APPROVAL ACTIONS

Numbered list. What executes after approval. Each step names:
1. The action
2. The executor (named — if AI executes a post-approval step, that must be explicit)
3. The system

If additional human steps follow the AI's post-approval action, they must be named. Approval does not mean the rest of the workflow is unobserved.

### 6. PROHIBITED WITHOUT APPROVAL

Bulleted hard-stop list. Actions that cannot execute before reviewer approval is recorded. Minimum three items. These are the enforcement structure — what makes the checkpoint real rather than advisory. Must be stated as absolutes:
- "Cannot" / "may not under any condition"
- Not "should" or "is expected not to"

### 7. AUDIT TRAIL

Required fields for every run:
- AI output: content hash or version identifier
- Reviewer: name or ID of the approving human
- Approval timestamp: exact date and time
- Decision: APPROVED / REJECTED
- Rejection reason (if rejected): which criterion failed

Plus: where the log is stored, how long it is retained.

### 8. INFORMATION GAPS *(conditional)*

Present only if more than three fields were inferred. Field name, what was inferred, what evidence would confirm it.

### 9. EXPECTED OUTCOMES

Five terminal states for this workflow:
- `Completed` — AI output delivered, reviewer approved, post-approval actions executed, log written
- `Completed with warnings` — Approved with conditions; anomalies flagged
- `Needs review` — AI output has anomaly; reviewer requests clarification
- `Blocked` — Reviewer rejected; missing data; approval deadline missed
- `Failed` — No output produced, or output rejected and corrective action not completed

Valid terminal status list:
`COMPLETED · COMPLETED_WITH_WARNINGS · NEEDS_REVIEW · BLOCKED · FAILED · SKIPPED · TIMED_OUT`

### 10. AUTONOMY EXPIRES WHEN

Seven checkbox conditions. Each marked applicable or not applicable with rationale.

1. Workflow steps, inputs, or outputs change materially
2. AI surface or tool changes
3. Policy or compliance context changes
4. An incident occurs *(always applicable)*
5. Error rate exceeds threshold
6. Recertification interval passes
7. **Reviewer role changes or becomes vacant** — Always applicable for SUPERVISED. If the named reviewer leaves or the role changes, the Control Plan must be updated before execution resumes.

Condition 7 is the one condition unique to SUPERVISED. It should be visually distinguishable from the others — it will always be checked applicable and its rationale is always the same.

### 11. ARCHITECTURE OPTIONS

Same structure as all artifact types. Each option must additionally be evaluated on whether it can enforce the blocking approval checkpoint deterministically. Any option that cannot enforce the checkpoint must be rejected with a stated reason — it is not a viable option regardless of other qualities.

Ten fields per option:
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

Selection metadata: Selected option / Selection by / Selection date.

### 12. BUILD HANDOFF PACK

Same 20-field structure as all artifact types. For the Control Plan specifically, this pack must include the approval hold, the named reviewer contract, the approval record format, the proof that the checkpoint blocks the terminal action, and one acceptance test demonstrating the block.

Fields in order:
1. Handoff status
2. Terminal-action boundary
3. Architecture decision record
4. Permissions and credentials
5. Deterministic controls
6. Human checkpoints *(this field is the primary field for SUPERVISED — it names the blocking checkpoint contract in full)*
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

### 13. OPERATOR DISPOSITION

Always last. Always unselected:
- `[ ] APPROVE_FOR_BUILD`
- `[ ] REVISE`
- `[ ] HOLD_FOR_EVIDENCE`
- `[ ] REJECT`

Operator fills: Name / role, Date, Packet version, Rationale.

---

## Structural Notes for Design

- **APPROVAL CHECKPOINT is the document.** Sections 3 (WHAT AI PREPARES) and 5 (POST-APPROVAL ACTIONS) exist to frame the checkpoint — before and after. The checkpoint itself must be the visual anchor.
- The five fields of the checkpoint (Reviewer / Reviews / Approves when / Rejects when / Turnaround) should be presented as a contained block with clear separation between fields. This is the closest thing this system has to a contract form.
- PROHIBITED WITHOUT APPROVAL is a hard-stop list — similar visual weight to the HUMAN_ONLY gate callout in the Governance Memo, but scoped to pre-approval actions rather than the entire workflow
- AUDIT TRAIL is a structured log spec — compact key-value block, similar to SCHEDULED TASK in the Cowork Config
- AUTONOMY EXPIRES WHEN condition 7 (reviewer vacancy) will always be checked applicable — it may benefit from being visually distinguished from the conditionally-applicable entries
- The amber verdict color (#B07514) communicates "proceed with caution, human required" — the design should feel different from the AUTONOMOUS green, more guarded

---

## Verdict Color

`SUPERVISED` — `#B07514`

All accent elements for this document use this color.
