# The Autonomy Gate — Operator Guide

This guide is for operations leaders, fractional operators, and founders' AI ops leads who use the Gate to make automation decisions. It is written for the human using the Gate, not the AI running it. The technical rules are in `rules.md`. The judge-facing prompts are in `JUDGE_GUIDE.md`. This is the practical field guide.

---

## When to Use It

Use the Gate whenever someone asks: "Can we automate this?" — or whenever you are evaluating a workflow for AI delegation.

The Gate is for decision-making, not implementation. It tells you whether to automate, at what level of autonomy, with what controls, and on which surface. It does not build the automation.

**Specific triggers:**
- A team member pitches a workflow for automation
- You are auditing a set of existing automations to assess their governance
- You are onboarding a new tool and evaluating which workflows it can run autonomously
- Someone wants to expand the scope of an existing automation
- An incident occurred and you need to reassess autonomy for an affected workflow
- You are preparing for a compliance review and need documentation of AI autonomy decisions

**When not to use it:**
- You have already decided to automate and just need implementation help — skip the Gate, go to your tooling
- The workflow is a personal assistant task (write me a summary, draft a response) — the Gate is for organizational business workflows with organizational consequences, not personal productivity tasks

---

## How to Describe a Workflow

The Gate accepts any format — a paragraph, a Slack message, a process doc excerpt, a tool name plus use case. You do not need to structure your input. The Gate normalizes it.

The richer your description, the higher the confidence. The four things that matter most:
1. **What does it do?** — The sequence of steps, not just the goal
2. **What happens if it's wrong?** — The worst realistic outcome, not the worst possible outcome
3. **Can it be undone?** — Specifically and quickly, or with difficulty and delay?
4. **What are the exceptions?** — Not "sometimes things are different" — what are the different cases?

If you do not know the answers to these questions, the Gate will tell you — and name them as evidence gaps. That information is useful: it tells you what you need to document before automation is possible.

---

## Reading the Three Sections

**Section 1 — Workflow Intake Snapshot**
This is the Gate's normalized representation of what you described. Read it before looking at the verdict. If the snapshot misunderstood your workflow, the verdict is based on the wrong workflow — fix the snapshot by clarifying your input and rerunning.

Key field to check: **Terminal action.** This is the last thing the workflow executes. The Gate's verdict is based on the terminal action, not the workflow label. If the terminal action in the snapshot is wrong, the verdict may be wrong.

**Section 2 — Autonomy Decision Packet**
This is the verdict. Two axes: autonomy level and surface. Plus confidence and justification.

- **Autonomy level:** What the AI is allowed to do. AUTONOMOUS means execute without a checkpoint. SUPERVISED means prepare and wait. SOP_FIRST means the process needs documentation work first. HUMAN_ONLY means this decision cannot be delegated.
- **Surface:** Where it runs. PROJECT means you open a Claude Project and run it manually. COWORK means it can run on a schedule without you. CODE_AGENT means a deterministic script or agent. NO_AI means no surface — human process only.
- **Confidence:** How complete the evidence was. HIGH means all required fields were populated and the adversarial check passed. MEDIUM means minor gaps. LOW means significant gaps — the verdict is conservative by design.
- **Justification:** Named rule and gate identifiers. If you want to understand why the verdict is what it is, these are the specific mechanisms to look up in `rules.md`.

**Section 3 — Artifact**
This is what you act on. The artifact type matches the verdict:
- AUTONOMOUS → Architecture or Setup Brief (how to build the automation)
- SUPERVISED → Control Plan (how to add the checkpoint)
- SOP_FIRST → Stabilization Plan (what to document before returning)
- HUMAN_ONLY → Governance Memo (why it stays human and what that process looks like)

The artifact is a document. You can share it with your team, include it in a project plan, or present it in a review without needing to explain the Gate's logic.

---

## Interpreting Each Verdict

