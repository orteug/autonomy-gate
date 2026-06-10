# The Autonomy Gate — Examples

This file contains 14 adversarial test workflows. Each demonstrates the complete Gate sequence: raw input → Workflow Intake Snapshot → Autonomy Decision Packet → execution artifact. Each cites the RULE-NN and GATE-NN that drove the verdict. Edge cases are labeled so the mechanism being demonstrated is visible, not just the output.

---

## Example 1 — Weekly KPI Report from Stable Data Sources

**Mechanism demonstrated:** Clean case — all four autonomy criteria pass. No GATE conditions. Baseline for AUTONOMOUS verdict. Surface distinction between PROJECT (human-initiated) and COWORK (scheduled).

**Raw input:**
> "Every Monday morning I want a summary of last week's pipeline, revenue, and support volume pulled from Salesforce, Stripe, and Zendesk — formatted and sent to the ops Slack channel."

---

**━━ WORKFLOW INTAKE SNAPSHOT ━━━━━━━━━━━━━━━━━━━━━**

```
Name:              Weekly Ops KPI Report
Initiator:         Human (ops team member, Monday morning)
Actions:           Human exports pipeline data from Salesforce, revenue summary from Stripe,
                   and support volume from Zendesk; pastes exports into session; operator
                   generates narrative summary and delivers a Slack-ready report in session
Systems touched:   Salesforce, Stripe, Zendesk (data sources — human exports; no direct
                   integration); Slack (delivery — human posts the report)
Data sensitivity:  Internal business metrics — not regulated, no customer PII in output
Frequency:         Weekly, Monday morning; human-initiated
Exception rate:    Low — structured data sources, stable schema, no judgment required
Failure consequence: Internal report is delayed or contains stale data; no external commitment made
Reversibility:     Fully reversible — send corrected report; Slack messages can be edited or deleted
Terminal action:   Slack-ready report produced in session (human posts to channel)
Audit trail:       Claude Project session history; data export timestamps from source systems

Evidence gaps: None — all required fields populated
```

**━━ AUTONOMY DECISION PACKET ━━━━━━━━━━━━━━━━━━━━━**

```
Autonomy:          AUTONOMOUS (AUT-1)
Surface:           PROJECT (SURFACE-1) — human-initiated cadence; human provides data exports
Confidence:        HIGH
Justification:     RULE-03 (all four criteria pass: reversible, observable, low exception rate,
                   low failure consequence); no GATE conditions triggered; RULE-05 adversarial
                   check passed without revision; PROJECT surface confirmed appropriate —
                   no external API calls; human pastes data exports; operator formats output
Controls required: Data export timestamps retained; report version retained in session history
Evidence gaps:     None
Conservative route: Not applied
Artifact required: template-project-setup.md
```

**Surface note:** If this runs on a cron schedule without human initiation, the surface changes to COWORK (SURFACE-2). The verdict (AUTONOMOUS) does not change; the artifact template does. See Example 13 for a fallback demonstration if COWORK is unavailable.

**━━ PROJECT SETUP BRIEF ━━━━━━━━━━━━━━━━━━━━━━━━━━**

**Weekly Ops KPI Report · AUTONOMOUS / PROJECT · HIGH**

This workflow receives last week's pipeline, revenue, and support exports — pasted by the user at the start of each session — and produces a formatted narrative summary ready to post to the ops Slack channel. It runs on a human-initiated Monday cadence inside a Claude Project. The operator reads the pasted data, generates analysis, and returns Slack-ready text — no external system connections, no money movement, no regulatory exposure. All four autonomy criteria pass cleanly, and no hard gate conditions apply.

**PURPOSE**
Eliminate the manual formatting and narrative work on Monday mornings. The user exports data, pastes it in, and receives a Slack-ready summary in one session — no manual writing required.

**RUN CADENCE**
Human-initiated, Monday morning. Operator does not schedule or run unattended. The person running the report pastes the prompt into the Claude Project and receives output within the session.

**KNOWLEDGE FILES**
- `reporting-template.md` · Defines the output format, section headers, and metric labeling convention the ops team expects
- `data-sources.md` · Documents which Salesforce reports, Stripe dashboards, and Zendesk views to export for the weekly report — ensures user exports from the correct source for each metric
- `baseline-benchmarks.md` · Prior week and month averages so the operator can surface "up 8% WoW" commentary rather than raw numbers

**CUSTOM INSTRUCTIONS**
```
You are the Weekly Ops KPI Report operator. When activated, follow this sequence exactly:

1. Ask the user to paste the Salesforce pipeline export, Stripe weekly revenue summary, and Zendesk ticket volume data for the reporting period.
2. Extract and label: pipeline value, deals advanced, deals closed, revenue total, refund volume, support tickets opened, support tickets resolved, median resolution time.
3. Write a narrative summary with these sections: Revenue · Pipeline · Support · Notable Trends. Each section: two to four sentences, one key number called out, one observation stated plainly.
4. Flag any number that differs by more than 15% from the prior week and label it: "Notable variance — [metric]: [value] vs [prior week value]."
5. Format for Slack: no markdown tables, use plain text lists, keep under 400 words.
6. Provide formatted copy ready to paste into the #ops-weekly Slack channel.
```

**OUTPUT FORMAT**
Every run produces: one Slack-ready text block, under 400 words, organized by Revenue / Pipeline / Support / Notable Trends. Delivered in the same session. Retained in the Claude Project history for reference.

**EXPECTED OUTCOMES**
- Completed: Formatted Slack report delivered in session with all four sections populated and metrics labeled
- Completed w/ warnings: One data source was incomplete — report delivered with the gap noted and the missing section flagged
- Needs review: Source data contains a variance exceeding 30% in any metric — the operator flags it before the report is posted
- Blocked: Two or more data sources missing — operator names the gaps and does not produce a partial report
- Failed: Output is delivered but contains a labeled error discovered after posting — send corrected version with "[CORRECTION]" prefix

**AUTONOMY EXPIRES WHEN**
- [x] The workflow's steps, inputs, or outputs change materially (e.g., new data source added, Slack channel changes, format spec updated)
- [x] The AI surface or tool used changes (model upgrade, platform migration)
- [ ] The policy or compliance context changes — not applicable; this workflow handles internal business metrics only
- [x] An incident occurs — any output that caused unintended harm or required correction
- [x] Error rate exceeds 10% of weekly runs requiring manual correction — review and re-submit to Gate
- [x] 6 months pass without a recertification review — review by [date: December 2026]
- [ ] The reviewer role changes or becomes vacant — not applicable; AUTONOMOUS verdict, no reviewer required

---

## Example 2 — Client Onboarding with Undocumented Exceptions

**Mechanism demonstrated:** Exception rate failure in RULE-03 base scoring. "Mostly the same" ≠ "always the same." RULE-05 adversarial check flags pressure to over-automate. SOP_FIRST is the correct verdict — not a failure state.

**Raw input:**
> "Our client onboarding involves sending a welcome email, setting up their account, scheduling a kickoff call, and getting them into our project management tool. It's mostly the same every time but sometimes things are different depending on the client. Can we automate it?"

---

**━━ WORKFLOW INTAKE SNAPSHOT ━━━━━━━━━━━━━━━━━━━━━**

```
Name:              Client Onboarding
Initiator:         New client engagement confirmed
Actions:           Send welcome email, set up account in [system unspecified],
                   schedule kickoff call, add client to project management tool
Systems touched:   Email platform, account management system (unspecified), calendar, PM tool
Data sensitivity:  Client contact data (PII); potentially contract and billing data
Frequency:         Per new client — frequency not stated
Exception rate:    Unknown — user states "sometimes things are different depending on the client"
                   but does not describe what "different" means or how often it occurs
Failure consequence: Incomplete — client access not granted, kickoff not scheduled, onboarding delayed;
                     potential reputational impact if high-profile client
Reversibility:     Partial — emails cannot be unsent; account setup can be reversed; calendar invite
                   can be cancelled
Terminal action:   Client added to PM tool (internal) and welcome email sent (external)
Audit trail:       Partial — depends on systems used

Evidence gaps: Exception types not described; systems not named; exception frequency not quantified;
               escalation path for exceptions not stated
```

**━━ AUTONOMY DECISION PACKET ━━━━━━━━━━━━━━━━━━━━━**

```
Autonomy:          SOP_FIRST (AUT-3)
Surface:           NO_AI (SURFACE-4)
Confidence:        LOW
Justification:     RULE-03 (exception rate fails: "sometimes things are different depending on the
                   client" is not a documented exception path — it signals undefined variance);
                   RULE-05 Challenge 1 (adversarial check: "mostly the same" is not the same as
                   "always the same" — pressure to over-automate present); RULE-09 (Jidoka stop:
                   unknown state on exception path — do not proceed to scoring)
Controls required: None — automation is premature
Evidence gaps:     Exception types undefined; systems not named; no escalation path for non-standard
                   clients; exception frequency unknown
Conservative route: SOP_FIRST applied — one revision from RULE-05 adversarial check
Artifact required: template-stabilization-plan.md
```

**━━ STABILIZATION PLAN ━━━━━━━━━━━━━━━━━━━━━━━━━━━**

**Client Onboarding · SOP_FIRST / NO_AI · LOW**

This workflow cannot be automated in its current state. The description identifies four steps in the standard path but does not define what "sometimes things are different" means — what triggers the variation, what decisions must be made, who makes them, or what the outcome should be. Automating the standard path while leaving exceptions undefined does not remove the exception handling problem. It removes the human who would have caught it. The stabilization work is not a delay to automation. It is the automation decision.

**WHY AUTOMATION IS PREMATURE**
The exception rate criterion in RULE-03 requires that exceptions be documented with clear rules for every case. "Sometimes things are different depending on the client" describes variance without defining it. Specifically:
- The types of client differences that trigger variation are not named
- The decision criteria for each variation are not described
- The escalation path when a variation falls outside the defined criteria is absent
- The systems involved are not specified, preventing assessment of reversibility per system

This is the most common onboarding automation failure pattern documented in operations practice: automation is built for the 80% standard path, and the 20% that requires judgment is silently dropped or silently wrong.

**STABILIZATION CHECKLIST**
- [ ] Document the current onboarding process step by step — no gaps, no "it depends": what happens, in what order, using which system, producing which output
- [ ] List every type of client variation observed in the past 12 months — by name, not by category. "Enterprise client" is a category. "Enterprise client requiring custom SLA in the welcome email" is a type.
- [ ] For each variation type: define the decision criteria (when does this apply?), the action taken (what changes?), and the owner (who decides?)
- [ ] Define the failure path: what happens when the account setup in [system] produces an error, the calendar invite bounces, or the PM tool access cannot be granted?
- [ ] Establish a baseline: how many clients were onboarded in the past 90 days? How many triggered a variation? How many required manual intervention?
- [ ] Run the documented process manually five times against real new clients without deviation before re-submitting

