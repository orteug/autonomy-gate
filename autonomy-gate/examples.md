# Canonical Calibration Examples

These concise examples calibrate decisions and required packet fields. They do not replace the full artifact templates. Every live response still follows `rules.md` and `reference/operating-contract.md`.

## Example 1 — Weekly KPI Narrative

Input: A team member supplies stable CRM and analytics exports and needs an internal narrative for manual Slack posting.

Autonomy: AUTONOMOUS
Assessment surface: Any supported Gate Project
Execution architecture: Human-triggered model workspace using supplied exports and producing an internal document
Builder surface: Platform administrator
Confidence: MEDIUM
Terminal action: Produce an internal Slack-ready narrative
Justification: RULE-03 supports bounded reversible document production; RULE-04 confirms no external publication
Controls required: Source validation, period reconciliation, no invented values, retained output
Evidence gaps: KPI definitions, error threshold, and retention policy
Handoff status: BLOCKED_FOR_EVIDENCE
Artifact required: template-project-setup.md

## Example 2 — Unstable Client Onboarding

Input: Every onboarding run differs, ownership is unclear, and exceptions are handled ad hoc.

Autonomy: SOP_FIRST
Assessment surface: Any supported Gate Project
Execution architecture: Human documentation and stabilization process before automation design
Builder surface: Process owner
Confidence: MEDIUM
Terminal action: Document and stabilize the onboarding process
Justification: RULE-03 finds high exception rate and RULE-09 finds unknown state and ownership
Controls required: Named owner, documented standard path, exception taxonomy, evidence log
Evidence gaps: Stable steps and exception rules
Handoff status: BLOCKED_FOR_EVIDENCE
Artifact required: template-stabilization-plan.md

## Example 3 — Refund Recommendation

Input: AI checks policy and order facts, then recommends whether a support lead should approve a refund.

Autonomy: AUTONOMOUS
Assessment surface: Any supported Gate Project
Execution architecture: Read-only policy and order analysis producing a recommendation
Builder surface: Internal engineering or Codex
Confidence: HIGH
Terminal action: Produce a refund eligibility recommendation
Justification: RULE-04 separates recommendation from money movement; no hard gate applies
Controls required: Read-only access, source citations, deterministic policy checks
Evidence gaps: None
Handoff status: BLOCKED_FOR_EVIDENCE
Artifact required: template-automation-architecture.md

## Example 4 — Refund Execution

Input: The workflow evaluates a refund and issues it after a support lead approves.

Autonomy: SUPERVISED
Assessment surface: Any supported Gate Project
Execution architecture: Deterministic refund workflow with a blocking approval checkpoint
Builder surface: Internal engineering or Codex
Confidence: MEDIUM
Terminal action: Issue a customer refund
Justification: RULE-04 identifies money movement and RULE-06 applies GATE-1
Controls required: Blocking approval, amount validation, idempotency, audit log
Evidence gaps: Approval authority and credential mechanism
Handoff status: BLOCKED_FOR_EVIDENCE
Artifact required: template-control-plan.md

## Example 5 — Outbound Email Campaign

Input: AI drafts personalized outreach and a named marketing lead approves before sending.

Autonomy: SUPERVISED
Assessment surface: Any supported Gate Project
Execution architecture: Drafting workspace with a blocking external-publication approval step
Builder surface: Platform administrator
Confidence: LOW
Terminal action: Send approved external email
Justification: RULE-06 applies GATE-4 and RULE-08 requires identifiable checkpoint ownership
Controls required: Named approver, rejection criteria, compliance review, send audit
Evidence gaps: Recipient volume, data-use approval, and rejection rubric
Handoff status: BLOCKED_FOR_EVIDENCE
Artifact required: template-control-plan.md

## Example 6 — Scheduled Internal Brief

Input: A scheduled process reads approved local files and writes an internal morning brief without publishing it.

Autonomy: AUTONOMOUS
Assessment surface: Any supported Gate Project
Execution architecture: Scheduled file workflow with deterministic input validation and internal output
Builder surface: Cowork administrator
Confidence: MEDIUM
Terminal action: Write an internal brief to the approved output folder
Justification: RULE-03 supports bounded reversible output and RULE-04 finds no external action
Controls required: Folder allowlist, source freshness, execution log, failure alert
Evidence gaps: Schedule owner and retention policy
Handoff status: BLOCKED_FOR_EVIDENCE
Artifact required: template-cowork-config.md

## Example 7 — Sensitive External Report

Input: AI prepares a customer-facing performance report that a named account lead must approve.

Autonomy: SUPERVISED
Assessment surface: Any supported Gate Project
Execution architecture: Drafting workspace with blocking account-lead approval before delivery
Builder surface: Platform administrator
Confidence: MEDIUM
Terminal action: Deliver a customer-facing performance report
Justification: RULE-06 applies GATE-4 because the output is externally reputation-sensitive
Controls required: Source verification, named approver, approval record, delivery log
Evidence gaps: Customer-specific disclosure policy
Handoff status: BLOCKED_FOR_EVIDENCE
Artifact required: template-control-plan.md

