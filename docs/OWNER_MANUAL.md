# The Autonomy Gate Owner Manual

Canonical operator documentation for assessing, specifying, authorizing, and governing AI-enabled workflows.

This Markdown file is the editable source for generated field-manual PDFs. Runtime authority remains in `autonomy-gate/rules.md` and `autonomy-gate/reference/operating-contract.md`.

## 1. Purpose And Authority

The Gate answers:

```text
Should AI participate in this recurring organizational workflow, how much authority is justified, and what must be built before it may operate?
```

It produces a defensible autonomy decision, architecture alternatives, and a Build Handoff Pack. It does not build, deploy, approve, or run the workflow.

The Gate may recommend. The operator selects architecture and records disposition. The builder implements only an approved pack. Legal, security, compliance, finance, HR, and other accountable authorities retain their normal responsibilities.

## 2. First Use

Create a persistent Claude Project or supported ChatGPT Project and upload the 16 runtime files listed in `START_HERE.md`. A Claude Project also receives `artifact-rendered.html`, for 17 uploaded files total. Set this instruction:

```text
You are The Autonomy Gate. Follow identity.md, rules.md, and operating-contract.md. Produce the canonical Markdown governance record, then create a separate rendered Claude Artifact containing the complete self-contained HTML Execution Artifact using artifact-rendered.html. Do not print HTML source in chat. The rendered Artifact must preserve every substantive section and exact canonical value from the Markdown. If Artifact rendering is unavailable, state ARTIFACT_RENDERING_UNAVAILABLE and return Markdown only.
```

The rendered Claude Artifact is the operator-facing deliverable. The Markdown record remains authoritative for validation and audit. Presentation may change; meaning may not.

Use five primary commands:

| Command | Purpose |
|---|---|
| `ASSESS` | Evaluate a new workflow |
| `RESOLVE EVIDENCE` | Supply facts named as missing |
| `SELECT ARCHITECTURE` | Record an operator choice from generated options |
| `APPROVE` | Record disposition after reviewing a complete pack |
| `REVIEW BUILD` | Compare implementation changes with authorization |

Advanced modes include `TRIAGE`, `REVISE`, `RECERTIFY`, `EXPLAIN`, and `CONFIGURE`.

## 3. Describe The Workflow

Submit free-form prose. Do not choose a template. Strong input names:

- Trigger and initiating actor
- Ordered actions
- Systems and data touched
- Terminal action, meaning the final thing that executes
- Failure consequence
- Reversibility
- Exception behavior
- Existing audit trail

The Gate never asks a clarifying question. Missing facts become `UNKNOWN`, cap confidence when decision-material, and appear as evidence gaps.

### Verify Intake Before Verdict

Read the output in this order:

1. Workflow Intake Snapshot
2. Terminal action
3. Autonomy Decision Packet
4. Architecture options
5. Execution artifact and Build Handoff Pack
6. State-aware next action
7. Operator disposition

If the terminal action is wrong, use `REVISE`. A refund recommendation and a refund transaction are different workflows because only one moves money.

## 4. Interpret Autonomy

| Autonomy | Meaning |
|---|---|
| `AUTONOMOUS` | AI may execute the bounded workflow without an approval checkpoint inside the run |
| `SUPERVISED` | AI prepares work; a blocking human approval is required before the terminal action |
| `SOP_FIRST` | The process is too unstable or undocumented to specify safely |
| `HUMAN_ONLY` | The terminal action may not be delegated to AI |

The Gate scores reversibility, observability, exception rate, and cost of failure. It then applies hard gates to the terminal action:

| Gate | Condition | Effect |
|---|---|---|
| `GATE-1` | Initiates money movement | At least `SUPERVISED` |
| `GATE-2` | Makes an irreversible external commitment | `HUMAN_ONLY` |
| `GATE-3` | Changes permissions or access controls | `HUMAN_ONLY` |
| `GATE-4` | Publishes regulated or reputationally sensitive material | At least `SUPERVISED` |
| `GATE-5` | Acts without audit trail or rollback | At least `SUPERVISED` until controls exist |

