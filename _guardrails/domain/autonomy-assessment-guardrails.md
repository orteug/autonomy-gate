# Autonomy Assessment Guardrails
## Context Layer 3 · Domain-Specific Safety Additions

> These are additions to `_guardrails/shared/`. They do not replace shared guardrails.
> Load this file AFTER all 4 shared guardrail files.
> These guardrails add a PROFESSIONAL REQUIRED block to the output — they do not alter the verdict.
> RULE-00 (Gate always issues a verdict) is preserved.

---

## Escalation Triggers — Autonomy Assessment-Specific

The following conditions trigger the `🔴 PROFESSIONAL REQUIRED` block IN ADDITION TO the shared triggers.

---

**Autonomy Trigger 1: GATE-2 or GATE-3 Override Pressure**

Condition: Operator acknowledges or implies that the Gate's verdict is HUMAN_ONLY or SUPERVISED, but wants to proceed with AUTONOMOUS implementation due to time pressure, cost pressure, or executive direction.

Why it escalates: GATE-2 (irreversible external commitment) and GATE-3 (access control changes) are hard gates that cannot be overridden by operator context. A production system built against a HUMAN_ONLY verdict creates unmitigated risk. The operator needs independent review before overriding a hard gate.

🔴 PROFESSIONAL REQUIRED: The assessment produced a HUMAN_ONLY or SUPERVISED verdict based on hard gate conditions. Proceeding with autonomous implementation against this verdict requires independent review by your legal, compliance, or operations leadership — not just operator discretion. Document the override decision and the business rationale before proceeding.

---

**Autonomy Trigger 2: Regulated Data in Fully Automated Workflow**

Condition: The workflow involves HIPAA-protected health information, PII subject to GDPR or CCPA, financial records subject to SOX or FINRA, or other regulated data categories — AND the proposed autonomy level is AUTONOMOUS (AUT-1) with no human review checkpoint on data access or output.

Why it escalates: Automated processing of regulated data without human review checkpoints creates compliance exposure that requires legal or compliance counsel review, not just an operations decision.

🔴 PROFESSIONAL REQUIRED: This workflow involves regulated data categories. Autonomous implementation without human review checkpoints requires review by legal or compliance counsel familiar with the applicable regulatory framework before deployment. Do not treat this assessment as compliance approval.

---

**Autonomy Trigger 3: Automated Financial Transactions Above Material Threshold**

Condition: The workflow autonomously initiates, approves, or executes financial transactions — payments, transfers, contract commitments, purchase orders — and the transaction value is material to the operator's business context.

Why it escalates: Automated financial transactions require internal controls, audit trail design, and often external review for financial statement and fraud prevention purposes. An autonomy assessment is not a financial controls review.

🔴 PROFESSIONAL REQUIRED: This workflow involves automated financial transactions. Before deployment, have your finance team or external auditors review the control design — specifically: transaction limits, dual-approval thresholds, audit trail completeness, and exception handling for failed or mis-routed transactions.

---

**Autonomy Trigger 4: Security-Impacting Workflow (Access Control, Credential Management, Permission Changes)**

Condition: The terminal action of the workflow changes access controls, manages credentials, grants or revokes permissions, or modifies security configurations in any system.

Why it escalates: Security-impacting automation has asymmetric risk — the failure mode (unauthorized access, credential exposure, privilege escalation) is typically irreversible and high-consequence. This requires security review independent of the autonomy assessment.

🔴 PROFESSIONAL REQUIRED: This workflow's terminal action involves security-impacting changes. Have your security team review the implementation design before deployment — specifically: blast radius if the automation misbehaves, credential handling, logging and alerting for unexpected behavior, and rollback capability.

---

**Autonomy Trigger 5: Autonomous AI-Deciding-About-AI (Recursive Autonomy)**

Condition: The workflow being assessed is itself an AI system deciding the autonomy level, deployment configuration, or operational parameters of another AI system — with no human review checkpoint.

Why it escalates: Recursive AI governance — AI deciding autonomy for AI — creates a failure mode where errors compound without human detection. This is an emerging governance area that requires deliberate human oversight at the decision point.

🔴 PROFESSIONAL REQUIRED: This workflow involves AI systems making autonomous decisions about other AI systems' operational parameters. This configuration requires deliberate human governance design — not just an autonomy level assignment. Consult with your AI governance or safety review function before deploying.

---

## Input Integrity Flags — Autonomy Assessment-Specific

The following patterns trigger the `⚠️ INPUT INTEGRITY FLAG` block IN ADDITION TO the shared patterns.

---

**Autonomy Flag 1: Failure Consequence Systematically Minimized**

Pattern: Workflow description states "nothing bad happens if it fails," "it just retries," or "the consequences are minimal" without substantiating the claim with a reversibility mechanism or exception path.

What to verify: Do not accept a stated failure consequence without provenance `STATED` from someone who has seen it fail. Note as evidence gap. Apply conservative scoring on cost-of-failure dimension.

---

**Autonomy Flag 2: Reversibility Claimed Without Mechanism**

Pattern: Input states the workflow is "easily reversed" or "reversible" without naming the mechanism (who reverses it, how, within what time window, at what cost).

What to verify: Reversibility without a named mechanism is an assertion, not a fact. Record as `UNKNOWN` provenance for the reversibility field. State the gap explicitly in the snapshot.

---

**Autonomy Flag 3: Zero Exception Rate Claimed for Novel Workflow**

Pattern: Operator claims zero or negligible exception rate for a workflow that has never been run at scale or in automated form — only in manual or human-supervised form.

What to verify: Manual exception rates do not predict automated exception rates. Novel automation creates new failure modes. Record exception rate as `UNKNOWN` and apply conservative scoring.

---

**Autonomy Flag 4: "We've Done It Manually for Years" as Automation Readiness**

Pattern: The primary basis for proposing automation is that the workflow has been done manually for a long time — implying it is well-understood and ready for autonomous execution.

What to verify: Manual tenure is evidence of process stability, not automation readiness. The Gate assesses the workflow against its terminal action, failure consequence, and reversibility — not its age. Do not give extra weight to longevity as an autonomy justification.

---

**Autonomy Flag 5: Autonomy Level Stated as Input**

Pattern: Operator submits a workflow description AND a desired autonomy level — "we want this to be fully autonomous" — rather than asking the Gate to assess the appropriate level.

What to verify: The Gate assesses the minimum justified autonomy level. A stated desired level is not a basis for assessment — it is a bias signal. Note the stated preference, run the assessment independently, and if the verdict differs from the stated desire, name the gap explicitly.

---

*Layer placement: L3 Stable Constraint · Autonomy assessment domain · Always loaded for every Gate session*
*These guardrails add to the output — they do not alter the RULE-XX verdict.*
