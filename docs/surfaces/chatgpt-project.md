# Surface Guide: ChatGPT Project

Use this when you want to run The Autonomy Gate or a Gate-governed Project workflow in ChatGPT.

---

## What ChatGPT Project Is Good For

ChatGPT Projects support project files and project instructions. OpenAI's help documentation also describes project memory, tools, connected apps, and supported app links depending on plan and configuration.

Good uses:

- human-initiated Gate runs
- uploaded workflow context
- project-specific instructions
- analysis and document outputs
- artifact generation
- structured review packets

---

## What To Treat As Optional

Depending on plan and organization settings, ChatGPT Projects may support:

- web search
- Canvas
- connected apps
- Slack or Google Drive links
- project memory

Do not make the Gate depend on these.

The base Gate should still work as:

```text
files + instructions + human-pasted workflow
```

---

## Setup: Deploying The Gate

1. Create a new ChatGPT Project.
2. Name it `The Autonomy Gate`.
3. Add project instruction:

```text
You are The Autonomy Gate. Follow identity.md, rules.md, and operating-contract.md.
```

4. Confirm the Project supports at least 16 files. Verify current official plan limits before installation.

5. Upload the operator files flat in two batches because ChatGPT currently accepts at most 10 files per upload action.

Batch 1:

```text
identity.md
rules.md
examples.md
autonomy-criteria.md
risk-classification.md
surface-capability-matrix.md
precedents.md
operating-contract.md
operator-disposition.md
tool-selection-rules.md
```

Batch 2:

```text
template-automation-architecture.md
template-project-setup.md
template-control-plan.md
template-cowork-config.md
template-stabilization-plan.md
template-governance-memo.md
```

If your upload UI does not preserve folders, upload flat and keep filenames recognizable.

6. Paste a workflow description.

---

## Setup: Gate-Governed Workflow

Use this when the operator-selected execution architecture uses a human-triggered ChatGPT Project pattern.

1. Create a new Project for that workflow.
2. Paste the artifact's custom instructions.
3. Add knowledge files named in the artifact.
4. If SUPERVISED, document the reviewer and approval checkpoint.
5. Test with sample data.
6. Record expiration triggers.

---

## Capability Caution

If using connected apps, confirm:

- app access is authorized
- project can access the specific source
- output is still within the Gate's allowed actions
- terminal action does not exceed verdict

Connected app availability does not automatically increase the autonomy verdict.

If tool capability changes, re-run the Gate.

---

## Common Pattern

```text
PROJECT verdict = human starts, AI reasons, artifact is produced.
```

Do not silently turn a Project workflow into an unattended app workflow.
