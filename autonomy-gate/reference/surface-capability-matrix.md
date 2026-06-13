# Surface Capability Matrix — Reference

This file is the authoritative record of what the Gate can legitimately route to. No capability claim is included without a source and date. Capabilities marked "planned," "in preview," or inferred from documentation are flagged explicitly.

Schema per row: `Capability | Surface | Supported today? | Source + date | Known limitation | Fallback`

The Gate's surface assignment in RULE-06 is constrained by this matrix. If a capability is not listed as "Yes — verified," the Gate may not route to it as primary.

Last verified: 2026-06-09

---

## SURFACE-1 — PROJECT (Claude Project)

A Claude Project is a structured workspace where the operator runs on a human-initiated cadence. It does not schedule or execute unattended work. The operator is invoked by a human pasting input; it does not trigger automatically.

| Capability | Surface | Supported today? | Source + date | Known limitation | Fallback |
|-----------|---------|-----------------|---------------|-----------------|---------|
| Custom system prompt / identity | PROJECT | Yes — verified | Anthropic Claude docs, 2026-06 | Prompt length limits apply | Use rules.md + identity.md as knowledge file |
| Knowledge file upload (PDF, MD, TXT) | PROJECT | Yes — verified | Anthropic Claude docs, 2026-06 | File size limits; no structured DB | Paste critical content into system prompt |
| Human-initiated conversation / run | PROJECT | Yes — verified | Anthropic Claude docs, 2026-06 | No scheduling; no unattended execution | COWORK for scheduled runs |
| Multi-turn context within session | PROJECT | Yes — verified | Anthropic Claude docs, 2026-06 | Context window limits apply | Summarize prior output; resubmit |
| Markdown document output | PROJECT | Yes — verified | Anthropic Claude docs, 2026-06 | Rendering depends on display context | Plain text fallback |
| Structured artifact generation (plans, memos, reports) | PROJECT | Yes — verified | Anthropic Claude docs, 2026-06 | Output is document; not executable | Handoff to CODE_AGENT for execution |
| Scheduled or unattended execution | PROJECT | No | Anthropic Claude docs, 2026-06 | Projects do not self-initiate | COWORK (if available); otherwise recurring manual run |
| File read/write on local disk | PROJECT | No | Anthropic Claude docs, 2026-06 | No filesystem access in Project | COWORK |
| External API calls | PROJECT | No | Anthropic Claude docs, 2026-06 | No tool-use in standard Project | CODE_AGENT |
| Integration with Slack, CRM, or external services | PROJECT | No | Anthropic Claude docs, 2026-06 | No connectors in standard Project | CODE_AGENT or COWORK |

**Appropriate for:** Weekly KPI reports (human-initiated), contract clause review, candidate shortlist preparation, compliance evidence summaries, any recurring analysis workflow where a human initiates each run.

**Not appropriate for:** Workflows that must run on a schedule without human initiation; workflows that require reading or writing files; workflows that require external API calls.

---

## SURFACE-2 — COWORK (Claude Cowork)

Claude Cowork supports multi-step local work with file access, scheduling, and system connectors. It can execute unattended on a schedule.

| Capability | Surface | Supported today? | Source + date | Known limitation | Fallback |
|-----------|---------|-----------------|---------------|-----------------|---------|
| Scheduled / unattended execution | COWORK | Yes — verified | Anthropic Claude Cowork docs, 2026-06 | Requires Cowork access (not universally available) | PROJECT with manual initiation |
| Local file read/write | COWORK | Yes — verified | Anthropic Claude Cowork docs, 2026-06 | Scoped to designated local folders | Explicit folder permissions required |
| Structured folder I/O (/inputs, /outputs, /logs) | COWORK | Yes — verified | Anthropic Claude Cowork docs, 2026-06 | Folder structure must be pre-established | Manual file management as fallback |
| Multi-step pipelines within one session | COWORK | Yes — verified | Anthropic Claude Cowork docs, 2026-06 | Session length and context limits apply | Break into staged runs |
| Terminal status emission (COMPLETED, FAILED, etc.) | COWORK | Yes — verified | Anthropic Claude Cowork docs, 2026-06 | Log must be configured explicitly | Manual log file in /logs folder |
| External API calls via connector | COWORK | Yes — in preview | Anthropic Claude Cowork docs, 2026-06 | Preview status — verify availability before routing | CODE_AGENT for stable API integration |
| Integration with Google Drive, Notion, Slack | COWORK | Yes — in preview | Anthropic Claude Cowork docs, 2026-06 | Connector availability varies by plan | CODE_AGENT with explicit API auth |
| Code execution | COWORK | No | Anthropic Claude Cowork docs, 2026-06 | Cowork is not a code execution environment | CODE_AGENT |
| Access to production databases | COWORK | No | Anthropic Claude Cowork docs, 2026-06 | Read via file export only | CODE_AGENT with read-only DB connector |

**Appropriate for:** Internal Slack digest from meeting notes, automated daily ops reports, support ticket triage routing, bounded backlog processing with review packets.