### AUTONOMOUS
The workflow can run without a human approval checkpoint on each execution. This does not mean unsupervised forever. Every AUTONOMOUS verdict includes an AUTONOMY EXPIRES WHEN section — review it and schedule the recertification date.

**What to do with it:**
- Review the artifact's CONTROLS section — these must be implemented before the automation goes live
- Confirm the audit trail requirement — the workflow must log what it did, even if no human reviews each run
- Note the recommended surface (PROJECT, COWORK, or CODE_AGENT) and confirm it matches what you have access to
- If the surface doesn't match, read the fallback note in the artifact

**Common mistake:** Treating AUTONOMOUS as permanent. It is not. An AUTONOMOUS verdict issued today expires if the workflow changes, the model changes, or an incident occurs. The AUTONOMY EXPIRES WHEN section names the conditions.

### SUPERVISED
The workflow runs with AI doing the preparation work and a human approving before execution. The approval checkpoint is part of the workflow design, not a workaround.

**What to do with it:**
- Identify the reviewer named in the Control Plan. If the reviewer field says "must be designated" — that is your first action. The workflow cannot be deployed without a named reviewer.
- Read the APPROVAL CHECKPOINT section: Reviewer, Reviews, Approves when, Rejects when, Turnaround. Confirm all four fields are accurate for your organization.
- Confirm the reviewer has the authority to block execution — not just to note concerns, but to stop it.
- Set up the audit trail before deployment. The audit log requirement in a SUPERVISED workflow is the mechanism that makes the checkpoint real.

**Common mistake:** Naming a reviewer who does not have time or authority to actually block execution. This is "Human-in-the-Loop Theater" (FAIL-6) — the checkpoint exists on paper but not in practice. If the reviewer cannot realistically review on the stated turnaround, either reduce the volume or designate a second reviewer.

### SOP_FIRST
The process is too undocumented or too variable to assign AI authority. This is not a failure verdict — it is the correct automation decision for most workflows in their current state.

**What to do with it:**
- Read the STABILIZATION CHECKLIST in the artifact. These are the specific items that must be completed before the Gate can be re-run.
- Assign a process owner who will lead the documentation work. Unowned stabilization checklists do not get done.
- Do not attempt to automate the "standard path" while leaving exceptions undocumented. This creates an automation that handles 80% of cases and silently fails the 20% that need the most care.
- Set a re-evaluation date. The artifact names an EARLIEST RE-EVALUATION milestone. Put it on your calendar.

**Common mistake:** Treating SOP_FIRST as "the automation is blocked." The documentation work is the automation decision — doing it unlocks a better automation, not just a permitted one.

### HUMAN_ONLY
This workflow cannot be delegated to AI. The terminal action triggered a hard gate condition (GATE-2 or GATE-3) that is structural — no amount of controls, checkpoints, or rule clarity changes the verdict.

**What to do with it:**
- Read the WHY THIS CANNOT BE DELEGATED section. It names the specific gate condition and the specific risk. This is your explanation when someone asks why AI can't handle it.
- Read WHAT WOULD CHANGE THIS VERDICT. Most HUMAN_ONLY workflows have a scope decomposition that enables AI assistance in the preparation phase — the terminal action stays human, but the work leading up to it can often be SUPERVISED or AUTONOMOUS. This section names what that split looks like.
- Read the HUMAN REVIEW PROCESS section. If the current human process is not documented, this is the moment to document it — the governance memo gives you the structure.

**Common mistake:** Treating HUMAN_ONLY as "AI can't touch this." AI can often assist with the preparation phase. The terminal action — the specific step that triggers the gate — is what must stay human. The preparation steps leading to it are often candidates for re-submission as a separate, scoped workflow.

---

## Acting on a LOW Confidence Verdict

A LOW confidence verdict means the Gate did not have enough information to issue a confident assessment. The verdict is still valid — it is conservative by design. You have two options:

**Option 1 — Act on the LOW confidence verdict**
The conservative route is already applied. If you are in a time-constrained situation and cannot gather more information, the LOW confidence artifact is usable. The Information Gaps section names exactly what is missing. You can implement with those gaps acknowledged.

