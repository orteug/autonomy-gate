# Risk Classification — Reference

This file defines the four risk levels (RISK-L1 through RISK-L4) and eight named failure patterns (FAIL-1 through FAIL-8) used by the Gate in Phase 1 assessments.

The adversarial check (RULE-05, Challenge 2) must reference at least one FAIL-NN pattern when naming the most likely failure mode. The base scoring (RULE-03) uses risk level to calibrate the cost of failure criterion.

---

## Risk Levels — RISK-L1 through RISK-L4

Risk levels combine failure consequence and reversibility. They are assigned during base scoring (RULE-03) under the "cost of failure" criterion.

---

### RISK-L1 — Low Risk

**Definition:** Internal-only consequences. Reversible within minutes. No external party is affected before correction. No financial, regulatory, or reputational exposure.

**Characteristics:**
- Failure is visible before it reaches a downstream decision-maker
- Correction requires minimal effort
- No customer, financial system, or compliance record is affected

**Workflow examples at this level:**
- Internal Slack digest from meeting notes (correction: send updated digest)
- Weekly KPI report to ops channel (correction: resend corrected report)
- Bounded backlog doc draft (correction: revise draft before PR is opened)
- Internal support ticket routing (correction: reroute ticket before agent acts)

**Gate implication:** Supports AUTONOMOUS where other criteria also pass.

---

### RISK-L2 — Medium Risk

**Definition:** Downstream teams or customers are affected, but correction is possible with effort. Some external visibility. No irreversible commitment.

**Characteristics:**
- Correction requires communication, effort, or coordination
- Customer-visible but correctable (e.g., a follow-up message can address the error)
- No financial transaction, permission change, or regulatory filing

**Workflow examples at this level:**
- Personalized outbound email campaign (correction: follow-up or retraction possible; original email persists)
- Lead assignment in CRM (correction: reassign; delayed response to lead)
- Candidate screening shortlist (correction: re-run; delayed hiring timeline)
- New hire onboarding task routing (correction: manual correction; delayed start)

**Gate implication:** Supports SUPERVISED. AUTONOMOUS is not appropriate without additional controls.

---

### RISK-L3 — High Risk

**Definition:** Financial loss, regulatory exposure, or significant reputational impact. Correction is partial or conditional on third-party cooperation. Some actions may be irreversible.

**Characteristics:**
- Financial impact: money moved, billing error, payment dispute
- Regulatory exposure: compliance record affected, audit trail required
- Reputational impact: external publication, customer communication, or press record
- Correction requires external cooperation or has a time window

**Workflow examples at this level:**
- Monthly financial close reconciliation (incorrect close affects financial records)
- Invoice processing and payment release (incorrect payment may not be recoverable)
- Social media scheduling with modification to copy (public error, reputational)
- Sanctions screening auto-clear (regulatory compliance, irreversible if false negative)
- Ecommerce high-risk order fulfillment/payment capture (financial + customer impact)

**Gate implication:** Requires SUPERVISED minimum. GATE-1 (moves money) or GATE-4 (external publication) likely apply. Named reviewer required (RULE-08).

---

### RISK-L4 — Critical Risk

**Definition:** Irreversible external commitment with major financial, legal, or security consequence. Correction requires external consent, legal process, or is impossible.

**Characteristics:**
- Irreversible after execution: no rollback without third-party action or legal remedy
- Affects external party's rights, finances, or security
- GATE-2 or GATE-3 applies independently

**Workflow examples at this level:**
- Vendor bank account change authorization (authorized payment routing is a direct BEC attack surface; $3.04B losses in 2025 per FBI IC3 2025 Annual Report)
- Access permission change in finance or security systems (GATE-3: who can see or do what)
- Signed contract submission to counterparty (GATE-2: irreversible external commitment)
- Regulatory filing submission — FINRA, SEC, OFAC (GATE-2: submission is irreversible; "Responsibility cannot be delegated to technology" per Consult CRA compliance guidance)
- Press release publication (GATE-2: published record; retraction does not erase)

**Gate implication:** `HUMAN_ONLY` with `NOT_APPLICABLE` handoff status. GATE-2 or GATE-3 overrides. No controls can reduce this terminal action to SUPERVISED; it cannot be delegated.

---

## Named Failure Patterns — FAIL-1 through FAIL-8

These are the domain-specific failure modes for AI automation governance. The adversarial check (RULE-05, Challenge 2) must name at least one applicable FAIL-NN pattern and assess whether the workflow description addresses it.

---

### FAIL-1 — Capability Bias

**What it looks like:** User asks "can AI do this?" and treats AI capability as sufficient justification for automation. The framing skips the consequence question entirely.

**Indicator phrases:** "AI can handle that," "just automate it," "GPT can do this easily," "there's a plugin for it"

**Required control:** The Gate answers the consequence question, not the capability question. Capability is never sufficient justification. RULE-03 always scores reversibility, observability, exception rate, and cost of failure — regardless of whether AI is technically capable.

**Adversarial check application:** When Challenge 1 ("Is this the minimum justified autonomy?") surfaces a capability-based framing, downgrade one level.

---

### FAIL-2 — Automation Bias

**What it looks like:** A human reviewer over-trusts structured or machine output and skips the review step. The checkpoint exists on paper but is not functioning as a real gate. Common when outputs are formatted, numbered, or appear "official."

**Indicator phrases:** "We'll have someone glance at it," "the AI is usually right," "it only needs a quick sign-off," "our team will catch any issues"

**Required control:** High-impact outputs require a named reviewer with a specific rubric and authority to stop execution (RULE-08). "Glance at it" is FAIL-6, not a checkpoint. The Control Plan must name: reviewer role, what they evaluate, criteria for approval, criteria for rejection, and turnaround time.