**RE-EVALUATION CRITERIA**
Re-submission to the Gate is appropriate when:
- All steps, systems, inputs, and outputs are documented without "it depends" gaps
- Every exception type observed in the past 12 months has a defined decision rule and owner
- The standard path has been executed five consecutive times without manual intervention
- Exception rate is quantified (percentage of clients requiring deviation from the standard path)

**EARLIEST RE-EVALUATION**
After the stabilization checklist is complete and the process has been run manually five times without deviation. Estimated minimum: 30–60 days from the start of the documentation work.

**EXPECTED OUTCOMES**
- Completed: Full stabilization checklist delivered to the team; process owner assigned; documentation sprint scheduled
- Completed w/ warnings: Partial checklist — some exception types identified but not all; process is partially documented; note which items remain open
- Needs review: Checklist reveals that exception rate is above 30% — escalate before continuing; re-assess whether this process is a candidate for automation at all
- Blocked: No process owner can be identified to lead the documentation work
- Failed: Documentation is produced but still contains "it depends" entries — return to checklist

**AUTONOMY EXPIRES WHEN**
- [x] The workflow's steps, inputs, or outputs change materially — any change to onboarding flow resets this plan
- [ ] The AI surface or tool used changes — not applicable; no AI surface assigned
- [ ] The policy or compliance context changes — monitor for client data handling policy changes that would affect onboarding
- [x] An incident occurs — any onboarding failure that required manual correction is a signal that stabilization is incomplete
- [ ] Error rate exceeds threshold — not applicable until automation is deployed
- [x] 90 days pass without completing the stabilization checklist — re-evaluate whether this workflow is a priority
- [ ] The reviewer role changes — not applicable; SOP_FIRST verdict

---

## Example 3 — Refund Eligibility Assessment (Recommendation Only)

**Mechanism demonstrated:** Terminal action = recommendation document. GATE-1 does not trigger because money does not move. Same workflow family as Example 4 — opposite verdict because the terminal action is different. See RULE-04.

**Raw input:**
> "When a refund request comes in, I want AI to check it against our store policy, the order history, delivery status, and the return window — and then tell the support lead whether to approve or deny it."

---

**━━ WORKFLOW INTAKE SNAPSHOT ━━━━━━━━━━━━━━━━━━━━━**

```
Name:              Refund Eligibility Assessment
Initiator:         Refund request received (customer submits via support channel)
Actions:           Retrieve order record, check delivery status, compare against store return
                   policy, assess return window, evaluate order history flags,
                   produce approve/deny recommendation with rationale for support lead
Systems touched:   Order management system (Shopify or equivalent), support ticketing,
                   store return policy document, delivery tracking
Data sensitivity:  Customer PII (name, order history), transaction data
Frequency:         Per refund request — daily in most ecommerce operations
Exception rate:    Low — assessment is rules-based against defined policy criteria
Failure consequence: Support lead receives a wrong recommendation; support lead is the final
                     decision authority — no money moves without human approval
Reversibility:     Fully reversible — the output is a document; the support lead approves or rejects
Terminal action:   Recommendation document delivered to support lead (internal)
Audit trail:       Recommendation logged with rationale; support lead decision logged separately

Evidence gaps: None — all required fields populated
```

**━━ AUTONOMY DECISION PACKET ━━━━━━━━━━━━━━━━━━━━━**

```
Autonomy:          AUTONOMOUS (AUT-1)
Surface:           CODE_AGENT (SURFACE-3)
Confidence:        HIGH
Justification:     RULE-04 (terminal action is recommendation document — GATE-1 does not trigger
                   because no financial transaction is initiated; the human support lead retains
                   approval authority); RULE-03 (all four criteria pass: fully reversible,
                   observable, low exception rate, low failure consequence — wrong recommendation
                   is caught by the human checkpoint); RULE-05 adversarial check passed without
                   revision
Controls required: Read-only access to order management and delivery systems; recommendation
                   logged with version stamp; support lead retains final approval authority;
                   no direct refund API access
Evidence gaps:     None
Conservative route: Not applied
Artifact required: template-automation-architecture.md
```

**━━ AUTOMATION ARCHITECTURE ━━━━━━━━━━━━━━━━━━━━━━**

**Refund Eligibility Assessment · AUTONOMOUS / CODE_AGENT · HIGH**

This workflow receives a refund request, checks it against store policy and order data, and delivers a recommendation document to the support lead. It qualifies for autonomous execution because the terminal action is a document — not a financial transaction. No money moves. The support lead reviews and approves or denies based on the recommendation. The operator has read-only access to source systems; it cannot initiate a refund, cancel an order, or contact the customer.

**TRIGGER**
Refund request received in support ticketing system (Zendesk, Gorgias, or equivalent). Webhook fires on new ticket tagged "refund-request."

**INPUTS**
- Order management system · Order record, line items, fulfillment status, delivery confirmation · Read-only
- Customer history · Return/refund history for the customer · Read-only
- Store policy document · Return window, eligible categories, exclusion list · Static file, updated by ops
- Delivery tracking · Carrier status for the relevant shipment · Read-only API

**EXECUTION SEQUENCE**
1. Retrieve order record from OMS using order ID extracted from ticket
2. Pull customer return history; flag if customer has exceeded return threshold
3. Check delivery status; flag if item is not yet delivered (window not yet open) or delivered outside return window
4. Compare against store return policy: category eligible? Window open? Value threshold met?
5. Assess all signals; produce recommendation: APPROVE · DENY · ESCALATE (when signals conflict)
6. Write recommendation document with: verdict, policy citation, order data summary, rationale in plain language
7. Attach recommendation to the support ticket; assign to support lead for final decision

**OUTPUTS**
Recommendation document attached to the support ticket. Format: verdict (APPROVE / DENY / ESCALATE) + policy section cited + one-paragraph rationale + order data summary. Retained in ticketing system for audit.

**ERROR HANDLING**
- If OMS record cannot be retrieved: output ESCALATE with reason "order record unavailable"
- If delivery tracking is unavailable: note gap in recommendation; do not assume delivered
- If policy document has not been updated in 90+ days: add warning flag to recommendation
- On any system error: create recommendation stub with error state; do not produce a blank ticket

**AUDIT TRAIL**
Every recommendation logged with: request ID, timestamp, data sources queried, policy version used, verdict, and rationale. Retained 12 months. Support lead decision (approve/deny/override) logged separately against the same request ID.

**CONTROLS**
- Read-only API scope — no write access to OMS, no refund initiation capability
- Policy document version tracked — operator uses the version current at time of assessment
- Support lead retains final approval authority — operator cannot close the ticket
- Recommendation reviewed before any refund is issued

**RECOMMENDED STACK**
Claude Code with read-only API integrations to your OMS and ticketing system. Alternatively: n8n or Zapier workflow with a Claude API node for reasoning step, plus read-only connectors to Shopify/Gorgias. Claude Code is preferred for auditability — every run produces a logged artifact.

**EXPECTED OUTCOMES**
- Completed: Recommendation document attached to ticket, support lead assigned, verdict stated with rationale
- Completed w/ warnings: One data source returned incomplete data — recommendation delivered with gap noted and ESCALATE flag set
- Needs review: Order data conflicts with policy (e.g., delivery status unclear) — ESCALATE verdict; support lead reviews directly
- Blocked: OMS unreachable; ticketing system authentication failed — create error stub; alert support lead
- Failed: Recommendation delivered with incorrect policy version cited — rerun with correct policy document; log the error

**AUTONOMY EXPIRES WHEN**
- [x] The workflow's steps, inputs, or outputs change materially (e.g., new return categories added, policy threshold changes)
- [x] The AI surface or tool used changes (model upgrade, OMS migration)
- [x] The policy or compliance context changes — store return policy changes immediately expire this verdict; update policy document and re-test
- [x] An incident occurs — any recommendation that led to an incorrect approval or denial requiring correction
- [x] Error rate exceeds 5% of recommendations requiring support lead override — review and re-submit to Gate
- [x] 6 months pass without a recertification review — review by [date: December 2026]
- [ ] The reviewer role changes or becomes vacant — not applicable; AUTONOMOUS verdict for this workflow (support lead reviews outputs, not the operator)

---

## Example 4 — Refund Issuance Under Threshold

**Mechanism demonstrated:** Same workflow family as Example 3. Terminal action changes from recommendation to financial transaction issuance. GATE-1 triggers. Verdict changes from AUTONOMOUS to SUPERVISED. This is the terminal action check at its most direct — see RULE-04.

**Raw input:**
> "Same as the refund check above, but instead of telling the support lead what to do, just go ahead and issue the refund automatically if it qualifies under $50. We've already defined the criteria — it's rule-based."

---

**━━ WORKFLOW INTAKE SNAPSHOT ━━━━━━━━━━━━━━━━━━━━━**

```
Name:              Automated Refund Issuance (Under $50)
Initiator:         Refund request received and policy criteria met automatically
Actions:           Retrieve order record, check delivery status, compare against policy,
                   verify amount is under $50, issue refund via payment processor
Systems touched:   Order management system, payment processor (Stripe or equivalent),
                   customer email (refund confirmation sent), support ticketing
Data sensitivity:  Customer PII, financial transaction data, payment credentials (indirect)
Frequency:         Per qualifying refund request
Exception rate:    Stated as low — but threshold ($50) is the only documented rule; no
                   exception handling for declined payment processor, fraud flags, or prior
                   dispute history is described
Failure consequence: Wrong refund issued — incorrect amount, duplicate refund, fraudulent
                     request processed; financial loss and potential dispute exposure
Reversibility:     Partial — refunds processed via Stripe can be disputed but not automatically
                   reversed; correction requires manual payment processor action and potential
                   customer contact
Terminal action:   Refund issuance via payment processor (financial transaction)
Audit trail:       Payment processor transaction logs; order management system record

Evidence gaps: Exception handling for declined transactions not described; fraud flag
               handling not addressed; duplicate refund prevention not addressed
```

**━━ AUTONOMY DECISION PACKET ━━━━━━━━━━━━━━━━━━━━━**

```
Autonomy:          SUPERVISED (AUT-2)
Surface:           CODE_AGENT (SURFACE-3)
Confidence:        MEDIUM
Justification:     RULE-04 (terminal action is financial transaction issuance — GATE-1 triggers;
                   "rule-based" label does not change the terminal action; GATE-1 overrides
                   AUTONOMOUS to SUPERVISED minimum); RULE-03 (cost of failure: financial
                   transaction requires human checkpoint regardless of threshold); RULE-05
                   Challenge 3 (adversarial check caught GATE-1 — user framing as "rule-based"
                   would have missed it)
Controls required: Refund amount cap enforced at code level; payment processor write access
                   scoped to refund-only; human approval checkpoint before issuance;
                   duplicate refund prevention; audit log per transaction
Evidence gaps:     Fraud flag handling not described; duplicate refund prevention mechanism
                   not specified
Conservative route: Not applied — GATE-1 structural override produces SUPERVISED regardless
Artifact required: template-control-plan.md
```