Confidence describes evidence supporting the decision. Handoff status describes implementation completeness. A `HIGH` confidence decision may still be `BLOCKED_FOR_EVIDENCE`.

## 5. Compare And Select Architecture

The assessment platform does not determine the production design. The packet keeps three roles separate:

| Field | Meaning |
|---|---|
| Assessment surface | Where the Gate ran |
| Execution architecture | How the workflow operates in production |
| Builder surface | Who or what implements it |

For `AUTONOMOUS` and `SUPERVISED` results, the Gate generates viable classes from:

- `PRIMARY`
- `NATIVE_SUITE`
- `LOW_CODE`
- `CODE_FIRST`
- `VENDOR_NEUTRAL`

Every option compares control fit, implementation effort, operating cost, maintenance burden, security fit, portability, skill requirements, and source evidence. Every absent class requires an evidence-based omission reason.

The Gate recommends but does not select. Record the generated option ID, selector identity or role, and date. Until selection, the pack cannot be `BUILD_READY`.

Named tool claims require official source evidence and a verification date. When the organization stack is unknown, use capability-first architecture rather than inventing products.

## 6. Resolve Evidence

`BLOCKED_FOR_EVIDENCE` means the decision may be sound while irreducible organizational inputs remain. Typical examples include:

- Approval authority
- Approved credential mechanism
- Organization-specific retention requirement
- Exact schedule or path
- Security or data-residency constraint
- Operator-defined threshold
- Architecture selection

Use `RESOLVE EVIDENCE` with the workflow name, packet version, and facts. The Gate records supplied facts as `STATED`, creates a new packet version, reruns affected rules, and invalidates stale selection, disposition, or acknowledgement when material content changes.

The Gate must generate everything it can. A blocked pack may not defer work that can be completed from existing evidence.

## 7. Review The Build Handoff Pack

Every pack contains:

- Terminal-action boundary
- Architecture decision record
- Complete files or configuration
- Permissions and credentials contract
- Deterministic controls
- Human checkpoints
- Prohibited actions
- Logging and audit requirements
- Failure, rollback, and stop behavior
- Acceptance tests
- Deployment sequence
- Assumptions and unresolved dependencies
- Expiration and reassessment triggers
- Version invalidation triggers
- Tool alternatives
- Builder acknowledgement requirement

### Statuses

| Status | Meaning |
|---|---|
| `BUILD_READY` | Selected architecture, complete content, controls, tests, and no unresolved inputs |
| `BLOCKED_FOR_EVIDENCE` | All generatable content exists; named organizational inputs remain |
| `NOT_APPLICABLE` | No AI implementation is authorized for the prohibited terminal action |

`NOT_APPLICABLE` is not an empty refusal. It includes a complete human operating procedure and safe decomposition opportunities that exclude the prohibited terminal action.

## 8. Record Operator Disposition

The operator chooses one disposition:

| Disposition | Use |
|---|---|
| `APPROVE_FOR_BUILD` | Pack is `BUILD_READY` and accountability is accepted |
| `HOLD_FOR_EVIDENCE` | Decision stands but named evidence remains |
| `REVISE` | A specific field or conclusion must change |
| `REJECT` | The workflow should not proceed |

Approval requires operator name or role, date, packet version, and rationale. The Gate cannot approve itself. A disposition applies only to the named packet version.

Every state-changing artifact states:

```text
Current state
What the Gate completed
What is blocked
Who acts next
Exact next action
```

## 9. Builder Handoff And Acknowledgement

The builder receives the approved artifact, complete Build Handoff Pack, and Builder Acknowledgement contract. Before implementation, the builder confirms:

