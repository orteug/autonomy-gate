# Surface Guide: Codex

Use this when the Gate returns:

```text
AUTONOMOUS / CODE_AGENT
SUPERVISED / CODE_AGENT
```

and the execution surface is Codex.

---

## What Codex Is For

Codex is appropriate for:

- repository work
- scripts
- tests
- code review
- deterministic automation
- API integration
- implementation of approval gates
- implementation of audit logs

---

## Instruction Surface

Codex reads `AGENTS.md` files before doing work. Official Codex documentation describes layered global and project guidance, where files closer to the current working directory appear later and can override earlier guidance.

Use `AGENTS.md` to load the Gate's packet into Codex context.

Important:

```text
AGENTS.md guides the agent.
Sandbox, approvals, hooks, and code-level checks enforce behavior.
```

---

## Setup Steps

1. Read the Gate artifact.
2. Add or update `AGENTS.md`.
3. Copy the Autonomy Decision Packet fields.
4. Define allowed actions.
5. Define prohibited actions.
6. Define test requirements.
7. Define audit log format.
8. Configure sandbox and approval policy appropriate to the workflow.
9. Add hooks or code checks for high-consequence blocked actions.

---

## AGENTS.md Starter

```markdown
# AGENTS.md

This repository is governed by The Autonomy Gate.

## Gate Verdict

- Autonomy: [AUTONOMY]
- Surface: CODE_AGENT
- Confidence: [CONFIDENCE]
- Terminal action: [TERMINAL ACTION]

## Allowed Actions

[Copy allowed actions from artifact.]

## Prohibited Actions

Do not execute:

[Copy prohibited actions from artifact.]

If a user asks for a prohibited action, stop and report BLOCKED.

## Approval Checkpoint

[Required for SUPERVISED verdicts.]

## Test Requirements

[Copy required tests from artifact.]

## Audit Requirements

Every run must emit one terminal status and write a log entry.

## Autonomy Expires When

[Copy expiration triggers.]
```

---

## Sandbox And Approval Guidance

Codex uses sandboxing and approval policies to control what the agent can technically do and when it must ask for approval.

For Gate-governed workflows:

- keep network access off unless required
- use read-only credentials by default
- require approval for writes outside scope
- require approval for external side effects
- use hooks or tests to block prohibited actions

---

## SUPERVISED / CODE_AGENT

For supervised workflows:

1. Stage output.
2. Halt before terminal action.
3. Require explicit approval.
4. Record approval identity and timestamp.
5. Execute only after approval.
6. Emit `BLOCKED` when approval is missing.

---

## Required Tests

Before live use:

- [ ] normal path passes
- [ ] missing input blocks
- [ ] malformed input blocks
- [ ] prohibited action blocks
- [ ] terminal action cannot run before approval
- [ ] logs are written
- [ ] dry-run mode produces no side effects
- [ ] expiration trigger pauses workflow

---

## Hooks

Codex hooks can run around tool calls and lifecycle events. Use hooks when a workflow needs mechanical checks around tool use, approvals, logging, or policy boundaries.

Examples:

- block shell commands that call prohibited endpoints
- scan prompts for secrets
- write audit log after tool use
- validate approval file before terminal action

---

## Handoff Checklist

- [ ] `AGENTS.md` created.
- [ ] Packet copied accurately.
- [ ] Sandbox policy reviewed.
- [ ] Approval policy reviewed.
- [ ] Hooks added if needed.
- [ ] Tests pass.
- [ ] Dry run passes.
- [ ] Audit log verified.
- [ ] Recertification date recorded.

