# ChatGPT Project Setup — Autonomy Gate Adapter

The Autonomy Gate uses the same decision logic and packet contract in ChatGPT Projects and Claude Projects. Installation differs by platform: ChatGPT requires a supported file allowance, flat uploads, and multiple upload actions for the current 16-file package. Runtime parity must be established through the acceptance suite rather than assumed.

---

## Scenario 1 — Deploying the Gate (Decision Layer)

**Step 1 — Create a new ChatGPT Project**

In ChatGPT, create a new Project. Name it: `The Autonomy Gate`.

**Step 2 — Set the project instructions**

In Project Settings → Instructions, paste exactly:

```
You are The Autonomy Gate. Follow identity.md, rules.md, and operating-contract.md. When you produce an Execution Artifact, render it as styled HTML immediately after the Markdown output. Output the HTML in a fenced code block labeled html. Use the design system in artifact-rendered.html as the exact style reference.
```

**Step 3 — Upload the operator files**

Upload the runtime files from `autonomy-gate/` flat, plus the rendered artifact reference. Do not upload the whole folder or its public-facing guides. ChatGPT Projects do not preserve the repository folder hierarchy in project sources, so keep every filename recognizable.

The current package requires 17 project files (16 runtime + 1 style reference). File limits vary by plan and may change; verify the current official OpenAI documentation before installation. A plan that cannot hold all 17 files is unsupported unless a separately tested bundled edition is provided.

ChatGPT currently accepts no more than 10 files in one upload action. Upload the files in two batches as shown below.

Files to upload — batch 1:

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
```

Files to upload — batch 2:

```
template-automation-architecture.md
template-project-setup.md
template-control-plan.md
template-cowork-config.md
template-stabilization-plan.md
template-governance-memo.md
artifact-rendered.html
```

`artifact-rendered.html` is in `examples/` in the repository. It is the HTML style reference — it defines every color, font, spacing, and layout rule the Gate must reproduce. Do not upload `README.md`.

**Step 4 — Run**

Paste any workflow description. The required output contract is the same three-section sequence used on the Claude stack: Workflow Intake Snapshot → Autonomy Decision Packet → Execution Artifact, followed by a styled HTML rendering of the artifact in a fenced code block. Save the HTML block to a file to open it in a browser. Validate verdict and artifact parity using `testing/openai/TEST_MATRIX.md`; do not infer parity from format alone.

---

## Scenario 2 — Deploying a Gate-Governed Workflow

After the Gate issues a PROJECT verdict, apply the complete BUILD HANDOFF PACK generated inside the artifact:

1. Create a new ChatGPT Project for the specific workflow
2. Paste the generated project instructions verbatim
3. Upload the exact generated knowledge-file manifest
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

If the selected architecture requires code, integrations, deterministic enforcement, or repository changes, use the Codex adapter (`adapters/openai/codex-AGENTS.md`) or the named builder alternative from the handoff pack.

---

## Packet Portability

The Autonomy Decision Packet contract is platform-independent. A conforming ChatGPT or Claude run uses the same required fields, RULE-NN and GATE-NN identifiers, and artifact taxonomy. Model outputs may vary in prose and must pass the calibration suite before being described as behaviorally equivalent.

A packet produced in ChatGPT can be handed to Codex using `adapters/openai/codex-AGENTS.md`. A packet produced in Claude can be handed to Claude Code using `adapters/claude/claude-code-CLAUDE.md`. The packet format, defined in `adapters/decision-packet-contract.md`, does not change between stacks.
