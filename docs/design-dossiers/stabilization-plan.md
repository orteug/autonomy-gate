# Design Dossier — Stabilization Plan

**Artifact type:** Stabilization Plan  
**Verdict:** SOP_FIRST  
**Architecture status:** Not selected — no architecture is authorized until stabilization is complete  
**Status:** Undesigned — needs full layout treatment

---

## What This Document Is

The Stabilization Plan is the execution artifact the Gate produces when a workflow is not ready for AI authority. The verdict is SOP_FIRST — meaning the process must be documented and run manually before any automation decision is made. This is not a rejection. It is the correct first action when a workflow has unresolved exceptions, undefined failure paths, or no baseline data.

The Stabilization Plan is fundamentally different from every other artifact type:
- There is no architecture selection (no OPT-N blocks)
- The BUILD HANDOFF PACK is always BLOCKED_FOR_EVIDENCE
- The primary deliverable is a work checklist, not a build specification
- The document describes what must be done before the Gate can be run again — not what the builder should build now

---

## Non-Negotiable Sections (in document order)

### 1. Document Header

Must display:
- Document type label: `STABILIZATION PLAN`
- Workflow name
- Verdict: `SOP_FIRST`
- Status: `Architecture not yet authorized`
- Confidence level: `HIGH`, `MEDIUM`, or `LOW`

The "Architecture not yet authorized" status must be visually present in the header — it distinguishes this document from every other artifact type and must be immediately clear to anyone who opens it.

### 2. Narrative Description

One paragraph. Must state:
- Why automation is premature for this workflow
- What instability was identified (specific — not "the process is unstable")
- What must be resolved before re-assessment

### 3. WHY AUTOMATION IS PREMATURE

Three required fields:

- **Criterion that failed** — must name the specific autonomy criterion: Exception rate / Reversibility / Observability / Cost of failure. Not a paraphrase — one of these four.
- **Observed instability** — the specific phrase or pattern in the workflow description that triggered SOP_FIRST. Quoted or closely paraphrased. Examples: "sometimes things are different depending on the client" signals undocumented exception handling; "we handle edge cases manually" means the exception path is undefined.
- **Risk if automated now** — what would happen if this workflow were automated in its current state. Concrete. Names the failure pattern from the risk classification framework (not invented).

This section is a diagnostic callout. It answers the operator's implicit question: "Why did I get this instead of a build artifact?"

### 4. STABILIZATION CHECKLIST

Ordered checkbox list. Must be completed in sequence — the operator cannot advance to the next item until the current one is done. Five required items:

- `[ ]` Document the current process step by step — no gaps, no "it depends"  
  *(Names every step: what triggers it, who performs it, what they do, what they produce, what comes next)*

- `[ ]` Identify every exception type  
  *(For each exception: what triggers it, who handles it, what they decide, what the possible outcomes are)*

- `[ ]` Define the failure path  
  *(For each critical step: what happens when unexpected output is produced, who is notified, within what timeframe, what the possible responses are)*

- `[ ]` Establish a baseline  
  *(Run the documented process manually and record: volume per cycle, frequency of deviations, exception rate per N runs, which steps produce the most variation)*

- `[ ]` Run the documented process manually N times without deviation  
  *(N is specified based on volume — minimum 10-20 runs recommended. High-volume workflows use a statistically meaningful sample.)*

The checkboxes must render as interactive HTML checkboxes or as clearly styled checkbox elements. The sequential dependency (do not advance until current is done) should be visually communicated — numbered list with checkbox, not just bullets.

### 5. RE-EVALUATION CRITERIA

Bulleted list of specific, measurable conditions that permit re-submission to the Gate. Every entry is an observable, measurable state — not a judgment call.

"When the process is stable" is not a criterion. Entries must name what stable looks like in measurable terms:
- Exception types documented with defined handling paths ✓
- Exception rate measured below a specific threshold over N cycles ✓
- Failure path defined for every step that can produce unexpected output ✓
- SOP followed without deviation for N consecutive runs ✓

At least four criteria required.

### 6. EARLIEST RE-EVALUATION

Single field. Names the earliest possible date or milestone for re-submission. Not "when ready" — a specific timeframe or event. Example: "After 30 consecutive days of documented manual execution and exception tracking, re-submit to the Gate with the completed SOP and baseline metrics."

### 7. INFORMATION GAPS *(conditional)*

Present only if more than three fields were inferred. Same format as all artifact types.

### 8. EXPECTED OUTCOMES