**━━ CONTROL PLAN ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━**

**Automated Refund Issuance (Under $50) · SUPERVISED / CODE_AGENT · MEDIUM**

This workflow checks refund eligibility and prepares a refund authorization package, which a named human reviewer approves before the payment processor executes the transaction. The terminal action — financial transaction issuance — triggers GATE-1, which sets SUPERVISED as the structural minimum regardless of how rule-based the eligibility criteria appear. The operator prepares; the human authorizes; the processor executes. "Rule-based" describes the eligibility logic, not the risk of the terminal action.

**WHAT AI PREPARES**
A Refund Authorization Package attached to each qualifying request, containing:
- Order ID, customer name, refund amount
- Policy check results (each criterion: passed/failed)
- Amount confirmation (verified under $50 threshold)
- Fraud flags present or absent
- Duplicate refund check (no prior refund on this order)
- Recommended action: AUTHORIZE · HOLD

Format: structured document, attached to the support ticket, assigned to the designated reviewer.

**APPROVAL CHECKPOINT**
```
Reviewer:      Support Lead (or designated finance approver — role must be named before deployment)
Reviews:       Policy check results, fraud flag status, amount, duplicate check, recommendation
Approves when: All policy criteria met; no fraud flags; amount under $50; no prior refund on order
Rejects when:  Any flag present; amount disputed; policy criteria uncertain; customer dispute history
Turnaround:    Same business day (target: 2 hours)
```

**POST-APPROVAL ACTIONS**
1. Reviewer approves in ticketing system (single click with approval record logged)
2. Operator receives approval signal; initiates Stripe refund API call
3. Refund confirmation sent to customer
4. Order record updated: refund status, amount, date, approver name
5. Support ticket closed with audit trail entry

**PROHIBITED WITHOUT APPROVAL**
- No refund may be issued without a logged reviewer approval
- No refund may exceed $50 regardless of operator or customer instruction
- Operator may not contact the customer about refund status before approval is logged

**AUDIT TRAIL**
Every transaction records: order ID, request ID, policy check results, fraud flag status, refund amount, reviewer name, approval timestamp, Stripe transaction ID. Retained 24 months. Accessible to finance team.

**EXPECTED OUTCOMES**
- Completed: Refund authorized, processed, customer notified, ticket closed with audit record
- Completed w/ warnings: Refund processed but customer notification failed — ticket flagged; customer follow-up required
- Needs review: Amount is close to $50 threshold and data is ambiguous — HOLD flag set; reviewer handles directly
- Blocked: Payment processor returns error; reviewer unreachable — hold refund; escalate to finance owner
- Failed: Duplicate refund detected post-issuance — freeze further refunds for this order; notify finance owner immediately

**AUTONOMY EXPIRES WHEN**
- [x] The workflow's steps, inputs, or outputs change materially (e.g., threshold increases above $50, new payment processor)
- [x] The AI surface or tool used changes
- [x] The policy or compliance context changes — any change to return policy immediately triggers re-review
- [x] An incident occurs — any incorrect, duplicate, or fraudulent refund processed
- [x] Error rate exceeds 2% of transactions requiring post-issuance correction — re-submit to Gate immediately
- [x] 3 months pass without a recertification review — review by [date: September 2026]
- [x] The reviewer role changes or becomes vacant — workflow must be paused until a new reviewer is designated

---

## Example 5 — Personalized Outbound Email Campaign

**Mechanism demonstrated:** LOW confidence from two sources — reviewer unidentifiable (RULE-08) and volume unquantified. GATE-4 triggers on external publication. Conservative route applied.

**Raw input:**
> "We want to send a personalized outreach sequence to our lead list — maybe 500 people. AI drafts the emails based on their LinkedIn info and our offer. Someone on the team checks it. What's the verdict?"

---

**━━ WORKFLOW INTAKE SNAPSHOT ━━━━━━━━━━━━━━━━━━━━━**

```
Name:              Personalized Outbound Email Campaign
Initiator:         Marketing team — campaign launch decision
Actions:           Pull lead list, enrich with LinkedIn data, draft personalized emails,
                   route for human review, send approved emails
Systems touched:   CRM or lead list, LinkedIn (data source), email platform, review interface
Data sensitivity:  Contact PII (name, company, role), scraped professional data
Frequency:         One campaign — ~500 recipients
Exception rate:    Unknown — no documentation of what constitutes a "bad draft" or rejection criteria
Failure consequence: Wrong, offensive, or legally non-compliant email sent at scale to 500+ people;
                     reputational and potential CAN-SPAM / GDPR exposure
Reversibility:     Irreversible once sent — cannot be recalled from recipient inboxes
Terminal action:   External email delivery to 500 contacts
Audit trail:       Email platform send logs; limited visibility into what AI generated vs. approved

Evidence gaps: Reviewer role not identified ("someone on the team"); review criteria not
               defined; rejection criteria not stated; LinkedIn data scraping compliance not assessed;
               volume is approximate ("maybe 500")
```

**━━ AUTONOMY DECISION PACKET ━━━━━━━━━━━━━━━━━━━━━**

```
Autonomy:          SUPERVISED (AUT-2) — conservative route applied (LOW confidence)
Surface:           PROJECT (SURFACE-1)
Confidence:        LOW
Justification:     GATE-4 (terminal action is external publication — SUPERVISED minimum;
                   email to 500 recipients is reputationally and legally exposed);
                   RULE-08 (reviewer role is "someone on the team" — checkpoint ownership rule
                   fails; reviewer must be named before deployment); RULE-06 (LOW confidence
                   because reviewer unidentifiable and review criteria undefined)
Controls required: Named reviewer with authority to block send; defined rejection criteria;
                   compliance review for LinkedIn data use and CAN-SPAM; sample review
                   (minimum 10% of drafts) before bulk send
Evidence gaps:     Reviewer role not named; review criteria not defined; data compliance
                   not assessed; volume approximate
Conservative route: SUPERVISED applied; checkpoint ownership required before deployment
Artifact required: template-control-plan.md
```

**━━ CONTROL PLAN ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━**

**Personalized Outbound Email Campaign · SUPERVISED / PROJECT · LOW**

This workflow drafts personalized outbound emails using lead data and routes them to a human reviewer before sending. It is classified SUPERVISED because external email to 500+ recipients triggers GATE-4 — the terminal action is an irreversible external publication. Confidence is LOW because the reviewer role is currently unidentified and review criteria are undefined. This workflow cannot be deployed until a named reviewer with blocking authority is designated and a rejection rubric is documented.

**WHAT AI PREPARES**
A draft email per contact, attached to a review batch, containing:
- Personalized opening referencing the lead's role or company (sourced from LinkedIn data)
- Offer statement tailored to the contact's industry category
- Call to action (one link, one ask)
- Draft labeled: "DRAFT — Not for send — Awaiting review"

Review batch delivered as a document: each draft presented with the data it was derived from, so the reviewer can confirm the personalization is accurate and appropriate.

**APPROVAL CHECKPOINT**
```
Reviewer:      [REQUIRED — must be named before deployment. "Someone on the team" is
                not acceptable. Checkpoint ownership rule (RULE-08) applies. Without a
                named reviewer, this workflow cannot be deployed.]
Reviews:       Accuracy of personalization; tone and brand compliance; offer statement
               correctness; legal compliance flags (CAN-SPAM, GDPR where applicable)
Approves when: Draft is accurate, on-brand, legally compliant, and ready to send as-is or
               with minor edits the reviewer can make directly
Rejects when:  Draft contains factual errors, inappropriate personalization, off-brand tone,
               or any compliance concern — rejected drafts return to operator for revision
Turnaround:    Review batch completed before any sends are initiated
```

**POST-APPROVAL ACTIONS**
1. Reviewer approves each draft individually (or approves batch after sample review of minimum 10%)
2. Approved drafts queued in email platform
3. Send executed on reviewer's authorization
4. Delivery metrics logged: sent, delivered, bounced, opened

**PROHIBITED WITHOUT APPROVAL**
- No email may be sent without logged reviewer approval
- Operator may not send directly from the draft without routing through the review step
- LinkedIn data may not be used for personalization until data compliance is confirmed

**AUDIT TRAIL**
Draft log: contact ID, draft content, data sources used, reviewer decision, timestamp. Send log: platform delivery record. Retained 12 months.

**INFORMATION GAPS**
- Reviewer role: Must be designated. Recommended: marketing lead or founder with authority to block send and legal awareness.
- Review criteria: Must be documented in writing before first batch. Recommend a 10-point rubric covering accuracy, tone, compliance, and CTA.
- LinkedIn data compliance: Verify your LinkedIn data sourcing method complies with LinkedIn ToS and applicable privacy regulations before using in outbound emails.
- Volume: Confirm actual send volume before deployment — campaigns above 1,000 contacts may require additional compliance steps in some jurisdictions.

**EXPECTED OUTCOMES**
- Completed: All approved drafts sent; delivery metrics logged; batch audit trail filed
- Completed w/ warnings: >5% of drafts required significant revision during review — increase review sample rate for next campaign
- Needs review: Any draft contains a compliance flag — pause batch; reviewer handles directly
- Blocked: Reviewer unavailable; compliance review not completed — do not send; reschedule with reviewer
- Failed: Email sent without reviewer approval — halt remaining sends; notify reviewer and legal owner immediately

**AUTONOMY EXPIRES WHEN**
- [x] The workflow's steps, inputs, or outputs change materially (new data source, new offer, new audience)
- [x] The AI surface or tool used changes
- [x] The policy or compliance context changes — any change to CAN-SPAM, GDPR enforcement, or LinkedIn ToS
- [x] An incident occurs — any complaint, bounce issue, or compliance flag
- [x] Error rate exceeds 10% of drafts requiring revision — re-submit to Gate
- [x] 3 months pass without a recertification review
- [x] The reviewer role changes or becomes vacant — workflow must pause until new reviewer is named

---

## Example 6 — Internal Slack Digest from Meeting Notes

**Mechanism demonstrated:** Clean AUTONOMOUS case for an internal, reversible, non-sensitive workflow. COWORK surface assigned because the workflow can run on a schedule. No GATE conditions. LOW friction path.

**Raw input:**
> "After each team meeting, I want a summary of the key decisions, action items, and owners from the transcript — posted to our internal Slack channel."

---

**━━ WORKFLOW INTAKE SNAPSHOT ━━━━━━━━━━━━━━━━━━━━━**

