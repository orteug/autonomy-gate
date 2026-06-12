# Golden Baseline: Scheduled Workflow With Project Fallback

## Input

I want the previous day's operations report ready automatically every morning, but I do not have Cowork, Codex automation, or another scheduled execution tool. I can paste stable exports and run it manually.

## Expected Decision

- Autonomy: `AUTONOMOUS`
- Surface: `PROJECT`
- Confidence: `MEDIUM`
- Rules: `RULE-03`, `RULE-06`
- Hard gates: `NONE`
- Artifact: `template-project-setup.md`
- Terminal action: Deliver the report in a human-initiated Project session; a human posts it.

## Required Behavior

- Name COWORK as the ideal scheduled surface and PROJECT as the available fallback.
- State that the fallback is not scheduled or unattended.
- Preserve the autonomy verdict while changing the execution model.

## Failure Conditions

- Claims PROJECT can run unattended.
- Changes the autonomy verdict solely because Cowork is unavailable.
- Omits the fallback limitations and upgrade path.