For a Stabilization Plan, expected outcomes describe documentation milestones — not workflow execution. Five states:
- `Completed` — Stabilization checklist complete; re-evaluation criteria met; ready for Gate re-assessment
- `Completed with warnings` — Most criteria met; one exception type remains undocumented; can proceed with that gap named
- `Needs review` — Stabilization work reveals a more complex process than described; scope needs revisiting
- `Blocked` — Owner cannot access the documentation or baseline data needed to complete the checklist
- `Failed` — Stabilization work stalls; re-assessment date passes without progress — escalate to process owner

Valid terminal status list:
`COMPLETED · COMPLETED_WITH_WARNINGS · NEEDS_REVIEW · BLOCKED · FAILED · SKIPPED · TIMED_OUT`

### 9. AUTONOMY EXPIRES WHEN

Seven checkbox conditions. For a Stabilization Plan, this section is forward-looking — it applies after re-assessment produces an AUTONOMOUS or SUPERVISED verdict. It is included here so the re-assessment team has it ready.

1. Workflow steps, inputs, or outputs change materially *(always applicable — SOP_FIRST workflows are especially vulnerable to drift once automation begins)*
2. AI surface or tool changes *(note for future assessment)*
3. Policy or compliance context changes
4. An incident occurs *(always applicable)*
5. Error rate exceeds threshold *(do not invent a percentage — value is set during re-assessment)*
6. Recertification interval passes *(do not invent a date — interval is set during re-assessment)*
7. Reviewer role changes or becomes vacant *(applicable if re-assessment produces SUPERVISED)*

Items 5 and 6 will always read "Not yet specified — defined at re-assessment." This must be rendered clearly, not left as a blank.

### 10. BUILD HANDOFF PACK

**Always BLOCKED_FOR_EVIDENCE.** No architecture is authorized. The 20 fields are still present — they are the evidence requirements the operator must satisfy before re-assessment can produce a build-ready artifact.

The pack's purpose here is to show what is missing — not what is ready. The `Handoff status: BLOCKED_FOR_EVIDENCE` state must be visually distinct from a `BUILD_READY` pack. This is not a buildable document.

Same 20 fields in the same order as all artifact types:
1. Handoff status *(always BLOCKED_FOR_EVIDENCE)*
2. Terminal-action boundary
3. Architecture decision record *(NOT_APPLICABLE — no architecture selected)*
4. Permissions and credentials
5. Deterministic controls
6. Human checkpoints
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

The Exact next action field (20) will always point to the first uncompleted item in the STABILIZATION CHECKLIST. There is no builder here — the person who acts next is the process owner.

### 11. OPERATOR DISPOSITION

Always last. Always unselected:
- `[ ] APPROVE_FOR_BUILD`
- `[ ] REVISE`
- `[ ] HOLD_FOR_EVIDENCE`
- `[ ] REJECT`

Note: APPROVE_FOR_BUILD is structurally blocked for SOP_FIRST — no architecture has been selected, so there is nothing to approve for build. The Gate will note this. The checkbox remains present but the gate recommendation will be HOLD_FOR_EVIDENCE.

Operator fills: Name / role, Date, Packet version, Rationale.

---

## Structural Notes for Design

- **No ARCHITECTURE OPTIONS section.** This is the only artifact type that omits it. The absence is intentional and should not look like an omission error — the document may benefit from a brief note where OPT-N blocks would normally appear, stating that architecture selection occurs at re-assessment.
- **STABILIZATION CHECKLIST is the functional core.** It needs the same visual weight the APPROVAL CHECKPOINT gets in the Control Plan. Ordered, numbered checkboxes with clear sequential framing. Not a simple bulleted list.
- **BLOCKED_FOR_EVIDENCE state in the BUILD HANDOFF PACK** needs a visual treatment that reads as "this is a placeholder" — different from the BUILD_READY pack in the Project Setup Brief. Consider a muted or greyed treatment, a lock icon state, or a clear status badge at the top of the pack.
- **WHY AUTOMATION IS PREMATURE** is a diagnostic callout — 3 fields explaining the failure. It can be compact and read as a findings block. It is not prescriptive, it is diagnostic.
- The SOP_FIRST verdict communicates "not yet" — the document should feel like a structured action plan, not a completed assessment. The checklist state should drive this feeling — there are boxes to check, work to do.
- The forward-looking AUTONOMY EXPIRES WHEN section with "not yet specified" entries for threshold and recertification is unique to this artifact type. Those entries need to be clearly labeled as pending, not blank.

---

## Verdict Color

`SOP_FIRST` — `#2E5B8C`

All accent elements for this document use this color.
