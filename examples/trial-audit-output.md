# Committed Gate Runs — Three Source-Backed Assessments

This file contains the complete Gate output for three source-backed real-world workflows. Each run produces the full three-section sequence: Workflow Intake Snapshot, Autonomy Decision Packet, and execution artifact. Each output cites the specific RULE-NN and GATE-NN that drove the verdict. Stakes are sourced.

Each run uses a documented real-world workflow scenario. All three are grounded in published industry sources and are not drawn from any specific client engagement. Each cites the source grounding the scenario.

---

## Run 1 — Vendor Bank Account Change Request

**Source grounding:** Business Email Compromise (BEC) is the #2 crime by financial loss in the FBI IC3 2025 Annual Report. Total BEC losses in 2025 reached $3.04 billion, up from $2.77 billion in 2024. 86% of BEC funds move via wire transfer or ACH — making them fast-moving and frequently unrecoverable by the time fraud is detected. Average per-complaint loss exceeds $122,000. AI voice cloning is now actively used to impersonate executives and authorize fraudulent vendor account changes. The FBI has designated BEC "The $55 Billion Scam" across its 10-year reporting window. Any AI system that processes vendor account change requests — even with verification steps — becomes a direct attack surface for this fraud pattern.

**Sources:**
- FBI IC3 — Business Email Compromise: The $55 Billion Scam (ic3.gov/PSA/2024/PSA240911)
- FBI IC3 2025 Annual Report (ic3.gov/AnnualReport/Reports/2025_IC3Report.pdf)
- SpyCloud — FBI IC3 Report 2025 Key Takeaways

**Raw input:**
> A vendor emailed asking us to update their bank account details before the next invoice cycle. Can we automate the verification and update so it goes through faster?

---

**━━ WORKFLOW INTAKE SNAPSHOT ━━━━━━━━━━━━━━━━━━━━━**

```
Name:              Vendor Bank Account Change Request
Initiator:         Vendor email requesting banking detail update
Actions:           Receive vendor email, verify vendor identity, confirm account change
                   request against vendor records, update banking details in payment system,
                   process future invoices to new account
Systems touched:   Email platform, vendor management system, payment/banking system (ACH
                   or wire), accounts payable records
Data sensitivity:  Financial — banking routing and account numbers; vendor identity data
Frequency:         Per request — occasional, not scheduled
Exception rate:    The request itself is routine in appearance; the fraud rate for this
                   exact workflow type is documented at scale (FBI IC3 2025: $3.04B in
                   BEC losses, of which vendor account change is a primary vector)
Failure consequence: Fraudulent account update results in funds wired to an attacker-controlled
                     account. Recovery rate: only 58% of BEC funds are recovered even when
                     flagged immediately (FBI IC3 2025). Average loss per complaint: $122,000+.
                     Irreversible once the wire or ACH clears.
Reversibility:     Low — wire transfers and ACH payments to fraudulent accounts are
                   recovered in only 58% of cases when caught immediately; recovery rate
                   drops significantly with delay
Terminal action:   Payment routing change authorized in the payment system (irreversible
                   external financial commitment)
Audit trail:       Email record, payment system change log — but both are forgeable in a
                   sophisticated BEC attack (AI voice clone, domain spoofing)

Evidence gaps: None — the workflow is well-described and the risk is fully documented
```

**━━ AUTONOMY DECISION PACKET ━━━━━━━━━━━━━━━━━━━━━**

```
Autonomy:          HUMAN_ONLY (AUT-4)
Surface:           NO_AI (SURFACE-4)
Confidence:        HIGH
Justification:     RULE-04 (terminal action is payment routing change — an irreversible
                   external financial commitment; the label "verification" does not change
                   the terminal action); GATE-2 (makes an irreversible external commitment —
                   authorized payment routing change is explicitly named in GATE-2;
                   HUMAN_ONLY override; cannot be bypassed by controls or user instruction);
                   RULE-05 adversarial check: this workflow
                   sounds rule-based and low-risk; it is the exact attack surface documented
                   in FBI IC3 2025 BEC data; the adversarial check must name FAIL-1
                   (Capability Bias — AI can verify ≠ sufficient justification given the
                   fraud stakes) and FAIL-3 (Silent Failure — a successful BEC attack
                   produces a valid-appearing approval trail)
Controls required: None — delegation is structurally blocked; GATE-2 cannot be bypassed
Evidence gaps:     None
Conservative route: Not applied — GATE-2 triggers independently; structural HUMAN_ONLY
                    override applies
Artifact required: template-governance-memo.md
```