**Option 2 — Gather the missing information and re-run**
Re-read the Evidence Gaps in the Autonomy Decision Packet. These are specific missing fields — not vague requests for more detail. Gather that specific information, then resubmit the workflow description with the gaps filled. The new run will produce a higher confidence verdict if the gaps are resolved.

**What not to do:** Treat LOW confidence as an invitation to argue with the verdict. The Gate did not downgrade confidence to be conservative for no reason — it downgraded because specific required fields could not be populated. Fill the fields.

---

## Scope Splitting

Some workflow descriptions contain multiple terminal actions with different risk profiles. The Gate will decompose these and issue separate verdicts per phase. Do not merge them back together.

Example: A workflow that "compiles data from five systems, formats it, and submits the regulatory filing" produces two verdicts — SUPERVISED for the compilation/formatting phase and HUMAN_ONLY for the submission step. You cannot use the SUPERVISED verdict to cover the submission.

**What to do with a split verdict:**
- Treat each phase as a separate workflow for implementation purposes
- The higher-restriction verdict governs the terminal action
- The preparation phase verdict governs the preparation steps only — it does not authorize the terminal action

---

## Recertification

Every artifact ends with AUTONOMY EXPIRES WHEN. This section names the conditions under which the current verdict is no longer valid.

**Minimum recertification triggers:**
- The workflow changes (new steps, new systems, new data)
- The AI tool or model changes (upgrade, migration, new platform)
- A policy or compliance context changes
- An incident occurs — any output that caused unintended harm or required correction
- The recertification date arrives

When any of these conditions occur, re-submit the workflow to the Gate. The recertification is not a formality. It is the mechanism that keeps the governance document accurate.

**For SUPERVISED verdicts:** The reviewer role vacancy condition is also a recertification trigger. If the named reviewer leaves the role, the workflow must be paused until a new reviewer is designated and re-submitted to the Gate.

---

## Building a Governance Stack

If you are running the Gate across a set of workflows — an audit, an operations review, a compliance preparation — this is the recommended approach:

1. Run each workflow through the Gate
2. Collect the Autonomy Decision Packets into a registry — one row per workflow: name, verdict, surface, confidence, recertification date
3. Group HUMAN_ONLY and LOW confidence verdicts for priority attention
4. SOP_FIRST workflows form a documentation backlog — assign owners and milestones
5. SUPERVISED workflows form a checkpoint registry — confirm reviewer assignments and turnaround SLAs
6. AUTONOMOUS workflows form an audit calendar — recertification dates tracked centrally
7. Review the registry quarterly; re-run any workflow whose recertification date has passed

The Gate produces the per-workflow artifacts. The registry is the governance view across all of them.

---

## Common Questions

**"Can I override a HUMAN_ONLY verdict if we add more controls?"**
No. GATE-2 and GATE-3 verdicts are structural. They cannot be overridden by operator context, user instruction, or additional controls. What can change: the scope of the workflow. If you decompose the workflow so that the terminal action is no longer the one that triggered the gate, re-submit the scoped version.

**"The Gate gave me SUPERVISED but I know this process is safe. Can I just run it as AUTONOMOUS?"**
The Gate assessed the process you described, not the process you know in your head. If the process is safer than described, re-submit with more detail — specifically: exception handling, failure consequence, and reversibility. If the Gate still returns SUPERVISED after a fuller description, the checkpoint is warranted.

**"What do I do with the artifact from a SOP_FIRST verdict? There's nothing to implement."**
The Stabilization Plan is an implementation document — it is just for process documentation, not AI implementation. The checklist in it is a project plan. Assign it an owner, schedule it, and run the Gate again when the checklist is complete.

**"The recommended surface (Cowork) is not available. Does that change the verdict?"**
No. Surface availability does not change the autonomy verdict. The artifact will include a fallback note with the nearest viable alternative surface and specific adjustments. Use the fallback. If the primary surface becomes available, re-submit for a surface upgrade — the autonomy verdict will likely remain the same, but the artifact format will change.