```
Name:              Meeting Summary Slack Digest
Initiator:         Meeting transcript uploaded or made available (post-meeting)
Actions:           Read transcript, extract decisions, action items, and owners,
                   format as structured digest, post to internal Slack channel
Systems touched:   Meeting transcript source (Zoom/Loom/Fireflies), Slack (internal channel)
Data sensitivity:  Internal meeting content — may include business strategy or personnel discussion;
                   not regulated; not customer PII
Frequency:         After each team meeting — weekly or more
Exception rate:    Low — transcript processing is well-defined; extraction criteria are stable
Failure consequence: Summary is incomplete or mislabels an action item owner — team member
                     follows up on the wrong task for one cycle; correctable
Reversibility:     Fully reversible — Slack messages can be edited or deleted; corrected
                   summary can be reposted
Terminal action:   Slack message to internal channel
Audit trail:       Slack post timestamp; transcript retained in source system

Evidence gaps: None significant
```

**━━ AUTONOMY DECISION PACKET ━━━━━━━━━━━━━━━━━━━━━**

```
Autonomy:          AUTONOMOUS (AUT-1)
Surface:           COWORK (SURFACE-2) — runs after each meeting on trigger; or PROJECT if
                   human-initiated
Confidence:        HIGH
Justification:     RULE-03 (all four criteria pass: fully reversible, observable, low exception
                   rate, low failure consequence); no GATE conditions triggered; RULE-05
                   adversarial check passed without revision
Controls required: Read-only transcript access; Slack write permission scoped to target channel only
Evidence gaps:     None
Conservative route: Not applied
Artifact required: template-cowork-config.md
```

**━━ COWORK PROJECT CONFIG ━━━━━━━━━━━━━━━━━━━━━━━━**

**Meeting Summary Slack Digest · AUTONOMOUS / COWORK · HIGH**

This workflow reads a meeting transcript after each team meeting, extracts decisions, action items, and named owners, and delivers a structured digest to the internal Slack channel. It runs unattended on a post-meeting trigger inside Claude Cowork. Internal content, fully reversible output, no external commitment, no GATE conditions. This is a clean autonomous workflow.

**LOCAL FOLDER STRUCTURE**
```
/inputs   — Transcripts land here. Source: Zoom export, Fireflies auto-download, or manual drop.
            Naming: YYYY-MM-DD_meeting-name.txt or .vtt
/outputs  — Formatted digest files retained locally after each run.
            Naming: YYYY-MM-DD_digest.md
/logs     — Run log per execution: timestamp, transcript filename, items extracted, Slack delivery status
```

**SCHEDULED TASK**
Trigger: new file in /inputs folder. Expected runtime: under 60 seconds per transcript. Frequency: per meeting — may run multiple times per week.

**EXECUTION SEQUENCE**
1. Detect new transcript file in /inputs
2. Parse transcript: identify meeting date, attendees, and agenda if present
3. Extract decisions (explicitly stated outcomes), action items (named tasks assigned to a person), and open questions (unresolved items flagged for follow-up)
4. Format digest: Date + Meeting Name header, three sections (Decisions / Action Items / Open Questions), owner names on each action item
5. Post to #team-digest Slack channel (or configured channel)
6. Save formatted output to /outputs; write run entry to /logs

**AUTHORIZED ACTIONS**
- Read transcript files from /inputs
- Write formatted digest to /outputs and /logs
- Post to the designated internal Slack channel

**PROHIBITED ACTIONS**
- May not post to public channels or external Slack workspaces
- May not summarize or retain content from transcripts not placed in /inputs by an authorized team member
- May not send summaries via email or any external channel
- May not edit or delete prior Slack messages

**EXPECTED OUTCOMES**
- Completed: Digest posted to Slack, output file saved, run logged
- Completed w/ warnings: Transcript was incomplete (cut off) — digest delivered with gap noted in Open Questions section
- Needs review: Transcript contains content flagged as sensitive (personnel discussion, legal reference) — post digest stub; flag for human review before full post
- Blocked: Slack API token expired; /inputs is empty — log the condition; send no output
- Failed: Post sent with incorrect action item owner — delete and repost corrected version; log the error

**AUTONOMY EXPIRES WHEN**
- [x] The workflow's steps, inputs, or outputs change materially (new Slack channel, new transcript format)
- [x] The AI surface or tool used changes (model upgrade, Cowork platform migration)
- [ ] The policy or compliance context changes — not applicable; internal summaries of internal meetings
- [x] An incident occurs — any digest that was materially incorrect and caused a task to be missed
- [x] Error rate exceeds 15% of runs requiring manual correction
- [x] 6 months pass without a recertification review — review by [date: December 2026]
- [ ] The reviewer role changes or becomes vacant — not applicable; AUTONOMOUS verdict

---

## Example 7 — Contract Clause Comparison Against Template

**Mechanism demonstrated:** Judgment required in output. Even when AI analysis is thorough, the output contains assessments that carry legal weight — requiring a human checkpoint. RULE-03 cost of failure criterion drives SUPERVISED.

**Raw input:**
> "We get vendor contracts weekly. I want AI to compare each incoming contract against our standard template, flag any deviations in key clauses — liability, IP ownership, termination rights — and tell me what's materially different."

---

**━━ WORKFLOW INTAKE SNAPSHOT ━━━━━━━━━━━━━━━━━━━━━**

```
Name:              Vendor Contract Clause Comparison
Initiator:         Incoming vendor contract received
Actions:           Parse incoming contract, load standard template, compare clause by clause
                   on liability, IP ownership, and termination rights, flag deviations,
                   produce deviation report for legal or business reviewer
Systems touched:   Contract storage (Google Drive, Dropbox, or equivalent), standard template
                   document, output delivery (email or document share)
Data sensitivity:  Legally binding commercial terms; potentially confidential vendor relationships
Frequency:         Weekly — per contract received
Exception rate:    Medium — contracts vary significantly; edge cases in IP and liability are common
Failure consequence: Material deviation missed; company signs contract with unfavorable terms
                     undetected; potential legal exposure
Reversibility:     Low — contracts are signed commitments; post-signing correction requires
                   renegotiation
Terminal action:   Deviation report delivered to legal/business reviewer (document, not signed commitment)
Audit trail:       Report retained; contract version at time of assessment retained

Evidence gaps: Reviewer role partially specified ("legal or business reviewer" — role must
               be named specifically before deployment)
```

**━━ AUTONOMY DECISION PACKET ━━━━━━━━━━━━━━━━━━━━━**

```
Autonomy:          SUPERVISED (AUT-2)
Surface:           PROJECT (SURFACE-1)
Confidence:        MEDIUM
Justification:     RULE-03 (cost of failure: missed clause deviation has legal and financial
                   consequence; judgment in interpretation of "materiality" requires human
                   review); RULE-08 (reviewer role partially identified — must be named
                   specifically for checkpoint ownership rule); RULE-05 adversarial check:
                   AI clause comparison is pattern-matching, not legal judgment — the reviewer
                   must have authority to reject the contract, not just note the deviation
Controls required: Named legal or business reviewer with contract-blocking authority;
                   template version control; report retained with contract version
Evidence gaps:     Reviewer role must be specified by name/title before deployment
Conservative route: Not applied
Artifact required: template-control-plan.md
```

**━━ CONTROL PLAN ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━**

**Vendor Contract Clause Comparison · SUPERVISED / PROJECT · MEDIUM**

This workflow receives incoming vendor contracts, compares each against the standard template on defined clause families, and delivers a deviation report to a named reviewer before any signature or commitment is made. The terminal action is a document — the contract is not signed by this workflow. The SUPERVISED verdict reflects that clause interpretation carries legal consequence and the deviation report's accuracy affects downstream decisions. The reviewer must have authority to block the contract, not only to receive the report.

**WHAT AI PREPARES**
A Clause Deviation Report for each contract, containing:
- Contract metadata: vendor name, contract date, contract type
- Clause comparison table: Clause · Standard template language · Incoming contract language · Assessment (Aligned / Minor deviation / Material deviation / Missing)
- Flagged items: any clause assessed as "Material deviation" or "Missing" listed separately with the specific text from each version
- Summary recommendation: "Ready for signature" / "Requires legal review" / "Requires negotiation on [clause name]"

**APPROVAL CHECKPOINT**
```
Reviewer:      [Named legal counsel or designated contract authority — must be specified.
                "Legal or business reviewer" is not sufficient for deployment.]
Reviews:       Accuracy of clause extraction; correctness of deviation assessments;
               completeness of flagged items; summary recommendation
Approves when: Deviations are as described, risk level is acceptable, and contract may proceed
Rejects when:  Material deviation is identified that requires renegotiation; AI missed a
               clause; assessment is incorrect; contract scope has changed
Turnaround:    2 business days per contract
```

**POST-APPROVAL ACTIONS**
1. Reviewer confirms deviation report is accurate
2. Reviewer approves to proceed (send to signing) or flags for renegotiation
3. Contract proceeds to signature process outside this workflow's scope
4. Report retained with contract record

**PROHIBITED WITHOUT APPROVAL**
- Operator may not mark a contract as "approved" or "ready to sign"
- Operator may not route the contract to signature without reviewer sign-off
- Operator may not communicate contract status to the vendor

**AUDIT TRAIL**
Deviation report version, contract version at time of assessment, reviewer name, approval timestamp, outcome (proceed/renegotiate). Retained for the contract's active duration plus 3 years.

**EXPECTED OUTCOMES**
- Completed: Deviation report delivered to reviewer, all flagged items described, recommendation stated
- Completed w/ warnings: Contract format was non-standard (scanned PDF, poor OCR) — report delivered with extraction confidence flagged; reviewer should cross-check key clauses manually
- Needs review: Contract contains an unusual clause type not in the template comparison set — flag for reviewer; do not assess unknown clause types
- Blocked: Standard template not available or version is outdated — halt; request updated template from legal
- Failed: Post-review discovery that a material deviation was missed — flag workflow for re-assessment; update clause comparison set

**AUTONOMY EXPIRES WHEN**
- [x] The workflow's steps, inputs, or outputs change materially (new clause families added, template revised)
- [x] The AI surface or tool used changes
- [x] The policy or compliance context changes — any change to standard template or company contracting policy
- [x] An incident occurs — any contract signed with an undetected material deviation
- [x] Error rate exceeds 5% of reports missing a material deviation
- [x] 6 months pass without recertification review
- [x] The reviewer role changes or becomes vacant — workflow paused until new reviewer designated

---

## Example 8 — Access Permission Change Request

**Mechanism demonstrated:** GATE-3 triggers on permission change. Same HUMAN_ONLY verdict as Example 9 (vendor bank account), different gate. "Rule-based" framing does not change the terminal action. See RULE-06 GATE-3.

**Raw input:**
> "When an employee requests access to the finance folder, verify manager approval, business reason, employment status, and role match; then decide whether access should be granted."

---

**━━ WORKFLOW INTAKE SNAPSHOT ━━━━━━━━━━━━━━━━━━━━━**