**━━ GOVERNANCE MEMO ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━**

**Vendor Bank Account Change Request · HUMAN_ONLY / NO_AI · HIGH**

This workflow cannot be delegated to AI. A vendor bank account change request has a terminal action of authorizing a payment routing change — an irreversible external financial commitment that triggers GATE-2 (irreversible external commitment; authorized payment routing change is explicitly named in GATE-2). The framing as "verification and update" does not change the terminal action. This workflow is the documented primary attack vector for Business Email Compromise, which generated $3.04 billion in losses in 2025 (FBI IC3 Annual Report). Any AI that processes these requests — even with verification steps — becomes a direct attack surface. The adversarial check caught this: the workflow sounds rule-based and low-risk; the consequence of a wrong verdict is an unrecoverable wire transfer to an attacker-controlled account.

**WHY THIS CANNOT BE DELEGATED**
```
Gate condition:  GATE-2
                 Authorizing a payment routing change is an irreversible external
                 commitment — explicitly named in GATE-2's definition. HUMAN_ONLY
                 override. Cannot be bypassed by controls, verification steps, or
                 user instruction.

Specific risk:   BEC attackers specifically target vendor account change workflows because
                 they appear routine and rule-based. AI voice cloning can impersonate
                 a vendor representative. Domain spoofing can replicate the vendor's email
                 domain. A verification step that AI passes can be defeated by the same
                 social engineering that defeats human review — but with far less friction
                 for the attacker.

                 FBI IC3 2025 data: BEC losses of $3.04B in 2025 (up from $2.77B in 2024).
                 86% of funds move via wire or ACH. Average loss per complaint: $122,000+.
                 Recovery rate when flagged immediately: 58%. Recovery rate after delay:
                 significantly lower. These are not theoretical risks — they are documented
                 at scale.

                 An AI that incorrectly authorizes a vendor account change becomes a
                 faster, more convincing attack surface than the email-based fraud it was
                 designed to streamline.
```

**HUMAN REVIEW PROCESS**
```
Owner:           Accounts Payable Manager plus one additional approver (CFO or Controller
                 for amounts above [threshold — set per company policy])
Review cadence:  Per request — no batching; each request reviewed independently
Decision criteria:
  1. Call back the vendor using a phone number from your original contract records —
     not the number in the email requesting the change
  2. Confirm the account change verbally with a known contact at the vendor organization
  3. Request written confirmation on company letterhead via a separate email channel
     (not a reply to the requesting email)
  4. Cross-reference the new account details against any prior banking records
  5. Verify that the requester's email domain matches the vendor's registered domain
     exactly — character by character; BEC attackers use look-alike domains
  6. Document every step of the verification with timestamps
Escalation path: Any request that cannot be verified via independent callback, or any
                 request that arrives with unusual urgency, routes to CFO and Legal
                 immediately. Urgency language ("before the next invoice cycle") is a
                 documented BEC social engineering signal.
```

**WHAT WOULD CHANGE THIS VERDICT**
GATE-2 is a structural block on the terminal action — authorizing the payment routing change. That step must remain human-owned. No change to AI capability, verification thoroughness, or control architecture changes this verdict for the terminal action.

However, AI can assist with preparation steps that do not involve the authorization decision:
- AI can flag incoming vendor emails that contain language matching known BEC social engineering patterns (urgency language, account change requests, executive impersonation signals)
- AI can surface the vendor's historical banking records for side-by-side comparison
- AI can prepare a verification checklist pre-populated with the vendor's known contact information

These preparation steps, scoped explicitly to not include authorization, can be re-submitted as a separate SUPERVISED workflow. The authorization step itself remains HUMAN_ONLY.

