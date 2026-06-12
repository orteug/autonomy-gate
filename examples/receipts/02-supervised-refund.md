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

BUILD HANDOFF PACK
Handoff status: BLOCKED_FOR_EVIDENCE
Required before build: Named approval authority and approved credential mechanism

━━ OPERATOR DISPOSITION ━━━
Disposition: PENDING
Name / role: not recorded
Date: not recorded
Packet version: v1
Rationale: not recorded
