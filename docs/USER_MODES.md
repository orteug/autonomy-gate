# User Modes — Starter Prompts and Paths

Ten modes. Each has one exact starter prompt. Copy, fill in the brackets, and submit.

---

## Mode 1 — Full Assessment (ASSESS)

Use when you have a workflow to evaluate.

**Starter prompt:**
```
[Describe the workflow in plain language. Include: what initiates it, what it does step by step, 
what systems or data it touches, how often it runs, what happens if it produces a wrong output, 
and whether the output can be corrected or undone.]
```

**What you get:**
- Workflow Intake Snapshot
- Autonomy Decision Packet with verdict, surface, and confidence level
- Full execution artifact with Build Handoff Pack
- OPERATOR DISPOSITION section for you to complete

**Evidence that produces HIGH confidence:**
Include failure consequence and reversibility in your description. Example additions:
- "If the output is wrong, we post a correction the next day — nothing is permanent."
- "The worst case is a delayed payment notice — reversible within 24 hours."

**Evidence-poor descriptions get LOW confidence and conservative routing. That is correct behavior — not a problem with the Gate.**

---

## Mode 2 — Quick Triage (TRIAGE)

Use when you want to know if a workflow is worth a full governance assessment.

**Starter prompt:**
```
Quick triage: [one or two sentences describing the workflow]. Is this worth a full assessment?
```

**What you get:**
- Preliminary verdict (autonomy level + surface)
- One-line rationale
- What a full assessment would add

**Does not produce:** Full artifact, Build Handoff Pack, or operator disposition section.

To proceed from triage to full assessment: submit the workflow as a full ASSESS prompt.

---

## Mode 3 — Resolve Missing Evidence (RESOLVE_EVIDENCE)

Use when a prior assessment returned `BLOCKED_FOR_EVIDENCE` or LOW confidence because of a specific missing value.

**Starter prompt:**
```
Evidence update for [workflow name]:
- [Field name]: [value]
- [Field name]: [value]
```

Example:
```
Evidence update for Weekly KPI Report:
- Error rate: under 2% per weekly run
- Recertification interval: 12 months
- Owner: ops team lead (Jamie Chen)
```

**What you get:**
- Updated snapshot with new provenance (`STATED`)
- Revised packet (new version)
- Updated Build Handoff Pack (`BLOCKED_FOR_EVIDENCE` → `BUILD_READY` only after affected-rule reassessment and architecture selection)

**Does not:** Restart the full assessment. Change the verdict unless new evidence directly affects scoring.

---

## Mode 4 — Compare Architecture Options (COMPARE_ARCHITECTURE)

Use when you want to understand why a specific surface was assigned, or evaluate an alternative.

**Precondition:** A packet must already exist for this workflow.

**Starter prompt:**
```
Architecture comparison for [workflow name]:
Compare [Surface A] vs [Surface B] for this workflow. What would each require?
```

Example:
```
Architecture comparison for Vendor Onboarding:
Compare Cowork vs Claude Code for this workflow. What would each require?
```

**What you get:**
- Feasibility of each surface
- Required controls for each
- Any disqualifying constraints
- Gate's primary recommendation with RULE-06 citation

---

## Mode 5 — Record Operator Disposition (APPROVE)

Use when you are ready to authorize, hold, revise, or reject a Build Handoff Pack.

**Starter prompt for APPROVE_FOR_BUILD:**
```
APPROVE_FOR_BUILD — [your name and role] — [date] — [packet version]
Rationale: [one or more sentences explaining why authorization is appropriate given the verdict, controls, and architecture]
```

**Starter prompt for HOLD_FOR_EVIDENCE:**
```
HOLD_FOR_EVIDENCE — [your name and role] — [date] — [packet version]
Missing: [what evidence is needed before you can authorize]
```

**Starter prompt for REVISE:**
```
REVISE — [your name and role] — [date] — [packet version]
Required change: [specific field or section that must change, and why]
```