```
Name:              Finance Folder Access Permission Request
Initiator:         Employee submits access request (ITSM or IT helpdesk)
Actions:           Retrieve employee record, verify manager approval (lookup in HR system),
                   confirm employment status, check role match against access policy,
                   decide whether access criteria are met, grant or deny access
Systems touched:   ITSM platform, HR system, identity/directory system (Active Directory,
                   Okta, or equivalent), finance folder permissions
Data sensitivity:  Employee PII; financial system access controls; regulated data exposure
Frequency:         Per request — multiple times weekly in most organizations
Exception rate:    Low — access policy criteria are stated as rule-based
Failure consequence: Unauthorized access to financial systems and data; compliance exposure
                     (SOX, GDPR depending on jurisdiction); security risk
Reversibility:     Reversible (access can be revoked) but exposure during the period of
                   unauthorized access is not reversible
Terminal action:   Permission change in identity management system (grants or denies access)
Audit trail:       ITSM ticket log; identity system change log

Evidence gaps: None — all required fields populated
```

**━━ AUTONOMY DECISION PACKET ━━━━━━━━━━━━━━━━━━━━━**

```
Autonomy:          HUMAN_ONLY (AUT-4)
Surface:           NO_AI (SURFACE-4)
Confidence:        HIGH
Justification:     RULE-04 (terminal action is permission change — GATE-3 triggers; AI modifying
                   who can access financial systems triggers GATE-3 regardless of how rule-based
                   the criteria appear); RULE-06 (GATE-3 override is HUMAN_ONLY — structural;
                   cannot be bypassed by user instruction or apparent simplicity of criteria);
                   RULE-05 Challenge 3 (adversarial check confirms GATE-3 — "rule-based" framing
                   is the most common source of gate misses)
Controls required: None — delegation is structurally blocked; see governance memo for
                   what AI may assist with in the preparation phase
Evidence gaps:     None
Conservative route: Not applied — GATE-3 structural override
Artifact required: template-governance-memo.md
```

**━━ GOVERNANCE MEMO ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━**

**Finance Folder Access Permission Request · HUMAN_ONLY / NO_AI · HIGH**

This workflow cannot be delegated to AI. The terminal action — granting or denying access to financial systems — triggers GATE-3, which mandates HUMAN_ONLY regardless of how clearly the access criteria are defined. This structural block applies even when the criteria appear rule-based. The reason is that AI modifying access controls in systems containing regulated financial data creates audit and compliance exposure that persists beyond the moment of access, and the criteria for access often contain edge cases (employment transitions, dual roles, temporary access requirements) that require human accountability. A "rule-based" access check that misclassifies one edge case grants financial data access to an unauthorized party — a consequence that is difficult to contain.

**WHY THIS CANNOT BE DELEGATED**
```
Gate condition:  GATE-3 — changes permissions or access controls
Specific risk:   AI granting finance folder access creates an unauditable chain of authority.
                 If access is granted incorrectly — wrong role, employment transition,
                 policy gap — the exposure begins immediately and cannot be unwound retroactively.
                 SOX compliance in public companies requires that access control decisions
                 be attributable to a named human authority, not an automated system.
```

**HUMAN REVIEW PROCESS**
```
Owner:           IT Security or designated Access Control Authority (specific role must be named
                 in your access control policy)
Review cadence:  Per request — target same-business-day response for standard requests;
                 2-hour SLA for urgent requests
Decision criteria: Manager approval confirmed in HR system; business reason is documented and
                   aligned with role; employee is actively employed; role matches access tier
                   in the access control policy; no flags from the security team
Escalation path: Requests involving senior finance roles, auditor access, or access during an
                 active investigation route to the CISO or CFO for final approval
```

**WHAT WOULD CHANGE THIS VERDICT**
AI can be used to assist the preparation phase without triggering GATE-3, provided the terminal action remains human-owned. Specifically:
- If AI's scope is limited to checking prerequisites (manager approval status in HR, employment status, role match) and producing a pre-verified packet for the human reviewer — with no write access to the identity system — the packet generation step could be re-submitted as `SUPERVISED / CODE_AGENT`.
- The permission change step must remain a separate, explicitly human-authorized action regardless of what the preparation phase automates.
- Re-submit the preparation phase only, explicitly scoped: "AI checks prerequisites and prepares the access packet. A named human authority reviews and executes the permission change."

**EXPECTED OUTCOMES**
- Completed: Access request reviewed by designated authority; decision (grant/deny) documented in ITSM ticket with rationale; identity system updated by human authority
- Completed w/ warnings: Request met all criteria but involved an employment transition — access granted with 30-day review flag
- Needs review: Request involves dual-role employee or temporary access requirement — escalate per escalation path above
- Blocked: Manager approval not obtainable; employment status unclear — do not grant access; return to requestor
- Failed: Access granted and subsequently found to be in error — revoke immediately; audit access logs for the period; document in security incident log

**AUTONOMY EXPIRES WHEN**
- [ ] The workflow's steps change — not applicable; verdict is HUMAN_ONLY; this memo is reviewed, not the workflow
- [ ] The AI surface changes — not applicable
- [x] The policy or compliance context changes — any change to access control policy, SOX requirements, or role definitions requires this memo to be reviewed
- [x] An incident occurs — any unauthorized access event triggers immediate re-review
- [x] 12 months pass without a recertification review of the access control policy itself
- [ ] The reviewer role changes — not applicable in the traditional sense; if the Access Control Authority role changes, the governance process itself must be updated

---

## Example 9 — Vendor Bank Account Change Request

**Mechanism demonstrated:** GATE-2 triggers on irreversible external commitment. The workflow label is "verification and update" — the terminal action is authorizing a payment routing change. This is the terminal action check under adversarial conditions: the workflow sounds rule-based, the risk is documented at scale, and the adversarial check must catch what the label conceals. See RULE-04, RULE-05, RULE-06 GATE-2.

**Source grounding:** Business Email Compromise (BEC) is the #2 crime by financial loss in the FBI IC3 2025 Annual Report. Total BEC losses in 2025 reached $3.04 billion. 86% of BEC funds move via wire transfer or ACH. Vendor account change requests are the documented primary attack vector — AI voice cloning is now used to impersonate vendor representatives and authorize fraudulent routing changes.

**Raw input:**
> A vendor emailed asking us to update their bank account details before the next invoice cycle. Can we automate the verification and update so it goes through faster?

---

**━━ WORKFLOW INTAKE SNAPSHOT ━━━━━━━━━━━━━━━━━━━━━**

```
Name:              Vendor Bank Account Change Request
Initiator:         Vendor email requesting banking detail update
Actions:           Receive vendor email, verify vendor identity, confirm change request
                   against vendor records, update banking details in payment system,
                   process future invoices to new account
Systems touched:   Email platform, vendor management system, payment/banking system
                   (ACH or wire), accounts payable records
Data sensitivity:  Financial — banking routing and account numbers; vendor identity data
Frequency:         Per request — occasional, not scheduled
Exception rate:    Fraud rate for this exact workflow type is documented at scale
                   (FBI IC3 2025: $3.04B in BEC losses, vendor account change is the
                   primary vector)
Failure consequence: Fraudulent account update results in funds wired to an
                     attacker-controlled account; recovery rate: 58% when caught
                     immediately (FBI IC3 2025); average loss: $122,000+; irreversible
                     once the wire or ACH clears
Reversibility:     Low — wire transfers to fraudulent accounts are recovered in only
                   58% of cases when caught immediately
Terminal action:   Payment routing change authorized in the payment system (irreversible
                   external financial commitment)
Audit trail:       Email record, payment system change log — both are forgeable in a
                   sophisticated BEC attack (AI voice clone, domain spoofing)

Evidence gaps: None — the workflow is well-described and the risk is fully documented
```

**━━ AUTONOMY DECISION PACKET ━━━━━━━━━━━━━━━━━━━━━**

```
Autonomy:          HUMAN_ONLY (AUT-4)
Surface:           NO_AI (SURFACE-4)
Confidence:        HIGH
Justification:     RULE-04 (terminal action is payment routing change — an irreversible
                   external financial commitment; "verification" is the label, not the
                   terminal action); GATE-2 (authorized payment routing change is
                   explicitly named in GATE-2 — irreversible external commitment;
                   HUMAN_ONLY override; cannot be bypassed by controls, verification
                   steps, or user instruction); RULE-05 adversarial check: this workflow
                   sounds rule-based and low-risk — it is the documented primary attack
                   surface for BEC fraud at scale; adversarial check must name FAIL-1
                   (Capability Bias — AI can verify ≠ sufficient given the fraud stakes)
                   and FAIL-3 (Silent Failure — a successful BEC attack produces a
                   valid-appearing approval trail)
Controls required: None — delegation is structurally blocked; GATE-2 cannot be bypassed
Evidence gaps:     None
Conservative route: Not applied — GATE-2 triggers independently; structural HUMAN_ONLY
                    override applies
Artifact required: template-governance-memo.md
```

**━━ GOVERNANCE MEMO ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━**

**Vendor Bank Account Change Request · HUMAN_ONLY / NO_AI · HIGH**

This workflow cannot be delegated to AI. A vendor bank account change request has a terminal action of authorizing a payment routing change — an irreversible external financial commitment explicitly named in GATE-2. The framing as "verification and update" does not change the terminal action. This workflow is the documented primary attack vector for Business Email Compromise, which generated $3.04 billion in losses in 2025 (FBI IC3 Annual Report). Any AI that processes these requests — even with verification steps — becomes a direct attack surface. The adversarial check caught this: the workflow sounds rule-based and low-risk; the consequence of a wrong verdict is an unrecoverable wire transfer to an attacker-controlled account.

**WHY THIS CANNOT BE DELEGATED**
```
Gate condition:  GATE-2
                 Authorizing a payment routing change is an irreversible external
                 commitment — explicitly named in GATE-2's definition. HUMAN_ONLY
                 override. Cannot be bypassed by controls, verification steps, or
                 user instruction.

Specific risk:   BEC attackers target vendor account change workflows because they
                 appear routine. AI voice cloning can impersonate a vendor
                 representative. Domain spoofing can replicate the vendor's email
                 domain. A verification step that AI passes can be defeated by the
                 same social engineering that defeats human review — but with far
                 less friction for the attacker.

                 FBI IC3 2025: $3.04B in BEC losses. 86% of funds move via wire
                 or ACH. Average loss per complaint: $122,000+. Recovery rate when
                 flagged immediately: 58%. These are documented at scale.
```

**HUMAN REVIEW PROCESS**
```
Owner:           Accounts Payable Manager plus one additional approver
Review cadence:  Per request — no batching; each request reviewed independently
Decision criteria:
  1. Call back the vendor using a number from your original contract records —
     not the number in the requesting email
  2. Confirm the account change verbally with a known contact at the vendor
  3. Request written confirmation via a separate email channel (not a reply)
  4. Cross-reference new account details against prior banking records
  5. Verify the requester's email domain character by character — BEC attackers
     use look-alike domains
  6. Document every step with timestamps
Escalation path: Any request that cannot be verified via independent callback,
                 or that arrives with unusual urgency, routes to CFO and Legal.
                 Urgency language ("before the next invoice cycle") is a
                 documented BEC social engineering signal.
```

