# Template: Stabilization Plan
**Verdict:** SOP_FIRST / NO_AI
**Section 20 additions applied:** EXPECTED OUTCOMES (Addition 2) · AUTONOMY EXPIRES WHEN (Addition 5)

---

This template is filled during Phase 2, Step 3 (RULE-12). Fill every section as a document — prose context, headers, formatted lists. No placeholder brackets in the final output. Presentable in a meeting without explanation.

A Stabilization Plan is not a rejection. It is the correct first action for a workflow that is not ready for AI authority. The documentation work named in this plan is the automation decision — not a prerequisite to the real work.

---

```
STABILIZATION PLAN
[Workflow Name] · SOP_FIRST / NO_AI · [Confidence]

[One paragraph: why automation is premature for this workflow, what instability
was identified, and what must be resolved before re-assessment.
Be specific: name the criterion that failed (exception rate, reversibility, observability,
or cost of failure) and what the description revealed. Do not say "the process is unstable" —
say what specifically makes it unstable.]

WHY AUTOMATION IS PREMATURE
Criterion that failed: [Exception rate / Reversibility / Observability / Cost of failure — name it]
Observed instability:  [Specific: what phrase or pattern in the description triggered SOP_FIRST.
                       Examples: "sometimes things are different depending on the client"
                       signals undocumented exception handling; "we handle edge cases manually"
                       means the exception path is not defined.]
Risk if automated now: [What would happen if this workflow were automated in its current state.
                       Concrete. Name the failure pattern from reference/risk-classification.md.]

STABILIZATION CHECKLIST
Complete in order. Do not advance to the next item until the current one is done.

[ ] Document the current process step by step — no gaps, no "it depends"
    [Name every step: what triggers it, who performs it, what they do, what they produce, what comes next.]

[ ] Identify every exception type: [list known exceptions from the description — or note "no exceptions identified; this is itself a gap"]
    [For each exception: what triggers it, who handles it, what they decide, what the possible outcomes are.]

[ ] Define the failure path
    [What happens when [specific step] produces unexpected output?
    Who is notified? Within what timeframe? What are the possible responses?
    If this cannot be answered, the process is not documented.]

[ ] Establish a baseline
    [Run the documented process manually and record: volume per cycle, frequency of deviations,
    exception rate per N runs, which steps produce the most variation.]

[ ] Run the documented process manually [N] times without deviation
    [N should be enough cycles to surface all exception types. A minimum of [10-20] runs is recommended
    before re-assessment. For high-volume workflows, a statistically meaningful sample applies.]

RE-EVALUATION CRITERIA
These are the specific, measurable conditions that permit re-submission to the Gate.
"When the process is stable" is not a criterion. Name what stable looks like.

• [Criterion 1 — e.g., All exception types are named in the SOP with defined handling paths]
• [Criterion 2 — e.g., Exception rate has been measured at <[X]% over [N] cycles]
• [Criterion 3 — e.g., Failure path is defined for every step that can produce unexpected output]
• [Criterion 4 — e.g., The SOP has been followed without deviation for [N] consecutive runs]

EARLIEST RE-EVALUATION
[Timeframe or milestone. Not "when ready" — name the earliest possible date or event.
Example: "After 30 consecutive days of documented manual execution and exception tracking,
re-submit to the Gate with the completed SOP and baseline metrics."]

INFORMATION GAPS (if applicable)
[Present only if RULE-11 flagged more than three inferred fields.
List: field name · what was inferred · what evidence would confirm it.]

EXPECTED OUTCOMES
[For a Stabilization Plan, expected outcomes describe the documentation milestones — not workflow execution.]
Completed:              [Stabilization checklist completed; re-evaluation criteria met; ready for Gate re-assessment.]
Completed w/ warnings:  [Most criteria met; one exception type remains undocumented; can proceed with that gap named.]
Needs review:           [Stabilization work reveals a more complex process than described — scope needs revisiting before continuing.]
Blocked:                [Owner cannot access the documentation or baseline data needed to complete the checklist.]
Failed:                 [Stabilization work stalls; re-assessment date passes without progress — escalate to process owner.]

Valid terminal statuses: COMPLETED · COMPLETED_WITH_WARNINGS · NEEDS_REVIEW · BLOCKED · FAILED · SKIPPED · TIMED_OUT

AUTONOMY EXPIRES WHEN
[For a Stabilization Plan, this section applies after re-assessment produces an AUTONOMOUS or SUPERVISED verdict.
It is included here as a forward-looking contract — so the re-assessment team has it ready.]

Mark each condition as applicable or not applicable. Do not omit conditions — note "not applicable" with rationale.

- [ ] The workflow's steps, inputs, or outputs change materially
      [Applicable — SOP_FIRST workflows are particularly vulnerable to FAIL-4 (Stale SOP Drift) once automation begins.]
- [ ] The AI surface or tool used changes
      [Applicable — note for future assessment]
- [ ] The policy or compliance context changes
      [Applicable / Not applicable — rationale]
- [ ] An incident occurs — any output that caused unintended harm or required correction
      [Applicable — always.]
- [ ] Error rate exceeds [threshold — to be specified at re-assessment]
      [Applicable — threshold will be set during re-assessment based on baseline data.]
- [ ] [N] months pass without a recertification review — [to be specified at re-assessment]
      [Applicable — recertification date to be set at re-assessment.]
- [ ] The reviewer role changes or becomes vacant
      [Applicable if re-assessment produces SUPERVISED verdict.]
```
