# Build Handoff Pack Contract

The Build Handoff Pack is the implementation-ready output of the Gate's Phase 2. It is the interface between the operator's governance decision and the builder's implementation. This document defines what a valid Build Handoff Pack must contain, what is forbidden, and what conditions determine its status.

---

## Pack Statuses

| Status | Meaning | When to use |
|--------|---------|-------------|
| `BUILD_READY` | All required content is fully generated and an architecture is selected; operator disposition `APPROVE_FOR_BUILD` can authorize implementation | Every referenced file, instruction block, test, control, and source-evidence citation is fully present |
| `BLOCKED_FOR_EVIDENCE` | Pack is structurally sound but specific operator-supplied values are required | Missing items are irreducible; all generatable content is already complete |
| `NOT_APPLICABLE` | No AI implementation pack is generated | Pairs with `HUMAN_ONLY`; the Governance Memo defines the human procedure and any safely decomposed preparatory work |

**BUILD_READY requires zero outstanding items.** If any file is described but not generated, any test is named but not written, architecture is unselected, or any value remains unresolved, the status is `BLOCKED_FOR_EVIDENCE`.

**BLOCKED_FOR_EVIDENCE is not a failed assessment.** The operator supplies missing evidence and the Gate reruns every affected rule. Promotion to `BUILD_READY` is never a text substitution.

Decision confidence and handoff status are separate. Confidence describes support for the autonomy verdict. Handoff status describes implementation completeness. A well-supported verdict can be `HIGH` confidence while its pack remains `BLOCKED_FOR_EVIDENCE`.

---

## What BUILD_READY Requires

A BUILD_READY Build Handoff Pack must contain:

### 0. Terminal-Action Boundary and Architecture Decision Record

State the exact authorized terminal action and the actions outside scope. Record the selected generated architecture option, selector identity or role, selection date, and rejected or omitted alternatives. The record must match the Autonomy Decision Packet and `ARCHITECTURE OPTIONS` block.

### 1. Complete Artifact Manifest

Every file the builder needs, listed with:

| Field | Requirement |
|-------|-------------|
| `Path` | Exact filename and location where the file should be created |
| `Purpose` | One-line description of what the file does |
| `Complete content` | The full file content, paste-ready — not a description, not a template with blanks |
| `Source evidence` | Which packet field or operator statement grounded this content |

No file may be described without its complete content. "Create a file that contains the project instructions" is not complete content. The file content itself must be present.

### 2. Assumptions

Explicit list of assumptions the Gate made when generating the pack. Each assumption is a claim about the workflow or organization that is grounded in the packet but not explicitly verified.

Example: "Assumed the CRM export format is consistent week-to-week. If format changes, the intake step must be updated."

### 3. Unresolved Dependencies

If any item could not be fully generated without organizational input that the Gate does not have, that item is listed here with:
- What is missing
- What the operator must supply
- How the builder should proceed once it is supplied

These are the only items that appear in the `BLOCKED_FOR_EVIDENCE` list. Everything else must be generated.

### 4. Prohibited Actions

Explicit list of what the implementation may not do, stated as implementation constraints — not as aspirational guidelines. Example: "This workflow may not initiate any outbound API call beyond the named read-only endpoints. Any additional API call requires a new Gate assessment."

### 5. Acceptance Tests

Complete test cases — not a request to write tests. Each acceptance test includes:
- Setup state
- Input or trigger
- Expected output or behavior
- Pass/fail criterion

### 6. Expiration Triggers

The conditions under which the autonomy authorization expires and recertification is required. Stated as observable events — not as policy intentions.

### 7. Rollback and Stop Conditions

What happens when the workflow must stop. Includes:
- Trigger conditions (error rate exceeded, approval timeout, system unavailable)
- Steps the builder must implement to halt cleanly
- What cannot be rolled back (named explicitly)

### 8. Permissions, Credentials, Controls, and Checkpoints

State least-privilege permissions, credential ownership and storage, deterministic controls, and every blocking human checkpoint. If no checkpoint applies, say so with a rationale. Model instructions do not count as deterministic enforcement.

### 9. Logging and Audit

State events and fields logged, storage location, retention, access, and review responsibility. Logs must make terminal-action execution and approval behavior independently reviewable.

### 10. Deployment Sequence