**Adversarial check application:** When Challenge 1 or Challenge 2 surfaces a vague approval step, check for FAIL-2 and FAIL-6 in combination. Downgrade confidence if reviewer is unidentifiable.

---

### FAIL-3 — Silent Failure

**What it looks like:** The system fails, stalls, or skips an exception without surfacing its state. Downstream processes proceed on bad data or missing output. The failure is invisible until damage is done.

**Indicator phrases:** "It just stops if something goes wrong," "we check it occasionally," "errors get logged somewhere," "it usually completes"

**Required control:** Every run emits a terminal status from the valid set: COMPLETED, COMPLETED_WITH_WARNINGS, NEEDS_REVIEW, BLOCKED, FAILED, SKIPPED, TIMED_OUT. The status is logged to a named destination. An alert fires on FAILED or BLOCKED. Artifact EXPECTED OUTCOMES section must define what each status looks like for this specific workflow.

**Adversarial check application:** Challenge 2 must name FAIL-3 when the workflow description does not specify error handling or when the audit trail is described as "partial" or absent (GATE-5 check).

---

### FAIL-4 — Stale SOP Drift

**What it looks like:** The workflow changes — a field is renamed, a policy is updated, an API changes behavior — but the automation continues running on the old rules. The discrepancy is not caught until it has been in production for weeks or months.

**Indicator phrases:** "We update the process as we go," "it's been running fine," "we'll fix it if something breaks," "we don't have a formal update process"

**Required control:** Autonomy expires on workflow, model, policy, or tool change. AUTONOMY EXPIRES WHEN section in every artifact must name this condition. Recertification cadence must be specified (RULE-13).

**Adversarial check application:** Challenge 3 must check whether the workflow description implies dependencies on external systems, policies, or data sources that change independently. FAIL-4 risk increases with every external dependency.

---

### FAIL-5 — Overbroad Agency

**What it looks like:** The system has more permission than the workflow requires. A reporting operator can access billing records. A routing operator can send external emails. Scope creep in permissions is a security and governance failure independent of the automation quality.

**Indicator phrases:** "It has admin access just to be safe," "we gave it full permissions so it doesn't get blocked," "it can access everything it needs and more"

**Required control:** Scope tools, permissions, spend limits, and data access to the minimum required for the specific workflow. The artifact must name what the operator is authorized to access and explicitly list what it is prohibited from accessing. FAIL-5 is the structural condition for GATE-3 escalation in future audits.

**Adversarial check application:** Challenge 1 must check whether the workflow description implies broader system access than the described actions require.

---

### FAIL-6 — Human-in-the-Loop Theater

**What it looks like:** The workflow claims human review exists. The reviewer lacks time, authority, criteria, or the practical ability to stop execution. The checkbox gets checked without the work being done.

**Indicator phrases:** "A manager signs off," "it goes through approval," "someone reviews it before it sends," "we have a review step"

**Required control:** The checkpoint ownership rule (RULE-08) applies. A real checkpoint names: the reviewer role (specific, not "manager"), what they evaluate (explicit criteria, not "the output"), the conditions under which they approve vs. reject, their turnaround time, and their authority to stop execution unilaterally. If any of these are absent, the confidence is capped at LOW and FAIL-6 is named in the packet.

**Adversarial check application:** Challenge 1 must probe every claimed approval step. "Signs off" without criteria is FAIL-6 until proven otherwise.

---

### FAIL-7 — Bad Data Becomes Authority

**What it looks like:** Incomplete, averaged, stale, or inferred data is treated as verified truth. The automation produces a high-confidence output based on inputs that were never validated. The confidence of the output exceeds the confidence of the inputs.

**Indicator phrases:** "It uses whatever's in the CRM," "we trust the data is correct," "it pulls from our spreadsheet," "the data is usually up to date"

**Required control:** Evidence gaps are named in the Workflow Intake Snapshot. Low-confidence inputs downgrade the autonomy verdict. The artifact must name the data sources relied on and specify what validation is applied before the automation acts on them. Data quality is a prerequisite for AUTONOMOUS — not an assumption.

**Adversarial check application:** Challenge 2 must name FAIL-7 when the workflow description references external data sources without describing validation logic.

---

### FAIL-8 — Partial Deployment Failure

**What it looks like:** The automation is deployed inconsistently across tools, versions, prompts, or permissions. One team is running version 1.0 rules; another is running an undocumented modified version. Handoffs between surfaces do not transfer state. The operator behaves differently in different contexts.

**Indicator phrases:** "We customized it for our team," "we updated the prompt a while back," "different offices use it differently," "it works differently in staging vs. production"

**Required control:** Version the operator. The Autonomy Decision Packet is the forward-looking handoff object — when moving between surfaces, the packet transfers with the workflow. AUTONOMY EXPIRES WHEN the AI surface or tool changes (RULE-13). Any deployment change requires re-assessment before the automation resumes.

**Adversarial check application:** Challenge 3 must check whether the workflow description implies cross-surface handoffs or multi-environment deployment without explicit version control.

---

## Adversarial Check — FAIL-NN Application Table

| Challenge | Primary FAIL-NN to check |
|-----------|--------------------------|
| Challenge 1: Is this minimum justified autonomy? | FAIL-1 (Capability Bias), FAIL-5 (Overbroad Agency), FAIL-6 (Human-in-the-Loop Theater) |
| Challenge 2: What is the most likely failure mode? | FAIL-2 (Automation Bias), FAIL-3 (Silent Failure), FAIL-7 (Bad Data Becomes Authority) |
| Challenge 3: Does the terminal action trigger any gate? | FAIL-4 (Stale SOP Drift), FAIL-8 (Partial Deployment Failure) |

Every adversarial check must reference at least one FAIL-NN by ID in the justification section of the Autonomy Decision Packet.
