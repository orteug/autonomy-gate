# Use Case Cookbook

This cookbook is organized by the sentence a real user says.

Each use case includes:

- user situation
- input to paste
- likely verdict
- why
- artifact
- next human action
- common failure
- safer version

---

## 1. "Can we automate this workflow?"

### Situation

Someone brings a vague automation idea.

### Input To Paste

```text
We are considering automating [workflow]. It starts when [trigger]. The steps are [steps]. It touches [systems]. The final output is [output]. If it goes wrong, [failure consequence]. Known exceptions are [exceptions].
```

### Likely Verdict

Depends on evidence.

### Why

This is the Gate's default use case.

### Artifact

Any artifact.

### Next Human Action

Read the snapshot first. If it misunderstood the workflow, re-run.

### Common Failure

Providing only the goal, not the steps.

### Safer Version

Name the terminal action explicitly.

---

## 2. "We have a messy process and no SOP."

### Input To Paste

```text
We want to automate client onboarding, but the process changes depending on client type. Different team members handle exceptions differently. We do not have a written SOP. The goal is to have AI route each new client to the right next steps.
```

### Likely Verdict

```text
SOP_FIRST / NO_AI
```

### Why

Exception handling is undocumented.

### Artifact

Stabilization Plan.

### Next Human Action

Assign a process owner and document standard and exception paths.

### Common Failure

Trying to automate the 80 percent standard path while ignoring exceptions.

### Safer Version

Start with a documentation workflow:

```text
Have AI convert interview notes about our onboarding process into a draft SOP for human review.
```

---

## 3. "I want AI to send outbound emails."

### Input To Paste

```text
We want AI to draft personalized outbound emails to 500 leads using CRM fields and send them to prospects. The goal is more pipeline. The reviewer is not defined yet.
```

### Likely Verdict

```text
SUPERVISED / PROJECT or SUPERVISED / CODE_AGENT
LOW or MEDIUM confidence
```

### Why

External communication and reputational risk require a checkpoint.

### Artifact

Control Plan.

### Next Human Action

Name reviewer, approval criteria, sending rules, and opt-out handling.

### Common Failure

Treating email drafts as the same as email sends.

### Safer Version

```text
AI drafts emails and produces a review queue. Human approves before sending.
```

---

## 4. "I want AI to issue refunds."

### Input To Paste

```text
When a refund request comes in, AI checks policy, order history, delivery status, and the return window. If it qualifies under $50, AI should issue the refund automatically.
```

### Likely Verdict

```text
SUPERVISED / CODE_AGENT
GATE-1
```

### Why

The terminal action moves money.

### Artifact

Control Plan.

### Next Human Action

Define approval checkpoint or change terminal action to recommendation only.

### Common Failure

Saying "it is rule-based" as if that bypasses money movement.

### Safer Version

```text
AI checks eligibility and recommends approve/deny. Support lead issues refund.
```

---

## 5. "I want AI to update vendor bank details."

### Input To Paste

```text
A vendor emailed asking us to update their bank account details before the next invoice cycle. Can we automate verification and update so it goes faster?
```

### Likely Verdict

```text
HUMAN_ONLY / NO_AI
GATE-2
```

### Why

Authorizing payment routing changes is an irreversible external commitment. GATE-2 triggers. No amount of verification logic, rule-matching, or email domain checks changes this verdict — the risk is not that the process is poorly designed, but that the authorization itself is being handed to an AI.

This is the entry point for Business Email Compromise (BEC) fraud. An attacker sends a convincing email impersonating a vendor. An automated system checks the request against criteria and approves it. The money moves. BEC causes billions in annual losses precisely because the workflow looks routine until it is not.

### Artifact

Governance Memo.

### Next Human Action

Document the human verification process: independent callback to a known number, dual-authorization requirement, confirmation logged before any change is made.

### Common Failure

Assuming AI verification makes the workflow safe. Verification quality does not change the verdict — the authorization step itself cannot be delegated.

### Safer Version

```text
AI prepares a vendor change review packet flagging the request, the claimed account details, and the communication trail. A human finance officer performs an independent callback to the vendor's verified number and authorizes the change.
```

---

## 6. "I want AI to screen resumes."

### Input To Paste

```text
For a specific support operations role, AI should review resumes against the job criteria and create a shortlist for the recruiter. A recruiter makes final decisions.
```

### Likely Verdict

```text
SUPERVISED / PROJECT
```

### Why

AI can assist with structured review, but hiring decisions and bias risk require human oversight.

### Artifact

Control Plan.

### Next Human Action

Define role criteria, reviewer, appeal/review path, and audit fields.

### Common Failure

Letting AI infer job criteria from vague role descriptions.

### Safer Version

Provide a rubric:

```text
Required skills, preferred skills, disqualifiers, and reviewer instructions are all defined.
```

---

## 7. "I want AI to prepare weekly KPI reports."

### Input To Paste

```text
Every Monday, the ops lead exports CRM, revenue, and support data and pastes it into the Project. AI should produce a Slack-ready summary with Revenue, Pipeline, Support, and Notable Trends.
```

### Likely Verdict

```text
AUTONOMOUS / PROJECT
```

### Why

Human initiated, internal, reversible, document output.

### Artifact

Project Setup Brief.

### Next Human Action

Create the Project and use the custom instructions.

### Common Failure

Claiming the Project pulls from source systems directly.

### Safer Version

Keep source export and Slack posting human-owned unless using a real runtime surface.

---

## 8. "I want AI to post meeting summaries to Slack."

### Input To Paste

```text
After each internal team meeting, AI should read the transcript, extract decisions and action items, and post a digest to our internal Slack channel.
```

### Likely Verdict

```text
AUTONOMOUS / COWORK
```