**Starter prompt for REJECT:**
```
REJECT — [your name and role] — [date] — [packet version]
Rationale: [why this workflow should not be built at this time]
```

**What you get:**
- Completed OPERATOR DISPOSITION section with all required fields
- State update and next-step instruction

**The Gate does not select APPROVE_FOR_BUILD on your behalf. You must provide all four required fields.**

---

## Mode 6 — Request Revision (REVISE)

Use when a specific field or section in the assessment is wrong and needs to be corrected before disposition.

**Starter prompt:**
```
Revision request for [workflow name]:
[Field or section name] is wrong. The correct value is: [correct value].
```

Example:
```
Revision request for Vendor Onboarding:
Terminal action is wrong. The workflow ends at approval of the vendor record, not creation — 
a human approves before the record is finalized.
```

**What you get:**
- Corrected field with provenance `STATED`
- Re-run of affected rules
- Updated packet (new version)
- Updated artifact if verdict or surface changed

---

## Mode 7 — Review a Built Workflow (REVIEW_BUILD)

Use when a builder reports a change during implementation and you need to know if it requires a new Gate assessment.

**Starter prompt:**
```
Build review for [workflow name] (packet [version]):
The builder changed [describe what changed]. Does this require a new assessment?
```

Example:
```
Build review for Weekly KPI Report (packet v1):
The builder added a step that auto-posts to Slack directly instead of returning text for the operator to post. Does this require a new assessment?
```

**What you get:**
- IN_SCOPE or OUT_OF_SCOPE determination
- If OUT_OF_SCOPE: which boundary was crossed and what rule governs it
- If IN_SCOPE: confirmation and record of the review

---

## Mode 8 — Recertify an Expired Workflow (RECERTIFY)

Use when the AUTONOMY EXPIRES WHEN condition in a prior artifact has triggered.

**Starter prompt:**
```
Recertification for [workflow name]:
Expiration condition triggered: [state which condition from the artifact].
Current state of the workflow: [any changes since the last assessment].
```

**What you get:**
- New full assessment (new packet version, independent of prior)
- Delta summary: what changed from the prior assessment
- New execution artifact
- New OPERATOR DISPOSITION section (prior disposition does not carry forward)

---

## Mode 9 — Explain a Rule or Verdict (EXPLAIN)

Use when you want to understand a rule, gate condition, or why a specific verdict was issued.

**Starter prompt:**
```
Explain [rule, gate, or verdict element].
```

Examples:
- "Explain GATE-2."
- "Why did this workflow get SUPERVISED instead of AUTONOMOUS?"
- "What is the difference between BLOCKED_FOR_EVIDENCE and NOT_APPLICABLE in the Build Handoff Pack?"

**What you get:** A direct explanation with rule citations. The verdict is not changed.

---

## Mode 10 — Configure the Workspace (CONFIGURE)

Use at the start of a session to load your organization profile, or to update specific profile fields.

**Starter prompt (full profile):**
```
CONFIGURE: [paste your completed organization-profile.md content]
```

**Starter prompt (partial update):**
```
CONFIGURE update:
- Financial threshold: $25,000
- Default recertification interval: 6 months
- Off-limits domains: No AI involvement in performance reviews
```

**What you get:** Confirmation of which fields were received and how they will affect subsequent assessments.

---

## Quick Reference

| I want to... | Use mode |
|-------------|---------|
| Evaluate a new workflow | ASSESS |
| Get a quick read before committing to full governance | TRIAGE |
| Supply a missing value (error rate, owner, threshold) | RESOLVE_EVIDENCE |
| Understand why a surface was chosen | COMPARE_ARCHITECTURE |
| Authorize (or hold/reject) a Build Handoff Pack | APPROVE |
| Correct a wrong field in the assessment | REVISE |
| Check if a builder's change needs a new assessment | REVIEW_BUILD |
| Reassess a workflow after an expiration trigger | RECERTIFY |
| Understand a rule or why a verdict was issued | EXPLAIN |
| Load organizational context for the session | CONFIGURE |