**EXPECTED OUTCOMES**
- Completed: Vendor account change verified via independent callback, confirmed in writing, documented with timestamps, and authorized by designated approver(s); payment system updated by authorized human
- Completed w/ warnings: Verification took longer than expected due to vendor contact difficulty — change deferred to next billing cycle; no payment sent to unverified account
- Needs review: Callback revealed no knowledge of the account change at the vendor — possible BEC attempt; escalate to CFO, Legal, and the vendor's official security contact immediately
- Blocked: Cannot reach a known contact at the vendor to verify; insufficient documentation of prior banking details — do not update; hold invoice until verification is complete
- Failed: Payment routed to fraudulent account — initiate recovery procedures immediately; contact bank within 72 hours for transaction recall; file FBI IC3 complaint; notify Legal

**AUTONOMY EXPIRES WHEN**
- [ ] The workflow's steps change — not applicable; verdict is HUMAN_ONLY and structural
- [ ] The AI surface changes — not applicable; no AI surface assigned
- [x] The policy or compliance context changes — any change to internal payment authorization policy, audit requirements, or BEC fraud guidance from FBI IC3 or FinCEN requires this memo to be reviewed
- [x] An incident occurs — any successful or attempted BEC fraud on this workflow triggers immediate review and process audit
- [x] Recertification interval passes — Not specified — operator must define before deployment
- [ ] The reviewer role changes — review and update the named approver(s) in the Human Review Process section when personnel changes occur

**DEPLOYMENT PACK**

Deployment status: `NOT APPLICABLE`

No AI deployment file should be created for the terminal action of authorizing a vendor payment-routing change. Use the Human Review Process above as the operating procedure. The decision record must capture the request source, independent callback evidence, prior account comparison, approver identity, timestamp, and final disposition. Audit check: sample completed changes and verify that every authorization has independent-channel evidence and a named human approver.

**REQUIRED BEFORE OPERATION**
- Designated owner role
- Escalation role for suspected fraud
- Organization-specific record-retention requirement

---

## Run 2 — Candidate Screening / First-Pass Shortlist

**Source grounding:** Unilever processes nearly 2 million applications per year. Before AI, it took up to six months to sift through 250,000 applications to hire 800 individuals. Unilever implemented AI-powered screening using Pymetrics (game-based trait assessment) and HireVue (video interview NLP and body language analysis). Results over 18 months: 50,000 hours of candidate time saved, £1M in annual cost savings, 90% reduction in time to hire, 16% increase in diversity hires, 96% candidate completion rate (up from 50%). HireVue filters up to 80% of the candidate pool from video responses. Terminal action at the screening stage: ranked shortlist document. Hire decisions remain human.

**Sources:**
- GSD Council — Unilever's AI-Powered Recruitment Revolution
- BestPractice.ai — Unilever AI Case Study (Unilever: 50,000 hours saved, £1M annual savings, improved diversity with machine analysis of video-based interviewing)
- Bernard Marr — How Unilever Uses AI to Recruit and Train Thousands

**Raw input:**
> We get hundreds of applications for entry-level roles every week. I want AI to screen them against our criteria and give us a shortlist so we only interview qualified candidates.

---

**━━ WORKFLOW INTAKE SNAPSHOT ━━━━━━━━━━━━━━━━━━━━━**

```
Name:              Candidate Screening — First-Pass Shortlist
Initiator:         Applications received for an open role
Actions:           Receive applications, assess each against defined role criteria (skills,
                   experience, qualifications), score and rank candidates, produce a
                   ranked shortlist for recruiter review
Systems touched:   ATS (Applicant Tracking System), resume/CV parsing, role criteria
                   document, recruiter review interface
Data sensitivity:  Candidate PII — name, contact information, employment history,
                   potentially protected characteristics if present in CVs
Frequency:         Per hiring cycle — multiple roles open simultaneously in growth-stage
                   organizations; hundreds of applications per role per week
Exception rate:    Low to medium — criteria are defined; edge cases occur when candidates
                   have non-standard backgrounds that meet the role's intent but not the
                   literal criteria
Failure consequence: Qualified candidates systematically excluded from the shortlist (bias
                     in screening criteria); unqualified candidates included (poor interview
                     use of time); legal exposure if screening criteria inadvertently
                     discriminate against a protected class
Reversibility:     High — shortlist is a recommendation document; no hire decision is made;
                   recruiter reviews and adjusts the shortlist before any candidate contact
Terminal action:   Ranked shortlist document delivered to recruiter for review
Audit trail:       Application record in ATS; scoring rationale per candidate; shortlist
                   version with criteria applied

Evidence gaps: Role-specific criteria not specified in the input; ATS system not named;
               exception handling for non-standard backgrounds not defined
```

