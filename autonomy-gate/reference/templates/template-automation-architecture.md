# Template: Automation Architecture
**Autonomy:** AUTONOMOUS  
**Architecture pattern:** Code-first, service, or integration
**Section 20 additions applied:** EXPECTED OUTCOMES (Addition 2) · AUTONOMY EXPIRES WHEN (Addition 5)

---

This template is filled during Phase 2, Step 3 (RULE-12). Fill every section as a document — prose context, headers, formatted lists. No placeholder brackets in the final output. Presentable in a meeting without explanation.

---

```
AUTOMATION ARCHITECTURE
[Workflow Name] · AUTONOMOUS · Code-first architecture · [Confidence]

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
- [ ] Error rate exceeds threshold — [if the workflow description names a threshold, use it exactly; if not, write: Not specified — operator must define before deployment. Do not invent a percentage.]
      [Applicable / Not applicable — rationale]
- [ ] Recertification interval passes — [if the workflow description names a date or interval, use it exactly; if not, write: Not specified — operator must define before deployment. Do not invent a date or cadence.]
      [Applicable — recertification date and responsible role if provided in input; otherwise Not specified]
- [ ] The reviewer role changes or becomes vacant
      [Not applicable — this AUTONOMOUS operating pattern has no approval checkpoint inside the run]

ARCHITECTURE OPTIONS
Generate the canonical PRIMARY, NATIVE_SUITE, LOW_CODE, CODE_FIRST, and VENDOR_NEUTRAL options required by RULE-10. Use one `OPT-N` heading per viable class. Every option states Execution architecture, Builder surface, Control fit, Implementation effort, Operating cost, Maintenance burden, Security fit, Portability, Skill requirements, and Source evidence. List every absent class under Omitted option classes with an evidence-based reason.

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
Generate complete `CLAUDE.md` and `AGENTS.md` configuration blocks appropriate to the named code-agent surface. Include allowed actions, prohibited actions, audit requirements, dry-run procedure, and one acceptance test. Do not leave placeholders. If a required value is absent, list it under REQUIRED BEFORE BUILD and generate the remaining grounded configuration.
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
