# Artifact Guide

The Gate always produces an artifact.

The artifact is the thing you act on.

---

## Artifact Map

| Verdict | Artifact |
|---|---|
| `AUTONOMOUS / PROJECT` | Project Setup Brief |
| `AUTONOMOUS / COWORK` | Cowork Project Config |
| `AUTONOMOUS / CODE_AGENT` | Automation Architecture |
| `SUPERVISED / any surface` | Control Plan |
| `SOP_FIRST / NO_AI` | Stabilization Plan |
| `HUMAN_ONLY / NO_AI` | Governance Memo |

---

## Project Setup Brief

### What It Is

A setup document for a human-initiated Project workflow.

### Who Uses It

- operations lead
- founder
- team member running the recurring workflow

### What It Contains

- purpose
- run cadence
- required knowledge files
- custom instructions
- output format
- expected outcomes
- autonomy expiration triggers

### What Done Looks Like

A person can create a Claude Project or ChatGPT Project, paste the instructions, upload the files, and run the workflow without more explanation.

### Common Failure

The brief implies live integrations even though the surface is only a Project.

Correct phrasing:

```text
User pastes exports. Operator produces Slack-ready text.
```

Incorrect phrasing:

```text
Operator pulls from Salesforce and posts to Slack.
```

---

## Automation Architecture

### What It Is

A technical specification for a deterministic automation or code-agent workflow.

### Who Uses It

- developer
- automation engineer
- Claude Code
- Codex

### What It Contains

- workflow scope
- input sources
- output destinations
- allowed actions
- prohibited actions
- terminal action
- implementation sequence
- test requirements
- audit log requirements
- rollback or dry-run plan

### What Done Looks Like

A builder can implement the workflow without guessing:

- what to read
- what to write
- what not to touch
- what must be logged
- what requires approval

### Common Failure

Treating a natural-language architecture as enforcement.

For code-agent workflows, high-consequence controls must become code, tests, hooks, or permission boundaries.

---

## Cowork Project Config

### What It Is

A configuration document for a scheduled or folder-based workflow surface.

### Who Uses It

- operator
- operations lead
- AI ops owner

### What It Contains

- folder structure
- schedule
- trigger condition
- input folder
- output folder
- log folder
- terminal statuses
- allowed actions
- prohibited actions
- fallback if Cowork is unavailable

### What Done Looks Like

Every run:

1. receives input in the expected place
2. produces output in the expected place
3. emits one terminal status
4. writes a log
5. respects prohibited actions

### Common Failure

No terminal status.

If no terminal status is emitted, the run is not observable.

---

## Control Plan

### What It Is

A checkpoint design for a supervised workflow.

### Who Uses It

- reviewer
- process owner
- operator
- implementation team

### What It Contains

- reviewer
- review criteria
- approval condition
- rejection condition
- turnaround time
- prohibited actions before approval
- audit requirements
- expected outcomes
- expiration triggers

### What Done Looks Like

The workflow cannot execute its terminal action until a real reviewer approves.

### Common Failure

Reviewer is vague.

Bad:

```text
Reviewer: manager
```

Better:

```text
Reviewer: Support Lead on duty in #support-ops, must approve before refund issuance.
```

---

## Stabilization Plan

### What It Is

A process documentation plan for workflows that are not ready for AI authority.

### Who Uses It

- process owner
- operations lead
- team manager

### What It Contains

- why automation is premature
- missing process evidence
- documentation checklist
- exception mapping
- failure-path requirements
- baseline measurement requirements
- earliest re-evaluation criteria

### What Done Looks Like

The team can explain:

- standard path
- exceptions
- failure handling
- owner
- metrics
- when to re-run the Gate

### Common Failure

Treating SOP_FIRST as "blocked."

SOP_FIRST is work. It tells you what must be documented to unlock safer automation.

---

## Governance Memo

### What It Is

A decision memo explaining why the terminal action stays human-owned.

### Who Uses It

- accountable executive
- process owner
- finance
- legal
- compliance
- security
- operations lead

### What It Contains

- gate condition
- terminal action
- specific risk
- why AI cannot own it
- human review process
- what would change the verdict
- expected human-process outcomes
- expiration triggers

### What Done Looks Like

Someone can take the memo to a meeting and defend why the workflow is not delegated to AI.

### Common Failure

Assuming HUMAN_ONLY means AI cannot help at all.

Correct:

```text
AI cannot own the terminal action. Preparation steps may be split and re-submitted.
```

---

## Artifact Quality Checklist

Before using an artifact:

- [ ] It names the workflow.
- [ ] It matches the verdict.
- [ ] It names the terminal action.
- [ ] It names allowed actions.
- [ ] It names prohibited actions where relevant.
- [ ] It names controls required.
- [ ] It names expected outcomes.
- [ ] It names expiration triggers.
- [ ] It has no unresolved placeholder brackets.
- [ ] It can be read without the full assessment.

