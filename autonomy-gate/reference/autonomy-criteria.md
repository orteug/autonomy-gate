# Autonomy Criteria — Reference

This file defines the four factors the Gate scores in Phase 1, Step 3 (RULE-03). It also provides the Automation Maturity Ladder that contextualizes where most workflows actually sit when they arrive at the Gate.

---

## The Automation Maturity Ladder

Most workflows that arrive at the Gate are described as automation candidates. Most are not. The ladder makes this legible.

| Stage | Name | Meaning | AI Authority |
|-------|------|---------|-------------|
| 0 | Undefined Work | Goal exists; process does not. No one can describe the steps. | None |
| 1 | Manual Work | A human performs the task, but inconsistently or tacitly. Steps live in someone's head. | None |
| 2 | SOP Work | Steps, inputs, outputs, exceptions, and owner are defined and documented. Anyone can follow it. | Assistive |
| 3 | Supervised Automation | AI drafts, routes, or executes with human checkpoints. Human owns the decision. | Conditional |
| 4 | Bounded Autonomy | AI executes within narrow permissions and emits logs. Human monitors exceptions. | Limited |
| 5 | Managed Automation | AI execution is monitored, audited, tested, and periodically recertified. Expiration conditions are active. | Operational |

**Rule for the Gate:** A workflow must reach Stage 2 before Stage 3 is possible. Stage 4 (AUTONOMOUS) requires Stage 2 plus all four criteria scoring clean. Stage 5 requires Stage 4 plus active monitoring, audit cadence, and named expiration conditions.

`SOP_FIRST` is not a failure verdict. It is often the most accurate answer to an automation request. The Stabilization Plan the Gate produces at `SOP_FIRST` is the correct first action — not a delay, but the automation decision itself.

The wrong question: "Can AI do this?"
The right question: "Is this process documented well enough that an agent could execute it without asking what to do next?"

---

## The Four Autonomy Criteria

These are scored in RULE-03 during Phase 1, Step 3. Each criterion is assessed independently. The most restrictive criterion governs the base verdict.

---

### Criterion 1 — Reversibility

**Definition:** Can the action be undone after execution? How quickly, completely, and at what cost?

**Why it matters:** An irreversible action means that a wrong output cannot be corrected after the fact. The Gate must account for this before granting any autonomous authority.

**Reversibility Matrix:**

| Level | Description | Gate implication |
|-------|-------------|-----------------|
| Fully reversible | Rollback in minutes; no external effect; correction is routine | Supports AUTONOMOUS (no gate on reversibility alone) |
| Partially reversible | Correction possible but requires effort, coordination, or external contact | Supports SUPERVISED; document rollback procedure in artifact |
| Conditionally reversible | Reversible only within a time window (e.g., wire transfers, 24h cancellation windows) | Supports SUPERVISED with explicit time constraint in artifact |
| Irreversible | No rollback; external commitment made; correction requires consent of a third party | Triggers GATE-2 check; may require HUMAN_ONLY |

**Worked examples:**
- Sending a Slack message to an internal channel → Fully reversible (can delete or correct)
- Sending an external email to a customer → Partially reversible (can send correction; original persists)
- Issuing a wire transfer → Conditionally reversible in some cases; often irreversible
- Filing a signed contract → Irreversible — GATE-2 applies

---

### Criterion 2 — Observability

**Definition:** Can a human verify what the system did, catch errors before they propagate, and audit the decision chain?

**Why it matters:** Unobservable automation produces FAIL-3 (Silent Failure). Errors that cannot be seen cannot be caught. The Gate requires observability as a precondition for AUTONOMOUS authority.

**Observability Requirements:**

| Level | Description | Gate implication |
|-------|-------------|-----------------|
| Fully observable | Logs at every step; human-readable output; state visible at any point; named reviewer has access | Supports AUTONOMOUS |
| Partially observable | Summary output produced; internal steps not individually logged; errors may not surface until downstream | Supports SUPERVISED; add audit trail requirement to artifact |
| Low observability | Output produced but steps are opaque; no audit log; no way to verify what ran | Supports SUPERVISED minimum; document GATE-5 (no audit trail) |
| Not observable | Black box; no output record; no way to verify execution | Triggers GATE-5; requires controls before any autonomy level possible |

**Observability requirements for AUTONOMOUS:**
- Every run emits a terminal status from the valid set: COMPLETED, COMPLETED_WITH_WARNINGS, NEEDS_REVIEW, BLOCKED, FAILED, SKIPPED, TIMED_OUT
- Outputs are stored in a named location with retention policy
- A human can reconstruct the decision chain from the log