or fallback:

```text
AUTONOMOUS / PROJECT
```

### Why

Internal, reversible, low consequence, but posting to Slack requires a surface with integration capability.

### Artifact

Cowork Project Config or Project Setup Brief fallback.

### Next Human Action

If using Project fallback, paste transcript and manually post the digest.

### Common Failure

Assigning `PROJECT` while still claiming automatic Slack posting.

---

## 9. "I want AI to change employee permissions."

### Input To Paste

```text
When a manager requests access for an employee, AI should check the role and update permissions in the identity system.
```

### Likely Verdict

```text
HUMAN_ONLY / NO_AI
GATE-3
```

### Why

The terminal action changes access controls. GATE-3 triggers. Access control changes are a direct security attack surface — who can see what and who can do what in any system cannot be delegated to AI regardless of how well-documented the criteria are.

### Artifact

Governance Memo.

### Next Human Action

Keep permission changes human-owned. Document the human review process.

### The Decomposition Opportunity

The preparation phase and the execution phase have different verdicts.

- **Preparation** (compile the access review, cross-reference roles against least-privilege policy, flag anomalies, produce a recommended-changes packet): re-submit this as its own workflow. Likely verdict: `SUPERVISED / CODE_AGENT` or `SUPERVISED / PROJECT`.
- **Execution** (applying the access changes): stays `HUMAN_ONLY`. Implement as a human process with the Governance Memo as the SOP.

AI can own the analysis. A named access owner applies the changes.

### Safer Version

```text
AI compiles an access review packet cross-referencing the role request, current permissions, and least-privilege policy. Human access owner reviews and applies the changes.
```

---

## 10. "I want AI to schedule approved social posts."

### Input To Paste

```text
When a post is marked approved in the content calendar, AI should resize the copy for LinkedIn and X, attach creative, and schedule the posts.
```

### Likely Verdict

```text
SUPERVISED / CODE_AGENT
GATE-4
```

### Why

The terminal action is external publication.

### Artifact

Control Plan.

### Next Human Action

Add review after copy resizing and before scheduling.

### Common Failure

Assuming "approved content" remains approved after AI edits it.

---

## 11. "I want AI to collect compliance evidence."

### Input To Paste

```text
For our upcoming audit, AI should collect evidence from our systems, organize it by control, and prepare the package for auditor submission.
```

### Likely Verdict

```text
SUPERVISED / PROJECT or SUPERVISED / CODE_AGENT
LOW or MEDIUM confidence
```

### Why

Compliance evidence is sensitive. Scope, systems, reviewer, and submission boundary matter. Almost all regulatory workflows have a preparation phase that can receive a supervised or autonomous verdict — and a submission phase that is HUMAN_ONLY.

Regulatory filings to bodies like FINRA, SEC, or OFAC are irreversible external commitments under GATE-2. The submission step cannot be delegated. The compilation work that leads to it is a separate workflow.

### Artifact

Control Plan (for evidence compilation). Governance Memo (for the submission step, if submitted separately).

### Next Human Action

Split the workflow before submitting to the Gate. Submit "compile and validate the compliance package and produce a filing-ready document" as one workflow. Submit "submit the filing" as a separate workflow. The first will receive SUPERVISED. The second will receive HUMAN_ONLY. Implement the first as governed AI; a named compliance officer handles the second.

### Safer Version

```text
AI compiles evidence by control, flags gaps, and produces a filing-ready package. Compliance owner reviews and submits.
```

---

## 12. "I want AI to reconcile financial records."

### Input To Paste

```text
At month end, compare Stripe payouts, bank deposits, invoices, and accounting ledger entries. Produce a variance report and route unresolved differences to finance.
```

### Likely Verdict

```text
SUPERVISED / CODE_AGENT
```

### Why

Financial close accuracy has audit and reporting consequence.

### Artifact

Control Plan.

### Next Human Action

Implement read-only data access and finance-owner review.

### Common Failure

Letting AI post ledger entries automatically.

---

## 13. "I want AI to run daily reports automatically, but I only have Projects."

### Input To Paste

```text
I want an automated daily ops report ready in Slack every morning. I do not have Cowork or scheduled automation. I can paste exports into a Project each morning.
```

### Likely Verdict

```text
AUTONOMOUS / PROJECT
MEDIUM or HIGH depending on evidence
```

### Why

The ideal surface is scheduled, but the available surface is human-initiated.

### Artifact

Project Setup Brief with fallback note.

### Next Human Action

Add a calendar reminder and maintain a manual run log.

### Common Failure

Calling it "automated" when a human still starts every run.

---

## 14. "The Gate gave HUMAN_ONLY. Can AI help at all?"

### Input To Paste

```text
The previous workflow received HUMAN_ONLY because the terminal action was [terminal action]. Can we split the preparation steps into a separate workflow where AI prepares the packet but a human owns the terminal action?
```

### Likely Verdict

```text
SUPERVISED / PROJECT
```

or

```text
AUTONOMOUS / PROJECT
```

depending on the split.

### Why

Preparation can be safe even when execution is not.

### Artifact

Project Setup Brief, Automation Architecture, or Control Plan.

### Next Human Action

Keep the terminal action outside the AI scope.

---

## 15. "I want to audit all our automations."

### Input To Paste

Run each workflow separately.

Then create a registry using:

```text
docs/GOVERNANCE_REGISTRY_TEMPLATE.md
```

### Likely Verdict

Multiple.

### Artifact

Multiple artifacts plus governance registry.

### Next Human Action

Group by:

- HUMAN_ONLY
- LOW confidence
- SUPERVISED without reviewer
- AUTONOMOUS with upcoming recertification
- SOP_FIRST backlog

