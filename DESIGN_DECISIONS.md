# Design Decisions — v2 & v3 Architecture
## The Autonomy Gate

> Maps structural changes to their source concept in:
> **Van Clief & McDermott, "ICM-Folder-Structure-as-Agentic-Architecture" (arXiv:2603.16021)**

---

## The Core Insight from the ICM Paper

Claude Projects are not just knowledge bases — they are **Interpretable Context Methodologies (ICMs)**. Folder position carries cognitive meaning. Different layers serve different cognitive roles. Mixing them degrades output.

| Layer | Role | Should contain |
|-------|------|----------------|
| L0 — Identity | Who the agent is | Fixed character, expertise, limits |
| L1 — Routing | Where inputs go | Input classification, mode selection |
| L2 — Task contract | How each task executes | Per-mode execution specs |
| L3 — Reference (stable) | Stable constraints | Frameworks, rules, decision logic |
| L4 — Working (per-run) | Per-session data | Session logs, calibration data |

---

## Decision 1: The RULE-XX System Is Already an Excellent L2+L3 Architecture

**v1 assessment:** The RULE-XX system in `autonomy-gate/rules.md` is the most rigorous task contract logic in the v1 portfolio. It includes:
- Explicit phase sequencing (Phase 1: RULE-01–06, Phase 2: RULE-10–14)
- Field provenance system (STATED / DERIVED / UNKNOWN / NOT_APPLICABLE)
- Hard gate logic (GATE-1, GATE-2, GATE-3) with non-negotiable triggers
- Adversarial check (RULE-05) built into every assessment

**Assessment:** This is the correct content for L3 (behavioral decision rules). The RULE-XX system is a constraint system — it governs what the Gate must do regardless of input. This is L3.

**What was missing:** L1 (routing) and an L2 wrapper with pre-assessment guardrail checks. The RULE-XX system is the execution contract. The routing layer determines how an input enters the system before RULE-01 fires.

---

## Decision 2: Create L2 Assessment Mode as a Wrapper, Not a Replacement (`_modes/assessment-mode.md`)

**v1 behavior:** The RULE-XX system governed execution. There was no pre-assessment checklist, no guardrail hooks, no structured output slot for confidence level or disclaimer block.

**v2 change:** `_modes/assessment-mode.md` is a lightweight wrapper:
- Pre-assessment checklist (guardrails loaded? adversarial flags scanned? LOW confidence indicators present?)
- Reference to RULE-XX system for execution (not duplication)
- Structural output slots: Input Integrity Flag (section 0), confidence level block after Decision Packet, Professional Required block after artifact, Disclaimer Block (always)

**ICM source:** Context Layer 2 (task contract). The wrapper adds the guardrail layer without interfering with the RULE-XX system. The execution logic lives in rules.md; the session contract lives in assessment-mode.md.

**What this avoids:** Duplicating RULE-XX content. The assessment-mode.md references rules.md; it does not restate the rules. A task contract that duplicates its own execution logic is a maintenance problem.

---

## Decision 3: Session Isolation ≠ No L4 Layer (`_working/_calibration_log.md`)

**v1 behavior:** `identity.md` explicitly states "The Gate does not remember previous sessions." This is a correct design decision — per-operator memory creates privacy concerns and workflow cross-contamination. The Gate should assess each workflow on its own merits.

**v2 change:** `_working/_calibration_log.md` — session log for **system calibration**, not operator memory.

**The distinction:**
- **Operator memory** (what the Gate deliberately excludes): "The last time this operator submitted a workflow, they got a SUPERVISED verdict." This is excluded because it could bias future assessments.
- **System calibration** (what the log captures): "Over 50 assessments, 40% produced HUMAN_ONLY verdicts — is the Gate over-applying GATE-2?" This is aggregate signal for improving the Gate, not memory of individual operators.

**ICM source:** Context Layer 4 (working/per-run data). The paper argues L4 absence is the most common gap. The Gate's session isolation design was correct — but it inadvertently eliminated the system learning mechanism. The calibration log restores L4 without violating session isolation.

---

## Decision 4: `routing.md` — L1 Layer That Was Missing

**v1 behavior:** No routing.md. Input went directly to RULE-01. There was no explicit layer for: pre-assessment guardrail loading, input classification (workflow vs. no-workflow), or references to where the execution contract lives.

**v2 change:** `routing.md` with Steps 0–3. Step 1 formalizes the only routing decision the Gate makes (workflow detected vs. no-workflow path). Step 2 references `_modes/assessment-mode.md` as the task contract entry point.

**ICM source:** Context Layer 1 (routing). Even a single-mode system needs a routing layer — it is where guardrails load and where the execution contract is referenced. Without L1, guardrails have nowhere to load.

---

## Decision 5: Guardrails Add to Output — They Do Not Alter Verdicts (v3)

**v1+v2 behavior:** GATE-2 and GATE-3 were correctly identified as hard gates producing HUMAN_ONLY verdicts. But there was no mechanism for flagging conditions where the verdict is correct AND a professional review is additionally required — e.g., a workflow involving regulated data that correctly gets AUT-2 (SUPERVISED) but still needs compliance counsel review before deployment.

**v3 change:** `_guardrails/domain/autonomy-assessment-guardrails.md` — 5 escalation triggers for conditions where professional review is required independent of the autonomy verdict.

**The RULE-00 compatibility design:** RULE-00 states the Gate always issues a verdict. The guardrails are designed to add a PROFESSIONAL REQUIRED block after the artifact — not to suppress the verdict. The operator receives: full assessment + execution artifact + professional escalation note (if triggered). RULE-00 is preserved.

**Why this matters:** A SUPERVISED verdict on a HIPAA-affected workflow is technically correct — it requires human review before execution. But the operator still needs compliance counsel review before deployment, which is a different requirement from the autonomy level. The guardrail surfaces this; the verdict captures the autonomy level.

---

## What Didn't Change

- `autonomy-gate/rules.md` — RULE-XX decision system. The best v1 task contract logic in the portfolio. No changes.
- `autonomy-gate/reference/` — all stable L3 frameworks: criteria, contracts, precedents, capability matrix, operating patterns. No time-sensitive data. Correctly placed.
- `adapters/` — cross-platform adapter contracts. Stable. No changes.
- `docs/` — user-facing documentation. Stable. No changes.
- RULE-00 behavioral contract — preserved exactly. Guardrails add to output; they do not violate RULE-00.

---

## The Autonomy Gate v1 Was the Most Rigorous Technical Architecture

Among the five repos in this upgrade wave:
- RULE-XX system: explicit, numbered, sequenced, with field provenance — no other v1 had this level of decision rigor
- Hard gate logic (GATE-2, GATE-3): non-negotiable safety boundaries correctly identified
- Field provenance (STATED / DERIVED / UNKNOWN): no other v1 had this — it prevents hallucination at the data layer
- Two-phase flow: cleanest L2 structure in the v1 portfolio

The v2+v3 upgrade adds architecture around an already strong core. The core doesn't change.

---

*Reference: Van Clief & McDermott, "ICM-Folder-Structure-as-Agentic-Architecture" (arXiv:2603.16021)*
*v2+v3 built: 2026-06-17*
