# The Autonomy Gate — Documentation

**Documentation version:** 1.0  
**Last verified:** 2026-06-10  
**Platform claims verified through:** 2026-06-10

---

## What Is The Autonomy Gate?

The Autonomy Gate is an AI operator that receives a description of any recurring organizational workflow and produces three things: whether AI should run it, at what level of authority, and exactly what to do next — in one pass, without asking clarifying questions.

It is a decision layer, not an executor. The Gate governs workflows. It does not run them.

---

## Start Here

| If you are... | Read this first |
|---|---|
| New to the Gate | [START_HERE.md](START_HERE.md) |
| Setting up for the first time | [OWNER_MANUAL.md](OWNER_MANUAL.md) |
| Looking for a specific workflow type | [USE_CASE_COOKBOOK.md](USE_CASE_COOKBOOK.md) |
| Reading a verdict you just received | [VERDICT_PLAYBOOK.md](VERDICT_PLAYBOOK.md) |
| Troubleshooting an unexpected result | [TROUBLESHOOTING.md](TROUBLESHOOTING.md) |
| Building a governance stack | [GOVERNANCE_REGISTRY_TEMPLATE.md](GOVERNANCE_REGISTRY_TEMPLATE.md) |
| Running the Gate across an organization | [POWER_USER_GUIDE.md](POWER_USER_GUIDE.md) |

---

## Full Document Index

### Core Guides

- [START_HERE.md](START_HERE.md) — First-time setup, five-minute install, and first test run
- [OWNER_MANUAL.md](OWNER_MANUAL.md) — Complete product reference, scoring logic, and all verdict types
- [VERDICT_PLAYBOOK.md](VERDICT_PLAYBOOK.md) — Every verdict combination mapped to allowed actions, required steps, and failure modes
- [USE_CASE_COOKBOOK.md](USE_CASE_COOKBOOK.md) — Real workflow scenarios organized by user situation
- [ARTIFACT_GUIDE.md](ARTIFACT_GUIDE.md) — What each execution artifact is, who uses it, and what done looks like
- [TROUBLESHOOTING.md](TROUBLESHOOTING.md) — What to do when output surprises you
- [GOVERNANCE_REGISTRY_TEMPLATE.md](GOVERNANCE_REGISTRY_TEMPLATE.md) — Registry schema, audit methodology, and recertification cadence
- [POWER_USER_GUIDE.md](POWER_USER_GUIDE.md) — Pre-qualifying workflows, live meeting protocol, extending the Gate, compliance evidence
- [GLOSSARY.md](GLOSSARY.md) — All terms used across the documentation

### Surface Guides

Use these after the Gate assigns a surface verdict.

- [surfaces/claude-project.md](surfaces/claude-project.md) — Claude Project setup and deployment
- [surfaces/chatgpt-project.md](surfaces/chatgpt-project.md) — ChatGPT Project setup and deployment
- [surfaces/cowork.md](surfaces/cowork.md) — Cowork setup, folder structure, and terminal status
- [surfaces/claude-code.md](surfaces/claude-code.md) — Claude Code setup, CLAUDE.md template, and enforcement
- [surfaces/codex.md](surfaces/codex.md) — Codex setup, AGENTS.md template, and sandbox policy

### Reference

- [reference/SOURCES.md](reference/SOURCES.md) — Platform sources and verified capability assumptions

---

## The Operator Files

The Gate runs inside Claude Projects or ChatGPT Projects. Upload these 14 files from the `autonomy-gate/` folder:

```text
identity.md
rules.md
examples.md
README.md
reference/autonomy-criteria.md
reference/risk-classification.md
reference/surface-capability-matrix.md
reference/precedents.md
reference/templates/template-automation-architecture.md
reference/templates/template-project-setup.md
reference/templates/template-cowork-config.md
reference/templates/template-control-plan.md
reference/templates/template-stabilization-plan.md
reference/templates/template-governance-memo.md
```

See [START_HERE.md](START_HERE.md) for complete setup instructions.

---

## Quick Verdict Reference

| You described this... | Likely verdict |
|---|---|
| Internal report, stable data, no external delivery | `AUTONOMOUS / PROJECT` |
| Report that needs to run on schedule without human initiation | `AUTONOMOUS / COWORK` |
| Script reading from a system to route or enrich data | `AUTONOMOUS / CODE_AGENT` |
| Any workflow ending with initiating a payment | `SUPERVISED` — GATE-1 |
| Any workflow ending with publishing externally | `SUPERVISED` — GATE-4 |
| Any workflow where exceptions are undocumented | `SOP_FIRST` |
| Any workflow ending with filing a regulatory document or changing a payment routing number | `HUMAN_ONLY` — GATE-2 |
| Any workflow that grants or revokes system access | `HUMAN_ONLY` — GATE-3 |

---

*The Autonomy Gate — minimum justified autonomy for every workflow.*
