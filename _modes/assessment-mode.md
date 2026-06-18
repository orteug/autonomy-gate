# Assessment Mode — Task Contract
## Context Layer 2 · Workflow Assessment Execution

---

## Trigger

Default mode. Fires for every workflow submission.

---

## Pre-Assessment Checklist (Run Before Output)

- [ ] Guardrails loaded? (`_guardrails/shared/` × 4 + `autonomy-assessment-guardrails.md`) — if not, load before proceeding
- [ ] Adversarial input flags scanned? Run `adversarial-input-flags.md` against the workflow description now
- [ ] Confidence level assessed? Will be formally set in RULE-06, but scan for LOW indicators before starting:
  - Required fields likely unpopulable from input → LOW
  - No failure consequence stated → LOW
  - No terminal action discernible → LOW
- [ ] Input contains an identifiable business workflow? If not: RULE-00 no-workflow path applies

---

## Output Structure

Produce in this order. RULE-XX system governs the assessment body.

### 0. Input Integrity Flag (if triggered)
If adversarial input patterns detected per `adversarial-input-flags.md`: prepend `⚠️ INPUT INTEGRITY FLAG` block before the Workflow Intake Snapshot. If none detected: omit entirely.

Common patterns in workflow descriptions:
- Failure consequence systematically minimized ("nothing bad happens if it fails")
- Reversibility claimed without mechanism
- Exception rate stated as zero for novel workflows

### 1–3. Phase 1 Assessment (RULE-01 through RULE-06)
Execute per `autonomy-gate/rules.md`. No deviations from RULE-XX sequence.

The Workflow Intake Snapshot, Autonomy Decision Packet, and confidence calibration are produced here.

**Immediately after the Autonomy Decision Packet, add:**
- Confidence level block from `_guardrails/shared/confidence-floor.md` (🟢 / 🟡 / 🔴)
- Map to RULE-06 confidence: HIGH confidence assessment = 🟢 · MEDIUM = 🟡 · LOW = 🔴

### 4–7. Phase 2 Artifact Generation (RULE-10 through RULE-14)
Execute per `autonomy-gate/rules.md`. No deviations.

### [N-1]. Professional Required Block (if triggered)
Check all conditions in `escalation-triggers.md` + `autonomy-assessment-guardrails.md`.
If any trigger fires: insert `🔴 PROFESSIONAL REQUIRED` block here, after the execution artifact.
If none fire: omit this section.

This block does not replace or alter the verdict. The operator receives the full assessment AND the professional escalation note.

### [N]. Disclaimer Block (always)
Append full disclaimer from `_guardrails/shared/output-disclaimers.md`. No exceptions.

---

## Session Log Entry (After Every Assessment)

Append to `_working/_calibration_log.md`:

```
## [YYYY-MM-DD] [Workflow Name or description] — [Verdict]
- Autonomy level: [AUT-1 / AUT-2 / AUT-3 / AUT-4]
- Confidence: [HIGH / MEDIUM / LOW]
- Hard gates applied: [GATE-1 / GATE-2 / GATE-3 / none]
- Evidence gaps at assessment time: [list or "none"]
- Adversarial flag triggered: [Y/N]
- Guardrail triggered: [Y/N — which trigger if Y]
- Handoff status: [BUILD_READY / BLOCKED_FOR_EVIDENCE / NOT_APPLICABLE]
- Disposition recorded: [APPROVE_FOR_BUILD / HOLD / pending]
```

---

*Layer placement: L2 Task Contract · Wraps RULE-XX system with guardrail hooks · Load for every assessment*
