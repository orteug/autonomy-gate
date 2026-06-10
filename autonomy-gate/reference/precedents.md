# Precedents

The Autonomy Gate's logic is not novel. It is a compact implementation of patterns that appear across AI governance, industrial automation, and operational risk management. These are cited for grounding — not as official endorsements.

---

## Proportional Oversight

**External pattern:** Oversight should be commensurate with risk, level of autonomy, and context of use. Human override capability, reversal ability, and awareness of system limits are named requirements.

**Gate implementation:** Autonomy verdict + confidence + hard gates. AUTONOMOUS, SUPERVISED, SOP_FIRST, and HUMAN_ONLY are authority levels matched to the workflow's risk and context — not labels of convenience.

---

## Graded Autonomy

**External pattern:** Effective agent governance does not use one-size-fits-all controls. Autonomy is graded — from observe to advise to act with approval to act autonomously — and different workflows warrant different levels.

**Gate implementation:** Four autonomy levels assigned to the minimum justified by the workflow. Autonomy is not binary. The Gate assigns the minimum operating authority the workflow earns.

---

## Jidoka — Automation With A Human Touch

**External pattern:** Automation should stop when an abnormality is detected. The system's ability to halt is as important as its ability to run.

**Gate implementation:** SOP_FIRST, HUMAN_ONLY, GATE overrides, and evidence gaps are the Gate's stop conditions. A chatbot keeps answering. An operator can stop the line.

---

## Terminal Action Risk

**External pattern:** Automated systems do not just reduce labor — they increase the speed at which errors become consequences. A software error that would take hours to notice manually can propagate at machine speed before any human sees it.

**Gate implementation:** RULE-04 terminal action check. The Gate scores the terminal action, not the workflow label. The same upstream analysis can be safe when it produces a recommendation and unsafe when it executes a payment.

---

## Runtime Guardrails

**External pattern:** Tool calls, approval checkpoints, and guardrails enforce authority at runtime. The governance layer and the execution layer are separate concerns.

**Gate implementation:** The Autonomy Decision Packet is the governance output. It is designed to become a runtime configuration object: allowed tools, blocked actions, approval-required actions, audit requirements, and expiry conditions. The Gate does not replace runtime guardrails — it produces the decision packet those guardrails should enforce.
