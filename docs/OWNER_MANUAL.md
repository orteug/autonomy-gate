# Owner Manual

The Autonomy Gate  
Product documentation for operators, founders, and AI workflow owners

---

## 1. Product Purpose

The Autonomy Gate answers one business question:

```text
Should AI be allowed to handle this workflow, and if yes, under what authority?
```

Most automation requests start with capability:

```text
Can AI do this?
```

The Gate starts with consequence:

```text
What happens if AI does this wrong?
```

That distinction is the product.

---

## 2. Product Boundary

The Gate is a decision layer.

It does:

- assess workflows
- assign autonomy level
- assign execution surface
- name missing evidence
- apply hard gates
- produce an execution artifact

It does not:

- connect to external systems
- run the workflow
- create production integrations
- approve itself
- replace human authority where human authority is required

Execution surfaces such as Claude Project, ChatGPT Project, Cowork, Claude Code, and Codex consume the Gate's output differently.

### The Executor Misconception

The artifact the Gate produces is a governance document — a Project Setup Brief, Control Plan, Automation Architecture, or Governance Memo. It is not a running automation. It is the specification and authority document for building one.

Running the Gate is step one. Implementing the artifact is step two. The Gate does not perform step two.

### Scope Boundary

The Gate is designed for **recurring organizational workflows** — processes that run repeatedly, where the question "how much authority should AI have over this?" has a non-trivial organizational answer.

It is not a general-purpose AI assistant. Do not use it for:

- One-time personal requests
- Ad hoc AI assistance with no recurring governance implication
- Tasks where you are the sole authority and sole person affected

If you are unsure whether the Gate applies, ask: *"If AI gets this wrong, does someone other than me face a consequence, and will this workflow run again?"* If yes to both, use the Gate. If no to either, use your general AI assistant directly.

---

## 3. Core Concepts

### Workflow

A repeatable business process with a trigger, inputs, actions, systems, and output.

Examples:

- triage refund requests
- summarize weekly KPIs
- screen resumes for one role
- process vendor bank account changes
- collect compliance evidence

### Terminal Action

The last thing that executes.

This is the most important concept in the product.

Examples:

| Workflow label | Terminal action | Why it matters |
|---|---|---|
| Refund assessment | Recommendation document | Does not move money |
| Refund automation | Refund issued | Moves money |
| Vendor verification | Payment routing changed | Irreversible external commitment |
| Content review | Internal recommendation | Reversible |
| Content scheduling | Public post scheduled | External publication |

The Gate scores the terminal action, not the workflow label.

### Autonomy

How much authority AI receives.

| Level | Meaning |
|---|---|
| `AUTONOMOUS` | AI runs without a human approval checkpoint inside the run. |
| `SUPERVISED` | AI prepares; human approves before execution. |
| `SOP_FIRST` | Process must be documented before automation. |
| `HUMAN_ONLY` | Terminal action stays human. |

### Surface

Where the work should run.

| Surface | Use when |
|---|---|
| `PROJECT` | Human starts a session and wants a document, analysis, or decision artifact. |
| `COWORK` | Workflow needs scheduled runs, local files, folder I/O, or unattended cadence. |
| `CODE_AGENT` | Workflow requires scripts, APIs, tests, deterministic integrations, or enforcement logic. |
| `NO_AI` | No AI surface should execute the terminal action. |

### Confidence

How complete the evidence was.

| Confidence | Meaning |
|---|---|
| `HIGH` | Required fields populated, no evidence gaps, adversarial check passed. |
| `MEDIUM` | Minor gaps exist, but the verdict is still defensible. |
| `LOW` | Significant gaps exist; conservative route applies. |

---

## How The Gate Scores A Workflow

The Gate runs every workflow through four independent criteria. Think of them as four doors — a workflow only reaches `AUTONOMOUS` if it passes through all four. The most restrictive criterion governs the verdict.

### Reversibility

*Can the action be undone, quickly, completely, and at reasonable cost?*

| Action | Reversibility |
|---|---|
| Sending a Slack message to an internal channel | Reversible — delete it or send a correction |
| Sending an email to a customer | Partially reversible — follow-up is possible, but the original stays sent |
| Filing a signed contract | Irreversible — no rollback without the other party's consent |
| Authorizing a payment routing change | Irreversible — GATE-2 triggers |

