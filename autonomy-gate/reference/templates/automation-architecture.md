# Template: Automation Architecture
**Verdict:** AUTONOMOUS / CODE_AGENT
**Section 20 additions applied:** EXPECTED OUTCOMES (Addition 2) · AUTONOMY EXPIRES WHEN (Addition 5)

---

This template is filled during Phase 2, Step 3 (RULE-12). Fill every section as a document — prose context, headers, formatted lists. No placeholder brackets in the final output. Presentable in a meeting without explanation.

---

```
AUTOMATION ARCHITECTURE
[Workflow Name] · AUTONOMOUS / CODE_AGENT · [Confidence]

[One paragraph: what this workflow does, why it qualifies for autonomous execution,
and what the operator is authorized to do. Name the terminal action explicitly.
State the evidence that justifies AUTONOMOUS — all four criteria passed, no gate triggered.]

TRIGGER
[What initiates execution — schedule, event, API call, file change, or system event.
Be specific: cron expression, webhook endpoint, file path pattern, or triggering condition.
Do not say "when needed" — name the exact trigger mechanism.]

INPUTS
• [System name] · [Data accessed] · [Permission level required]
• [System name] · [Data accessed] · [Permission level required]
[One bullet per input source. Minimum permission principle: only what is needed for this workflow.]

EXECUTION SEQUENCE
1. [Action] — [System] — [Output produced]
2. [Action] — [System] — [Output produced]
3. [Action] — [System] — [Output produced]
[Continue. Each step names the action, the system it executes in, and what it produces.
Last step is the terminal action — must match the terminal action identified in RULE-04.]

OUTPUTS
[Where results go, in what format, how they are named, retained for how long.
Name the specific destination: Slack channel, folder path, database table, email address.
Specify retention period.]

ERROR HANDLING
[What happens on failure at each step. Rollback procedure if applicable.
Who is alerted, on what channel, within what timeframe.
Do not say "errors are logged" without naming where and who checks them.]

AUDIT TRAIL
[What is logged on every run: minimum fields — timestamp, trigger source, input record count,
output location, terminal status, any anomalies detected.
Where the log is stored. Retention period.]

CONTROLS
Required before deployment:
• [Control 1 — e.g., audit log configured and tested]
• [Control 2 — e.g., rollback procedure documented and tested]
• [Control 3 — e.g., error alert routed to named owner]
• [Control 4 — e.g., permission scope limited to minimum required]

RECOMMENDED STACK
[One recommendation with rationale: Claude Code / Make / Zapier / n8n.
Why this stack for this workflow. What the operator needs to set up before first run.]

INFORMATION GAPS (if applicable)
[Present only if RULE-11 flagged more than three inferred fields.
List: field name · what was inferred · what evidence would confirm it.]

EXPECTED OUTCOMES
Completed:              [What done looks like — specific. Output delivered, log entry written, status emitted.]
Completed w/ warnings:  [What partial success looks like — output delivered but anomalies flagged.]
Needs review:           [What triggers a human checkpoint mid-run — specific threshold or condition.]
Blocked:                [What stops execution — named condition, not "an error occurred."]
Failed:                 [What constitutes failure and what follows — rollback, alert, retry logic.]

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
- [ ] Error rate exceeds [threshold — specify: e.g., >2% of runs produce incorrect output]
      [Applicable / Not applicable — rationale; specify threshold]
- [ ] [N] months pass without a recertification review — [specify date]
      [Applicable — specify recertification date and responsible role]
- [ ] The reviewer role changes or becomes vacant
      [Not applicable — AUTONOMOUS / CODE_AGENT has no reviewer role]
```
