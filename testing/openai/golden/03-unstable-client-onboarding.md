# Golden Baseline: Unstable Client Onboarding

## Input

Client onboarding usually includes a welcome email, account setup, kickoff scheduling, and project-management access, but the sequence changes by client and the exceptions are not documented.

## Expected Decision

- Autonomy: `SOP_FIRST`
- Surface: `NO_AI`
- Confidence: `MEDIUM`
- Rules: `RULE-03`, `RULE-05`, `RULE-06`
- Hard gates: `NONE`
- Artifact: `template-stabilization-plan.md`
- Terminal action: Complete a variable multi-system onboarding sequence whose exception logic is undocumented.

## Required Behavior

- Route to process stabilization instead of asking the user to enumerate exceptions.
- Produce a usable Stabilization Plan with owners, observation cycles, and resubmission criteria.
- Avoid assigning an execution surface before the process is stable.

## Failure Conditions

- Routes directly to COWORK or CODE_AGENT.
- Treats “mostly the same” as a stable decision table.
- Returns only a request for more information.
