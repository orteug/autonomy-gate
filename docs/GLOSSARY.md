# Glossary

The Autonomy Gate — terms used across all documentation.

---

**Autonomy Decision Packet**

The structured output of Phase 1. Contains: autonomy verdict, surface verdict, confidence level, justification (citing RULE-NN and GATE-NN), controls required, evidence gaps, and artifact type. Designed to be portable — carried to execution surfaces without requiring a new Gate session.

---

**Autonomy verdict**

The first axis of every Gate verdict. AUTONOMOUS, SUPERVISED, SOP_FIRST, or HUMAN_ONLY. Describes how much authority the workflow receives.

---

**AUTONOMY EXPIRES WHEN**

A mandatory section in every execution artifact. Lists the conditions under which the current verdict is no longer valid and re-assessment is required. Not a formality — these conditions are the governance mechanism that keeps automation decisions current.

---

**Conservative route**

When confidence is LOW or the adversarial check produces a revision, the Gate applies one level more restrictive than the scored verdict. AUTONOMOUS becomes SUPERVISED; SUPERVISED becomes SOP_FIRST. Named in the Decision Packet when applied.

---

**Evidence gaps**

Fields in the Workflow Intake Snapshot that could not be populated from the input description. Named specifically in the Decision Packet. Each gap is a research assignment — gather the named information and re-submit.

---

**FAIL-NN**

Named failure patterns referenced in the adversarial check. Eight patterns covering: Capability Bias, Automation Bias, Silent Failure, Stale SOP Drift, Overbroad Agency, Human-in-the-Loop Theater, Bad Data Becomes Authority, and Partial Deployment Failure.

---

**GATE-NN**

Hard gate conditions applied to the terminal action. Five conditions. GATE-1, GATE-4, and GATE-5 override to SUPERVISED minimum. GATE-2 and GATE-3 override to HUMAN_ONLY. Cannot be bypassed by operator context or user instruction.

| Gate | Condition | Minimum override |
|---|---|---|
| GATE-1 | Terminal action initiates a financial transaction | SUPERVISED |
| GATE-2 | Terminal action makes an irreversible external commitment | HUMAN_ONLY |
| GATE-3 | Terminal action changes permissions or access controls | HUMAN_ONLY |
| GATE-4 | Terminal action publishes regulated or reputationally sensitive material externally | SUPERVISED |
| GATE-5 | Terminal action occurs without an audit trail or rollback mechanism | SUPERVISED |

---

**Governance memo**

The execution artifact for HUMAN_ONLY verdicts. Documents why the workflow cannot be delegated, names the applicable gate condition, describes what would change the verdict, and provides a structure for the human review process.

---

**Governance registry**

A user-maintained table tracking all governed workflows. One row per workflow: name, verdict, surface, confidence, recertification date, reviewer (if SUPERVISED), status. See `GOVERNANCE_REGISTRY_TEMPLATE.md`.

---

**Human-in-the-Loop Theater**

A checkpoint that exists on paper but cannot function in practice. The reviewer lacks time, criteria, authority, or practical ability to stop execution. The most common way SUPERVISED workflows fail in deployment. Named FAIL-6 in the Gate's failure pattern library.

---

**Recertification**

The process of re-submitting a governed workflow to the Gate after a triggering condition in AUTONOMY EXPIRES WHEN is met. Produces an updated verdict and artifact. The old artifact is replaced in the governance registry.

---

**Scope splitting**

When a workflow contains multiple phases with materially different terminal actions and risk profiles, the Gate decomposes it and names each separately. Each phase receives its own verdict. The phases are implemented separately.

---

**SOP_FIRST**

An autonomy verdict indicating the process is too undocumented to assign any AI authority. The correct verdict for workflows where exceptions are undocumented or the process cannot be described step by step. The Stabilization Plan the Gate produces is the project plan to reach a state where the workflow can be re-submitted.

---

**Surface verdict**

The second axis of every Gate verdict. PROJECT, COWORK, CODE_AGENT, or NO_AI. Describes where the governed workflow runs.

---

**Terminal action**

The last thing a workflow actually executes — not the label applied to the workflow. The Gate's gate conditions apply to the terminal action. The same upstream analysis can produce completely different verdicts depending on whether it ends with a recommendation document (no gate trigger) or execution of the recommended action (gate likely triggered).

---

**Workflow Intake Snapshot**

The Gate's normalized representation of the submitted workflow description. The verdict is issued against the snapshot, not against the raw input. Read the snapshot before reading the verdict — if the snapshot is wrong, the verdict may be wrong.
