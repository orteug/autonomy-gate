# Surface Guide: Claude Project

Use this when the Gate returns:

```text
AUTONOMOUS / PROJECT
SUPERVISED / PROJECT
```

---

## What Claude Project Is Good For

Claude Project is good for:

- human-initiated work
- project-specific instructions
- uploaded project knowledge
- document generation
- analysis
- review packets
- formatted outputs
- repeatable prompts

Official Claude support describes Projects as self-contained workspaces with their own chat histories and knowledge bases, where users can upload documents and define project instructions.

---

## What Claude Project Is Not

Claude Project is not a runtime engine by itself.

Do not assume it can:

- schedule itself
- run unattended
- access your local filesystem
- call APIs by default
- post to Slack by itself
- update CRM records by itself
- issue refunds
- change permissions

If the workflow needs those capabilities, route to Cowork or CODE_AGENT, or use a manual fallback.

---

## Setup: Deploying The Gate

1. Create a Claude Project.
2. Name it `The Autonomy Gate`.
3. Add project instruction:

```text
You are The Autonomy Gate. Follow identity.md.
```

4. Upload these 14 files:

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

5. Start a project chat.
6. Paste a workflow description.

---

## Setup: Deploying A Gate-Governed Workflow

Use this after the Gate returns a Project Setup Brief or Control Plan.

1. Create one Claude Project for the specific workflow.
2. Paste the artifact's custom instructions.
3. Upload knowledge files named in the artifact.
4. Run one test.
5. Save the first successful output.
6. Record recertification date.

---

## Test Before Use

Before operational use:

- [ ] Project instruction is set.
- [ ] Required files are uploaded.
- [ ] Test input produces expected output.
- [ ] Output contains no unresolved placeholders.
- [ ] Human knows what to paste.
- [ ] Human knows where to deliver output.
- [ ] Recertification trigger is recorded.

---

## Common Patterns

### Weekly KPI Report

Human exports data, pastes into Project, receives Slack-ready summary.

### Candidate Shortlist Prep

Human uploads resumes and rubric, Gate prepares review packet.

### Contract Clause Review

Human uploads contract and template, Gate produces comparison packet.

---

## Red Flags

Do not use Claude Project as the primary surface if the artifact says:

- run every morning automatically
- pull from Salesforce
- post to Slack
- issue refund
- update vendor record
- change access
- write to database

Those require a runtime surface or human manual step.

