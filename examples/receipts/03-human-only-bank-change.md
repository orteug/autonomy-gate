━━ WORKFLOW INTAKE SNAPSHOT ━━━
Name: Vendor bank account change
Terminal action: Authorize a new external payment destination
Evidence gaps: None

━━ AUTONOMY DECISION PACKET ━━━
Workflow ID: WF-20260611-003
Packet version: v1
Autonomy: HUMAN_ONLY
Assessment surface: Claude Project
Execution architecture: Human-controlled verification and authorization procedure with no AI implementation
Builder surface: No builder
Confidence: HIGH
Terminal action: Authorize a new external payment destination
Justification: RULE-04 identifies an irreversible external commitment and RULE-06 applies GATE-2
Controls required: Independent callback verification, dual authorization, retained decision record
Evidence gaps: None
Handoff status: NOT_APPLICABLE
Artifact required: Governance Memo

━━ GOVERNANCE MEMO ━━━

AI may not verify or authorize the bank-account change. The controller follows the documented human verification and dual-authorization procedure.

BUILD HANDOFF PACK
Handoff status: NOT_APPLICABLE
Terminal-action boundary: Authorize a new external payment destination; AI may not verify, approve, or submit that authorization
Architecture decision record: NOT_APPLICABLE because GATE-2 prohibits AI execution of the terminal action
Permissions and credentials: No AI access to vendor master data write controls, payment credentials, or authorization systems
Deterministic controls: Human procedure requires independent callback verification and dual authorization before any system change
Human checkpoints: Controller verifies the request and a second authorized human approves the change
Prohibited actions: AI may not select verification evidence, contact the requester using supplied contact details, approve the change, or update payment routing
Logging and audit: Retain request source, independent contact source, verification results, both authorizers, timestamps, decision, and changed fields
Failure, rollback, and stop behavior: Stop when independent verification, ownership, or dual authorization is unavailable; do not change the account and escalate suspected fraud
Deployment sequence: Document the human procedure, train authorized roles, test the record and escalation path, then authorize human operation
Assumptions: The organization can retrieve a previously verified contact channel and enforce dual authorization
Unresolved dependencies: None for the stated procedure
Expiration and reassessment triggers: Verification policy, authorization roles, payment system, vendor-master process, or legal context changes; any incident
Version invalidation triggers: Any material process, role, control, or terminal-action change creates a new packet version and invalidates prior disposition
Tool alternatives: No tool may execute the prohibited terminal action; tools may assist only with bounded evidence compilation under separate assessment
Builder acknowledgement: Not applicable to the prohibited action; the human procedure owner acknowledges the operating record
Current state: DISPOSITION_PENDING
What the Gate completed: Applied GATE-2, prohibited AI execution, generated the human procedure, and bounded safe preparation work
What is blocked: Operator disposition on the human procedure
Who acts next: Controller or designated procedure owner
Exact next action: Review the procedure and record the disposition for packet v1
Human operating procedure: Controller retrieves the vendor contact from a previously verified source, performs an independent callback, compares the request with retained vendor records, documents evidence, obtains a second authorized approval, updates the account through the human-controlled system, and retains the decision record
Safe decomposition opportunities: AI may compile existing vendor records and produce a discrepancy checklist for human review, but it may not choose the contact channel, determine authenticity, authorize the change, or write payment data
Acceptance tests:
- Setup: Simulated bank-change request with requester-supplied contact details
  Input: Run the human review procedure
  Expected: Reviewer ignores supplied contact details, verifies through the retained channel, and records dual authorization before any change
  Pass criterion: No payment destination changes without independent verification and two human authorization records

━━ OPERATOR DISPOSITION ━━━
Disposition: PENDING
Name / role: not recorded
Date: not recorded
Packet version: v1
Rationale: not recorded
