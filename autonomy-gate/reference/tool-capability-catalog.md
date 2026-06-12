# Tool Capability Catalog

This catalog maps tool categories to the capabilities relevant to autonomous workflow governance. The Gate uses this catalog to match workflow architecture requirements to available tools.

**Usage rules:**
- Tools are selected because they satisfy named capability requirements — not because they are familiar or popular.
- When the organization's technology stack profile names approved tools, the Gate recommends from the approved set only.
- When no stack profile is present, the Gate describes required capabilities without naming specific products.
- Capability claims are current as of the catalog version date. Treat this as maintained product data, not timeless knowledge.
- Tool limitations, licensing, and procurement considerations are as important as capabilities. Both are listed.

**Catalog version:** 2026-06-11

---

## Category 1 — Trigger Mechanisms

Triggers initiate workflow execution. The required trigger type must match what the autonomy pattern requires.

| Mechanism | Type | Capabilities | Limitations |
|-----------|------|-------------|-------------|
| Cron / scheduler | Time-based | Fixed or dynamic intervals; timezone support; retry on missed fire | Does not respond to events; cannot halt on failure without external monitoring |
| Webhook receiver | Event-based | Responds to external events immediately; payload carries context | Requires public endpoint or webhook gateway; must handle retries and deduplication |
| Queue consumer | Event-based, async | Durable delivery; backpressure; at-least-once or exactly-once semantics | Queue depth, consumer lag, and dead-letter handling require observability |
| Human-initiated | Manual | Operator controls when and whether to run | No automation without human action; cannot be scheduled |
| API call | On-demand | External system initiates; standardized input format | Caller must be authenticated; synchronous calls block caller |

**Selection rule:** AUTONOMOUS workflows may use any trigger type. SUPERVISED workflows require a human approval checkpoint after triggering but before the terminal action — the trigger type does not change this requirement.

---

## Category 2 — Integration and iPaaS Platforms

Integration platforms connect systems without custom code. They are the primary option for teams without engineering capacity.

| Platform | Autonomy capabilities | Human-in-the-loop support | Audit trail | Key constraint |
|----------|----------------------|--------------------------|-------------|---------------|
| Workato | Multi-step recipes; conditional logic; error handling; API integration | Approval actions with configurable timeout | Recipe run history | Enterprise pricing; procurement required |
| Zapier | Simple multi-step Zaps; filter/conditional; delay steps | Paths with conditional logic; no native approval gate | Zap run history | Complexity limit; not suited for durable workflows |
| Make (Integromat) | Complex scenario flows; routers; iterators; error handlers | Approval via webhook or email confirmation | Scenario execution logs | Module limits per plan; error handling requires configuration |
| n8n | Self-hosted or cloud; complex flows; code nodes; AI integrations | Custom approval node via webhook or human task | Execution logs; self-hosted = operator-managed retention | Requires technical setup for self-hosted; maintenance burden |
| Power Automate | Microsoft 365 native; Teams approval flows; SharePoint integration | Native Approval connector; Teams-based review | Audit log in Microsoft Purview | Microsoft licensing dependency; best in Microsoft environments |
| Workato / Boomi / MuleSoft | Enterprise iPaaS | Human approval via task queues or email | Comprehensive audit | Enterprise procurement; implementation partner typically required |

**Selection rule:** Prefer the organization's existing approved iPaaS. A platform already in use has established credentials, support, and procurement — lower total cost than introducing a new tool.

---

## Category 3 — Workflow Orchestration and Durable Execution

For workflows that require retries, timeouts, compensation, long-running state, or multi-step coordination beyond what iPaaS supports.

| Tool | Type | Capabilities | Limitations |
|------|------|-------------|-------------|
| Temporal | Durable workflow engine | Exactly-once semantics; retries; timeouts; sagas; compensation; durable timers | Engineering required; infrastructure to operate; learning curve |
| Apache Airflow | DAG orchestration | Complex dependencies; scheduling; retries; backfill | Python required; infrastructure to manage; no durable state within task |
| Prefect | Python-native orchestration | Similar to Airflow; cloud-managed option; better observability | Python required; less mature ecosystem than Airflow |
| GitHub Actions / CI/CD runners | Event-driven job execution | Code-defined; version-controlled; trigger on push, schedule, or API | Stateless; no long-running state; not designed for business workflows |
| Cloud schedulers (AWS EventBridge, GCP Cloud Scheduler, Azure Logic Apps) | Managed scheduling | No infrastructure to manage; native cloud integration | Cloud-vendor specific; varying feature sets |
| Serverless functions (AWS Lambda, GCP Cloud Functions, Azure Functions) | Event-driven execution | Scales to zero; low operational overhead | No native state; cold start latency; timeout limits |

**Selection rule:** Use durable workflow engines (Temporal, Airflow) when the workflow runs for minutes or hours, requires compensation on failure, or has complex multi-step dependencies. Use serverless or schedulers for simple, short, stateless tasks.

---

## Category 4 — AI Model Access Patterns

How the organization accesses AI model capabilities.