Give the ordered path from non-production setup through acceptance testing, operator approval, builder acknowledgement, and activation. No production activation occurs inside the Gate.

### 11. Version Invalidation and Tool Alternatives

Name material changes that create a new packet version and invalidate prior architecture selection, operator disposition, and builder acknowledgement. Include the selected tool path and at least one viable fallback or a capability-neutral alternative that preserves controls.

### 12. Builder Acknowledgement

Require the builder to confirm terminal-action parity, control implementation, files, dependencies, acceptance evidence, and scope-change behavior before implementation begins.

---

## What Is Forbidden

The following are not permitted in a `BUILD_READY` Build Handoff Pack:

| Forbidden | Why |
|-----------|-----|
| Blank templates | The builder must not complete governance templates — only the operator does |
| Bracketed placeholders (`[fill in]`, `[your value here]`) | Every placeholder means the pack is incomplete |
| Instructions to "customize" | The builder implements the specification as written; customization requires operator disposition |
| File names without full content | Describing a file is not generating it |
| Instructions for the builder to determine policy | Policy is set by the operator via the Gate |
| Claims that a model prompt enforces a control | Model prompts are guidance; enforcement requires deterministic code or configuration |

---

## What BLOCKED_FOR_EVIDENCE Generates

A BLOCKED_FOR_EVIDENCE pack still generates all content the Gate can produce without the missing values. The builder receives:

- All files that can be fully generated
- All acceptance tests that do not depend on missing values
- Architecture description with named gaps
- Clear statement of exactly what the operator must supply and in what format

The `BLOCKED_FOR_EVIDENCE` list contains only irreducible missing inputs. It does not contain items the Gate chose not to generate. If the Gate can generate it, it must.

Example: A `BLOCKED_FOR_EVIDENCE` pack for a SUPERVISED workflow includes a complete `CLAUDE.md` with the approval checkpoint structure, while naming the missing error-rate threshold and recertification interval as organizational evidence.

## What NOT_APPLICABLE Generates

`NOT_APPLICABLE` is a refusal of AI execution for the prohibited terminal action, not an empty response. It includes:

- A complete human operating procedure with owner, verification evidence, decision criteria, escalation, recordkeeping, and audit check
- The exact prohibited terminal action and gate basis
- Safe decomposition opportunities: bounded preparation work AI may perform without authorizing or executing the terminal action, or a grounded explanation that none is safe
- Acceptance checks for the human procedure
- Version invalidation and reassessment triggers

No AI deployment manifest is generated for the prohibited action.

## Material-Change Invalidation

A change to terminal action, architecture, controls, permissions, credentials, data flow, tool capabilities, approval behavior, or prohibited actions creates a new packet version. It invalidates the prior architecture selection, operator disposition, and builder acknowledgement. The affected rules must rerun before implementation resumes.

---

## Manifest File Template

Each file in the artifact manifest is presented in this format:

```
── [filename] ──────────────────────────────────────
Purpose: [one line]
Source:  [packet field or operator statement that grounded this content]

[Complete file content — paste-ready, no placeholders]
────────────────────────────────────────────────────
```

The builder copies this content verbatim. No editing required. If editing is required, the pack is incomplete.

---

## Builder Responsibilities

When receiving a BUILD_READY Build Handoff Pack:

1. Compare the terminal action in the pack against what you intend to build. They must match exactly.
2. Confirm you can implement all required controls as listed. If a control cannot be implemented, stop and return to the operator.
3. Do not expand scope beyond the terminal action boundary.
4. If a tool substitution is required that changes the controls (e.g., replacing an approved API with direct database access), stop. A new Gate assessment is required.
5. Complete the Builder Acknowledgement before beginning implementation.

The builder may not proceed without an `APPROVE_FOR_BUILD` operator disposition recorded in the artifact.

---

## References

- Operator Disposition: `autonomy-gate/reference/operator-disposition.md`
- Builder Acknowledgement: `autonomy-gate/reference/builder-acknowledgement.md`
- Workflow Architecture Contract: `autonomy-gate/reference/workflow-architecture-contract.md`
- User Journey Contract (REVIEW_BUILD mode): `autonomy-gate/reference/user-journey-contract.md`
- Governed by RULE-14 and RULE-15.
