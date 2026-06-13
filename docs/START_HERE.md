# Start Here

Welcome to The Autonomy Gate.

This guide is for someone who has never used an AI operator before.

---

## The One-Sentence Version

The Autonomy Gate helps you decide whether a business workflow should be handled by AI, how much authority AI should get, which implementation architectures are viable, and what must be true before a builder begins.

---

## What You Need

You need:

- Access to a Claude or ChatGPT Project with capacity for the 16 runtime files; verify current official plan limits before installation
- The `autonomy-gate/` folder
- One workflow you are considering automating
- Ten minutes for the first run

You do not need:

- Coding experience
- API keys
- Automation software
- A perfect process document
- Prior AI experience

---

## What The Gate Does

When you paste a workflow description, the Gate produces three sections:

1. `WORKFLOW INTAKE SNAPSHOT`
   - What the Gate thinks the workflow is
   - Who starts it
   - What systems it touches
   - What happens at the end
   - What evidence is missing

2. `AUTONOMY DECISION PACKET`
   - Whether AI can handle it
   - The technology-neutral execution architecture and builder role
   - How confident the Gate is
   - Which rules and gates drove the decision

3. `EXECUTION ARTIFACT`
   - The document you act on
   - Examples: Project Setup Brief, Control Plan, Governance Memo, Stabilization Plan

---

## What The Gate Does Not Do

The Gate does not:

- Build the automation for you
- Run scheduled jobs
- Connect to Slack, Salesforce, Stripe, Zendesk, or databases by itself
- Replace legal, compliance, HR, finance, or security review
- Guarantee your workflow description is accurate
- Make unsafe workflows safe by adding vague "human review"

The Gate decides and specifies. Execution happens only after architecture selection, operator disposition, and builder acknowledgement.

---

## The Executor Misconception

The most common first-time mistake: **running the Gate and thinking the automation is now running.**

It is not.

When the Gate produces a Project Setup Brief, a Control Plan, or a Governance Memo — that is a governance document. It tells you what to build and under what conditions. You still have to build it.

The Gate is a decision layer. Think of it as a zoning board, not a construction crew. It tells you what is permitted, at what scale, with what safeguards. The building happens after the decision.

---

## When Not To Use The Gate

The Gate is designed for **recurring organizational workflows** — processes that run repeatedly, where the question "how much authority should AI have, and what happens when it goes wrong?" has a real organizational answer.

Do not use the Gate for:

- One-time personal requests ("draft this email for me")
- Ad hoc AI assistance ("summarize this document")
- Tasks where you are the only authority and the only person affected

The two-question test before you submit:

```text
1. Is this a recurring workflow that will run again and again?
2. If AI gets it wrong, does someone other than me face a consequence?
```

If both answers are yes, the Gate is the right tool.

If either answer is no, use your general AI assistant directly. The Gate will produce a technically valid output for any input — but for personal or one-time requests, that output will be a governance framework for a process that does not need one. It will not be useful.

The Gate governs workflows. It does not assist with tasks.

---

## Five-Minute Setup In Claude Project

1. Create a new Claude Project.
2. Name it `The Autonomy Gate`.
3. Set the project instruction:

```text
You are The Autonomy Gate. Follow identity.md, rules.md, and operating-contract.md. Produce the canonical Markdown governance record, then create a separate rendered Claude Artifact containing the complete self-contained HTML Execution Artifact using artifact-rendered.html. Do not print HTML source in chat. Preserve every substantive section and exact canonical value from the Markdown. If Artifact rendering is unavailable, state ARTIFACT_RENDERING_UNAVAILABLE and return Markdown only.
```

4. Upload these files from `autonomy-gate/`:

```text
identity.md
rules.md
examples.md
reference/autonomy-criteria.md
reference/risk-classification.md
reference/surface-capability-matrix.md
reference/precedents.md
reference/operating-contract.md
reference/operator-disposition.md
reference/tool-selection-rules.md
reference/templates/template-automation-architecture.md
reference/templates/template-project-setup.md
reference/templates/template-cowork-config.md
reference/templates/template-control-plan.md
reference/templates/template-stabilization-plan.md
reference/templates/template-governance-memo.md
```

That is 16 runtime files. Also upload `examples/artifact-rendered.html` as the design reference, for 17 uploaded files total. Do not upload `README.md`, `JUDGE_GUIDE.md`, `WRITEUP.md`, or other files from `examples/`.

