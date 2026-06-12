# Build Handoff Pack Contract

The Build Handoff Pack is the implementation-ready output of the Gate's Phase 2. It is the interface between the operator's governance decision and the builder's implementation. This document defines what a valid Build Handoff Pack must contain, what is forbidden, and what conditions determine its status.

---

## Pack Statuses

| Status | Meaning | When to use |
|--------|---------|-------------|
| `READY` | All required content is fully generated; operator disposition `APPROVE_FOR_BUILD` can authorize implementation | Every referenced file, instruction block, test, and control is fully present as paste-ready content |
| `BLOCKED` | Pack is structurally sound but specific operator-supplied values are required | Missing items are irreducible — the Gate cannot generate them without real organizational input; all generatable content is already complete |
| `NOT_APPLICABLE` | No pack is generated | Pairs with HUMAN_ONLY / NO_AI verdict; implementation artifact is a Governance Memo only |

**READY requires zero outstanding items.** If any file is described but not generated, any test is named but not written, or any value is marked for the operator to fill — the status is `BLOCKED`, not `READY`.

**BLOCKED is not a failure.** It means the governance architecture is complete and the builder can begin planning. The operator supplies the missing values; the builder does not re-assess. When the operator supplies all BLOCKED items, the pack becomes READY without re-running the Gate.

---

## What READY Requires

A READY Build Handoff Pack must contain:

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

These are the only items that appear in the BLOCKED list. Everything else must be generated.

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

---

## What Is Forbidden

The following are not permitted in a READY Build Handoff Pack:

| Forbidden | Why |
|-----------|-----|
| Blank templates | The builder must not complete governance templates — only the operator does |
| Bracketed placeholders (`[fill in]`, `[your value here]`) | Every placeholder means the pack is incomplete |
| Instructions to "customize" | The builder implements the specification as written; customization requires operator disposition |
| File names without full content | Describing a file is not generating it |
| Instructions for the builder to determine policy | Policy is set by the operator via the Gate |
| Claims that a model prompt enforces a control | Model prompts are guidance; enforcement requires deterministic code or configuration |

---

## What BLOCKED Generates

A BLOCKED pack still generates all content the Gate can produce without the missing values. The builder receives:

- All files that can be fully generated
- All acceptance tests that do not depend on missing values
- Architecture description with named gaps
- Clear statement of exactly what the operator must supply and in what format

The BLOCKED list contains only irreducible missing inputs. It does not contain items the Gate chose not to generate. If the Gate can generate it, it must.

Example: A BLOCKED pack for a SUPERVISED workflow includes a complete `CLAUDE.md` with the approval checkpoint structure, but marks the error-rate threshold and recertification interval as BLOCKED because those are organizational policy decisions the operator must supply.

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

When receiving a READY Build Handoff Pack:

1. Compare the terminal action in the pack against what you intend to build. They must match exactly.
2. Confirm you can implement all required controls as listed. If a control cannot be implemented, stop and return to the operator.
3. Do not expand scope beyond the terminal action boundary.
4. If a tool substitution is required that changes the controls (e.g., replacing an approved API with direct database access), stop. A new Gate assessment is required.
5. Complete the Builder Acknowledgement before beginning implementation.

The builder may not proceed without an `APPROVE_FOR_BUILD` operator disposition recorded in the artifact.

---

## References

- Operator Disposition: `autonomy-gate/reference/operator-disposition.md`
- Builder Acknowledgement: `autonomy-gate/reference/templates/template-builder-acknowledgement.md`
- Workflow Architecture Contract: `autonomy-gate/reference/workflow-architecture-contract.md`
- User Journey Contract (REVIEW_BUILD mode): `autonomy-gate/reference/user-journey-contract.md`
- Governed by RULE-14 and RULE-15.
