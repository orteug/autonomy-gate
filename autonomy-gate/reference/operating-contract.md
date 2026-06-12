# Operating Contract

This is a canonical runtime file. It defines the lifecycle, output fields, architecture-selection requirement, and handoff statuses used by every Gate deployment. If another guide conflicts with this file, this file governs.

## Decision Fields

Every Autonomy Decision Packet contains these distinct fields:

- `Autonomy`: `AUTONOMOUS`, `SUPERVISED`, `SOP_FIRST`, or `HUMAN_ONLY`.
- `Assessment surface`: where the Gate assessment ran, such as Claude Project or ChatGPT Project.
- `Execution architecture`: the production design, expressed in technology-neutral capabilities first and named tools only when supported by the organization's confirmed stack.
- `Builder surface`: who or what implements the selected architecture, such as internal engineering, a platform administrator, a low-code specialist, Claude Code, or Codex.
- `Confidence`: `HIGH`, `MEDIUM`, or `LOW`; this concerns the autonomy decision, not implementation completeness.
- `Handoff status`: `BUILD_READY`, `BLOCKED_FOR_EVIDENCE`, or `NOT_APPLICABLE`.

`PROJECT`, `COWORK`, and `CODE_AGENT` are implementation patterns. They may inform an execution architecture or builder surface, but they are not universal production-platform verdicts.

## Canonical Lifecycle

The workflow record uses these states:

| State | Meaning |
|---|---|
| `SUBMITTED` | A workflow description has been received. |
| `ASSESSED` | The autonomy decision packet has been issued. |
| `ARCHITECTURE_SELECTED` | The operator selected an implementation architecture from the supported alternatives. |
| `HANDOFF_BLOCKED` | The handoff is `BLOCKED_FOR_EVIDENCE`. |
| `DISPOSITION_PENDING` | A complete artifact awaits operator disposition. |
| `APPROVED_FOR_BUILD` | The operator recorded approval with required metadata. |
| `IN_BUILD` | The builder acknowledged the approved pack and began implementation. |
| `VALIDATING` | Implementation is being checked against acceptance criteria. |
| `ACTIVE` | The workflow is operating under the approved packet. |
| `PAUSED` | Operation is deliberately suspended pending operator action. |
| `EXPIRED` | An expiration trigger fired; the workflow must not run. |
| `RECERTIFICATION_REQUIRED` | A new Gate assessment is required before operation resumes. |
| `REJECTED` | The operator rejected the workflow; no build is authorized. |

Permitted transitions:

```text
SUBMITTED -> ASSESSED
ASSESSED -> ARCHITECTURE_SELECTED | HANDOFF_BLOCKED | REJECTED
HANDOFF_BLOCKED -> ASSESSED | ARCHITECTURE_SELECTED | REJECTED
ARCHITECTURE_SELECTED -> DISPOSITION_PENDING | HANDOFF_BLOCKED
DISPOSITION_PENDING -> APPROVED_FOR_BUILD | HANDOFF_BLOCKED | ASSESSED | REJECTED
APPROVED_FOR_BUILD -> IN_BUILD | REJECTED
IN_BUILD -> VALIDATING | PAUSED | ASSESSED
VALIDATING -> ACTIVE | IN_BUILD | PAUSED | ASSESSED
ACTIVE -> PAUSED | EXPIRED | ASSESSED
PAUSED -> ACTIVE | EXPIRED | ASSESSED
EXPIRED -> RECERTIFICATION_REQUIRED
RECERTIFICATION_REQUIRED -> SUBMITTED
```

An evidence update creates a new packet version and reruns every rule whose inputs changed. It invalidates an existing disposition whenever the verdict, terminal action, required controls, selected architecture, or handoff contents change.

## Architecture Selection

After assessment, the Gate produces architecture alternatives appropriate to the known stack:

1. Primary recommendation using confirmed approved tools when feasible.
2. Native-suite option minimizing new procurement.
3. Low-code or integration-platform option for limited engineering capacity.
4. Code-first option for durability, custom controls, testing, or scale.
5. Vendor-neutral option when portability matters or the stack is unknown.

An option class may be omitted only with a stated evidence-based reason. The operator selects the architecture. The Gate does not issue `BUILD_READY` before selection.

## Handoff Statuses

- `BUILD_READY`: the architecture is selected; every referenced file has complete content and source evidence; all controls and acceptance tests are specified; no unresolved operator input remains.
- `BLOCKED_FOR_EVIDENCE`: all generatable content is present, but named irreducible organizational inputs remain. Supplying evidence triggers affected-rule reassessment before status promotion.
- `NOT_APPLICABLE`: no implementation is authorized, normally for `HUMAN_ONLY` outcomes.

Runtime terminal statuses such as `BLOCKED`, `FAILED`, or `TIMED_OUT` describe an execution run. They never describe handoff readiness.

## Authority Boundaries

The Gate may recommend a disposition but may not record `APPROVE_FOR_BUILD`. Approval requires operator name and role, date, packet version, and rationale. A builder may not start until an approved `BUILD_READY` pack is acknowledged. A change to terminal action, controls, architecture, credentials, permissions, or tool capabilities requires operator review and may require reassessment.