The rendered Claude Artifact is the operator-facing deliverable. The Markdown output is the auditable source record. Confirm both formats contain the same verdict, confidence, handoff status, terminal action, architecture options, controls, exact status tokens, and disposition fields.

5. Start a new chat in the project.
6. Paste a workflow description.

Use this first test:

```text
We generate a weekly KPI report every Monday morning. A team member exports data from our CRM and analytics tools, pastes it in, and we need a formatted narrative summary for a human to review and post to our ops Slack channel. The format is standardized and the sources are stable. If the narrative is wrong, it can be corrected before posting. The workflow has no system write access.
```

Expected result:

```text
AUTONOMOUS · HIGH with architecture options
Artifact: Project Setup Brief
```

If you get that shape, the Gate is working.

---

## How To Read The First Output

Do not read the verdict first.

Read in this order:

1. Check the `Workflow Intake Snapshot`.
2. Confirm the `Terminal action`.
3. Read the `Autonomy Decision Packet`.
4. Read the final artifact.
5. Decide what human action comes next.

The most important field is `Terminal action`.

That is the final thing the workflow does. A workflow that "checks refund eligibility" is different from a workflow that "issues the refund." The first produces a recommendation. The second moves money.

---

## The Four Possible Autonomy Verdicts

| Verdict | Plain meaning |
|---|---|
| `AUTONOMOUS` | AI can run without a human approval checkpoint inside the run. |
| `SUPERVISED` | AI can prepare the work, but a human must approve before the terminal action. |
| `SOP_FIRST` | The workflow is too undocumented or unstable. Document the process before automating. |
| `HUMAN_ONLY` | The terminal action cannot be delegated to AI. |

---

## Common Implementation Patterns

| Pattern | Plain meaning |
|---|---|
| `PROJECT` | Human-initiated Claude Project or ChatGPT Project. Good for analysis and artifacts. |
| `COWORK` | Scheduled or local file workflow surface, when available. |
| `CODE_AGENT` | Claude Code or Codex. Good for scripts, integrations, APIs, tests, and enforcement. |

These are implementation patterns, not autonomy verdicts. The packet records the assessment surface, execution architecture, and builder surface separately.

---

## What To Do After A Verdict

Do not choose a template. Use the five primary commands in `USER_MODES.md`: `ASSESS`, `RESOLVE EVIDENCE`, `SELECT ARCHITECTURE`, `APPROVE`, and `REVIEW BUILD`.

Use this table to interpret the artifact:

| If the Gate says | Do this |
|---|---|
| `AUTONOMOUS` with Project pattern | Create a workflow-specific Project using the Project Setup Brief. |
| `AUTONOMOUS` with a scheduled local-file or connector architecture | Use the Cowork Config and set up folders, schedule, and logs. |
| `AUTONOMOUS` with a code-first architecture | Give the Automation Architecture to the selected builder. |
| `SUPERVISED` | Implement the Control Plan and named approval checkpoint before the terminal action. |
| `SOP_FIRST` | Assign a process owner and complete the Stabilization Plan. |
| `HUMAN_ONLY` | Use the Governance Memo as the human process document; no AI execution handoff is authorized. |

---

## Your First Three Tests

Run these after the first setup test.

### Test 1: Clean Project Workflow

```text
We generate a weekly KPI report every Monday morning. A team member exports data from our CRM and analytics tools, pastes it in, and we need a formatted narrative summary delivered to our ops Slack channel. The format is standardized and the sources are stable.
```

Expected:

```text
AUTONOMOUS with a Project implementation pattern
```

### Test 2: Money Movement

```text
When a refund request comes in, I want AI to check it against our policy and automatically issue the refund if it qualifies under $50.
```

Expected:

```text
SUPERVISED with a code-first implementation pattern
GATE-1 should be cited.
```

### Test 3: Irreversible External Commitment

```text
A vendor emailed asking us to update their bank account details before the next invoice cycle. Can we automate the verification and update so it goes through faster?
```

Expected:

```text
HUMAN_ONLY with NOT_APPLICABLE handoff status
GATE-2 should be cited.
```

---

## Beginner Rule

If you are unsure what to do with the result, do not ask the Gate to override itself.

Instead, read:

- `USER_MODES.md`
- the validated receipts in `../examples/receipts/`
- the artifact the Gate produced

The Gate is designed to be conservative when evidence is missing.
