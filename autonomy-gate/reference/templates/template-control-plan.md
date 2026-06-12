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

BUILD HANDOFF PACK
Deployment status: [READY or BLOCKED per RULE-14]
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