**Fallback if COWORK unavailable:** Use SURFACE-1 (PROJECT) with manual cadence. Artifact must state: "If Cowork is unavailable, the nearest alternative is PROJECT with the following adjustments: (1) human initiates each run manually on the scheduled cadence, (2) output is pasted into Slack manually, (3) log file must be maintained manually."

---

## SURFACE-3 — CODE_AGENT (Claude Code / Codex)

Claude Code and Codex support deterministic workflows, scripts, integrations, and enforcement logic. They can read and write to systems via APIs and execute code.

| Capability | Surface | Supported today? | Source + date | Known limitation | Fallback |
|-----------|---------|-----------------|---------------|-----------------|---------|
| Code generation and execution | CODE_AGENT | Yes — verified | Anthropic Claude Code docs, 2026-06 | Sandboxed; requires explicit system permissions | COWORK for file-based workflows |
| System-to-system integration via API | CODE_AGENT | Yes — verified | Anthropic Claude Code docs, 2026-06 | API credentials must be provisioned separately | Manual export/import as interim |
| Deterministic logic enforcement | CODE_AGENT | Yes — verified | Anthropic Claude Code docs, 2026-06 | Logic must be explicitly specified; no inference | SUPERVISED with a human-triggered review architecture for ambiguous rules |
| Scheduled execution via cron or trigger | CODE_AGENT | Yes — verified | Anthropic Claude Code docs, 2026-06 | Scheduling infrastructure must be set up by operator | COWORK for simpler scheduling |
| Database read/write | CODE_AGENT | Yes — verified | Anthropic Claude Code docs, 2026-06 | Permissions scoped to minimum required | Read-only by default; write requires explicit provisioning |
| Audit log generation | CODE_AGENT | Yes — verified | Anthropic Claude Code docs, 2026-06 | Log destination must be configured | Output to flat file if no log service |
| Rollback execution | CODE_AGENT | Yes — conditional | Anthropic Claude Code docs, 2026-06 | Only if rollback logic is coded explicitly | SUPERVISED with human-triggered review if rollback is not implemented |
| Human approval checkpoint (pre-execution) | CODE_AGENT | Yes — conditional | Anthropic Claude Code docs, 2026-06 | Approval must be coded as blocking step | SUPERVISED with human-triggered review for natural-language approval |
| Self-scheduling / autonomous recurrence | CODE_AGENT | Yes — conditional | Anthropic Claude Code docs, 2026-06 | Requires cron or event trigger configured by operator | COWORK |
| External UI rendering | CODE_AGENT | No | Anthropic Claude Code docs, 2026-06 | Terminal/API output only | PROJECT for human-readable formatted output |

**Appropriate for:** Refund eligibility assessment, lead enrichment and CRM routing, monthly financial close reconciliation, invoice matching, access permission preparation packet, social media scheduling with approval gate, bounded backlog automation.

**Not appropriate for:** Workflows that require natural-language review by a non-technical reviewer (use PROJECT); workflows that need to run without any infrastructure setup (use COWORK or PROJECT).

---

## SURFACE-4 — NO_AI

No surface assigned. Pairs only with SOP_FIRST (AUT-3) and HUMAN_ONLY (AUT-4).

| Capability | Surface | Supported today? | Source + date | Known limitation | Fallback |
|-----------|---------|-----------------|---------------|-----------------|---------|
| Human decision-making | NO_AI | Yes — always | N/A | Requires named human owner with authority | N/A |
| Manual process execution | NO_AI | Yes — always | N/A | Consistency depends on documentation quality | SOP development as prerequisite |
| Governance memo / stabilization plan documentation | NO_AI | Yes — always | N/A | N/A | N/A |

**Assigned when:** Terminal action triggers GATE-2 or GATE-3 (HUMAN_ONLY), or when exception rate is undocumented/high (SOP_FIRST). The workflow is not ready for AI authority on any surface.

---

## Surface Selection Decision Tree

```
Is the workflow a deterministic integration or script? → CODE_AGENT
↓ No
Does it need to run on a schedule without human initiation? → COWORK (if available) → else PROJECT with manual cadence
↓ No
Is it a human-initiated recurring analysis or document? → PROJECT
↓ No criteria match
Does ANY gate condition apply? → NO_AI (paired with HUMAN_ONLY or SOP_FIRST)
```

---

## Fallback Logic — Required in Every Artifact

Per RULE-06: if the preferred implementation tool is unavailable, the architecture comparison must name a fallback and explain any control, trigger, logging, or operating adjustments. Silent substitution is not acceptable.

**Standard fallback text by surface:**

**If COWORK is recommended but unavailable:**
> If Cowork is unavailable, the nearest alternative is PROJECT (Claude Project) with the following adjustments: (1) initiate each run manually on the intended schedule, (2) deliver output to the destination channel manually, (3) maintain a manual log file recording each run date, output location, and any errors or anomalies.

**If CODE_AGENT is recommended but unavailable:**
> If Claude Code or Codex is unavailable, the nearest alternative is PROJECT (Claude Project) with the following adjustments: (1) paste each data export into the Project session manually, (2) request the analysis or document as a structured output, (3) a technical resource must implement the integration or scheduling separately before full automation is possible. The Project handles the reasoning layer; the execution layer requires separate setup.
