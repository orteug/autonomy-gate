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

BUILD HANDOFF PACK
Handoff status: BUILD_READY
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
