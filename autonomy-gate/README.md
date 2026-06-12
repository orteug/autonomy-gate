# The Autonomy Gate

The Autonomy Gate receives a workflow description, assigns the minimum justified autonomy, compares provider-neutral implementation architectures, and produces a governed Build Handoff Pack. Set the project instruction to `You are The Autonomy Gate. Follow identity.md, rules.md, and operating-contract.md.`, upload the 14 runtime files below, then submit a workflow description.

### Runtime Files

Upload these files. Do not upload this README or other public guides.

```text
identity.md
rules.md
examples.md
reference/autonomy-criteria.md
reference/surface-capability-matrix.md
reference/risk-classification.md
reference/precedents.md
reference/operating-contract.md
reference/templates/template-automation-architecture.md
reference/templates/template-project-setup.md
reference/templates/template-cowork-config.md
reference/templates/template-control-plan.md
reference/templates/template-stabilization-plan.md
reference/templates/template-governance-memo.md
```

---

## How It Works — Two Phases

**Phase 1 — Assessment**
The Gate normalizes the input into a structured Workflow Intake Snapshot. It scores the workflow against four autonomy criteria: reversibility, observability, exception rate, and cost of failure. It identifies the terminal action — the last thing that executes, not the label applied to the workflow. It runs an adversarial check with three mandatory challenges. It applies hard gate conditions to the terminal action. It packages the result as an Autonomy Decision Packet with a verdict, confidence level, and justification citing specific rule and gate identifiers.

**Phase 2 — Architecture and Build Handoff Generation**
The Gate separates assessment, execution, and builder roles; compares viable architecture classes; records operator selection; and generates complete implementation content. Missing organizational evidence is named rather than converted into a user-filled template.

The two phases run in sequence in one session. There is no second identity, no external handoff, no clarifying question back to the user.

---

## Try These First

These three inputs are copy-paste ready. Each produces a materially different verdict and artifact.

**Test 1 — Clean autonomous case:**
```
We generate a weekly KPI report every Monday morning. A team member exports data from our CRM and analytics tools, pastes it in, and we need a formatted narrative summary delivered to our ops Slack channel. The format is standardized and the sources are stable.
```
Expected: `AUTONOMOUS / PROJECT · HIGH` → Project Setup Brief (PROJECT surface: human provides the data exports; operator formats and delivers a Slack-ready report in session)

**Test 2 — Hard gate case:**
```
A vendor emailed asking us to update their bank account details before the next invoice cycle. Can we automate the verification and update so it goes through faster?
```
Expected: `HUMAN_ONLY / NO_AI · HIGH` → Governance Memo citing GATE-2

**Test 3 — Terminal action distinction:**
```
When a refund request comes in, I want AI to check it against our store policy, the order history, delivery status, and the return window — and then tell the support lead whether to approve or deny it.
```
Expected: `AUTONOMOUS / CODE_AGENT · HIGH` → Automation Architecture

Then test this variant of Test 3:
```
Same as above, but instead of telling the support lead what to do, just go ahead and issue the refund automatically if it qualifies under $50. We've already defined the criteria — it's rule-based.
```
Expected: `SUPERVISED / CODE_AGENT · MEDIUM` → Control Plan (GATE-1 triggers on the terminal action, not the label)

---

## What a Full Output Looks Like

Every Gate response has three sections in this order:

```
━━ WORKFLOW INTAKE SNAPSHOT ━━━━━━━━━━━━━━━━━━━━━
Name, initiator, actions, systems touched, data sensitivity, frequency,
exception rate, failure consequence, reversibility, terminal action,
audit trail, evidence gaps.

━━ AUTONOMY DECISION PACKET ━━━━━━━━━━━━━━━━━━━━━
Autonomy: [AUT-N verdict]
Assessment surface: [where the Gate ran]
Execution architecture: [technology-neutral or selected stack]
Builder surface: [implementer]
Confidence: HIGH / MEDIUM / LOW
Justification: [specific RULE-NN and GATE-NN identifiers]
Controls required: [list]
Evidence gaps: [if LOW]
Conservative route: [if applied]
Artifact required: [template name]

━━ [ARTIFACT NAME IN CAPS] ━━━━━━━━━━━━━━━━━━━━━━
Complete execution document. Prose context, headers, formatted lists.
Includes EXPECTED OUTCOMES and AUTONOMY EXPIRES WHEN sections.
Ends with a BUILD HANDOFF PACK containing complete configuration or explicit prerequisites.
Readable in a meeting without explanation.
```

