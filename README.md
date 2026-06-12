# The Autonomy Gate

The Autonomy Gate receives a workflow description, assigns the minimum justified autonomy, compares provider-neutral implementation architectures, and produces a governed Build Handoff Pack. Create a Claude Project or supported ChatGPT Project, set the instruction to `You are The Autonomy Gate. Follow identity.md, rules.md, and operating-contract.md.`, upload the 14 runtime files below, then submit a workflow description.

## Judge Path

You do not need to read the whole repository.

1. Run the vendor bank-change prompt in [Try These First](#try-these-first) to see `GATE-2` refuse an irreversible external commitment.
2. Open [the validated productization receipts](examples/receipts/) to inspect autonomous, supervised, and refusal outcomes without installing anything.
3. Use [JUDGE_GUIDE.md](JUDGE_GUIDE.md) to audit any named mechanism with a falsifiable prompt.
4. Read [ORIGIN.md](ORIGIN.md) for the authentic problem provenance and [WRITEUP.md](WRITEUP.md) for the product argument.

The first meaningful proof is the refusal case, not the file tree.

### Runtime Files

Upload these files from `autonomy-gate/`. Do not upload the entire repository or the public guides alongside the runtime package.

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

Claude Projects can receive these in their folder structure. For ChatGPT Projects, upload the files flat and follow the plan and batching notes in `adapters/openai/chatgpt-project-setup.md`.

---

## How It Works — Two Phases

**Phase 1 — Assessment**
The Gate normalizes the input into a structured Workflow Intake Snapshot. It scores the workflow against four autonomy criteria: reversibility, observability, exception rate, and cost of failure. It identifies the terminal action — the last thing that executes, not the label applied to the workflow. It runs an adversarial check with three mandatory challenges. It applies hard gate conditions to the terminal action. It packages the result as an Autonomy Decision Packet with a verdict, confidence level, and justification citing specific rule and gate identifiers.

**Phase 2 — Architecture and Build Handoff Generation**
The Gate separates assessment, execution, and builder roles, compares viable architecture classes, and fills the matching artifact. Users select an architecture and supply only irreducible organizational evidence; they do not complete blank governance templates.

The two phases run in sequence in one session. There is no second identity, no external handoff, no clarifying question back to the user.

---

## Try These First

These three inputs are copy-paste ready. Each produces a materially different verdict and artifact.

**Test 1 — Clean autonomous case:**
```
We generate a weekly KPI report every Monday morning. A team member exports data from our CRM and analytics tools, pastes it in, and we need a formatted narrative summary delivered to our ops Slack channel. The format is standardized and the sources are stable. If the report has a mistake, it gets caught in review before we post it — and since it's just an internal Slack message, the worst case is we post a correction. Nothing irreversible happens.
```
Expected autonomy: `AUTONOMOUS · HIGH`. Assessment surface: Project. Execution architecture: human-triggered document workflow. Build Handoff Pack: `BLOCKED_FOR_EVIDENCE` pending operator-defined error-rate threshold and recertification interval.

**Test 2 — Hard gate case:**
```
A vendor emailed asking us to update their bank account details before the next invoice cycle. Can we automate the verification and update so it goes through faster?
```
Expected autonomy: `HUMAN_ONLY · HIGH`; handoff status: `NOT_APPLICABLE`; Governance Memo citing GATE-2

**Test 3 — Terminal action distinction:**
```
When a refund request comes in, I want AI to check it against our store policy, the order history, delivery status, and the return window — and then tell the support lead whether to approve or deny it.
```
Expected autonomy: `AUTONOMOUS · HIGH`; code-first architecture option; Automation Architecture

Then test this variant of Test 3:
```
Same as above, but instead of telling the support lead what to do, just go ahead and issue the refund automatically if it qualifies under $50. We've already defined the criteria — it's rule-based.
```
Expected autonomy: `SUPERVISED · MEDIUM`; code-first execution architecture; Control Plan because GATE-1 triggers on the terminal action

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
Ends with a BUILD HANDOFF PACK containing complete configuration or an explicit evidence-block list.
Readable in a meeting without explanation.
```

The artifact detaches from the other two sections. A judge, ops leader, or colleague can receive just the artifact and act on it without seeing the assessment.

---

## Verdicts

Autonomy, three implementation roles, handoff status, and confidence are always distinct.

| Autonomy | Meaning |
|----------|---------|
| AUTONOMOUS | AI executes without a human approval checkpoint |
| SUPERVISED | AI prepares; human approves before execution |
| SOP_FIRST | Process too unstable to assign any autonomy level |
| HUMAN_ONLY | Judgment or risk cannot be delegated — structural block |

`PROJECT`, `COWORK`, and `CODE_AGENT` are implementation patterns. The packet records `Assessment surface`, `Execution architecture`, and `Builder surface` so production design is not limited by the platform running the Gate.

---

## Limitations

These are design decisions, not workarounds.

- **The Gate does not build automations.** It decides whether and where a workflow should be automated, and produces the artifact the operator acts on. Building the automation is the next step, out of scope.
- **The Gate does not ask clarifying questions.** Rule 0. Every input produces a verdict. Sparse input produces a LOW confidence verdict with named gaps — not a question back to the user.
- **The Gate does not maintain memory across sessions.** Each assessment is independent. The Autonomy Decision Packet is designed to be portable — paste it into a Cowork, Claude Code, or Codex session when those surfaces are available.
- **The Gate does not implement live integrations.** It designs an execution architecture and names an appropriate builder, which may use Project, Cowork, code-agent, low-code, or service patterns. It does not execute API calls, trigger webhooks, or connect to external systems. That is the runtime layer.
- **The Gate does not replace legal, compliance, or security review.** HUMAN_ONLY verdicts on regulated workflows (GATE-2, GATE-3) are structural governance decisions. They require human authority regardless of what the Gate produces.
- **Verdicts expire.** Every artifact includes an AUTONOMY EXPIRES WHEN section. A verdict issued today is not valid after a workflow change, model upgrade, policy change, or incident. Recertification is required.

---

## The Productionized Opinion

A workflow should not be automated because AI can perform it. It should receive only the minimum autonomy justified by its reversibility, observability, exception rate, and cost of failure.

The gate question is not "Can AI do this?" It is "What happens if AI does this wrong — and is the system prepared for that?" If the consequence cannot be bounded, observed, reversed, or assigned to a human owner, the workflow cannot be autonomous. The Gate structurally cannot route something to AUTONOMOUS if it fails the consequence test.

SOP_FIRST is not a failure verdict. It is often the correct automation decision. The most common reason workflows return SOP_FIRST is undocumented exception handling — if the team cannot describe what happens when the workflow breaks, it is not ready to be autonomous. Documentation is not a delay to automation. It is the automation decision.

---

## Product Depth

The repository uses progressive disclosure:

- `autonomy-gate/` contains the 14-file runtime and supporting contracts.
- `examples/` contains committed receipts.
- `docs/` is optional operator documentation; it is not required for judging or first use.
- `print-manual/` and `testing/` are supporting product and validation material, not part of the fast path.

Depth remains available on demand, but no judge or first-time operator must traverse it to understand the product.

## License

Copyright 2026 Ariel Ortiz. Licensed under the [Apache License 2.0](LICENSE).

## Forward Note

The Autonomy Decision Packet is a portable work order. Its Build Handoff Pack translates the selected production architecture for the named builder without binding the design to the assessment platform.

---

## Repository Structure

```
repo-root/
├── README.md                ← This file (GitHub landing page)
├── WRITEUP.md               ← Origin story and architectural rationale
├── JUDGE_GUIDE.md           ← Falsifiable test prompts per RULE-NN and GATE-NN
├── examples/
│   ├── README.md
│   └── trial-audit-output.md  ← Three complete Gate runs with sources
├── docs/
│   └── AUTONOMY_GATE_FIELD_MANUAL.pdf
│
├── autonomy-gate/           ← Runtime source; upload only the 14 files listed above
│   ├── identity.md
│   ├── rules.md
│   ├── examples.md
│   ├── README.md
│   └── reference/
│       ├── README.md
│       ├── autonomy-criteria.md
│       ├── surface-capability-matrix.md
│       ├── risk-classification.md
│       ├── precedents.md
│       └── templates/
│           ├── README.md
│           ├── template-automation-architecture.md
│           ├── template-project-setup.md
│           ├── template-cowork-config.md
│           ├── template-control-plan.md
│           ├── template-stabilization-plan.md
│           └── template-governance-memo.md
```
