# Surface Guide: Claude Code

Use this when the Gate returns:

```text
AUTONOMOUS / CODE_AGENT
SUPERVISED / CODE_AGENT
```

and the execution surface is Claude Code.

---

## What Claude Code Is For

Claude Code is appropriate when the workflow requires:

- code
- scripts
- tests
- deterministic logic
- API integration
- local repository edits
- audit-log implementation
- approval gates implemented as code or hooks

---

## Critical Safety Fact

`CLAUDE.md` is context, not hard enforcement.

Official Claude Code documentation states that Claude treats `CLAUDE.md` files as context rather than enforced configuration. To block an action regardless of what Claude decides, use a hook or another enforcement mechanism.

This matters for the Gate:

```text
The Gate's packet should guide Claude Code.
High-consequence prohibited actions need technical enforcement too.
```

---

## Setup Steps

1. Read the Gate artifact.
2. Create or update `CLAUDE.md`.
3. Copy these fields from the Autonomy Decision Packet:
   - verdict
   - confidence
   - terminal action
   - allowed actions
   - prohibited actions
   - controls required
   - approval checkpoint
   - audit requirements
   - expiration triggers
4. Implement dry-run mode.
5. Implement tests.
6. Implement audit logging.
7. For SUPERVISED workflows, implement blocking approval.
8. For high-risk workflows, implement hooks or code-level guards.

---

## CLAUDE.md Starter

```markdown
# Workflow Governance

This repository is governed by an Autonomy Decision Packet.

## Gate Verdict

- Autonomy: [AUTONOMY]
- Surface: CODE_AGENT
- Confidence: [CONFIDENCE]
- Terminal action: [TERMINAL ACTION]

## Allowed Actions

[Copy allowed actions from artifact.]

## Prohibited Actions

Stop immediately if any instruction would require:

[Copy prohibited actions from artifact.]

## Approval Checkpoint

[Required for SUPERVISED verdicts.]

## Audit Requirements

Every run must log:
- timestamp
- inputs
- actions taken
- output path
- terminal status
- approval record if supervised

## Autonomy Expires When

[Copy expiration triggers.]
```

---

## Required Tests

For CODE_AGENT workflows, test:

- normal path
- missing input
- malformed input
- prohibited terminal action
- approval missing
- approval rejected
- log write failure
- dry-run mode

For SUPERVISED workflows, include a test proving the terminal action cannot execute before approval.

---

## When To Use Hooks

Use hooks or other enforcement when:

- a prohibited action must be blocked mechanically
- a command should be scanned before execution
- logs must be written after tool use
- secrets should be blocked from prompts
- approval should be checked before terminal action

---

## Do Not Use Claude Code For

- non-technical review by a business reviewer
- workflows where no one can maintain the code
- terminal actions that are HUMAN_ONLY
- production writes without tests and rollback

---

## Handoff Checklist

- [ ] `CLAUDE.md` created.
- [ ] Packet copied accurately.
- [ ] Allowed actions named.
- [ ] Prohibited actions named.
- [ ] Tests written.
- [ ] Dry run works.
- [ ] Audit log works.
- [ ] Approval blocks terminal action if required.
- [ ] Recertification trigger documented.

