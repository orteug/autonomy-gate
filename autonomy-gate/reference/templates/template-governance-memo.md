# Template: Governance Memo
**Autonomy:** HUMAN_ONLY  
**Handoff status:** NOT_APPLICABLE
**Section 20 additions applied:** EXPECTED OUTCOMES (Addition 2) · AUTONOMY EXPIRES WHEN (Addition 5)

---

This template is filled during Phase 2, Step 3 (RULE-12). Fill every section as a document — prose context, headers, formatted lists. No placeholder brackets in the final output. Presentable in a meeting without explanation.

A Governance Memo is not a dead end. It names exactly what would have to be true for the verdict to change. That specificity is the productive output — it tells the ops leader what to build, change, or bound before re-assessment.

---

```
GOVERNANCE MEMO
[Workflow Name] · HUMAN_ONLY · No AI execution handoff · [Confidence]

[One paragraph: what this workflow does, why it cannot be delegated to AI,
and what the specific risk or judgment requirement blocks automation.
Name the GATE condition that triggered. State the terminal action explicitly.
Be concrete: not "it involves risk" — name what would happen if AI executed this autonomously.]

WHY THIS CANNOT BE DELEGATED
Gate condition:  [GATE-N — named condition and its full definition from rules.md.
                 Example: GATE-2 — makes an irreversible external commitment.
                 If multiple gates apply, name all of them.]
Terminal action: [The specific action that triggered the gate. Not the workflow label — the actual last execution step.]
Specific risk:   [What would happen if AI executed this autonomously. Concrete and specific.
                 Example for vendor bank account: "If AI authorized a bank account change submitted by
                 a spoofed vendor email, payment would route to a fraudulent account. Per FBI IC3 2025,
                 86% of BEC funds move via wire or ACH — average per-complaint loss exceeds $122,000.
                 Funds are recovered in only 58% of flagged cases."]
Failure pattern: [FAIL-NN from risk-classification.md most likely to materialize.
                 State why this failure pattern is particularly dangerous for this specific workflow.]

HUMAN REVIEW PROCESS
Owner:              [Role responsible for this decision. Named role, not "management" or "the team."
                    If the owner cannot be identified from the workflow description, this is an evidence gap.]
Review cadence:     [How often this is evaluated. For single-event workflows: per-instance.
                    For recurring workflows: frequency of re-review.]
Decision criteria:  [What the human evaluates when making this call. Specific and actionable.
                    Example: "Verifies the request came from the vendor's registered contact via a
                    previously established channel. Cross-references the account number against two
                    prior invoices. Confirms via phone call to the vendor's published number — not
                    the number in the email."]
Escalation path:    [Who else must be involved for high-stakes instances. Named roles. What threshold
                    triggers escalation. Example: "Any account change above $[X] requires CFO sign-off."]

WHAT WOULD CHANGE THIS VERDICT
These are specific, concrete conditions that would permit re-assessment. Not "when AI improves." Not "when controls are better."

• [Condition 1 — e.g., "If the transaction value is capped below $[X] and a pre-approved rules table
  exists defining the exact conditions under which a routing change can proceed, re-submit as
  SUPERVISED with a code-first execution architecture and GATE-1 acknowledged."]
• [Condition 2 — e.g., "If the terminal action is changed to 'prepare a recommendation for human authorization'
  rather than 'authorize the account change,' the workflow splits: AI prepares the verification packet
  (SUPERVISED with a code-first execution architecture); a human authorizes the terminal action, which remains HUMAN_ONLY."]
• [Condition 3 — if applicable — e.g., "If a second independent verification channel is added and
  the workflow scope is limited to flagging rather than acting, re-submit with updated terminal action."]

The gate condition itself does not change. The workflow scope must change to remove the terminal action that triggers the gate.

INFORMATION GAPS (if applicable)
[Present only if RULE-11 flagged more than three inferred fields.
List: field name · what was inferred · what evidence would confirm it.]

EXPECTED OUTCOMES
[For a Governance Memo, expected outcomes describe the human review process — not AI execution.]
Completed:              [Human review completed; decision documented; action taken or declined; record filed.]
Completed w/ warnings:  [Decision made but one criterion was not fully verifiable — noted in the record with rationale.]
Needs review:           [Case escalated beyond standard criteria — awaiting higher-authority sign-off.]
Blocked:                [Required information unavailable; review cannot proceed; action halted.]
Failed:                 [Review did not occur before action was taken — this is a control failure. Immediate escalation required.]

Valid terminal statuses: COMPLETED · COMPLETED_WITH_WARNINGS · NEEDS_REVIEW · BLOCKED · FAILED · SKIPPED · TIMED_OUT

AUTONOMY EXPIRES WHEN
[For a Governance Memo, this section applies if the workflow is later re-scoped and re-assessed.
It is included as a forward-looking contract.]

Mark each condition as applicable or not applicable. Do not omit conditions — note "not applicable" with rationale.

- [ ] The workflow's steps, inputs, or outputs change materially
      [Applicable — if scope changes to remove the gate-triggering terminal action, re-assess.]
- [ ] The AI surface or tool used changes
      [Not applicable — HUMAN_ONLY authorizes no AI execution architecture for this terminal action. If future reassessment authorizes bounded preparatory work,
      this condition becomes applicable at that time.]
- [ ] The policy or compliance context changes
      [Applicable — regulatory or policy changes may tighten or relax the gate condition. Re-assess if context changes.]
- [ ] An incident occurs — any outcome that caused unintended harm or required correction
      [Applicable — always. Any incident triggers immediate reassessment of the human review process.]
- [ ] Error rate exceeds threshold
      [Not applicable — HUMAN_ONLY workflows have no automation error rate to monitor.
      Human decision error rate is tracked separately under the review process.]
- [ ] Recertification interval passes — [if the workflow description names a date or interval, use it exactly; if not, write: Not specified — operator must define before deployment. Do not invent a cadence or date.]
      [Applicable — governance documents should be reviewed periodically or when the workflow changes.
      Specify next review date and responsible role.]
- [ ] The reviewer role changes or becomes vacant
      [Applicable — if the named Owner role changes or becomes vacant, the Governance Memo must be
      updated with a new designated owner before the workflow can proceed.]

BUILD HANDOFF PACK
Handoff status: NOT_APPLICABLE
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
Human operating procedure: [complete owner, verification, decision, escalation, record, and audit procedure]
Safe decomposition opportunities: [bounded preparation work that may proceed without executing the prohibited terminal action, or a grounded explanation that none is safe]
State explicitly that no AI deployment files should be created for the gate-triggering terminal action. Generate the complete human review procedure, decision-record fields, required verification evidence, escalation path, and one audit check. If the owner or escalation role is unknown, list it under REQUIRED BEFORE OPERATION rather than inventing it.
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
