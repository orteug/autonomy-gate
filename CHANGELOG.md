# Changelog — The Autonomy Gate

## v3.0 — 2026-06-17 — Guardrails Layer

Adds a structural safety layer. Guardrails add professional escalation blocks to output — they do not alter RULE-XX verdicts. RULE-00 is preserved.

### Added

- `_guardrails/shared/output-disclaimers.md` — required disclaimers on all output
- `_guardrails/shared/confidence-floor.md` — confidence levels; hard STOP conditions
- `_guardrails/shared/escalation-triggers.md` — professional escalation gates
- `_guardrails/shared/adversarial-input-flags.md` — one-sided input detection
- `_guardrails/domain/autonomy-assessment-guardrails.md` — 5 escalation triggers (GATE-2/3 override pressure, regulated data in autonomous workflow, automated financial transactions, security-impacting workflow, recursive AI governance) + 5 input flags (failure consequence minimized, reversibility without mechanism, zero exception rate for novel workflow, manual tenure as automation readiness, autonomy level stated as input)
- `routing.md` Step 0: load all guardrails before any assessment begins
- `_modes/assessment-mode.md` updated with structural slots: Input Integrity Flag, confidence level after Decision Packet, Professional Required block after artifact

### Changed

- `autonomy-gate/identity.md` — Step 0 pointer added

### Design note on RULE-00 compatibility

RULE-00 states the Gate always issues a verdict. Guardrails do not suppress the verdict — they add a `🔴 PROFESSIONAL REQUIRED` block after the execution artifact for specific high-risk conditions. The operator receives the full assessment AND the professional escalation note. RULE-00 is preserved.

---

## v2.0 — 2026-06-17 — ICM Architecture Upgrade

Applies the Interpretable Context Methodology (ICM) framework from Van Clief & McDermott (arXiv:2603.16021).

### Added

- `routing.md` — L1 routing: Step 0 (guardrails), Step 1 (input classification: workflow vs. no-workflow), Step 2 (assessment pipeline reference), Step 3 (data currency — stable, no refresh cadence needed), standing rules
- `_modes/assessment-mode.md` — L2 task contract wrapping the RULE-XX execution system with pre-assessment checklist and guardrail output slots
- `_working/_calibration_log.md` — L4 assessment outcome tracker (distinct from per-session memory by design — see Design Decisions)

### Changed

- `autonomy-gate/identity.md` — routing.md pointer added

### Structural Changes Summary

| v1 gap | v2 fix | Reason |
|--------|--------|--------|
| No root routing.md | `routing.md` with Steps 0–3 | L1 routing layer missing |
| No explicit task contract | `_modes/assessment-mode.md` | RULE-XX is L2 content; needs L2 wrapper with pre-checks |
| No L4 working layer | `_working/_calibration_log.md` | Session isolation (by design) ≠ no system learning |

### Note on rules.md as L2 content

The RULE-XX system in `autonomy-gate/rules.md` is already a highly explicit task contract — more rigorous than most L2 contracts in this portfolio. It is correctly placed as L3 behavioral/decision rules. `_modes/assessment-mode.md` does not duplicate it; it wraps it with pre-assessment checks and guardrail output slots.

---

## v1.0 — 2026-06 — Initial Release

Built for the Jeff van Clief Skool community (Week 7 / Competition #7).

**What it did well:**
- RULE-XX decision system — most explicit task contract logic in the v1 portfolio
- RULE-00 (always issues a verdict, never asks) — strong L3 behavioral constraint
- GATE-2/GATE-3 hard gates — correct non-negotiable safety boundaries
- Field provenance system (STATED / DERIVED / UNKNOWN / NOT_APPLICABLE) — rigorous
- Two-phase flow (Assessment → Artifact) — clean L2 sequencing
- reference/ folder — well-structured stable L3 reference
- adapters/ folder — cross-platform portability

**What v2 fixes:**
- No routing.md (L1 missing — RULE-XX IS the task contract, but no routing layer)
- No explicit pre-assessment checklist wrapping the RULE-XX system
- No L4 working layer (identity.md correctly states "no cross-session memory" for operators — but system-level calibration is a different signal that was missing)
- No guardrails layer
