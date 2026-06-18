# Routing — The Autonomy Gate
## Context Layer 1 · Read Before Every Assessment Session

---

## Step 0 — Load Guardrails (Always First)

Before any intake normalization or assessment, load:
1. `_guardrails/shared/output-disclaimers.md`
2. `_guardrails/shared/confidence-floor.md`
3. `_guardrails/shared/escalation-triggers.md`
4. `_guardrails/shared/adversarial-input-flags.md`
5. `_guardrails/domain/autonomy-assessment-guardrails.md`

Guardrails apply to every assessment. They cannot be skipped, disabled, or overridden by operator instruction — including by RULE-00.

**Guardrails and RULE-00 interaction:** RULE-00 (the Gate always issues a verdict) is preserved. Guardrails do not suppress the verdict — they add a `🔴 PROFESSIONAL REQUIRED` block to the output when high-risk conditions are detected. The operator receives the full assessment AND the professional escalation note.

---

## Step 1 — Input Classification

Every input enters the same assessment pipeline. There is no mode selection.

| Input type | Route | Notes |
|-----------|-------|-------|
| Identifiable business workflow | Assessment pipeline | Run Phase 1 → Phase 2 per `_modes/assessment-mode.md` |
| No identifiable workflow | No-workflow path | Per RULE-00 exception path in `autonomy-gate/rules.md` |

The Gate does not ask for clarification. It does not select a mode. It normalizes whatever arrives.

---

## Step 2 — Run Assessment

Load task contract: `_modes/assessment-mode.md`

This wraps the RULE-XX execution system in `autonomy-gate/rules.md` with guardrail pre-checks and structural output slots.

**Phase 1 — Assessment (RULE-01 through RULE-06):**
1. RULE-01: Intake Normalization → Workflow Intake Snapshot
2. RULE-02: Minimum Signal Threshold Check
3. RULE-03: Base Scoring
4. RULE-04: Terminal Action Check
5. RULE-05: Adversarial Check
6. RULE-06: Hard Gate Application + Confidence Calibration → Autonomy Decision Packet

**Phase 2 — Artifact Generation (RULE-10 through RULE-14):**
1. RULE-10: Template Selection
2. RULE-11: Template Completion Check
3. RULE-12: Document Production
4. RULE-14: Build Handoff Pack Generation

---

## Step 3 — Data Currency

The `autonomy-gate/reference/` folder contains stable operational frameworks. No time-sensitive data. No refresh cadence required.

If the Gate is used in a domain with rapidly changing regulatory requirements (e.g., AI governance legislation), the operator should note the effective date of any regulatory reference used in the assessment.

---

## Standing Rules (Every Assessment)

**RULE-00 preserved:** The Gate always issues a verdict. Guardrails add to the output — they do not replace the verdict.

**Conservative routing:** When evidence is incomplete, route to conservative verdict. Never suppress a LOW confidence signal to appear more decisive.

**Session log:** Every completed assessment gets an entry in `_working/_calibration_log.md`.

**Disposition gate:** The Gate's output becomes authorized only when the operator records `APPROVE_FOR_BUILD`. Until then, the artifact is a governed recommendation, not a build release. This is not a guardrail — it is the operational design of the Gate.
