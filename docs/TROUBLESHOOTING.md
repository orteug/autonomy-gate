# Troubleshooting

Use this when the Gate output surprises you.

---

## The Gate Gave LOW Confidence. Did I Fail?

No.

LOW confidence means the Gate could not populate one or more required fields.

Do this:

1. Read `Evidence gaps`.
2. Gather the missing information.
3. Re-run the Gate with the missing details included.

Do not argue with the verdict until you have filled the gaps.

---

## The Gate Gave HUMAN_ONLY. Can I Override It?

No.

If `GATE-2` or `GATE-3` applies, the terminal action cannot be delegated.

What you can do:

1. Read `WHAT WOULD CHANGE THIS VERDICT`.
2. Split preparation from execution.
3. Re-submit only the preparation phase.

Example:

```text
Do not automate vendor bank account authorization.
Do automate preparation of a verification packet for human review.
```

---

## The Gate Said PROJECT, But I Wanted Full Automation

PROJECT means human-initiated work inside Claude Project or ChatGPT Project.

It is right when:

- a human starts the run
- user provides data
- AI produces a document or analysis
- no schedule or external API is required

If you need scheduling, files, APIs, or system writes, re-submit the workflow with that requirement explicit. The Gate may route to COWORK or CODE_AGENT.

---

## The Gate Said COWORK, But I Do Not Have Cowork

Use the fallback note.

Usually this means:

- human starts each run manually
- input is pasted or uploaded
- output is delivered manually
- log is maintained manually

The autonomy verdict may stay the same, but the execution model changes.

---

## The Gate Said CODE_AGENT, But I Am Not Technical

CODE_AGENT means the workflow needs code, APIs, deterministic logic, tests, or enforcement.

Your options:

1. Hand the artifact to a developer.
2. Use Claude Code or Codex with the relevant surface guide.
3. Use the PROJECT fallback for manual analysis while implementation waits.

Do not pretend a Project can do live integration work.

---

## The Gate Misunderstood My Workflow

Check the Workflow Intake Snapshot.

If the snapshot is wrong, the verdict is based on the wrong workflow.

Fix by re-running with:

- clearer steps
- named systems
- terminal action
- failure consequence
- reversibility
- exception handling

Template:

```text
Correction: The terminal action is not [wrong action]. The terminal action is [correct action]. The workflow does not [wrong assumption]. It only [correct scope].
```

---

## The Gate Seems Too Cautious

It may be correct.

The Gate is designed to assign minimum justified autonomy, not maximum possible automation.

If the verdict feels too cautious:

1. Check evidence gaps.
2. Check hard gates.
3. Check terminal action.
4. Check cost of failure.
5. Re-run with stronger evidence if available.

Do not lower controls because the output is inconvenient.

---

## The Reviewer Field Is Unknown

For SUPERVISED workflows, this is a deployment blocker.

Do this:

1. Name the reviewer role.
2. Confirm they have blocking authority.
3. Define how approval is given.
4. Define what happens if they do not respond.
5. Re-run or update the Control Plan.

Bad:

```text
Reviewer: manager
```

Good:

```text
Reviewer: Support Lead on duty. Approval must be posted in the support ticket before refund issuance.
```

---

## My Workflow Has Two Terminal Actions

The Gate decomposed your workflow and issued a split verdict — naming two phases with different risk profiles.

This is not an error. It is the correct governance decision.

Example:

```text
"Compile the compliance data, format it, and submit the filing."
```

Phase 1 (compile and format) may receive `SUPERVISED / CODE_AGENT`.
Phase 2 (submit the filing) may receive `HUMAN_ONLY / NO_AI` — GATE-2.

What to do:

1. Treat each phase as a separate workflow for implementation purposes.
2. Submit Phase 1 as a governed automation. Implement what the Gate produces for it.
3. Implement Phase 2 as a human process with the Governance Memo as the SOP.
4. The phases operate separately. Phase 1 produces a ready-to-act package. A human owns Phase 2.

Do not try to combine the phases under the more permissive verdict. The restriction applies to the terminal action of each phase, not the whole workflow.

---

## My Reviewer Cannot Keep Up With The Volume

You received a SUPERVISED verdict, but the reviewer cannot realistically review at the volume or cadence the workflow runs at.

This is Human-in-the-Loop Theater — a checkpoint that exists on paper but cannot function in practice.

Options:

1. **Route only exceptions to review.** Design the automation to flag borderline cases. Standard, unambiguous cases proceed; edge cases go to the reviewer. This is almost always the correct solution.
2. **Designate a second reviewer.** Split the review volume between two named reviewers with a defined rotation. Both must be named in the Control Plan.
3. **Reduce the run cadence.** If the workflow runs more often than review capacity allows, reduce cadence until it matches.
4. **Re-scope the workflow.** Separate the cases that require judgment from the ones that are truly rule-based. Re-submit each scoped description as its own workflow. The rule-based cases may receive `AUTONOMOUS`. The judgment cases stay `SUPERVISED`.

Do not deploy a SUPERVISED workflow without a functioning checkpoint. A reviewer who cannot keep up is not a reviewer.

---

## The Output Has Placeholder Brackets

Final artifacts should not contain unresolved placeholders unless the placeholder is explicitly naming an evidence gap.

Do this:

1. Identify each bracketed field.
2. Decide whether it is an evidence gap or accidental incompletion.
3. If accidental, re-run with more complete input.
4. If evidence gap, assign an owner to fill it.

---

## The Workflow Changed After Approval

Re-run the Gate.

Any of these require re-assessment:

- workflow steps, inputs, or outputs changed materially
- the AI surface or model changed — any upgrade, platform migration, or tool change
- policy or compliance context changed
- an incident occurred — any output that caused unintended harm or required correction
- the error rate crossed the threshold named in the artifact's AUTONOMY EXPIRES WHEN section
- the recertification date in the artifact has passed
- the reviewer role changed or became vacant (SUPERVISED only)

Do not treat old approval as covering a changed workflow. If you cannot find an AUTONOMY EXPIRES WHEN section for the automation, it has not been governed by the Gate — re-submit as a fresh assessment.

---

## The Gate Says AUTONOMOUS. Does That Mean No Humans Are Needed?

No.

AUTONOMOUS means no approval checkpoint is required inside each run.

Humans still:

- initiate some runs
- configure the surface
- review logs
- respond to incidents
- re-certify the workflow
- update the Gate when context changes

---

## The Gate Says The Workflow Can Run, But My Tool Cannot Do It

Surface availability is separate from autonomy.

Example:

```text
AUTONOMOUS / COWORK
```

Means:

```text
This workflow can be autonomous if Cowork-like capabilities exist.
```

If you do not have that surface, use fallback or re-scope.

---

## The Gate Did Not Ask Clarifying Questions

Correct.

The Gate is designed not to ask clarifying questions. It proceeds with available evidence, names gaps, and routes conservatively.

If you want a better verdict, provide better input and re-run.

