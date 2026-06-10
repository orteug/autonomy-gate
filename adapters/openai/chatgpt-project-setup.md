# ChatGPT Project Setup — Autonomy Gate Adapter

The Autonomy Gate is platform-agnostic. The same operator folder runs in a ChatGPT Project using the same setup steps. The packet produced is identical. The verdict, justification, and artifact are consumed by Codex and human reviewers the same way they are consumed on the Claude stack.

---

## Scenario 1 — Deploying the Gate (Decision Layer)

**Step 1 — Create a new ChatGPT Project**

In ChatGPT, create a new Project. Name it: `The Autonomy Gate`.

**Step 2 — Set the project instructions**

In Project Settings → Instructions, paste exactly:

```
You are The Autonomy Gate. Follow identity.md and rules.md.
```

**Step 3 — Upload the operator files**

Upload the contents of the `autonomy-gate/` folder flat. ChatGPT Projects do not support folder navigation at file selection — upload all files to the same project knowledge base.

Files to upload:

```
identity.md
rules.md
examples.md
autonomy-criteria.md
surface-capability-matrix.md
risk-classification.md
template-automation-architecture.md
template-project-setup.md
template-cowork-config.md
template-control-plan.md
template-stabilization-plan.md
template-governance-memo.md
```

Do not upload `README.md`.

**Step 4 — Run**

Paste any workflow description. The output is the same three-section sequence as the Claude stack: Workflow Intake Snapshot → Autonomy Decision Packet → Execution Artifact.

---

## Scenario 2 — Deploying a Gate-Governed Workflow

After the Gate issues a PROJECT verdict (AUTONOMOUS / PROJECT or SUPERVISED / PROJECT), use the artifact to set up a governed ChatGPT Project:

1. Create a new ChatGPT Project for the specific workflow
2. Paste the artifact's custom instructions block as the project instructions
3. Upload the knowledge files named in the artifact
4. Configure the approval checkpoint if the verdict is SUPERVISED (see Control Plan)
5. Note the AUTONOMY EXPIRES WHEN conditions and calendar the recertification date

---

## Platform Capability Notes

ChatGPT Projects support:
- Project instructions (equivalent to Claude's custom instructions)
- Uploaded files in the project knowledge base
- Project memory across chats within the project
- Tools: web search, Canvas (plan-dependent), connected apps (plan-dependent)

ChatGPT Projects do not support (in standard configuration):
- Scheduled or unattended execution
- Local filesystem access
- External API calls without a connected app

If the workflow requires capabilities beyond document reasoning and analysis, the verdict will route to CODE_AGENT. Use the Codex adapter (`adapters/openai/codex-AGENTS.md`) for those workflows.

---

## Packet Portability

The Autonomy Decision Packet produced by a ChatGPT Project Gate run is identical in structure to one produced by a Claude Project Gate run. Both reference the same RULE-NN and GATE-NN identifiers. Both produce the same artifact types.

A packet produced in ChatGPT can be handed to Codex using `adapters/openai/codex-AGENTS.md`. A packet produced in Claude can be handed to Claude Code using `adapters/claude/claude-code-CLAUDE.md`. The packet format, defined in `adapters/decision-packet-contract.md`, does not change between stacks.