## Example 8 — Vendor Bank Change

Input: A vendor asks to replace its bank-account details before the next payment cycle.

Autonomy: HUMAN_ONLY
Assessment surface: Any supported Gate Project
Execution architecture: Human-controlled independent verification and dual authorization
Builder surface: No builder for the terminal action
Confidence: HIGH
Terminal action: Authorize and record a new payment destination
Justification: RULE-04 identifies an irreversible external commitment and RULE-06 applies GATE-2
Controls required: Independent callback, segregation of duties, retained change record
Evidence gaps: None
Handoff status: NOT_APPLICABLE
Artifact required: template-governance-memo.md

## Example 9 — Permission Change

Input: AI grants a contractor production-administrator access after a manager requests it.

Autonomy: HUMAN_ONLY
Assessment surface: Any supported Gate Project
Execution architecture: Human identity-governance procedure with no delegated permission change
Builder surface: No builder for the terminal action
Confidence: HIGH
Terminal action: Grant production administrator permissions
Justification: RULE-04 identifies an access-control change and RULE-06 applies GATE-3
Controls required: Human authorization, least privilege, access log, expiry
Evidence gaps: None
Handoff status: NOT_APPLICABLE
Artifact required: template-governance-memo.md

## Example 10 — Invoice Payment

Input: A workflow validates an invoice and submits payment after controller approval.

Autonomy: SUPERVISED
Assessment surface: Any supported Gate Project
Execution architecture: Deterministic invoice validation with blocking controller approval and payment API call
Builder surface: Internal engineering or Codex
Confidence: MEDIUM
Terminal action: Submit an invoice payment
Justification: RULE-06 applies GATE-1 to money movement
Controls required: Dual validation, approval record, duplicate prevention, reconciliation
Evidence gaps: Controller role and payment threshold
Handoff status: BLOCKED_FOR_EVIDENCE
Artifact required: template-control-plan.md

## Example 11 — Regulated Filing Draft and Submit

Input: AI prepares and submits a regulatory filing after legal review.

Autonomy: SUPERVISED
Assessment surface: Any supported Gate Project
Execution architecture: Drafting and validation service that halts for legal approval before submission
Builder surface: Internal engineering or Codex
Confidence: MEDIUM
Terminal action: Submit a regulated filing externally
Justification: RULE-06 applies GATE-4; submission authority remains human-controlled
Controls required: Legal approval, schema validation, immutable filing record
Evidence gaps: Filing system and legal approver
Handoff status: BLOCKED_FOR_EVIDENCE
Artifact required: template-control-plan.md

## Example 12 — Scheduled File Distribution

Input: A scheduled local workflow prepares files and waits for a reviewer before moving them to an external connector.

Autonomy: SUPERVISED
Assessment surface: Any supported Gate Project
Execution architecture: Scheduled file workflow with a blocking review state before connector delivery
Builder surface: Cowork administrator
Confidence: MEDIUM
Terminal action: Deliver approved files through an external connector
Justification: RULE-04 identifies external delivery and RULE-06 requires supervision
Controls required: Folder allowlist, blocking review, delivery log, retry limits
Evidence gaps: Reviewer and connector permissions
Handoff status: BLOCKED_FOR_EVIDENCE
Artifact required: template-control-plan.md

## Example 13 — Customer Response Drafting

Input: AI drafts a sensitive customer response and a support manager approves before sending.

Autonomy: SUPERVISED
Assessment surface: Any supported Gate Project
Execution architecture: Project drafting workflow with human-controlled send action
Builder surface: Platform administrator
Confidence: MEDIUM
Terminal action: Send a sensitive customer response
Justification: RULE-06 applies GATE-4 to reputation-sensitive external communication
Controls required: Named manager, source review, approval record, send separation
Evidence gaps: Escalation rubric
Handoff status: BLOCKED_FOR_EVIDENCE
Artifact required: template-control-plan.md

## Example 14 — Fully Specified KPI Project

Input: The KPI definitions, source schemas, correction threshold, six-month recertification interval, owner, and retention policy are all supplied.

Autonomy: AUTONOMOUS
Assessment surface: Any supported Gate Project
Execution architecture: Human-triggered approved model workspace producing an internal narrative from validated exports
Builder surface: Platform administrator
Confidence: HIGH
Terminal action: Produce an internal Slack-ready narrative
Justification: RULE-03 supports bounded reversible document production and all decision evidence is present
Controls required: Source validation, fixed KPI dictionary, anomaly handling, retained output
Evidence gaps: None
Handoff status: BUILD_READY
Artifact required: template-project-setup.md