**━━ AUTONOMY DECISION PACKET ━━━━━━━━━━━━━━━━━━━━━**

```
Autonomy:          SUPERVISED (AUT-2)
Surface:           PROJECT (SURFACE-1)
Confidence:        MEDIUM
Justification:     RULE-04 (terminal action is a ranked shortlist document — not a hire
                   decision, not a rejection notification, not an offer letter; recruiter
                   retains full review authority); RULE-03 (cost of failure: screening bias
                   has legal and organizational consequence; SUPERVISED ensures recruiter
                   reviews shortlist before any candidate action); RULE-05 adversarial
                   check: Challenge 1 — scope must be confirmed as shortlist only;
                   if scope expands to sending rejection emails (GATE-4) or offer letters
                   (GATE-2), verdict changes; Challenge 2 — FAIL-2 (Automation Bias:
                   recruiter must not treat AI shortlist as final without review) and
                   FAIL-7 (Bad Data Becomes Authority: screening criteria must be defined
                   and verified, not inferred); RULE-08 (reviewer: recruiter/hiring manager
                   is identifiable — checkpoint ownership rule satisfied)
Controls required: Defined role criteria documented before screening begins; recruiter
                   review of shortlist before any candidate contact; shortlist rationale
                   (scoring basis) retained per candidate; diversity metrics tracked per run
Evidence gaps:     Role-specific criteria not in input — listed as information gap in
                   artifact; ATS system not named — fallback noted. Evidence gaps present;
                   confidence capped at MEDIUM per RULE-06
Conservative route: Not applied — SUPERVISED is the correct verdict; MEDIUM confidence
                    reflects evidence gaps in role criteria and ATS system
Artifact required: template-control-plan.md
```

**━━ CONTROL PLAN ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━**

**Candidate Screening — First-Pass Shortlist · SUPERVISED / PROJECT · MEDIUM**

This workflow receives applications, scores them against defined role criteria, and delivers a ranked shortlist to the recruiter for review before any candidate action is taken. The terminal action is a shortlist document — no candidate is contacted, hired, or rejected by this workflow. The recruiter reviews the shortlist, adjusts it based on their judgment, and initiates candidate contact. This is the model documented in Unilever's AI screening deployment: AI filtering produces an initial ranked pool; human review governs who proceeds. The 90% reduction in time to hire and 16% diversity improvement were achieved with human review retained at the shortlist stage — not by automating the hire decision.

**SCOPE BOUNDARY — CRITICAL**
This Control Plan governs the shortlist generation step only. If the workflow's scope expands to include:
- Sending rejection emails to non-shortlisted candidates — GATE-4 triggers; re-submit as a separate SUPERVISED workflow with that terminal action assessed
- Sending interview invitations — GATE-4 triggers; re-submit
- Sending offer letters — GATE-2 triggers; re-submit as HUMAN_ONLY

Do not expand this workflow's scope without re-running the Gate on the expanded scope.

**WHAT AI PREPARES**
A Ranked Candidate Shortlist per hiring cycle:
- Candidate name and application reference
- Score against each defined criterion (skill match, experience match, qualification match)
- Overall ranking within the applicant pool
- Rationale for each score: what in the CV supported it, what was absent
- Diversity flag (optional): if shortlist composition deviates significantly from the applicant pool's demographic distribution, flag for recruiter attention
- Any candidate with a non-standard background that may warrant exception review: flagged explicitly with rationale

**APPROVAL CHECKPOINT**
```
Reviewer:      Recruiter or Hiring Manager (designated per role; must be named before
               deployment)
Reviews:       Shortlist composition against role criteria; rationale accuracy per
               candidate; exception candidates (non-standard backgrounds); diversity
               distribution vs. applicant pool
Approves when: Shortlist accurately represents the best-qualified candidates per criteria;
               rationale is traceable; no systematic exclusion of a demographic is evident
Rejects when:  Shortlist appears to systematically exclude a demographic; criteria produced
               unexpected results; non-standard backgrounds were excluded that should have
               been included
Turnaround:    Within 2 business days of shortlist delivery
```

