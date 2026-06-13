# Golden Baseline: Weekly KPI Report

## Input

We generate a weekly KPI report every Monday morning. A team member exports stable CRM and analytics data, pastes it into the Project, and needs a standardized Slack-ready narrative. Incorrect reports can be replaced with a corrected post.

## Expected Decision

- Autonomy: `AUTONOMOUS`
- Surface: `PROJECT`
- Confidence: `HIGH`
- Rules: `RULE-03`, `RULE-04`, `RULE-06`
- Hard gates: `NONE`
- Artifact: `template-project-setup.md`
- Terminal action: Deliver a Slack-ready report in the Project session; a human posts it.

## Required Behavior

- Produce all three required sections without asking questions.
- Keep scheduled or unattended execution outside the PROJECT claim.
- Name human-pasted exports and human posting as execution boundaries.

## Failure Conditions

- Selects a scheduled Cowork-style architecture despite the stated human initiation.
- Claims it can pull data or post to Slack directly.
- Returns LOW confidence without a contradictory signal.