The Gate gets more conservative as reversibility decreases. Irreversible terminal actions trigger a hard gate check regardless of how clean the rest of the workflow scores.

### Observability

*Can a human see what the system did, verify the output, and catch errors before they spread?*

A workflow that logs every step and produces human-readable output is fully observable. A workflow that runs in the background and surfaces only a final result — no log, no audit trail, no intermediate checkpoints — is a black box.

The Gate cannot route a black box to `AUTONOMOUS`. If errors cannot be seen, they cannot be caught.

### Exception Rate

*What percentage of instances fall outside the standard path, and are those exceptions documented?*

This is where most automation candidates fail — not because the standard case is hard, but because undocumented exceptions are where damage occurs.

Watch for these phrases. Each one is a signal that exception handling is not documented:

- "It's mostly the same every time but sometimes things are different"
- "We handle it manually when it doesn't go through"
- "It depends on the client"
- "Usually it works, but occasionally..."
- "Our team deals with the edge cases"

Any of these and the Gate routes to `SOP_FIRST`. Documentation is not a delay to automation — it is the automation decision.

### Cost of Failure

*What is the worst realistic outcome if this workflow produces wrong output?*

Note: worst *realistic*, not worst possible.

| Level | Definition |
|---|---|
| Low | Internal only, correctable before anyone acts on it |
| Medium | Downstream teams or customers affected, correction is possible with effort |
| High | Financial loss, regulatory exposure, or significant reputational impact; correction is partial or conditional |
| Critical | Irreversible external commitment with major financial, legal, or security consequence |

High and Critical costs do not automatically produce `HUMAN_ONLY` verdicts, but they trigger a hard gate check and raise the bar for `AUTONOMOUS` significantly.

---

## 4. Installation In Claude Project

1. Create a Claude Project.
2. Name it `The Autonomy Gate`.
3. Add project instruction:

```text
You are The Autonomy Gate. Follow identity.md.
```

4. Upload the operator files.
5. Start a new project chat.
6. Paste a workflow description.

Minimum files:

```text
identity.md
rules.md
examples.md
reference/autonomy-criteria.md
reference/risk-classification.md
reference/surface-capability-matrix.md
reference/precedents.md
reference/templates/*.md
```

If your platform does not preserve folders, upload the files flat and keep filenames unchanged.

---

## 5. Installation In ChatGPT Project

1. Create a ChatGPT Project.
2. Name it `The Autonomy Gate`.
3. Add project instruction:

```text
You are The Autonomy Gate. Follow identity.md and rules.md.
```

4. Confirm the Project supports at least 13 files. The current package requires Go, Plus, Pro, Edu, Business, or Enterprise; Free Projects allow only 5 files.
5. Upload the same 13 operator files shown in the Claude installation section, flat, in two batches. ChatGPT currently accepts at most 10 files per upload action.
6. Start a new project chat.
7. Paste a workflow description.

ChatGPT Projects support project files and project instructions. Depending on plan and settings, Projects may also have memory, web search, connected apps, and other tools. Treat these as optional capabilities, not required Gate behavior.

---

## 6. How To Describe A Workflow

The Gate accepts messy input, but better input produces better confidence.

Use this format when possible:

```text
Workflow name:
Who starts it:
What triggers it:
Inputs:
Steps:
Systems touched:
Output:
Who uses the output:
What happens if it is wrong:
Can it be reversed:
Known exceptions:
Desired automation:
```

Example:

```text
Workflow name: Weekly KPI report
Who starts it: Ops lead every Monday
Inputs: CRM export, revenue export, support ticket export
Steps: Paste exports, summarize Revenue/Pipeline/Support, flag notable variance
Systems touched: Claude Project only; source systems are exported manually
Output: Slack-ready text
What happens if wrong: Team makes decisions on stale or incorrect data
Can it be reversed: Yes, post a correction
Known exceptions: Missing export, unusually high variance
Desired automation: AI formats and writes the report
```

---

## 7. The Two-Phase Flow

### Phase 1: Assessment

The Gate:

1. Normalizes your input into a Workflow Intake Snapshot.
2. Scores the workflow against four autonomy criteria:
   - reversibility
   - observability
   - exception rate
   - cost of failure
3. Identifies the terminal action.
4. Runs the adversarial check.
5. Applies hard gates.
6. Issues the Autonomy Decision Packet.

### Phase 2: Artifact Generation

The Gate:

1. Selects the artifact template.
2. Fills the artifact from the snapshot and packet.
3. Names missing evidence instead of hiding it.
4. Produces a complete document.

---

## 8. Hard Gates

Hard gates override base scoring.

| Gate | Condition | Minimum result |
|---|---|---|
| `GATE-1` | Moves money | `SUPERVISED` minimum |
| `GATE-2` | Irreversible external commitment | `HUMAN_ONLY` |
| `GATE-3` | Changes permissions or access controls | `HUMAN_ONLY` |
| `GATE-4` | Publishes regulated or reputationally sensitive material externally | `SUPERVISED` minimum |
| `GATE-5` | Acts without audit trail or rollback | `SUPERVISED` minimum |

These gates are not suggestions.

If `GATE-2` or `GATE-3` triggers, controls cannot downgrade the risk enough to delegate the terminal action.

---

## 9. Reading The Output

### Step 1: Check The Snapshot

Ask:

- Did it understand the workflow?
- Did it name the correct systems?
- Did it identify the correct terminal action?
- Did it name evidence gaps?

If the snapshot is wrong, re-run with a corrected description.

### Step 2: Read The Packet

Ask:

- What autonomy level did it assign?
- What surface did it assign?
- What confidence did it assign?
- Which rules or gates did it cite?
- What controls are required?

### Step 3: Use The Artifact

The artifact is the document you act on.

Do not act from the packet alone if the artifact contains controls, reviewer requirements, or expiration triggers.

---

## 10. Acting On The Artifact

| Artifact | What to do |
|---|---|
| Project Setup Brief | Create the Project and use the custom instructions. |
| Automation Architecture | Give to a builder or code agent. |
| Cowork Project Config | Set up folders, schedule, logs, and permissions. |
| Control Plan | Implement the approval checkpoint before execution. |
| Stabilization Plan | Document and stabilize the process first. |
| Governance Memo | Keep the terminal action human-owned. |

---

## 11. Recertification

Every verdict expires.

Re-run the Gate when:

- workflow steps change
- systems change
- data sources change
- model or AI surface changes
- policy or compliance context changes
- incident occurs
- error threshold is exceeded
- reviewer role changes
- recertification date arrives

Do not treat a verdict as permanent.

---

## 12. Common Owner Mistakes

### Mistake 1: Treating "AI can do this" as "AI should own this"

Capability is not authority.

### Mistake 2: Ignoring terminal action

The same analysis can be safe as a recommendation and unsafe as an automated action.

### Mistake 3: Using PROJECT for live integrations

Claude Project and ChatGPT Project are best for human-initiated reasoning and artifacts. They are not the same as a scheduled integration runtime.

### Mistake 4: Treating LOW confidence as failure

LOW confidence means the Gate found missing evidence and routed conservatively.

### Mistake 5: Letting a reviewer exist only on paper

A SUPERVISED workflow requires a real reviewer with blocking authority.

---

## Verdict Pattern Match

Use this to predict the verdict before you run the Gate.

| You described this... | Likely verdict |
|---|---|
| Internal report, stable data, no external delivery | `AUTONOMOUS / PROJECT` |
| Same report, needs to run on schedule without human initiation | `AUTONOMOUS / COWORK` |
| Script that reads from a system and routes or enriches data | `AUTONOMOUS / CODE_AGENT` |
| Any workflow that ends with initiating a payment | `SUPERVISED` — GATE-1 |
| Any workflow that ends with publishing externally | `SUPERVISED` — GATE-4 |
| Any workflow where "it depends" is the exception answer | `SOP_FIRST` |
| Any workflow where the last step moves a routing number or files a regulatory document | `HUMAN_ONLY` — GATE-2 |
| Any workflow that would grant or revoke system access | `HUMAN_ONLY` — GATE-3 |
| Any workflow where you cannot describe what happens when it fails | `LOW` confidence |

When the verdict matches your prediction, your calibration is good. When it diverges, read the justification — you learned something about the workflow.

---

## 13. Owner Checklist

Before using a Gate artifact:

- [ ] I checked the terminal action.
- [ ] I understand the verdict.
- [ ] I understand the surface.
- [ ] I know what artifact I received.
- [ ] I know what human action happens next.
- [ ] I checked evidence gaps.
- [ ] I checked controls required.
- [ ] I noted expiration triggers.
- [ ] I know when to re-run the Gate.
