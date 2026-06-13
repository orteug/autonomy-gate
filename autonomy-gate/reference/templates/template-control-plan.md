# Template: Control Plan
**Verdict:** SUPERVISED / [Surface]
**Section 20 additions applied:** EXPECTED OUTCOMES (Addition 2) · AUTONOMY EXPIRES WHEN (Addition 5)

---

This template is filled during Phase 2, Step 3 (RULE-12). Fill every section as a document — prose context, headers, formatted lists. No placeholder brackets in the final output. Presentable in a meeting without explanation.

The checkpoint ownership rule (RULE-08) applies: the reviewer role must be identifiable from the workflow description. If the reviewer role cannot be identified, confidence is capped at LOW and the reviewer field is listed as an evidence gap.

---

```
CONTROL PLAN
[Workflow Name] · SUPERVISED / [Surface] · [Confidence]

[One paragraph: what AI prepares, what the human reviews, and why this workflow
requires a checkpoint before execution proceeds.
Name the specific gate condition or criterion that produced the SUPERVISED verdict.
State the terminal action and why it requires human authorization.]

WHAT AI PREPARES
[Specific description of the output AI produces before the checkpoint.
Format: what file, document, or record is produced.
Destination: where it is placed for the reviewer.
Naming convention: how it is labeled so the reviewer can find it.
Do not say "the output" — name the specific artifact.]

APPROVAL CHECKPOINT
Reviewer:          [Named role — not "a manager" or "someone on the team." If unknown, this is an evidence gap
                   and confidence is LOW per RULE-08. State: "Reviewer: [unknown — must be designated before deployment]"]
Reviews:           [Exactly what the reviewer evaluates — not "the output." Specific criteria:
                   "Verifies that the listed line items match the purchase order within $[X] tolerance.
                   Confirms vendor name matches the approved vendor list. Checks that due date is
                   within the standard payment window."]
Approves when:     [Conditions under which execution proceeds. Specific and measurable.]
Rejects when:      [Conditions under which execution is blocked. What happens to the rejected item.]
Turnaround:        [Expected timeframe — business hours, not "as soon as possible."]

POST-APPROVAL ACTIONS
[What executes after approval. Step by step. Named executor for each step.
Do not describe AI actions after approval as autonomous — if additional human steps follow,
name them. If AI executes post-approval steps, confirm they are bounded and logged.]
1. [Action] — [Executor] — [System]
2. [Action] — [Executor] — [System]
3. [Action] — [Executor] — [System]

PROHIBITED WITHOUT APPROVAL
The following actions cannot execute before reviewer approval is recorded:
• [Prohibited action 1 — e.g., send external communication]
• [Prohibited action 2 — e.g., post payment or initiate financial transaction]
• [Prohibited action 3 — e.g., update the customer record]
[Every Control Plan must name at least three actions that are blocked until approval. This is the enforcement structure that makes the checkpoint real rather than theater (FAIL-6).]

AUDIT TRAIL
[What is logged. The following fields are required for every SUPERVISED workflow:
AI output: content hash or version identifier
Reviewer: name or ID of the approving human
Approval timestamp: exact date and time
Decision: APPROVED / REJECTED
Rejection reason: if rejected, what criterion failed
Where the log is stored, how long it is retained.]

INFORMATION GAPS (if applicable)
[Present only if RULE-11 flagged more than three inferred fields.
List: field name · what was inferred · what evidence would confirm it.]

EXPECTED OUTCOMES
Completed:              [What done looks like — AI output delivered, reviewer approved, post-approval actions executed, log entry written.]
Completed w/ warnings:  [What partial success looks like — approved with conditions; post-approval issues flagged.]
Needs review:           [What triggers a NEEDS_REVIEW status — AI output has anomaly; reviewer requests clarification.]
Blocked:                [What stops execution — reviewer rejection, missing data, approval deadline missed.]
Failed:                 [What constitutes failure — no output produced, or output rejected and corrective action not completed.]

Valid terminal statuses: COMPLETED · COMPLETED_WITH_WARNINGS · NEEDS_REVIEW · BLOCKED · FAILED · SKIPPED · TIMED_OUT

AUTONOMY EXPIRES WHEN
Mark each condition as applicable or not applicable. Do not omit conditions — note "not applicable" with rationale.

- [ ] The workflow's steps, inputs, or outputs change materially
      [Applicable / Not applicable — rationale]
- [ ] The AI surface or tool used changes (model upgrade, platform migration)
      [Applicable / Not applicable — rationale]
- [ ] The policy or compliance context changes
      [Applicable / Not applicable — rationale]
- [ ] An incident occurs — any output that caused unintended harm or required correction
      [Applicable — always. Any incident triggers reassessment.]
- [ ] Error rate exceeds threshold — [if the workflow description names a threshold, use it exactly; if not, write: Not specified — operator must define before deployment. Do not invent a percentage.]
      [Applicable — use threshold from input only; do not invent a value]
- [ ] Recertification interval passes — [if the workflow description names a date or interval, use it exactly; if not, write: Not specified — operator must define before deployment. Do not invent a date or cadence.]
      [Applicable — recertification date and responsible role if provided in input; otherwise Not specified]
- [ ] The reviewer role changes or becomes vacant
      [Applicable — SUPERVISED workflows depend on a named reviewer. If the reviewer role changes
      or becomes vacant, the Control Plan must be updated with the new reviewer before execution resumes.]

ARCHITECTURE OPTIONS
Generate the canonical PRIMARY, NATIVE_SUITE, LOW_CODE, CODE_FIRST, and VENDOR_NEUTRAL options required by RULE-10. Use one `OPT-N` heading per viable class. Every option states Execution architecture, Builder surface, Control fit, Implementation effort, Operating cost, Maintenance burden, Security fit, Portability, Skill requirements, and Source evidence. Reject any option that cannot enforce the blocking approval checkpoint deterministically. List every absent class under Omitted option classes with an evidence-based reason.

Selected option: [generated option ID or NOT_SELECTED]
Selection by: [operator identity or role, or NOT_RECORDED]
Selection date: [ISO date or NOT_RECORDED]

BUILD HANDOFF PACK
Handoff status: [BUILD_READY or BLOCKED_FOR_EVIDENCE per RULE-14]
Terminal-action boundary: [exact authorized terminal action and explicit out-of-scope boundary]
Architecture decision record: [selected option, selection metadata, and rejected or omitted alternatives; use NOT_APPLICABLE where no AI architecture is authorized]
Permissions and credentials: [least-privilege access, credential owner, storage, rotation, and unavailable values]
Deterministic controls: [controls implemented in code or configuration rather than model prompts]
Human checkpoints: [blocking checkpoint contract, or None with rationale]
Prohibited actions: [implementation constraints that may not execute]
Logging and audit: [events, fields, location, retention, and reviewer]
Failure, rollback, and stop behavior: [failure paths, halt conditions, rollback or compensation, and irreversible limits]
Deployment sequence: [ordered non-production setup, validation, approval, and activation steps]
Assumptions: [grounded assumptions, or None]
Unresolved dependencies: [irreducible missing inputs only, or None]
Expiration and reassessment triggers: [observable events that end authorization]
Version invalidation triggers: [material changes that create a new packet version and invalidate prior selection, disposition, and acknowledgement]
Tool alternatives: [selected option plus viable fallback or safe capability-neutral alternative]
Builder acknowledgement: [required acknowledgement state and reference to the complete acknowledgement contract]
Current state: [canonical lifecycle state]
What the Gate completed: [assessment, architecture, and handoff work completed]
What is blocked: [specific blocker or None]
Who acts next: [operator, evidence owner, builder, or human procedure owner]
Exact next action: [one executable action]
Generate the complete configuration for the assigned surface, including the approval hold, named reviewer contract, approval record, prohibited terminal action before approval, and one acceptance test proving the checkpoint blocks execution. Do not leave placeholders. Missing reviewer or threshold values appear only under REQUIRED BEFORE BUILD.
```

OPERATOR DISPOSITION
This section is always present and always unselected. The Gate may recommend a disposition but may not select APPROVE_FOR_BUILD on behalf of the operator.

[ ] APPROVE_FOR_BUILD
[ ] REVISE
[ ] HOLD_FOR_EVIDENCE
[ ] REJECT

Gate recommendation: [optional — based on Build Handoff Pack status; never pre-selects APPROVE_FOR_BUILD]

Name / role:    [operator fills]
Date:           [operator fills]
Packet version: [operator fills]
Rationale:      [operator fills]