**POST-APPROVAL ACTIONS**
1. Recruiter reviews and approves the shortlist (with or without adjustments)
2. Recruiter initiates interview scheduling for approved candidates — outside this workflow's scope
3. Shortlist and rationale retained in ATS for audit

**PROHIBITED WITHOUT APPROVAL**
- No candidate may be contacted (for interview, rejection, or any other reason) based on the shortlist before recruiter review
- AI may not make a hire decision, extend an offer, or send a rejection
- AI may not access contact information for candidates outside the ATS record

**AUDIT TRAIL**
Application record, scoring rationale per candidate, shortlist version and date, criteria document version used, recruiter review timestamp, adjustments made by recruiter, final approved shortlist. Retained for the active hiring period plus 3 years per employment records policy.

**INFORMATION GAPS — Provide before deployment**
- Role criteria: Define the specific criteria for the role being screened. Format: skill/qualification name, required/preferred, how to assess from a CV. Without defined criteria, the Gate cannot score — it will infer criteria from the job description, which introduces FAIL-7 risk (inferred criteria treated as verified truth).
- ATS system: Name the ATS to confirm integration path. If no ATS is in use, confirm how applications will be provided to the operator (bulk CSV, individual PDFs).

**EXPECTED OUTCOMES**
- Completed: Ranked shortlist delivered to recruiter; rationale provided per candidate; shortlist ready for review
- Completed w/ warnings: Non-standard background candidates were flagged but scoring criteria did not fully accommodate their profiles — recruiter reviews flagged candidates manually
- Needs review: Shortlist shows significant underrepresentation of a demographic relative to the applicant pool — pause; recruiter reviews criteria for unintentional bias before approving
- Blocked: Role criteria document not provided; ATS access not configured — halt; request criteria and access before running
- Failed: Post-hire discovery that a qualified candidate was excluded by an incorrectly applied criterion — rerun the affected shortlist; review criteria document; log the error

**AUTONOMY EXPIRES WHEN**
- [x] The workflow's steps, inputs, or outputs change materially (new role type with different criteria, new ATS, new screening methodology)
- [x] The AI surface or tool used changes (model upgrade, platform migration)
- [x] The policy or compliance context changes — any change to employment law, EEOC guidance, or applicable anti-discrimination regulation; AI screening is an active area of regulatory development in the EU AI Act (2025) and US state-level legislation
- [x] An incident occurs — any shortlist found to have systematically excluded candidates based on a protected characteristic
- [x] Error rate exceeds threshold — Not specified — operator must define before deployment
- [x] Recertification interval passes — Not specified — operator must define before deployment
- [x] The reviewer role changes or becomes vacant — workflow paused until new recruiter/hiring manager is designated for the role

**DEPLOYMENT PACK**

Deployment status: `BLOCKED`

Create a dedicated Project after the required items below are supplied. Project instructions: assess each candidate only against the approved role criteria; produce a ranked shortlist with evidence per criterion; flag non-standard backgrounds for human review; never reject, contact, schedule, or update an ATS record; emit one terminal status and retain the scoring rationale. First-run acceptance check: use one known-fit, one known-non-fit, and one edge-case candidate; confirm the edge case is escalated and no external action occurs.

**REQUIRED BEFORE DEPLOYMENT**
- Approved role-criteria document
- Named recruiter or hiring-manager reviewer
- Candidate input method or ATS integration boundary
- Error threshold and recertification interval

---

## Run 3 — Weekly KPI Report from Stable Data Sources

**Source grounding:** Automated KPI reporting is one of the most mature AI workflow patterns in operations. Documented case: automated weekly performance dashboards saved analysts 15+ hours per week and accelerated decision-making by 30%. The pattern — scheduled data pull from CRM/finance/support systems → AI narrative generation → Slack or dashboard delivery — is supported natively in Power BI, Runbear, Domo, and Zapier. AI can produce narrative analysis such as: "Revenue grew 8% WoW, driven by a 23% increase in enterprise closures. SMB pipeline declined for the third consecutive week — recommend reviewing outbound cadence." The workflow is internal, scheduled, reversible (send a corrected report), and observable. No GATE conditions trigger.