**WHAT WOULD CHANGE THIS VERDICT**
GATE-2 is a structural block on the terminal action. No change to AI capability, verification thoroughness, or control architecture changes this verdict for the authorization step. However, AI can assist with preparation steps scoped explicitly to exclude authorization: flagging incoming emails matching BEC patterns, surfacing the vendor's historical banking records, preparing a verification checklist. These preparation steps, re-submitted as a separate SUPERVISED workflow with the authorization step explicitly excluded, can receive a different verdict for that scope only.

**EXPECTED OUTCOMES**
- Completed: Account change verified via independent callback, confirmed in writing, documented with timestamps, authorized by designated approver; payment system updated by human
- Completed w/ warnings: Verification took longer than expected — change deferred to next billing cycle; no payment sent to unverified account
- Needs review: Callback revealed no knowledge of the change at the vendor — possible BEC attempt; escalate to CFO, Legal, and the vendor's official security contact immediately
- Blocked: Cannot reach a known contact to verify — do not update; hold invoice until verification is complete
- Failed: Payment routed to fraudulent account — initiate bank recall within 72 hours; file FBI IC3 complaint; notify Legal

**AUTONOMY EXPIRES WHEN**
- [ ] The workflow's steps change — not applicable; verdict is HUMAN_ONLY and structural
- [ ] The AI surface changes — not applicable; no AI surface assigned
- [x] The policy or compliance context changes — any change to internal payment authorization policy or BEC guidance from FBI IC3 or FinCEN requires review
- [x] An incident occurs — any successful or attempted BEC fraud on this workflow triggers immediate process audit
- [x] 6 months pass without a recertification review of the human verification process

---

## Example 10 — Monthly Financial Close Reconciliation

**Mechanism demonstrated:** HIGH confidence case with GATE-1 SUPERVISED minimum. Shows that HIGH confidence and SUPERVISED are not contradictory — thorough information can produce a confident, well-controlled verdict that is still not AUTONOMOUS.

**Raw input:**
> "At month-end, compare our Stripe payouts, bank deposits, invoice records, and accounting ledger entries; produce a variance report and route unresolved differences to the finance owner."

---

**━━ WORKFLOW INTAKE SNAPSHOT ━━━━━━━━━━━━━━━━━━━━━**

```
Name:              Monthly Financial Close Reconciliation
Initiator:         Month-end trigger (scheduled or manual initiation by finance team)
Actions:           Pull Stripe payout records, pull bank deposit statements, pull invoice
                   records from accounting platform, compare all three against ledger entries,
                   identify variances, classify variance type (timing difference, error,
                   unmatched), produce variance report, route unresolved items to finance owner
Systems touched:   Stripe API, bank account export or API, accounting platform
                   (QuickBooks, Xero, or equivalent), finance owner inbox or task system
Data sensitivity:  Financial records — revenue, banking transactions, invoices; regulated
Frequency:         Monthly — month-end
Exception rate:    Low to medium — most variances are timing differences with documented patterns
Failure consequence: Missed or misclassified variance affects financial close accuracy;
                     downstream impact on financial statements, tax reporting, audit compliance
Reversibility:     Analysis is reversible (corrected report can be rerun); any accounting
                   entries made on the basis of a wrong report require adjustment
Terminal action:   Variance report delivered to finance owner; unresolved items routed for
                   human resolution (no ledger entries made by this workflow)
Audit trail:       Data pull timestamps; reconciliation run log; variance report version;
                   finance owner resolution log

Evidence gaps: None — all required fields populated
```

**━━ AUTONOMY DECISION PACKET ━━━━━━━━━━━━━━━━━━━━━**

```
Autonomy:          SUPERVISED (AUT-2)
Surface:           CODE_AGENT (SURFACE-3)
Confidence:        HIGH
Justification:     RULE-03 (cost of failure: financial close accuracy affects financial
                   statements and audit compliance — SUPERVISED minimum regardless of analysis
                   quality); GATE-1 (workflow touches financial transaction data and produces
                   output that drives accounting decisions — SUPERVISED minimum); RULE-05
                   adversarial check passed; terminal action is report delivery, not ledger
                   modification — but financial consequence of a wrong report justifies
                   maintaining SUPERVISED
Controls required: Read-only access to all financial data sources; no write access to ledger;
                   finance owner named and available; variance report version retained;
                   resolution log maintained
Evidence gaps:     None
Conservative route: Not applied — HIGH confidence; GATE-1 structural minimum
Artifact required: template-control-plan.md
```

**━━ CONTROL PLAN ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━**

**Monthly Financial Close Reconciliation · SUPERVISED / CODE_AGENT · HIGH**

This workflow pulls financial records from Stripe, the bank, and the accounting platform, runs the reconciliation comparison, and delivers a variance report to the finance owner for resolution. The workflow has read-only access to all financial sources and produces no ledger entries. It qualifies for SUPERVISED — not AUTONOMOUS — because the variance report directly drives accounting decisions, and financial close accuracy carries regulatory and audit consequence. The finance owner reviews the report, approves the reconciliation, and resolves unmatched items.

**WHAT AI PREPARES**
A Monthly Reconciliation Report containing:
- Summary: total items compared, matched count, variance count by type
- Variance table: item ID · source system · amount · ledger amount · difference · classification (timing difference / likely error / unmatched)
- Unresolved items list: items the workflow could not classify, with available data on each
- Data source status: pull timestamp and record count per source system

**APPROVAL CHECKPOINT**
```
Reviewer:      Finance Owner (CFO, Controller, or designated close authority)
Reviews:       Variance classifications; completeness of data pull; unresolved items;
               overall reconciliation accuracy
Approves when: Variances are classified correctly; unresolved items are identified with
               sufficient context for resolution; data sources are complete and current
Rejects when:  Data pull is incomplete; classification appears incorrect on material items;
               unresolved item count exceeds threshold without explanation
Turnaround:    2 business days after report delivery (aligned with month-end close schedule)
```

**POST-APPROVAL ACTIONS**
1. Finance owner reviews and approves reconciliation report
2. Unresolved items routed to appropriate handler (AP team, bank contact, or accounting platform support)
3. Adjusting entries made by finance team outside this workflow's scope
4. Reconciliation signed off in accounting platform by finance owner

**PROHIBITED WITHOUT APPROVAL**
- Workflow may not initiate any ledger entry or accounting platform write action
- Workflow may not send reconciliation data to external parties (auditors, banks) without finance owner authorization

**AUDIT TRAIL**
Data pull log per source system: source, timestamp, record count. Variance report version number and date. Finance owner review timestamp and approval record. Resolution log per unresolved item. Retained 7 years per standard accounting records policy.

**EXPECTED OUTCOMES**
- Completed: Reconciliation report delivered; all items classified; unresolved items listed; finance owner assigned for review
- Completed w/ warnings: One data source returned partial data — report delivered with gap noted; finance owner reviews affected period manually
- Needs review: Variance count exceeds prior-month baseline by >20% — flag for finance owner before proceeding with close
- Blocked: Stripe API unavailable; bank export not received — halt; notify finance owner; reschedule pull
- Failed: Post-close discovery of a misclassified material variance — rerun reconciliation; issue corrected report; document in close log

**AUTONOMY EXPIRES WHEN**
- [x] The workflow's steps, inputs, or outputs change materially (new data source, accounting platform migration)
- [x] The AI surface or tool used changes
- [x] The policy or compliance context changes — any change to accounting standards, audit requirements, or financial reporting obligations
- [x] An incident occurs — any misclassified variance that affected a financial statement
- [x] Error rate exceeds 1% of items misclassified on any run — re-submit to Gate immediately
- [x] 12 months pass without a recertification review — review by [date: June 2027]
- [x] The reviewer role changes or becomes vacant — workflow paused until new finance owner is designated

---

## Example 11 — Social Media Scheduling from Approved Content

**Mechanism demonstrated:** GATE-4 triggers even when content is pre-approved. External publication requires a checkpoint regardless. RULE-03 cost of failure criterion also supports SUPERVISED. Shows that "approved" does not mean "no checkpoint needed."

**Raw input:**
> "When a post is marked approved in the content calendar, resize the copy for LinkedIn and X, attach the approved creative, and schedule the posts for the campaign window."

---

**━━ WORKFLOW INTAKE SNAPSHOT ━━━━━━━━━━━━━━━━━━━━━**

```
Name:              Social Media Scheduling from Approved Content
Initiator:         Post marked "approved" in content calendar
Actions:           Pull approved post from content calendar, resize copy for LinkedIn
                   character limit and X character limit, attach approved creative asset,
                   schedule posts for campaign window in social media publishing platform
Systems touched:   Content calendar (Notion, Airtable, or equivalent), creative asset
                   storage, social media publishing platform (Buffer, Hootsuite, or equivalent),
                   LinkedIn and X APIs (via publishing platform)
Data sensitivity:  Brand-published content — public, reputationally sensitive
Frequency:         Per approved post — multiple times weekly during active campaigns
Exception rate:    Low — copy resizing is mechanical; approval is already confirmed
Failure consequence: Wrong post published externally; reputational damage; incorrect campaign
                     timing; copy error that survived the approval process appears publicly
Reversibility:     Partial — scheduled posts can be deleted before publish; published posts
                   can be deleted but are not fully retractable (screenshots, reshares)
Terminal action:   External publication on LinkedIn and X
Audit trail:       Publishing platform schedule log; creative asset version

Evidence gaps: Copy resize rules not fully specified — what is the approved copy for LinkedIn
               vs X? Does resizing require creative judgment or mechanical truncation?
```

**━━ AUTONOMY DECISION PACKET ━━━━━━━━━━━━━━━━━━━━━**

```
Autonomy:          SUPERVISED (AUT-2)
Surface:           CODE_AGENT (SURFACE-3)
Confidence:        MEDIUM
Justification:     GATE-4 (terminal action is external publication — SUPERVISED minimum
                   regardless of pre-approval; published content is public and reputationally
                   exposed); RULE-03 (cost of failure: public post error has reputational
                   consequence; AI may introduce copy changes during resizing that were not
                   in the approved version); RULE-05 adversarial check: "pre-approved"
                   does not eliminate the publication risk — copy modification during resizing
                   is the most likely failure point
Controls required: Named reviewer for the resize step before scheduling is locked;
                   version comparison (original vs. resized) must be part of the review;
                   no post may be scheduled without human confirmation of the resized version
Evidence gaps:     Resize rules partially specified; reviewer for resize step not named
Conservative route: Not applied
Artifact required: template-control-plan.md
```

**━━ CONTROL PLAN ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━**

**Social Media Scheduling from Approved Content · SUPERVISED / CODE_AGENT · MEDIUM**

