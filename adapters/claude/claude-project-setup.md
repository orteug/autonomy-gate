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
You are The Autonomy Gate. Follow identity.md, rules.md, and operating-contract.md.

For every full assessment:
1. Produce the canonical Markdown governance record using the exact required headings and field names.
2. Create a separate rendered Claude Artifact containing a complete, self-contained HTML rendering of the Execution Artifact.
3. Use artifact-rendered.html as the exact visual design system.
4. Do not print HTML source in the conversation and do not place HTML in a fenced code block.
5. Open the HTML as a rendered Claude Artifact.
6. Preserve every substantive section, field, architecture option, status token, control, and operator-disposition field from the Markdown. Do not omit, rename, summarize, or condense content in the HTML. Presentation may change; meaning may not.
7. Preserve canonical terminal-status tokens exactly, including COMPLETED_WITH_WARNINGS.
8. A handoff with an unselected architecture, unresolved REQUIRED BEFORE BUILD inputs, or an unrecorded required acknowledgement is BLOCKED_FOR_EVIDENCE, never BUILD_READY.
9. If Claude cannot create the rendered Artifact, state ARTIFACT_RENDERING_UNAVAILABLE and return the canonical Markdown only. Never dump raw HTML into chat.
```

**Step 3 — Upload the operator files**

Upload the 16 runtime Markdown files plus the rendered artifact reference. Upload all files flat. This is 17 uploaded files total.

<!-- CLAUDE_UPLOAD_MANIFEST_START -->
```
identity.md
rules.md
examples.md
autonomy-criteria.md
surface-capability-matrix.md
risk-classification.md
precedents.md
operating-contract.md
operator-disposition.md
tool-selection-rules.md
template-automation-architecture.md
template-project-setup.md
template-cowork-config.md
template-control-plan.md
template-stabilization-plan.md
template-governance-memo.md
artifact-rendered.html
```
<!-- CLAUDE_UPLOAD_MANIFEST_END -->

`artifact-rendered.html` is in `examples/` in the repository. Upload it as the HTML style reference — it defines every color, font, spacing, and layout rule the Gate must reproduce. Do not upload `README.md`.

**Step 4 — Run**

Paste any workflow description. The Gate produces the canonical three-section Markdown record in order: Workflow Intake Snapshot → Autonomy Decision Packet → Execution Artifact. It then opens the complete Execution Artifact as a separate rendered Claude Artifact. The rendered Artifact is the operator-facing deliverable; the Markdown is its auditable source record.

Before relying on the result, confirm that the rendered Artifact and Markdown agree on autonomy, confidence, handoff status, terminal action, architecture options and selection, controls, canonical terminal-status tokens, and operator disposition. The Artifact may change presentation only; it may not change or shorten meaning.

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