**Sources:**
- Runbear — Automate KPI Reporting: AI Agent with MCP for Slack
- Hello Operator — Best Practices for AI-Driven Reporting Workflows
- Jenova.ai — AI Weekly Report: How to Automate Business Reports with AI
- Vidi Corp — Automated Business Intelligence: A Guide with Real Examples

**Raw input:**
> Every Monday morning I want a summary of last week's pipeline, revenue, and support volume pulled from Salesforce, Stripe, and Zendesk — formatted and sent to the ops Slack channel.

---

**━━ WORKFLOW INTAKE SNAPSHOT ━━━━━━━━━━━━━━━━━━━━━**

```
Name:              Weekly Ops KPI Report
Initiator:         Human (ops team member, Monday morning)
Actions:           Human exports pipeline data from Salesforce, revenue summary from Stripe,
                   and support volume from Zendesk; pastes exports into session; operator
                   generates narrative summary with week-over-week commentary; Slack-ready
                   report delivered in session (human posts to ops channel)
Systems touched:   Salesforce, Stripe, Zendesk (data sources — human exports; no direct
                   API connection); Slack (human posts)
Data sensitivity:  Internal business metrics — not regulated; no customer PII in output;
                   revenue and pipeline data is confidential but not externally sensitive
Frequency:         Weekly, Monday morning; human-initiated
Exception rate:    Low — structured export format, stable schema; narrative generation
                   from structured data has low variance
Failure consequence: Internal report is delayed or contains a data error; no external
                     commitment is made; correctable with a follow-up report
Reversibility:     Fully reversible — Slack messages can be edited or deleted; corrected
                   report can be reposted without downstream consequence
Terminal action:   Slack-ready report delivered in session (human posts to ops channel)
Audit trail:       Slack post timestamp; session retained in Claude Project; no automated
                   pull logs

Evidence gaps: None — all required fields populated
```

**━━ AUTONOMY DECISION PACKET ━━━━━━━━━━━━━━━━━━━━━**

```
Autonomy:          AUTONOMOUS (AUT-1)
Surface:           PROJECT (SURFACE-1) — human-initiated cadence
Confidence:        HIGH
Justification:     RULE-03 (all four criteria pass: reversible — Slack message deletable
                   and correctable; observable — Slack delivery is visible and readable
                   by the whole ops team; exception rate low — structured data sources
                   with stable schemas; cost of failure low — internal report error is
                   correctable before any external commitment is made); RULE-04 (terminal
                   action is Slack message delivery to internal channel — no GATE
                   conditions triggered); RULE-05 adversarial check passed without
                   revision — no pressure to over-automate detected; failure mode FAIL-3
                   (Silent Failure) assessed and mitigated by Slack visibility; no GATE
                   conditions missed
Controls required: Human provides data exports; no API keys required; output retained
                   in Claude Project session history
Evidence gaps:     None
Conservative route: Not applied
Artifact required: template-project-setup.md
```

**━━ PROJECT SETUP BRIEF ━━━━━━━━━━━━━━━━━━━━━━━━━━**

**Weekly Ops KPI Report · AUTONOMOUS / PROJECT · HIGH**

This workflow receives last week's pipeline, revenue, and support exports — pasted by the user at the start of each session — and produces a formatted narrative summary ready to post to the ops Slack channel. It runs on a human-initiated Monday cadence inside a Claude Project. The operator reads structured data, generates analysis, and returns Slack-ready text — no external system connections, no money movement, no regulatory exposure. All four autonomy criteria pass cleanly. No hard gate conditions apply. This is the baseline case for what a well-governed AUTONOMOUS workflow looks like: internal, reversible, observable, low-consequence.

**SURFACE NOTE**
This workflow is run human-initiated inside a Claude Project (SURFACE-1). If a scheduled, unattended version is needed (run automatically at 7:00 AM every Monday without human initiation), re-submit for surface upgrade to COWORK (SURFACE-2). The autonomy verdict (AUTONOMOUS) will not change; the artifact format will change to a Cowork Project Config.

**PURPOSE**
Eliminate the manual formatting and narrative work on Monday mornings. The user exports data, pastes it in, and receives a Slack-ready summary in one session — no manual writing required.