This workflow takes approved content from the calendar, produces platform-resized versions for LinkedIn and X, and schedules them for publication — with a human checkpoint on the resized copy before scheduling is confirmed. GATE-4 applies because the terminal action is external publication. Pre-approval of the source content does not cover the resized versions: any copy modification during the resizing step creates a new version that has not been approved. The reviewer confirms the resized copy matches the intent of the approved original before the posts are scheduled.

**WHAT AI PREPARES**
A Scheduling Review Package per approved post:
- Original approved copy (LinkedIn and X versions if separately approved, or unified source)
- Resized copy: LinkedIn version (3,000 character limit — strategic trim if over limit) and X version (280 characters — trim with priority rules: CTA preserved, key message preserved, hashtags trimmed last)
- Diff view: any text changed from approved copy to resized copy, highlighted
- Scheduled time per platform (from campaign window)
- Creative asset attached (no modification)

**APPROVAL CHECKPOINT**
```
Reviewer:      Content Lead or Campaign Manager (named role — must be designated before deployment)
Reviews:       Resized copy accuracy vs. approved original; CTA preserved; no meaning changed;
               creative asset correct; scheduled time aligned with campaign window
Approves when: Resized copy is accurate, CTA preserved, no meaning changed from approved original
Rejects when:  Copy meaning changed during resize; wrong creative asset attached; scheduling
               time conflicts with campaign plan; any text not in the approved version appears
Turnaround:    Same-day review (target: 4 hours before scheduled publish time)
```

**POST-APPROVAL ACTIONS**
1. Reviewer approves scheduling package in publishing platform
2. Posts locked for scheduled publish time
3. Publishing platform executes at scheduled time
4. Delivery log updated with publish confirmation

**PROHIBITED WITHOUT APPROVAL**
- No post may be locked or scheduled without reviewer confirmation of the resized copy
- AI may not modify the creative asset
- AI may not change the scheduled publish time without reviewer input

**AUDIT TRAIL**
Approved original version, resized version, diff log, reviewer name, approval timestamp, scheduled time, publish confirmation. Retained 12 months.

**EXPECTED OUTCOMES**
- Completed: Both posts scheduled with reviewer approval; creative attached; campaign window preserved
- Completed w/ warnings: Character limit required significant trimming — reviewer noted intent change; content was revised by reviewer before approval
- Needs review: Resize would require removing the CTA entirely — flag for reviewer; do not schedule
- Blocked: Approved creative asset not found in storage; publishing platform authentication failed — halt; notify content lead
- Failed: Post published with copy that differed from approved version — delete immediately; repost correct version; log the error

**AUTONOMY EXPIRES WHEN**
- [x] The workflow's steps, inputs, or outputs change materially (new platform added, resize rules change)
- [x] The AI surface or tool used changes
- [x] The policy or compliance context changes — any regulated advertising or financial services disclosure requirements
- [x] An incident occurs — any incorrect post published externally
- [x] Error rate exceeds 5% of resized posts requiring significant revision by reviewer
- [x] 6 months pass without a recertification review
- [x] The reviewer role changes or becomes vacant — workflow paused until new content lead is named

---

## Example 12 — New Hire Onboarding Checklist Routing

**Mechanism demonstrated:** Multi-step workflow with multiple human sign-off points. COWORK surface for the routing and tracking function; SUPERVISED because human approval is required at the routing decision point.

**Raw input:**
> "When a new hire starts, I need their equipment ordered, accounts set up, a buddy assigned, and their first-week schedule sent. Can AI handle the routing and tracking so nothing falls through the cracks?"

---

**━━ WORKFLOW INTAKE SNAPSHOT ━━━━━━━━━━━━━━━━━━━━━**

```
Name:              New Hire Onboarding Checklist Routing
Initiator:         New hire start date confirmed in HR system
Actions:           Detect new hire start date, generate onboarding task list, route tasks
                   to responsible owners (IT for equipment, IT/ops for accounts, manager
                   for buddy assignment, HR for schedule), track completion status,
                   flag overdue tasks
Systems touched:   HR system (start date, new hire data), task management or ITSM, email
                   or Slack for notifications, calendar (schedule delivery)
Data sensitivity:  New hire PII (name, start date, role, email); internal process data
Frequency:         Per new hire — weekly in growth-stage companies
Exception rate:    Low to medium — standard path is clear; exceptions occur when role
                   requires non-standard equipment, security clearance, or remote setup
Failure consequence: Task not completed before start date — new hire arrives without equipment,
                     access, or orientation; negative first impression; potential legal exposure
                     if required HR steps are missed
Reversibility:     Most tasks are reversible; equipment orders have a lead time that creates
                   a time constraint
Terminal action:   Task routing to owners + notification delivery (internal)
Audit trail:       Task completion log; notification sent timestamps

Evidence gaps: Exception handling for non-standard roles not described; equipment lead time
               thresholds not specified
```

**━━ AUTONOMY DECISION PACKET ━━━━━━━━━━━━━━━━━━━━━**

```
Autonomy:          SUPERVISED (AUT-2)
Surface:           COWORK (SURFACE-2)
Confidence:        MEDIUM
Justification:     RULE-03 (cost of failure: incomplete onboarding has legal and reputational
                   consequence; routing to wrong owner creates delays that may not be catchable
                   before start date); RULE-08 (routing step requires human sign-off — the
                   manager must confirm buddy assignment; HR must confirm schedule; IT must
                   confirm equipment spec); RULE-05 adversarial check: "AI handle the routing"
                   includes the buddy assignment decision, which is a human judgment call
Controls required: Human sign-off at the buddy assignment step; manager confirmation of
                   first-week schedule; IT confirmation of equipment spec before order is placed
Evidence gaps:     Exception handling for non-standard roles; equipment lead time threshold
Conservative route: Not applied
Artifact required: template-control-plan.md
```

**━━ CONTROL PLAN ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━**

**New Hire Onboarding Checklist Routing · SUPERVISED / COWORK · MEDIUM**

This workflow generates the onboarding task list, routes tasks to responsible owners, sends notifications, and tracks completion — with human sign-off required at two points: buddy assignment (manager decision) and equipment order confirmation (IT decision). The routing and tracking functions are autonomous; the judgment calls embedded in the workflow are supervised. This is the appropriate split for an onboarding workflow: AI eliminates the coordination overhead; humans retain the decisions that require context about the new hire or the team.

**WHAT AI PREPARES**
- Onboarding task list generated from new hire data (role, start date, location, equipment tier)
- Task assignments routed to: IT (equipment order + account setup), manager (buddy assignment), HR (first-week schedule delivery)
- Notification sent to each owner with their specific task, due date, and new hire details
- Completion tracker updated as tasks are confirmed

**APPROVAL CHECKPOINT**
```
Reviewer:      Manager (buddy assignment) · IT Lead (equipment spec and order) · HR (schedule)
Reviews:       Manager: buddy assignment is appropriate for this new hire's role and personality;
               IT: equipment spec is correct and lead time is achievable before start date;
               HR: first-week schedule is finalized and accurate
Approves when: Each owner confirms their task is assigned correctly and achievable on time
Rejects when:  Buddy assignment conflicts with manager's context; equipment spec is wrong;
               schedule has conflicts or missing required orientation sessions
Turnaround:    All confirmations required 5 business days before start date
```

**POST-APPROVAL ACTIONS**
1. Manager confirms buddy → workflow sends buddy introduction email
2. IT confirms equipment → workflow places equipment order (external action — IT retains order authority)
3. HR confirms schedule → workflow sends first-week schedule to new hire
4. All tasks tracked to completion; overdue items escalated to hiring manager 48 hours before start

**PROHIBITED WITHOUT APPROVAL**
- Equipment orders may not be placed without IT confirmation of spec and lead time
- New hire contact (schedule, welcome email) may not be initiated without HR sign-off
- Buddy assignment may not be communicated to either party without manager confirmation

**AUDIT TRAIL**
Task list version, routing log with timestamps, owner confirmation records, escalation log for overdue items. Retained 3 years per HR records policy.

**EXPECTED OUTCOMES**
- Completed: All tasks confirmed and completed before start date; new hire receives equipment, access, buddy introduction, and first-week schedule
- Completed w/ warnings: One task completed late but before start date — log the delay; review SLA for that owner
- Needs review: Equipment lead time is insufficient for start date — escalate immediately; options review required
- Blocked: Manager unavailable to confirm buddy assignment 5 days before start — escalate to HR or hiring manager backup
- Failed: Task missed; new hire arrives without required item — document; assign resolution owner; debrief on checklist gap

**AUTONOMY EXPIRES WHEN**
- [x] The workflow's steps, inputs, or outputs change materially (new onboarding step added, system changed)
- [x] The AI surface or tool used changes
- [ ] The policy or compliance context changes — monitor for regulatory onboarding requirements
- [x] An incident occurs — any new hire who arrived without a required item or access
- [x] Error rate exceeds 10% of tasks requiring manual intervention to complete
- [x] 6 months pass without a recertification review
- [x] Any reviewer role changes — workflow must be re-mapped with the new owner's name and capacity confirmed

---

## Example 13 — Compliance Evidence Collection

**Mechanism demonstrated:** LOW confidence from regulatory sensitivity and evidence gaps in scope. Shows that regulatory context alone is sufficient to downgrade confidence, even when the base criteria might support a higher verdict. RULE-06 confidence calibration.

**Raw input:**
> "We need to collect evidence for our annual SOC 2 audit. It's basically pulling screenshots, logs, and access reports from about a dozen systems. Can AI automate the evidence collection?"

---

**━━ WORKFLOW INTAKE SNAPSHOT ━━━━━━━━━━━━━━━━━━━━━**

```
Name:              SOC 2 Compliance Evidence Collection
Initiator:         Annual audit cycle begins (date specified by auditor)
Actions:           Pull screenshots, access logs, and reports from identified systems,
                   organize by SOC 2 control category, compile into an evidence package
Systems touched:   Up to 12 systems — not named; includes access control systems, logging
                   platforms, HR system, and any system in scope for SOC 2
Data sensitivity:  Highly regulated — evidence used in a formal audit; any error or gap
                   affects audit outcome; evidence may include employee PII and
                   system architecture details
Frequency:         Annual
Exception rate:    Unknown — systems not specified; some systems may require manual
                   screenshot (no API); some evidence types may require auditor interpretation
Failure consequence: Incomplete or incorrect evidence package delays audit completion;
                     worst case: audit finding or failure; regulatory exposure
Reversibility:     Collection is reversible (re-collect); but an audit deadline creates a
                   hard time constraint — missed evidence at submission is not reversible
Terminal action:   Evidence package delivered to compliance team for review (not submitted
                   to auditor directly by this workflow)
Audit trail:       Evidence collection log per system; version control on evidence package

Evidence gaps: Systems not named (critical — collection method differs by system);
               evidence types per control category not defined; SOC 2 scope (Type I or
               Type II, which Trust Service Criteria) not specified; auditor's evidence
               format requirements not provided
```

