# Calibration Log — The Autonomy Gate
## Context Layer 4 · Assessment Outcome Tracker

> Updated after every completed assessment. This is how the Gate improves.
> Note: The Gate does not maintain cross-session memory for operators (by design).
> This log is for system calibration — identifying systematic biases in verdict distribution,
> hard gate firing rates, and evidence gap patterns — not for tracking individual operators.

---

## Log Format

```
## [YYYY-MM-DD] [Workflow Name or type] — [Verdict: AUT-1/2/3/4]
- Autonomy level: [AUT-1 AUTONOMOUS / AUT-2 SUPERVISED / AUT-3 SOP_FIRST / AUT-4 HUMAN_ONLY]
- Confidence: [HIGH / MEDIUM / LOW]
- Hard gates applied: [GATE-1 / GATE-2 / GATE-3 / none]
- Evidence gaps at assessment: [list or "none"]
- Adversarial flag triggered: [Y/N]
- Guardrail triggered: [Y/N — which trigger if Y]
- Handoff status: [BUILD_READY / BLOCKED_FOR_EVIDENCE / NOT_APPLICABLE]
- Disposition recorded: [APPROVE_FOR_BUILD / HOLD / pending / not reported]
- Assessment note: [one sentence if non-standard routing, otherwise "standard assessment"]
```

---

## Assessments

*No assessments logged yet. First entry will appear here.*

---

## Calibration Signals

*Patterns that emerge across assessments — verdict distribution, gap frequency, hard gate firing rate.*

Example calibration questions to answer over time:
- What % of assessments result in HUMAN_ONLY? Is the Gate over-applying GATE-2?
- What are the most common evidence gaps? Should intake prompt address them?
- Are adversarial flags correlated with lower-confidence assessments?