| Pattern | Description | Controls | Constraint |
|---------|-------------|----------|-----------|
| Direct API (Anthropic, OpenAI) | Application calls provider API directly | API key management; rate limits; usage monitoring | Data leaves to provider; data policy must permit |
| Azure OpenAI Service | OpenAI models via Microsoft Azure | Private endpoints; VNet integration; Microsoft compliance coverage | Azure subscription required; model availability may lag |
| Google Vertex AI | Google models (Gemini) + partner models via GCP | GCP IAM; VPC; data residency options | GCP subscription; Vertex-specific API differences |
| AWS Bedrock | Multiple models (Anthropic Claude, others) via AWS | IAM; VPC; CloudTrail audit | AWS subscription; model coverage varies |
| Local / self-hosted | Open-weight models running on org infrastructure | Full data control; no external data transfer | Engineering to deploy and maintain; performance and capability limits |
| Model gateway (LiteLLM, Portkey, etc.) | Abstraction layer over multiple providers | Provider switching; unified logging; rate limiting; fallback | Additional infrastructure layer; latency overhead |

**Selection rule:** Match to the organization's approved AI provider and data handling policy. When the workflow touches PII or regulated data, verify the provider's data processing agreements before routing data through the model.

---

## Category 5 — Human-in-the-Loop Mechanisms

For SUPERVISED workflows, a blocking human approval checkpoint is required before the terminal action.

| Mechanism | How it works | Timeout handling | Audit trail |
|-----------|-------------|-----------------|-------------|
| Email approval link | System sends email with approve/reject links | Configurable; escalation on timeout | Email delivery log; click timestamp |
| Microsoft Teams Adaptive Card | Approval card posted to Teams channel | Adaptive Card timeout; escalation flow | Teams message history; Approval connector audit |
| Slack Block Kit / workflow | Message with action buttons in Slack | No native timeout — requires external timer | Slack audit logs (paid plans) |
| Dedicated approval platform (Jira, ServiceNow, Workato Tasks) | Task created in approval system | Configured in platform; SLA alerts | Platform audit trail |
| Code-enforced checkpoint | Workflow halts; resumes only on explicit API call | Custom timeout and escalation in code | Application logs |

**Selection rule:** SUPERVISED workflows require a mechanism that is **blocking** (the terminal action cannot execute without approval) and **audited** (the approval decision is logged with timestamp and approver identity). A Slack message without a blocking mechanism is not a valid approval checkpoint.

---

## Category 6 — Audit and Observability

Every autonomous workflow requires an audit trail.

| Capability | Description | Required for |
|------------|-------------|-------------|
| Structured logging | Timestamped, queryable log of each step | All autonomous workflows |
| Execution history | Full record of inputs, outputs, and decision points per run | AUTONOMOUS and SUPERVISED |
| Approval record | Who approved, when, and what they approved | SUPERVISED (mandatory) |
| Error log | Exceptions, retries, failures, and resolutions | All workflows |
| Alerting | Operator notification on failure or threshold breach | Required by GATE-5 controls |
| Retention enforcement | Log data retained for stated period; purged on schedule | Per audit requirements in packet |

**Selection rule:** GATE-5 workflows (no audit trail or rollback) cannot be AUTONOMOUS. If the current tooling does not support structured logging and retention, GATE-5 applies and the verdict is at minimum SUPERVISED.

---

## Category 7 — Agent and Interoperability Patterns

For workflows that involve AI agents coordinating with tools, systems, or other agents.

| Pattern | Description | Autonomy implication |
|---------|-------------|---------------------|
| Tool/function calling | AI model invokes named functions; results returned to model | Model controls when tools are called — deterministic constraints must be enforced outside the model |
| MCP (Model Context Protocol) | Standardized tool access for AI agents | Same as tool calling; MCP adds discoverability and authorization layer |
| Agent-to-agent handoff | One AI agent passes a task or result to another | Chain-of-responsibility audit required; each agent boundary is a control point |
| Browser/computer-use automation | AI agent operates UI directly | High risk — no API contract; UI changes break the workflow silently; requires tight scope |
| RPA | Script-driven UI automation (no AI judgment) | Deterministic; auditable; but brittle to UI changes |
| Human task queue | AI creates a task; human completes it | Native SUPERVISED pattern — AI prepares, human acts |

**Selection rule:** Tool/function calling and MCP are the preferred interoperability patterns for AI workflows. Prohibited actions and scope boundaries must be enforced at the tool layer — not in the model prompt. A model that can be prompted to invoke a prohibited tool has no real control.

---

## Selection Rules Summary

1. **Prefer approved tools.** When the organization's stack profile names a tool that satisfies the required capability, use it. Do not recommend a new tool when an existing approved one works.

2. **Capability before brand.** Match tools to required capabilities (trigger type, approval mechanism, audit trail, idempotency) — not to familiarity.

3. **Deterministic for controls.** Approval thresholds, prohibited actions, and schema validation are implemented in deterministic code or configuration. Model prompts are guidance, not enforcement.

4. **Blocking for approval checkpoints.** SUPERVISED workflows require a blocking mechanism. A notification is not a checkpoint.

5. **Audit for all autonomy.** Every autonomous workflow must have a structured, retained audit trail. No audit trail = GATE-5 applies.

6. **Technology-neutral when unknown.** When the stack profile is absent, describe required capabilities. Name specific tools only when the stack is confirmed.