**━━ AUTONOMY DECISION PACKET ━━━━━━━━━━━━━━━━━━━━━**

```
Autonomy:          SUPERVISED (AUT-2) — conservative route applied (LOW confidence)
Surface:           PROJECT (SURFACE-1)
Confidence:        LOW
Justification:     RULE-06 (LOW confidence: regulatory sensitivity of SOC 2 evidence; multiple
                   required snapshot fields not fully populated — systems not named, evidence
                   types not defined, scope not specified); RULE-09 (Jidoka stop: unknown
                   state on which systems are in scope and what evidence each requires);
                   RULE-02 (required fields not fully populated — confidence cap applies);
                   RULE-05 adversarial check: "basically pulling screenshots and logs"
                   understates complexity — SOC 2 evidence has specific format and chain of
                   custody requirements
Controls required: Named compliance reviewer; evidence format confirmed with auditor before
                   collection begins; system scope documented; chain of custody maintained
Evidence gaps:     Systems not named; evidence types per control not defined; SOC 2 scope
                   not specified; auditor format requirements not provided
Conservative route: SUPERVISED applied; scope documentation required before deployment
Artifact required: template-control-plan.md
```

**━━ CONTROL PLAN ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━**

**SOC 2 Compliance Evidence Collection · SUPERVISED / PROJECT · LOW**

This workflow can assist with evidence collection for a SOC 2 audit once the scope is defined. Confidence is LOW because the systems in scope are unnamed, the evidence types per control category are undefined, and the auditor's format requirements have not been specified. The collection step can be partially automated — structured data pulls and log exports are automatable; screenshots and auditor-interpretation evidence must remain manual. The compliance team must review and approve the evidence package before it is submitted to the auditor.

**WHAT AI PREPARES**
A structured evidence collection run per system in scope, producing:
- Structured log exports: pulled via API or system export function; organized by control category
- Evidence index: one row per control, listing the evidence type required, the source system, the collection method used, and the status (collected / requires manual pull / not yet available)
- Gap report: any control category where evidence cannot be automatically collected

**APPROVAL CHECKPOINT**
```
Reviewer:      Compliance Lead or designated SOC 2 project owner
Reviews:       Evidence completeness per control category; accuracy of collected evidence;
               format compliance with auditor requirements; chain of custody integrity
Approves when: All required evidence is collected; format is correct; evidence package is
               complete and ready for auditor submission
Rejects when:  Evidence is incomplete; format does not match auditor requirements; chain of
               custody gap detected; any control category has zero evidence
Turnaround:    Review complete 5 business days before auditor submission deadline
```

**POST-APPROVAL ACTIONS**
1. Compliance lead reviews and approves evidence package
2. Package submitted to auditor by compliance lead (outside this workflow's scope)
3. Collection log retained as audit trail

**PROHIBITED WITHOUT APPROVAL**
- Evidence package may not be submitted to the auditor by this workflow
- No system access credentials may be retained beyond the collection run

**INFORMATION GAPS — Action required before deployment**
- Systems in scope: Name all 12 systems; confirm which have API access and which require manual collection
- Evidence types: For each SOC 2 Trust Service Criterion in scope, define what evidence is required and in what format
- SOC 2 scope: Confirm Type I or Type II; confirm which Trust Service Criteria apply
- Auditor format requirements: Request from auditor before collection begins — do not collect and reformat post-collection

**EXPECTED OUTCOMES**
- Completed: Evidence package assembled, compliance lead reviewed, all control categories covered
- Completed w/ warnings: 1–3 controls required manual collection — documented in gap report; compliance lead handled manually
- Needs review: Evidence format does not match auditor requirements — halt; confirm format before proceeding
- Blocked: More than 3 systems do not have accessible API or export; collection cannot be automated for those controls
- Failed: Evidence submitted to auditor with a gap — notify auditor immediately; provide corrected evidence within the audit timeline

**AUTONOMY EXPIRES WHEN**
- [x] The workflow's steps, inputs, or outputs change materially (new systems in scope, new control categories)
- [x] The AI surface or tool used changes
- [x] The policy or compliance context changes — SOC 2 framework updates; auditor changes; Trust Service Criteria revisions
- [x] An incident occurs — any evidence gap that affected an audit finding
- [x] 12 months pass — recertification required before each annual audit cycle
- [x] The reviewer role changes or becomes vacant — workflow must be re-assigned before next collection run

---

## Example 14 — Daily Ops Report (Fallback Surface Logic)

**Mechanism demonstrated:** Ideal surface is COWORK (scheduled, unattended). User has confirmed no Cowork access. Fallback surface logic from RULE-06 activates: PROJECT is named as the nearest viable alternative with specific adjustments listed. This is the only case where surface fallback is explicitly demonstrated.

**Raw input:**
> "I want an automated daily ops report — pull the previous day's numbers from our systems and have it ready in Slack every morning when the team arrives. I don't have access to Claude Cowork or any scheduled automation tool."

---

**━━ WORKFLOW INTAKE SNAPSHOT ━━━━━━━━━━━━━━━━━━━━━**

```
Name:              Daily Ops Report (Scheduled)
Initiator:         Ideally: schedule (each morning, before team arrives); confirmed:
                   human-initiated (user has no scheduled automation access)
Actions:           User pastes prior-day metric exports into session; operator generates
                   formatted ops report; user posts Slack-ready output to ops channel
Systems touched:   Data sources (CRM, support tool, financial platform — specifics not stated;
                   user exports manually); Slack (user posts)
Data sensitivity:  Internal business metrics; not regulated; no customer PII in output
Frequency:         Daily — every morning
Exception rate:    Low — structured export format, stable reporting template
Failure consequence: Internal report delayed or missing; team makes decisions without prior-day data
Reversibility:     Fully reversible — corrected report can be reposted
Terminal action:   Slack-ready report delivered in session (user posts to ops channel)
Audit trail:       Slack post timestamp; session retained by user if needed

Evidence gaps: Data source systems not named; ideal surface (COWORK) confirmed unavailable
```

**━━ AUTONOMY DECISION PACKET ━━━━━━━━━━━━━━━━━━━━━**

```
Autonomy:          AUTONOMOUS (AUT-1)
Surface:           PROJECT (SURFACE-1) — fallback from COWORK (SURFACE-2)
Confidence:        MEDIUM
Justification:     RULE-03 (all four criteria pass: reversible, observable, low exception rate,
                   low failure consequence); no GATE conditions; RULE-06 surface fallback
                   applied — COWORK is the recommended surface for a scheduled daily workflow
                   but user has confirmed it is unavailable; PROJECT is the nearest viable
                   alternative with the adjustments listed below
Controls required: Export access only (user provides data; no API connection); output
                   retained per session; human initiates and posts each morning
Evidence gaps:     Data source systems not named — cannot confirm read-only access scope
                   without knowing source platforms; COWORK unavailability confirmed
Conservative route: Not applied
Artifact required: template-project-setup.md
```

**━━ PROJECT SETUP BRIEF ━━━━━━━━━━━━━━━━━━━━━━━━━━**

**Daily Ops Report · AUTONOMOUS / PROJECT · MEDIUM**

This workflow produces the previous day's ops summary from data the user pastes at the start of each session and delivers a Slack-ready report for the user to post to the ops channel. The ideal surface for a daily scheduled report is COWORK, which can run unattended on a timer and pull directly from connected systems. Because COWORK is unavailable, this workflow runs on a human-initiated cadence inside a Claude Project: someone pastes the prior-day exports and triggers the report each morning. The verdict (AUTONOMOUS) does not change with the surface fallback; the execution model does. All four autonomy criteria pass cleanly and no GATE conditions apply.

**SURFACE FALLBACK NOTE**
The recommended surface for this workflow is COWORK (SURFACE-2), which supports unattended scheduled execution. The user has confirmed COWORK access is unavailable. PROJECT is the nearest viable alternative with the following adjustments:
- The workflow will not run automatically each morning — a human must open the Claude Project and trigger it
- If the trigger is missed, the report is delayed until someone runs it; there is no automatic alert
- Suggested mitigation: add the daily report trigger to a calendar reminder or recurring Slack message for the ops team lead
- If COWORK access becomes available in the future, re-submit this workflow for a surface upgrade to COWORK; the autonomy verdict will not change

**PURPOSE**
Eliminate manual morning data gathering by producing a ready-to-review ops summary each day before the team's standup.

**RUN CADENCE**
Human-initiated, each morning. Target: run before 9:00 AM standup. The ops team lead (or designated person) opens the Claude Project and pastes the trigger prompt. Not scheduled. Not unattended.

**KNOWLEDGE FILES**
- `daily-report-template.md` · Defines sections, metric labels, and format for the daily ops report
- `data-sources.md` · Documents which specific views, reports, or exports contain the prior day's data for each system
- `alert-thresholds.md` · Defines what constitutes a notable variance for each metric — so the operator can flag outliers

**CUSTOM INSTRUCTIONS**
```
You are the Daily Ops Report operator. When activated with the trigger phrase "Run daily ops report for [date]", follow this sequence:

1. Ask the user to paste: prior-day Salesforce pipeline activity, prior-day Stripe revenue summary, and prior-day support ticket summary.
2. Extract and label key metrics per the reporting template.
3. Write the ops summary: Revenue · Pipeline · Support · Notable Variances. Each section: two to three sentences. Flag any metric outside the alert threshold.
4. Format for Slack: plain text, no tables, under 300 words.
5. Provide the completed report ready to post to #ops-daily.
```

**OUTPUT FORMAT**
One Slack-ready text block per run, under 300 words, organized by Revenue / Pipeline / Support / Notable Variances. Delivered in session. Retained in project history.

**EXPECTED OUTCOMES**
- Completed: Formatted report delivered; all four sections populated; ready to post to Slack
- Completed w/ warnings: One data source not available — report delivered with the section noted as "data unavailable — update manually"
- Needs review: Notable variance exceeds 25% on any metric — flag before posting; ops lead confirms the number before the report goes out
- Blocked: Two or more data sources missing — do not produce a partial report; request data before running
- Failed: Report posted with an error discovered post-send — send corrected version with "[CORRECTION]" prefix; log the error

**AUTONOMY EXPIRES WHEN**
- [x] The workflow's steps, inputs, or outputs change materially (new data source, new Slack channel, format change)
- [x] The AI surface or tool used changes — including if COWORK becomes available; re-submit for surface upgrade
- [ ] The policy or compliance context changes — not applicable; internal metrics only
- [x] An incident occurs — any report that contained incorrect data and was used for a business decision
- [x] Error rate exceeds 10% of runs requiring manual correction
- [x] 6 months pass without a recertification review — review by [date: December 2026]
- [ ] The reviewer role changes — not applicable; AUTONOMOUS verdict