**"How do I know when to re-run the Gate on an existing automation?"**
Check its AUTONOMY EXPIRES WHEN section. If any condition in that list has been met — workflow change, model change, policy change, incident, error rate threshold crossed, recertification date passed — re-run the Gate. If you cannot find the AUTONOMY EXPIRES WHEN section, the automation has not been governed by the Gate and should be re-submitted.

---

## Taking the Packet to Execution Surfaces

The Gate is the decision layer. The Autonomy Decision Packet it produces is a portable work order — the same packet is consumed differently depending on which surface runs the workflow.

**The principle:** Do not send raw intent to an execution surface. Send the governed packet. The packet contains the terminal action, allowed actions, prohibited actions, approval checkpoints, audit requirements, and expiration conditions. An execution surface that receives this runs better work than one that receives a plain description.

---

### AUTONOMOUS / PROJECT (Claude Project or ChatGPT Project)

The artifact is the setup document. Take the Project Setup Brief and:
1. Create a new Claude Project (or ChatGPT Project)
2. Paste the artifact's custom instructions as the project's system prompt
3. Upload the knowledge files named in the artifact
4. The workflow runs on human-initiated cadence — no scheduling needed

**What the surface can do:** Human-initiated sessions, document and analysis outputs, multi-turn context within a session. **What it cannot do:** External API calls, local file access, scheduled or unattended execution. If the workflow requires those, re-submit for a COWORK or CODE_AGENT surface upgrade.

---

### AUTONOMOUS / COWORK (Claude Cowork)

The artifact is the Cowork Project Config. Take it and:
1. Create the folder structure named in the artifact (`/inputs`, `/outputs`, `/logs`)
2. Set the Cowork project instructions from the artifact's custom instructions block
3. Configure the run schedule from the artifact's cadence field
4. Confirm the terminal status schema — the artifact names the valid terminal statuses the Cowork run must emit

**What the surface can do:** Scheduled unattended execution, local file read/write, multi-step pipelines, structured folder I/O. The fallback note in the artifact tells you what to adjust if Cowork is unavailable.

---

### AUTONOMOUS or SUPERVISED / CODE_AGENT (Claude Code or Codex)

The artifact is the Automation Architecture or Control Plan. Use it to govern the agent:

**For Claude Code:** Add a `CLAUDE.md` to your repo that imports or summarizes the Autonomy Decision Packet. Include the prohibited actions list and the approval checkpoint requirement verbatim. The `CLAUDE.md` is context for Claude Code — it shapes behavior but is not hard enforcement. For true blocking, implement approval gates as code.

**For Codex:** Add an `AGENTS.md` to your repo with the same content. Name the allowed actions, prohibited actions, and required audit log format. Codex receives governed work orders, not raw intent.

**For SUPERVISED verdicts:** The approval checkpoint in the Control Plan must be implemented as a blocking step before the terminal action executes. The approval checkpoint is not a review of the output after the fact — it must block execution.

---

### SUPERVISED or AUTONOMOUS / ChatGPT Project (OpenAI)

The Gate's files are portable. Upload the same folder to a ChatGPT Project and set the project instructions to: `You are The Autonomy Gate. Follow identity.md and rules.md.`

The output — Workflow Intake Snapshot, Autonomy Decision Packet, artifact — is identical. The packet produced by ChatGPT Projects is consumed by Codex the same way the Claude-produced packet is consumed by Claude Code.

---

### HUMAN_ONLY / NO_AI

Do not implement this workflow on any execution surface. The Governance Memo is the implementation. Distribute it to the named approvers, use the Human Review Process section as the SOPs for the manual workflow, and schedule the recertification review named in AUTONOMY EXPIRES WHEN.

The preparation steps described in WHAT WOULD CHANGE THIS VERDICT are candidates for re-submission as a separate, scoped workflow with the terminal action excluded.
