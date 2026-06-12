# Builder Acknowledgement

The Builder Acknowledgement is completed by the implementer before any code is written or configuration is applied. It confirms the builder has read the Build Handoff Pack, understands the scope, and accepts the implementation constraints.

A signed Builder Acknowledgement is required before implementation begins. The operator retains a copy alongside the governance artifact.

---

## When to Complete This

Complete this acknowledgement after:
1. Receiving a Build Handoff Pack with `APPROVE_FOR_BUILD` operator disposition
2. Reading the full execution artifact and Build Handoff Pack
3. Before writing any code, configuring any system, or applying any setting

Do not proceed if:
- The operator disposition is still `PENDING`
- The Build Handoff Pack status is `BLOCKED_FOR_EVIDENCE` (missing values must be resolved first)
- Any required control cannot be implemented as specified (stop and return to operator)

---

## Acknowledgement Form

```
BUILDER ACKNOWLEDGEMENT

Workflow:        [workflow name from artifact]
Packet version:  [version this acknowledgement covers — e.g., v1]
Builder:         [name, role, or team]
Date:            [date completed]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

SECTION 1 — SCOPE CONFIRMATION

Terminal action (from packet):
[Restate the terminal action exactly as written in the Autonomy Decision Packet]

Terminal action (as I will implement it):
[Describe how you will implement the terminal action — must match above exactly]

If these differ: STOP. Return to the operator. A new Gate assessment is required.

Allowed actions:
[List what the implementation may do]

Prohibited actions:
[List what the implementation may not do — copied from the Pack]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

SECTION 2 — CONTROL CONFIRMATION

Required controls (from packet):
[List each required control and how you will implement it]

Control | Implementation approach
------- | ------------------------
[Control 1] | [Implementation — deterministic code/config, not prompt]
[Control 2] | [Implementation]

Approval checkpoint (if SUPERVISED):
[ ] The approval checkpoint is blocking — the terminal action cannot execute without it
[ ] The approver identity and timestamp are logged
[ ] Rejection handling is implemented

If any required control cannot be implemented: STOP. Identify the control below and return to the operator.

Controls I cannot implement as specified:
[None — or list with explanation]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

SECTION 3 — IMPLEMENTATION PLAN

File-by-file plan:
[List every file you will create or modify, with a one-line description of the change]

File | Action | Description
---- | ------ | -----------
[filename] | Create/Modify | [what it will contain]

Dependencies and prerequisites:
[What must exist before implementation can begin — credentials, permissions, infrastructure]

Estimated implementation order:
[Order in which files/components will be built]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

SECTION 4 — ACCEPTANCE CRITERIA MAP

[For each acceptance criterion in the Build Handoff Pack, name how you will verify it]

Criterion | Verification method
--------- | -------------------
[Criterion 1] | [Test, log, screenshot, or observable output]
[Criterion 2] | [Verification method]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

SECTION 5 — UNRESOLVED ITEMS

Unresolved items from the `BLOCKED_FOR_EVIDENCE` list that the operator has now supplied:
[List items + values supplied, or "None — pack was BUILD_READY"]

Items I cannot resolve without operator input:
[None — or list with explanation; operator must respond before implementation proceeds]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

SECTION 6 — SCOPE CHANGE COMMITMENT

I understand that:
- My authorization covers only the terminal action and scope named in the packet
- If implementation requires expanding scope, substituting a tool that changes the controls, or adding an action not named in the Build Handoff Pack, I must stop and return to the operator
- A scope change requires a new Gate assessment before I may proceed
- I may not authorize scope changes myself

[ ] I accept these constraints

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

SECTION 7 — IMPLEMENTATION EVIDENCE (Completed after build)

[This section is completed after implementation. The builder provides evidence for each acceptance criterion before declaring the build complete.]

Criterion | Evidence
--------- | --------
[Criterion 1] | [Test result, log excerpt, screenshot path, or observable output]

Scope changes encountered during implementation:
[ ] None
[ ] Yes — [describe; stop and return to operator if controls changed]

Build declared complete by:
Name:   [builder name]
Date:   [date]
Notes:  [any implementation notes relevant to the operator]
```

---

## What Happens After

The builder submits the completed acknowledgement (Sections 1–6) to the operator before implementation begins. The operator reviews it alongside the governance artifact.

After implementation, the builder completes Section 7 and returns it to the operator. The operator reviews the evidence against the acceptance criteria before marking the workflow as operational.

If a scope change was encountered during implementation: the builder stops, notifies the operator, and does not proceed. A new Gate assessment is required before the changed scope is authorized.
