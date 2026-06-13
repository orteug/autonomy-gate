# Claude Project Setup — Autonomy Gate Adapter

This file covers two scenarios: (1) deploying The Autonomy Gate itself inside a Claude Project, and (2) deploying a Gate-governed workflow inside a Claude Project after the Gate has issued a verdict.

---

## Scenario 1 — Deploying the Gate (Decision Layer)

Use this when you want to run The Autonomy Gate in a Claude Project to assess workflows.

**Step 1 — Create a new Claude Project**

In Claude (claude.ai), create a new Project. Name it: `The Autonomy Gate` or any name that makes the purpose clear to your team.

**Step 2 — Set the custom instruction**

In Project Settings → Custom Instructions, paste exactly:

```
You are The Autonomy Gate. Follow identity.md, rules.md, and operating-contract.md. When you produce an Execution Artifact, render it as styled HTML immediately after the Markdown output. Output the HTML in a fenced code block labeled html. Use the design system in artifact-rendered.html as the exact style reference.
```

**Step 3 — Upload the operator files**

Upload the contents of the `autonomy-gate/` folder plus the rendered artifact reference. Upload all files flat — Claude Projects do not support folders. Files to upload:

```
identity.md
rules.md
examples.md
autonomy-criteria.md
surface-capability-matrix.md
risk-classification.md
precedents.md
operating-contract.md
template-automation-architecture.md
template-project-setup.md
template-cowork-config.md
template-control-plan.md
template-stabilization-plan.md
template-governance-memo.md
artifact-rendered.html
```

`artifact-rendered.html` is in `examples/` in the repository. Upload it as the HTML style reference — it defines every color, font, spacing, and layout rule the Gate must reproduce. Do not upload `README.md`.

**Step 4 — Run**

Paste any workflow description. The Gate produces three sections in order: Workflow Intake Snapshot → Autonomy Decision Packet → Execution Artifact, followed by a styled HTML rendering of the artifact in a fenced code block. Save the HTML block to a file to open it in a browser.

---

## Scenario 2 — Deploying a Gate-Governed Workflow (PROJECT Surface)

Use this when the operator-selected execution architecture uses a human-triggered Claude Project pattern and the Gate has produced a Project Setup Brief or Control Plan.

**Step 1 — Read the generated build handoff pack**

The Gate's Project Setup Brief or Control Plan contains a complete BUILD HANDOFF PACK. It provides:
- Custom instructions to paste verbatim
- Knowledge files to upload
- Run cadence and operator behavior

**Step 2 — Create a new Claude Project**

One project per governed workflow. Do not combine multiple governed workflows into one project unless their verdicts, contexts, and approval chains are identical.

**Step 3 — Apply the generated project instructions**

Paste the generated project instructions verbatim. Do not translate packet fields into another template or paraphrase the constraints.

**Step 4 — Upload knowledge files named in the artifact**

The artifact's KNOWLEDGE FILES section names what to upload and why. Upload exactly those files. Do not add files not listed without re-running the Gate on the updated workflow scope.

**Step 5 — Configure the approval checkpoint (SUPERVISED only)**

If the verdict is SUPERVISED: the APPROVAL CHECKPOINT section names the reviewer, the review criteria, and the turnaround. Before the project goes live, confirm with the named reviewer that they have access, understand their authority to block, and will review on the stated turnaround.

**Step 6 — Note the recertification date**

The artifact's AUTONOMY EXPIRES WHEN section lists the conditions that invalidate this verdict. Calendar the recertification date. When any condition is met, re-run the Gate.

---

## What PROJECT Can and Cannot Do

**Can do:**
- Human-initiated sessions
- Document, analysis, and report generation
- Multi-turn reasoning within a session
- Structured artifact output (plans, memos, reports, Slack-ready text)

**Cannot do:**
- Schedule or run unattended
- Access local filesystem
- Make external API calls (Salesforce, Stripe, Zendesk, Slack, etc.)
- Initiate actions without human input

If the workflow requires any of the "cannot do" capabilities, the selected architecture must use an implementation pattern that provides them, such as Cowork, a code agent, a low-code platform, or a service. Use the fallback note if the preferred tool is unavailable.