---

### Criterion 3 — Exception Rate

**Definition:** What percentage of workflow instances fall outside the standard path? Is exception handling defined and documented?

**Why it matters:** Undocumented exceptions are the primary cause of `SOP_FIRST` verdicts. A workflow that handles 80% of cases cleanly while silently failing the 20% that require judgment is not a successful automation. It is a liability that appears successful most of the time.

**Exception Rate Assessment:**

| Level | Description | Gate implication |
|-------|-------------|-----------------|
| Low and documented | Clear rules for every exception type; edge cases mapped and tested; exception path is deterministic | Supports AUTONOMOUS |
| Low and estimated | User believes exceptions are rare but cannot name them; no documented exception handling | Supports SUPERVISED; exception documentation required before AUTONOMOUS |
| Medium (known exceptions) | Some exception types identified; handling is defined for known cases; unknown edge cases acknowledged | Supports SUPERVISED |
| High or undocumented | "It depends on the situation"; exceptions handled case-by-case; "mostly the same" | Returns SOP_FIRST regardless of other criteria |

**Signal phrases that indicate undocumented exceptions:**
- "It's mostly the same every time but sometimes things are different"
- "We handle it manually when it doesn't go through"
- "It depends on the client / customer / situation"
- "Usually it works, but occasionally..."
- "Our team deals with the edge cases"

Any of these phrases in the workflow description triggers the exception rate criterion as "undocumented." The Gate cannot know what the exception path is. The user has confirmed it is not defined.

---

### Criterion 4 — Cost of Failure

**Definition:** What is the consequence if the workflow produces wrong output or fails mid-execution? Can the damage be bounded, observed, and corrected?

**Why it matters:** Cost of failure is the final gate before AUTONOMOUS can be granted. Low reversibility and low observability alone can be mitigated with controls. High failure cost with irreversibility is the condition that produces HUMAN_ONLY.

**Failure Consequence Classes:**

| Class | Description | Gate implication |
|-------|-------------|-----------------|
| Low | Internal only; reversible; correctable before anyone acts; no regulatory or financial exposure | Supports AUTONOMOUS |
| Medium | Requires correction effort; downstream teams are affected; customer-visible but correctable | Supports SUPERVISED |
| High — Operational | Disrupts a business process; significant correction effort; customer impact | Requires SUPERVISED minimum; document rollback in artifact |
| High — Financial | Financial loss, payment error, billing impact, regulatory penalty | Triggers GATE-1 check; requires SUPERVISED minimum |
| High — Regulatory | Compliance failure, audit exposure, regulatory reporting error | Triggers GATE-2/GATE-4 check; may require HUMAN_ONLY |
| High — Reputational | External publication error, customer data exposure, brand impact | Triggers GATE-4 check; requires SUPERVISED minimum |
| Catastrophic | Irreversible external commitment with major financial, legal, or reputational consequence | HUMAN_ONLY; GATE-2 or GATE-3 |

---

## How the Four Criteria Combine

The criteria are scored independently. The base verdict is the most restrictive result across all four.

| All four criteria at same level | Base verdict |
|---------------------------------|-------------|
| All support AUTONOMOUS | AUTONOMOUS (subject to adversarial check and gate application) |
| Any criterion supports only SUPERVISED | SUPERVISED maximum |
| Exception rate: undocumented or high | SOP_FIRST (overrides other criteria) |
| Cost of failure: catastrophic + reversibility: irreversible | HUMAN_ONLY (pending gate confirmation) |

The adversarial check (RULE-05) and hard gate application (RULE-06) may revise this base verdict downward. They never revise it upward.

---

## Stage 4 Prerequisites (Before AUTONOMOUS Can Be Issued)

For a workflow to receive an AUTONOMOUS verdict, all of the following must be true:

- [ ] Reversibility: fully or conditionally reversible with rollback procedure documented
- [ ] Observability: every run emits terminal status; logs retained; human-readable output
- [ ] Exception rate: exceptions documented and handled deterministically
- [ ] Failure consequence: bounded, observable, and correctable
- [ ] All four RULE-02 required fields fully populated (no confidence cap)
- [ ] Adversarial check passed without revision
- [ ] No GATE condition triggered by the terminal action
- [ ] Surface with autonomous execution capability assigned (SURFACE-2 or SURFACE-3)

If any prerequisite is not met, the verdict is SUPERVISED or below.