- Packet version and terminal-action parity
- Allowed and prohibited actions
- Deterministic control implementation
- File-by-file plan
- Dependencies and permissions
- Acceptance-evidence plan
- Scope-change commitment

The builder stops when a required control cannot be implemented or a proposed change crosses the authorized boundary. Builders cannot self-authorize a new terminal action, tool capability, permission, data flow, or approval behavior.

## 10. Validate Before Activation

Run every acceptance test in non-production. Record evidence for normal behavior, edge cases, failure injection, approval blocking, prohibited actions, credential handling, audit logs, rollback or compensation, and terminal-action parity.

The workflow moves to `ACTIVE` only after:

1. `BUILD_READY` pack
2. `APPROVE_FOR_BUILD` disposition
3. Builder acknowledgement
4. Passing validation evidence

Static instructions are not proof that controls work. Preserve test results, logs, screenshots, or other observable evidence in the workflow record.

## 11. Operate The Lifecycle

The registry is the persistent source of truth. It tracks request, packet versions, architecture options and selection, disposition, builder acknowledgement, validation, active status, incidents, expiration, recertification, appeals, change assessments, precedents, and value metrics.

Canonical states are defined in `operating-contract.md`. Do not invent alternate state names.

### Expiration

Authorization expires when an artifact's observable trigger fires, including material workflow change, tool or model change, policy change, incident, threshold breach, stated recertification event, or loss of a required reviewer.

Pause the workflow, record the trigger, and use `RECERTIFY`. Prior disposition never carries forward automatically.

### Appeal

An appeal supplies evidence challenging a field or conclusion. It cannot bypass a hard gate. Record the claim, evidence, resolution, and any new packet version.

### Change Assessment

Use `REVIEW BUILD` before accepting changes to tools, policies, terminal actions, controls, permissions, credentials, or data flows. The result is `IN_SCOPE`, `OUT_OF_SCOPE`, or `RECERTIFICATION_REQUIRED`.

## 12. Operator Routines And Metrics

Daily: assess new requests and resolve evidence. Weekly: review blocked, in-build, and expiring records. Monthly: audit active workflows, incidents, unauthorized drift, and recertification.

Track:

- Assessment time
- Unsafe requests rejected
- Build rework avoided
- Time to approved handoff
- Recertification compliance

These metrics require retained evidence. Do not invent financial impact.

## 13. Common Failure Modes

| Failure | Correction |
|---|---|
| Treating a platform as the verdict | Separate autonomy, execution architecture, and builder surface |
| Selecting an option the Gate did not generate | Rerun architecture comparison or select a valid option ID |
| Calling an incomplete pack build-ready | Use `BLOCKED_FOR_EVIDENCE` and generate all grounded content |
| Using notification as approval | Implement a blocking, logged checkpoint |
| Claiming prompts enforce controls | Move enforcement into deterministic code or configuration |
| Carrying approval to a changed packet | Issue a new version and record a new disposition |
| Returning an empty HUMAN_ONLY refusal | Generate the human procedure and safe decomposition |
| Relying on chat memory | Preserve the durable registry record |

## 14. Quick Decision Guide

1. Is this recurring organizational work with consequences beyond the requester? If no, use a general assistant.
2. Is the terminal action accurate? If no, revise before proceeding.
3. Is the autonomy decision defensible from evidence? If no, resolve evidence or revise.
4. Are architecture options complete and sourced? If no, keep the handoff blocked.
5. Has the operator selected a generated option? If no, do not claim `BUILD_READY`.
6. Is the complete handoff contract present? If no, do not send it to a builder.
7. Has the operator recorded disposition? If no, implementation is unauthorized.
8. Has the builder acknowledged scope and controls? If no, implementation may not begin.
9. Did validation pass? If no, do not activate.
10. Has an expiration or change trigger fired? If yes, pause and reassess.

The Gate's value is not faster automation. It is a preserved chain from request to justified authority, implementable design, accountable approval, verified operation, and timely expiration.
