# Template: Project Setup Brief
**Autonomy:** AUTONOMOUS  
**Architecture pattern:** Human-triggered knowledge-work workflow
**Section 20 additions applied:** EXPECTED OUTCOMES (Addition 2) · AUTONOMY EXPIRES WHEN (Addition 5)

---

This template is filled during Phase 2, Step 3 (RULE-12). Fill every section as a document — prose context, headers, formatted lists. No placeholder brackets in the final output. Presentable in a meeting without explanation.

---

```
PROJECT SETUP BRIEF
[Workflow Name] · AUTONOMOUS · Human-triggered knowledge-work architecture · [Confidence]

[One paragraph: what this workflow does inside a Claude Project, what the operator
produces on each run, and the human-initiated cadence it runs on.
State explicitly: this is human-initiated. It does not run on a schedule without initiation.
If the user wanted unattended scheduled execution, the surface would be COWORK.
Name the terminal action and why no GATE conditions trigger.]

PURPOSE
[One sentence. What the operator produces and for whom.]

RUN CADENCE
[Human-initiated frequency. Not scheduled. Not unattended.
Example: "The ops lead pastes the prior week's data export each Monday morning."
Name who initiates the run, what they paste in, and when.]

KNOWLEDGE FILES
• [File name] · [What it contains] · [Why the operator needs it]
• [File name] · [What it contains] · [Why the operator needs it]
[One bullet per file uploaded to the Claude Project.
Include: rules.md, identity.md, and any workflow-specific reference files needed.]

CUSTOM INSTRUCTIONS
[Full instruction block — ready to paste into the Claude Project system prompt.
Do not summarize — write the actual instruction text the user will paste.
Example: "You are The Autonomy Gate. Follow identity.md and rules.md. When you receive a workflow
description, execute Phase 1 (assessment) then Phase 2 (artifact generation) per rules.md.
Always produce three sections in order: Workflow Intake Snapshot, Autonomy Decision Packet,
and the execution artifact. Never ask clarifying questions."]

OUTPUT FORMAT
[What every run produces. Structure, length, destination.
Name the specific output: document, table, summary, Slack-ready text.
State where it goes: pasted into a channel, saved to a folder, emailed.
Note any format requirements: headers required, word count target, attachment format.]

INFORMATION GAPS (if applicable)
[Present only if RULE-11 flagged more than three inferred fields.
List: field name · what was inferred · what evidence would confirm it.]

EXPECTED OUTCOMES
Completed:              [What done looks like — output delivered in expected format, ready for use.]
Completed w/ warnings:  [What partial success looks like — output produced but gaps or anomalies noted.]
Needs review:           [What signals that a human should review before acting on the output.]
Blocked:                [What prevents the operator from producing a complete output.]
Failed:                 [What constitutes failure — no output produced, major evidence gap, or error in logic.]

Valid terminal statuses: COMPLETED · COMPLETED_WITH_WARNINGS · NEEDS_REVIEW · BLOCKED · FAILED · SKIPPED · TIMED_OUT

AUTONOMY EXPIRES WHEN
Mark each condition as applicable or not applicable. Do not omit conditions — note "not applicable" with rationale.

- [ ] The workflow's steps, inputs, or outputs change materially
      [Applicable / Not applicable — rationale]
- [ ] The AI surface or tool used changes (model upgrade, platform migration, Claude Project access changes)
      [Applicable / Not applicable — rationale]
- [ ] The policy or compliance context changes
      [Applicable / Not applicable — rationale]
- [ ] An incident occurs — any output that caused unintended harm or required correction
      [Applicable — always. Any incident triggers reassessment.]
- [ ] Error rate exceeds threshold — [if the workflow description names a threshold, use it exactly; if not, write: Not specified — operator must define before deployment. Do not invent a percentage or run count.]
      [Applicable / Not applicable — rationale]
- [ ] Recertification interval passes — [if the workflow description names a date or interval, use it exactly; if not, write: Not specified — operator must define before deployment. Do not invent a date or cadence.]
      [Applicable — recertification date and responsible role if provided in input; otherwise Not specified]
- [ ] The reviewer role changes or becomes vacant
      [Not applicable — this AUTONOMOUS operating pattern has no approval checkpoint. A human initiates the run but does not approve the terminal action.]

ARCHITECTURE OPTIONS
Generate the canonical PRIMARY, NATIVE_SUITE, LOW_CODE, CODE_FIRST, and VENDOR_NEUTRAL options required by RULE-10. Use one `OPT-N` heading per viable class. Every option states Execution architecture, Builder surface, Control fit, Implementation effort, Operating cost, Maintenance burden, Security fit, Portability, Skill requirements, and Source evidence. Treat a Project as an implementation pattern inside an option, not as the verdict. List every absent class under Omitted option classes with an evidence-based reason.

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
Generate the exact project instructions, exact knowledge-file manifest, first-run prompt, expected result, and one acceptance check. The output must be ready to paste or upload without translating fields into another template. If a required workflow-specific file is missing, name it under REQUIRED BEFORE BUILD.
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