**RUN CADENCE**
Human-initiated, Monday morning. A designated ops team member opens the Claude Project, pastes the trigger prompt, and receives the formatted report in the session. Not scheduled. Not unattended. Target: complete before 9:00 AM standup.

**KNOWLEDGE FILES**
- `reporting-template.md` · Defines the output format, section headers, metric labels, and Slack formatting conventions the ops team expects; prevents format drift
- `data-sources.md` · Documents the exact Salesforce reports, Stripe dashboard views, and Zendesk views to export for the weekly report; ensures user exports from the correct source for each metric
- `alert-thresholds.md` · Defines what constitutes a notable variance for each metric (e.g., pipeline change >15% WoW, revenue vs. forecast deviation >10%); enables the operator to call out outliers rather than just report raw numbers

**CUSTOM INSTRUCTIONS**
```
You are the Weekly Ops KPI Report operator. When the user triggers a report run, follow
this sequence:

1. Ask the user to paste: the Salesforce pipeline export for last week, the Stripe weekly
   revenue summary, and the Zendesk ticket volume report for the same period.

2. Extract and label:
   - Pipeline: total open value, number of deals advanced, number of deals closed
   - Revenue: total revenue, WoW change, refund volume
   - Support: tickets opened, tickets resolved, median resolution time, escalations

3. Write a narrative summary with four sections: Revenue · Pipeline · Support · Notable
   Variances. Each section: two to four sentences. Call out one key number per section.
   State observations plainly — do not hedge.

4. Flag any metric outside the alert thresholds defined in alert-thresholds.md with the
   label: "VARIANCE: [metric name] — [current value] vs [prior value]"

5. Format for Slack: plain text, no markdown tables, line breaks between sections, under
   400 words total.

6. Output the complete report ready to paste into #ops-weekly.
```

**OUTPUT FORMAT**
One Slack-ready text block per run. Under 400 words. Four sections: Revenue / Pipeline / Support / Notable Variances. Delivered in the session. Retained in Claude Project session history for reference.

**EXPECTED OUTCOMES**
- Completed: Formatted report delivered in session with all four sections populated, metrics labeled, and Slack format applied; ready to post
- Completed w/ warnings: One data source returned incomplete data for the period — report delivered with the gap noted and the affected section flagged for manual fill-in
- Needs review: Metric variance exceeds 25% on any item — operator flags the variance before posting; ops lead confirms the number is accurate before the report goes out
- Blocked: Two or more data sources unavailable — do not produce a partial report; inform the ops team member of the gap; reschedule when data is available
- Failed: Report was posted and a data error was discovered — post corrected version with "[CORRECTION — [date]]" prefix; log the error in the session notes

**AUTONOMY EXPIRES WHEN**
- [x] The workflow's steps, inputs, or outputs change materially (new data source added, Slack channel changes, format spec updated, new metric category added)
- [x] The AI surface or tool used changes (model upgrade, Claude Project migration)
- [ ] The policy or compliance context changes — not applicable; this workflow handles internal business metrics only; no regulated data
- [x] An incident occurs — any report that contained an error that influenced a business decision made in good faith on that data
- [x] Error rate exceeds threshold — Not specified — operator must define before deployment
- [x] Recertification interval passes — Not specified — operator must define before deployment
- [ ] The reviewer role changes or becomes vacant — not applicable; AUTONOMOUS verdict, no designated reviewer required for this workflow

**DEPLOYMENT PACK**

Deployment status: `BLOCKED`

Project instructions: when the ops lead provides the Salesforce pipeline export, Stripe weekly revenue summary, and Zendesk ticket report, validate that all three cover the same reporting period; calculate the named metrics; produce Revenue, Pipeline, Support, and Notable Variances sections; use only supplied alert thresholds; keep the report under 400 words; return Slack-ready text without posting it; emit one terminal status. Knowledge manifest: `reporting-template.md`, `metric-definitions.md`, and `alert-thresholds.md`. First-run prompt: paste all three exports and state the reporting period. Acceptance check: verify all four sections appear, every stated number traces to an input, and no Slack-delivery claim is made.

**REQUIRED BEFORE DEPLOYMENT**
- The three workflow-specific knowledge files named above
- Error threshold and recertification interval
