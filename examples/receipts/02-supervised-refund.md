━━ WORKFLOW INTAKE SNAPSHOT ━━━
Name: Refund recommendation and execution
Terminal action: Issue a customer refund after blocking human approval
Evidence gaps: Approval authority and production credentials are not supplied

━━ AUTONOMY DECISION PACKET ━━━
Workflow ID: WF-20260611-002
Packet version: v1
Autonomy: SUPERVISED
Assessment surface: ChatGPT Project
Execution architecture: Deterministic refund workflow with model-assisted eligibility analysis and a blocking approval checkpoint
Builder surface: Internal engineering or an approved low-code specialist
Confidence: MEDIUM
Terminal action: Issue a customer refund after blocking human approval
Justification: RULE-04 identifies money movement and RULE-06 applies GATE-1 supervision
Controls required: Blocking approval, amount validation, idempotency, audit log, duplicate prevention
Evidence gaps: Approval authority and production credentials are not supplied
Handoff status: BLOCKED_FOR_EVIDENCE
Artifact required: Control Plan

━━ CONTROL PLAN ━━━

The workflow may analyze eligibility and prepare a refund request. It must halt before money movement until an authorized reviewer approves.

ARCHITECTURE OPTIONS
### OPT-1 — PRIMARY
**Execution architecture:** Durable workflow service with deterministic eligibility validation, model-assisted analysis, a blocking approval state, and an idempotent refund connector
**Builder surface:** Internal engineering
**Control fit:** Strong fit for blocking approval, duplicate prevention, immutable decision records, retries, and compensation
**Implementation effort:** Medium to high because production integration, credentials, and operational ownership are required
**Operating cost:** Hosting, model, and payment-platform costs require organization-specific evidence
**Maintenance burden:** Engineering ownership, incident response, dependency updates, and control testing
**Security fit:** Supports least-privilege service credentials and separation between preparation, approval, and execution
**Portability:** High when workflow state and connector interfaces remain provider-neutral
**Skill requirements:** Backend engineering, workflow orchestration, payment integration, security, and operations
**Source evidence:** Technology-neutral capability requirements from GATE-1, the control plan, and workflow architecture contract

### OPT-2 — LOW_CODE
**Execution architecture:** Approved integration platform with durable state, a blocking human-approval step, and an idempotent payment connector
**Builder surface:** Approved low-code specialist
**Control fit:** Viable only if approval blocks execution and audit records, retries, and duplicate prevention are enforceable
**Implementation effort:** Medium after the organization confirms an approved platform and connector
**Operating cost:** Platform and connector pricing are unknown until the approved stack is supplied
**Maintenance burden:** Platform administration, connector monitoring, and regression checks after vendor changes
**Security fit:** Requires enterprise identity, least-privilege credentials, approved data residency, and auditable approval records
**Portability:** Moderate because flow definitions and connectors may be platform-specific
**Skill requirements:** Integration-platform design, payment controls, and operational support
**Source evidence:** Technology-neutral capability basis; named platform claims require official-source verification before selection

### OPT-3 — CODE_FIRST
**Execution architecture:** Custom stateful service and queue with policy code, approval API, payment adapter, audit store, and compensation path
**Builder surface:** Internal engineering or contracted software team
**Control fit:** Maximum deterministic control and testability for money movement
**Implementation effort:** High because the organization owns the service lifecycle
**Operating cost:** Infrastructure and engineering costs are not supplied
**Maintenance burden:** Highest option due to hosting, observability, incident response, and dependency ownership
**Security fit:** Can meet strict separation-of-duty and secrets requirements when implemented and reviewed correctly
**Portability:** High at the architecture level; payment adapters remain provider-specific
**Skill requirements:** Software engineering, security engineering, payment integration, and site reliability
**Source evidence:** Workflow architecture contract and GATE-1 control requirements

### OPT-4 — VENDOR_NEUTRAL
**Execution architecture:** Provider-neutral durable workflow engine, blocking approval interface, audit store, and idempotent payment adapter selected from the approved stack
**Builder surface:** Implementation owner determined after stack confirmation
**Control fit:** Defines the required controls without assuming an available product
**Implementation effort:** Unknown until the technology stack and build owner are confirmed
**Operating cost:** Unknown until tools and hosting are selected
**Maintenance burden:** Depends on the chosen implementation and ownership model
**Security fit:** Requires confirmed identity, credential, residency, retention, and separation-of-duty controls
**Portability:** Highest because capabilities and interfaces are specified independently of products
**Skill requirements:** Workflow architecture, security, payment operations, and implementation skills matching the selected stack
**Source evidence:** Technology-neutral basis from the packet, control plan, and tool-selection rules

Omitted option classes:
- NATIVE_SUITE — No organization suite or native payment workflow capability was supplied, so viability cannot be evidenced

Selected option: NOT_SELECTED
Selection by: NOT_RECORDED
Selection date: NOT_RECORDED

BUILD HANDOFF PACK
Handoff status: BLOCKED_FOR_EVIDENCE
Terminal-action boundary: Prepare a refund request and issue the refund only after a blocking approval by the authorized human role
Architecture decision record: No option selected; OPT-1 is recommended and NATIVE_SUITE is omitted because no organization suite capability was supplied
Permissions and credentials: Read eligibility evidence and use a least-privilege refund credential only after approval; credential mechanism remains unresolved
Deterministic controls: Validate amount and eligibility, block before payment, prevent duplicates, require idempotency, and retain the approval record
Human checkpoints: Authorized reviewer must approve before the payment connector can execute; reviewer identity remains unresolved
Prohibited actions: Do not issue, retry, increase, or redirect a refund without a valid approval bound to the request
Logging and audit: Record request hash, eligibility result, amount, reviewer identity, decision, timestamp, connector response, and terminal status
Failure, rollback, and stop behavior: Stop on missing evidence, approval timeout, duplicate request, permission mismatch, or connector uncertainty; never retry an ambiguous payment automatically
Deployment sequence: Resolve architecture and organizational evidence, create configuration, test the blocking checkpoint and idempotency in non-production, record disposition and acknowledgement, then activate
Assumptions: The payment provider supports an idempotent refund operation and auditable response identifiers; this must be verified after selection
Unresolved dependencies: Architecture selection, approval authority, approved credential mechanism, and provider capability evidence
Expiration and reassessment triggers: Terminal action, refund policy, amount rules, approval role, provider, permissions, or control behavior changes; any incident
Version invalidation triggers: Any material change creates a new packet version and invalidates prior selection, disposition, and acknowledgement
Tool alternatives: Use an approved low-code or code-first implementation only if it enforces the same blocking approval, idempotency, audit, and credential boundaries
Builder acknowledgement: Prohibited until the pack becomes BUILD_READY and the operator records APPROVE_FOR_BUILD
Current state: HANDOFF_BLOCKED
What the Gate completed: Issued the supervised decision, generated four architecture options, and produced every grounded handoff field
What is blocked: Architecture selection, approval authority, credential mechanism, and provider capability evidence
Who acts next: Operations owner and payment-system owner
Exact next action: Select a generated architecture option and supply the named organizational evidence for a new packet version
Required before build: Operator-selected generated architecture, named approval authority, approved credential mechanism, and official provider capability evidence

━━ OPERATOR DISPOSITION ━━━
Disposition: PENDING
Name / role: not recorded
Date: not recorded
Packet version: v1
Rationale: not recorded
