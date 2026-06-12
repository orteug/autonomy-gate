━━ WORKFLOW INTAKE SNAPSHOT ━━━
Name: Weekly KPI narrative
Terminal action: Produce an internal Slack-ready narrative for human posting
Evidence gaps: None

━━ AUTONOMY DECISION PACKET ━━━
Workflow ID: WF-20260611-001
Packet version: v1
Autonomy: AUTONOMOUS
Assessment surface: Claude Project
Execution architecture: Human-triggered model workspace using supplied exports and producing an internal document
Builder surface: Platform administrator
Confidence: HIGH
Terminal action: Produce an internal Slack-ready narrative for human posting
Justification: RULE-03 supports bounded reversible document production; RULE-04 confirms no external publication terminal action
Controls required: Validate reporting period, reject missing sources, retain output, prohibit direct Slack posting
Evidence gaps: None
Handoff status: BUILD_READY
Artifact required: Project Setup Brief

━━ PROJECT SETUP BRIEF ━━━

The Project accepts operator-supplied CRM and analytics exports, validates reporting periods, and produces a standardized internal narrative. A human reviews and posts the result.

ARCHITECTURE OPTIONS
### OPT-1 — PRIMARY
**Execution architecture:** Human-triggered governed model workspace that accepts operator-supplied exports and produces an internal narrative without publishing it
**Builder surface:** Platform administrator
**Control fit:** Workspace instructions enforce source validation, bounded output, and prohibition of external actions
**Implementation effort:** Low; configure instructions and run the acceptance check
**Operating cost:** Existing approved model-workspace usage; contract-specific cost is outside the supplied evidence
**Maintenance burden:** Review instructions when source formats, models, or reporting rules change
**Security fit:** Uses operator-supplied internal exports and grants no write access to source or destination systems
**Portability:** Instructions and acceptance criteria can move to another governed model workspace
**Skill requirements:** Workspace administration and KPI reporting knowledge
**Source evidence:** Technology-neutral capability basis from the packet and workflow architecture contract

### OPT-2 — NATIVE_SUITE
**Execution architecture:** Existing enterprise productivity suite with an approved model workspace and document output
**Builder surface:** Enterprise platform administrator
**Control fit:** Suitable only if the native workspace can prohibit connectors and retain reviewable output
**Implementation effort:** Low to medium depending on existing workspace governance
**Operating cost:** Existing suite entitlement must be confirmed by the organization
**Maintenance burden:** Platform policy and model-version review
**Security fit:** Can inherit enterprise identity and retention controls when confirmed
**Portability:** Moderate because instructions export but suite governance settings may not
**Skill requirements:** Suite administration and reporting-domain knowledge
**Source evidence:** Technology-neutral option; named-suite capability verification remains an organizational implementation task

### OPT-3 — VENDOR_NEUTRAL
**Execution architecture:** Any approved model workspace that accepts files, follows durable instructions, and returns an internal document without system write access
**Builder surface:** Platform administrator
**Control fit:** Preserves the no-publication boundary through capability requirements rather than vendor features
**Implementation effort:** Medium because the chosen workspace must be qualified against the acceptance test
**Operating cost:** Depends on the selected approved provider and is not established by the workflow evidence
**Maintenance burden:** Provider qualification and periodic instruction regression testing
**Security fit:** Requires approved data handling, identity, retention, and no connector write permissions
**Portability:** High because the contract is capability-based
**Skill requirements:** Model-workspace administration, security review, and KPI reporting knowledge
**Source evidence:** Workflow architecture contract and packet controls

Omitted option classes:
- LOW_CODE — The workflow has no cross-system execution or routing requirement that justifies an integration platform
- CODE_FIRST — Custom software adds operating burden without improving the bounded document-production terminal action

Selected option: OPT-1
Selection by: Operations owner
Selection date: 2026-06-12

BUILD HANDOFF PACK
Handoff status: BUILD_READY
Terminal-action boundary: Produce an internal Slack-ready narrative; the workflow may not post it or modify source systems
Architecture decision record: OPT-1 selected by Operations owner on 2026-06-12; LOW_CODE and CODE_FIRST omitted for lack of integration need and unnecessary operating burden
Permissions and credentials: Read operator-supplied exports only; no production credentials, connectors, or write permissions
Deterministic controls: Reject missing source names and conflicting reporting periods before analysis
Human checkpoints: None inside the run; a human-owned Slack post occurs outside the authorized terminal action
Prohibited actions: Do not invent values, post externally, call source systems, or modify records
Logging and audit: Record packet version, source names, reporting period, terminal status, and retained output location
Failure, rollback, and stop behavior: Stop on missing or conflicting evidence; discard invalid drafts because no external action has occurred
Deployment sequence: Create project instructions, run the acceptance test with non-production exports, record disposition and acknowledgement, then enable operator use
Assumptions: Export formats remain stable enough for the stated validation rules
Unresolved dependencies: None
Expiration and reassessment triggers: Source schema, terminal action, model workspace, policy, or control changes; any incident
Version invalidation triggers: A material change creates a new packet version and invalidates architecture selection, disposition, and builder acknowledgement
Tool alternatives: Use another approved model workspace only if it preserves file input, durable instructions, no write access, and the same acceptance test
Builder acknowledgement: Required before the platform administrator applies the configuration
Current state: DISPOSITION_PENDING
What the Gate completed: Issued the autonomy decision, compared architectures, recorded OPT-1 selection, and generated the complete project handoff
What is blocked: Operator disposition and builder acknowledgement
Who acts next: Operations owner
Exact next action: Record APPROVE_FOR_BUILD, REVISE, HOLD_FOR_EVIDENCE, or REJECT for packet v1
Manifest:
- Path: project-instructions.md
  Purpose: Define the bounded Project workflow
  Source evidence: Packet terminal action and required controls
  Complete content: Use only operator-supplied exports. Validate source names and reporting periods. Produce the standardized internal KPI narrative. Never post to Slack or modify source systems.
Acceptance tests:
- Setup: Valid exports for the same reporting period
  Input: One weekly reporting run
  Expected: A source-grounded internal narrative
  Pass criterion: The output contains no invented values and performs no external action

━━ OPERATOR DISPOSITION ━━━
Disposition: PENDING
Name / role: not recorded
Date: not recorded
Packet version: v1
Rationale: not recorded
