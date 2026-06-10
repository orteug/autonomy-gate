# Start Here

Welcome to The Autonomy Gate.

This guide is for someone who has never used an AI operator before.

---

## The One-Sentence Version

The Autonomy Gate helps you decide whether a business workflow should be handled by AI, how much authority AI should get, what platform should run it, and what document you need before acting.

---

## What You Need

You need:

- Access to Claude Projects, or a ChatGPT Go, Plus, Pro, Edu, Business, or Enterprise Project with capacity for the 13 runtime files
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
   - Which surface should run it
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

The Gate decides. Execution happens on the right surface after the decision.

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
You are The Autonomy Gate. Follow identity.md.
```

4. Upload these files from `autonomy-gate/`:

```text
identity.md
rules.md
examples.md
README.md
reference/autonomy-criteria.md
reference/risk-classification.md
reference/surface-capability-matrix.md
reference/precedents.md
reference/templates/template-automation-architecture.md
reference/templates/template-project-setup.md
reference/templates/template-cowork-config.md
reference/templates/template-control-plan.md
reference/templates/template-stabilization-plan.md
reference/templates/template-governance-memo.md
```

That is 14 files. Do not upload `JUDGE_GUIDE.md`, `OPERATOR_GUIDE.md`, `WRITEUP.md`, or the `examples/` subfolder — those are human-facing reference and are not needed by the Gate.

5. Start a new chat in the project.
6. Paste a workflow description.

Use this first test:

```text
We generate a weekly KPI report every Monday morning. A team member exports data from our CRM and analytics tools, pastes it in, and we need a formatted narrative summary delivered to our ops Slack channel. The format is standardized and the sources are stable.
```

Expected result:

```text
AUTONOMOUS / PROJECT · HIGH
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

## The Four Possible Surface Verdicts

| Surface | Plain meaning |
|---|---|
| `PROJECT` | Human-initiated Claude Project or ChatGPT Project. Good for analysis and artifacts. |
| `COWORK` | Scheduled or local file workflow surface, when available. |
| `CODE_AGENT` | Claude Code or Codex. Good for scripts, integrations, APIs, tests, and enforcement. |
| `NO_AI` | Do not run this workflow on an AI surface. |

---

## What To Do After A Verdict

Use this table:

| If the Gate says | Do this |
|---|---|
| `AUTONOMOUS / PROJECT` | Create a workflow-specific Project using the Project Setup Brief. |
| `AUTONOMOUS / COWORK` | Use the Cowork Config and set up folders, schedule, and logs. |
| `AUTONOMOUS / CODE_AGENT` | Give the Automation Architecture to a builder or code agent. |
| `SUPERVISED / anything` | Implement the Control Plan and named approval checkpoint before execution. |
| `SOP_FIRST / NO_AI` | Assign a process owner and complete the Stabilization Plan. |
| `HUMAN_ONLY / NO_AI` | Use the Governance Memo as the human process document. |

---

## Your First Three Tests

Run these after the first setup test.

### Test 1: Clean Project Workflow

```text
We generate a weekly KPI report every Monday morning. A team member exports data from our CRM and analytics tools, pastes it in, and we need a formatted narrative summary delivered to our ops Slack channel. The format is standardized and the sources are stable.
```

Expected:

```text
AUTONOMOUS / PROJECT
```

### Test 2: Money Movement

```text
When a refund request comes in, I want AI to check it against our policy and automatically issue the refund if it qualifies under $50.
```

Expected:

```text
SUPERVISED / CODE_AGENT
GATE-1 should be cited.
```

### Test 3: Irreversible External Commitment

```text
A vendor emailed asking us to update their bank account details before the next invoice cycle. Can we automate the verification and update so it goes through faster?
```

Expected:

```text
HUMAN_ONLY / NO_AI
GATE-2 should be cited.
```

---

## Beginner Rule

If you are unsure what to do with the result, do not ask the Gate to override itself.

Instead, read:

- `VERDICT_PLAYBOOK.md`
- `TROUBLESHOOTING.md`
- the artifact the Gate produced

The Gate is designed to be conservative when evidence is missing.
