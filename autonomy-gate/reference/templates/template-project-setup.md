# Template: Project Setup Brief
**Verdict:** AUTONOMOUS / PROJECT
**Section 20 additions applied:** EXPECTED OUTCOMES (Addition 2) · AUTONOMY EXPIRES WHEN (Addition 5)

---

This template is filled during Phase 2, Step 3 (RULE-12). Fill every section as a document — prose context, headers, formatted lists. No placeholder brackets in the final output. Presentable in a meeting without explanation.

---

```
PROJECT SETUP BRIEF
[Workflow Name] · AUTONOMOUS / PROJECT · [Confidence]

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
      [Not applicable — AUTONOMOUS / PROJECT has no approval checkpoint. Human initiates but does not approve.]

BUILD HANDOFF PACK
Handoff status: [BUILD_READY or BLOCKED_FOR_EVIDENCE per RULE-14]
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