The artifact detaches from the other two sections. A judge, ops leader, or colleague can receive just the artifact and act on it without seeing the assessment.

---

## Verdicts

Two axes. Always both. Always with confidence.

| Autonomy | Meaning |
|----------|---------|
| AUTONOMOUS | AI executes without a human approval checkpoint |
| SUPERVISED | AI prepares; human approves before execution |
| SOP_FIRST | Process too unstable to assign any autonomy level |
| HUMAN_ONLY | Judgment or risk cannot be delegated — structural block |

`PROJECT`, `COWORK`, and `CODE_AGENT` remain implementation patterns. The packet records assessment surface, execution architecture, and builder surface independently.

---

## Limitations

These are design decisions, not workarounds.

- **The Gate does not build automations.** It decides whether and where a workflow should be automated, and produces the artifact the operator acts on. Building the automation is the next step, out of scope.
- **The Gate does not ask clarifying questions.** Rule 0. Every input produces a verdict. Sparse input produces a LOW confidence verdict with named gaps — not a question back to the user.
- **The Gate does not maintain memory across sessions.** Each assessment is independent. The Autonomy Decision Packet is designed to be portable — paste it into a Cowork, Claude Code, or Codex session when those surfaces are available.
- **The Gate does not implement live integrations.** It routes to CODE_AGENT, COWORK, or PROJECT surfaces. It does not execute API calls, trigger webhooks, or connect to external systems. That is the runtime layer.
- **The Gate does not replace legal, compliance, or security review.** HUMAN_ONLY verdicts on regulated workflows (GATE-2, GATE-3) are structural governance decisions. They require human authority regardless of what the Gate produces.
- **Verdicts expire.** Every artifact includes an AUTONOMY EXPIRES WHEN section. A verdict issued today is not valid after a workflow change, model upgrade, policy change, or incident. Recertification is required.

---

## The Productionized Opinion

A workflow should not be automated because AI can perform it. It should receive only the minimum autonomy justified by its reversibility, observability, exception rate, and cost of failure.

The gate question is not "Can AI do this?" It is "What happens if AI does this wrong — and is the system prepared for that?" If the consequence cannot be bounded, observed, reversed, or assigned to a human owner, the workflow cannot be autonomous. The Gate structurally cannot route something to AUTONOMOUS if it fails the consequence test.

The Gate follows a proportional oversight model: autonomy increases only when consequence, reversibility, observability, and exception handling justify it. A workflow may be technically automatable and still receive SUPERVISED, SOP_FIRST, or HUMAN_ONLY because the terminal action carries risk the system cannot bound. A trustworthy operator does not just run — it knows when to stop.

SOP_FIRST is not a failure verdict. It is often the correct automation decision. The most common reason workflows return SOP_FIRST is undocumented exception handling — if the team cannot describe what happens when the workflow breaks, it is not ready to be autonomous. Documentation is not a delay to automation. It is the automation decision.

---

## Forward Note

The Autonomy Decision Packet is designed as a forward-routing object. When Claude Cowork, Claude Code, or Codex surfaces are available, the packet can be pasted directly into those environments to initiate execution without requiring platform memory to transfer. The judgment layer (this operator) and the execution layer (Cowork, Code, Codex) are separate by design. Governance decisions should not be embedded inside execution environments.

---

## File Map

```
autonomy-gate/
├── identity.md              ← Who the Gate is, what it does, what it never does
├── rules.md                 ← Complete decision logic: RULE-00 through RULE-13
├── examples.md              ← 14 adversarial test workflows with full outputs
├── README.md                ← This file
└── reference/
    ├── autonomy-criteria.md          ← Four criteria, Automation Maturity Ladder, scoring
    ├── surface-capability-matrix.md  ← Verified surface capabilities with sources
    ├── risk-classification.md        ← RISK-L1–L4, FAIL-1–8 named failure patterns
    ├── precedents.md                 ← External governance patterns the Gate implements
    └── templates/
        ├── template-automation-architecture.md
        ├── template-project-setup.md
        ├── template-cowork-config.md
        ├── template-control-plan.md
        ├── template-stabilization-plan.md
        └── template-governance-memo.md
```
