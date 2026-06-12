# Template: Cowork Project Config
**Verdict:** AUTONOMOUS / COWORK
**Section 20 additions applied:** EXPECTED OUTCOMES (Addition 2) · AUTONOMY EXPIRES WHEN (Addition 5)

---

This template is filled during Phase 2, Step 3 (RULE-12). Fill every section as a document — prose context, headers, formatted lists. No placeholder brackets in the final output. Presentable in a meeting without explanation.

---

```
COWORK PROJECT CONFIG
[Workflow Name] · AUTONOMOUS / COWORK · [Confidence]

[One paragraph: what this workflow does inside Claude Cowork, what it reads,
what it writes, and how it runs on schedule without human initiation.
State the terminal action explicitly. State why no GATE conditions trigger.
Note: if Cowork is unavailable, name the fallback surface and adjustments required.]

LOCAL FOLDER STRUCTURE
  /inputs     [What lands here and from where. Source system, file format, naming convention.]
  /outputs    [What the operator writes. Format, naming convention, retention period.]
  /logs       [What is recorded on every run. Minimum fields: timestamp, run ID, terminal status, input count, output location, errors.]

SCHEDULED TASK
Frequency:          [Daily / Weekly / other — specific schedule, not "regularly"]
Trigger condition:  [Cron expression or event trigger — specific]
Expected runtime:   [Approximate duration per run]
Run window:         [Time of day or day of week — when execution is acceptable]

EXECUTION SEQUENCE
1. [Action] — [System or folder] — [Output produced]
2. [Action] — [System or folder] — [Output produced]
3. [Action] — [System or folder] — [Output produced]
[Continue. Last step is the terminal action — must match RULE-04.]

AUTHORIZED ACTIONS
The operator is authorized to:
• [Specific action 1 — e.g., read files from /inputs]
• [Specific action 2 — e.g., write files to /outputs]
• [Specific action 3 — e.g., write a log entry to /logs]
[List only what this workflow requires. Minimum permission principle applies (FAIL-5).]

PROHIBITED ACTIONS
The operator may not, under any condition:
• [Prohibited action 1 — e.g., send external emails or messages without a human checkpoint]
• [Prohibited action 2 — e.g., modify files outside /inputs and /outputs]
• [Prohibited action 3 — e.g., access systems not listed in INPUTS above]
[Every COWORK config must name at least three prohibited actions. Scope limits prevent FAIL-5.]

FALLBACK IF COWORK IS UNAVAILABLE
[Per RULE-06 surface fallback logic: if Cowork is unavailable, state the nearest alternative surface
and the specific adjustments required. Do not omit this section.]
Nearest alternative: PROJECT (Claude Project)
Adjustments required:
• [Adjustment 1 — e.g., human initiates each run manually on the scheduled cadence]
• [Adjustment 2 — e.g., input files are pasted into the session rather than read from /inputs]
• [Adjustment 3 — e.g., output is copied manually to the destination]

INFORMATION GAPS (if applicable)
[Present only if RULE-11 flagged more than three inferred fields.
List: field name · what was inferred · what evidence would confirm it.]

EXPECTED OUTCOMES
Completed:              [What done looks like — output written to /outputs, log entry written, COMPLETED status emitted.]
Completed w/ warnings:  [What partial success looks like — run finished but anomalies logged.]
Needs review:           [What triggers a NEEDS_REVIEW status — specific threshold or condition requiring human attention before next run.]
Blocked:                [What stops execution before completion — named condition.]
Failed:                 [What constitutes failure — FAILED status emitted, alert sent, no output written.]

Valid terminal statuses: COMPLETED · COMPLETED_WITH_WARNINGS · NEEDS_REVIEW · BLOCKED · FAILED · SKIPPED · TIMED_OUT

AUTONOMY EXPIRES WHEN
Mark each condition as applicable or not applicable. Do not omit conditions — note "not applicable" with rationale.

- [ ] The workflow's steps, inputs, or outputs change materially
      [Applicable / Not applicable — rationale]
- [ ] The AI surface or tool used changes (Cowork version, model upgrade, connector change)
      [Applicable — Cowork connectors are in preview; any connector change requires reassessment.]
- [ ] The policy or compliance context changes
      [Applicable / Not applicable — rationale]
- [ ] An incident occurs — any output that caused unintended harm or required correction
      [Applicable — always. Any incident triggers reassessment.]
- [ ] Error rate exceeds threshold — [if the workflow description names a threshold, use it exactly; if not, write: Not specified — operator must define before deployment. Do not invent a percentage.]
      [Applicable — use threshold from input only; do not invent a value]
- [ ] Recertification interval passes — [if the workflow description names a date or interval, use it exactly; if not, write: Not specified — operator must define before deployment. Do not invent a date or cadence.]
      [Applicable — recertification date and responsible role if provided in input; otherwise Not specified]
- [ ] The reviewer role changes or becomes vacant
      [Not applicable — AUTONOMOUS / COWORK has no approval checkpoint.]

BUILD HANDOFF PACK
Deployment status: [READY or BLOCKED per RULE-14]
Generate the exact folder tree, complete project instructions, run trigger, terminal-status log format, failure behavior, and one non-production acceptance run. Do not leave placeholders. If schedule, path, or connector details are missing, name them under REQUIRED BEFORE BUILD and configure manual trigger as the conservative fallback.
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
