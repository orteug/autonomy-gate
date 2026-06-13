# Gate Workspace Setup

This guide walks an operator through configuring a persistent Gate workspace: a Claude Project or ChatGPT Project where the Gate's files live permanently and the operator's organization profile is always available.

A configured workspace means: no re-uploading files, no re-explaining organizational context, and a consistent set of governance defaults applied to every workflow the operator submits.

---

## What Goes in the Workspace

**Permanent files — always present:**

These files are uploaded once and never removed. They define the Gate's behavior.

| File | Purpose |
|------|---------|
| `identity.md` | Gate identity, two-phase flow, design constraints |
| `rules.md` | Complete decision logic (RULE-00 through RULE-15) |
| `examples.md` | Calibration examples for 14 workflow types |
| `autonomy-criteria.md` | Scoring criteria for the four autonomy dimensions |
| `risk-classification.md` | Risk classification reference |
| `surface-capability-matrix.md` | What each execution surface can and cannot do |
| `precedents.md` | Prior decisions and governance precedents |
| `operating-contract.md` | Canonical lifecycle, architecture selection, handoff statuses, and authority boundaries |
| `template-project-setup.md` | Artifact template: AUTONOMOUS with a human-triggered knowledge-work architecture |
| `template-control-plan.md` | Artifact template: SUPERVISED |
| `template-automation-architecture.md` | Artifact template: AUTONOMOUS with a code-first, service, or integration architecture |
| `template-cowork-config.md` | Artifact template: COWORK |
| `template-governance-memo.md` | Artifact template: HUMAN_ONLY |
| `template-stabilization-plan.md` | Artifact template: SOP_FIRST |
| `operator-disposition.md` | Four disposition states and transition rules |
| `tool-selection-rules.md` | Tool substitution and selection constraints |

Total: 16 files. These are the canonical runtime files. Do not remove or rename them.

**Organization profile — loaded at session start:**

Your organization profile (`organization-profile.md`) is either:
- Uploaded to the workspace as a permanent file (recommended for team workspaces), or
- Pasted at the beginning of each session using the CONFIGURE trigger

For a personal workspace, paste the profile. For a shared team workspace, upload it as a 17th permanent file.

**Workflow artifacts — session-specific:**

Completed governance artifacts (execution documents + Build Handoff Packs) are not stored in the workspace. They belong in your workflow record system (folder, Notion, shared drive, or equivalent). The Gate does not archive completed artifacts across sessions.

---

## Personal Operator Workspace

For a single operator assessing workflows on their own.

**Setup:**

1. Create a new Claude Project or ChatGPT Project named "Autonomy Gate" (or equivalent).
2. Upload the 16 canonical runtime files listed above. In Claude Project, also upload `artifact-rendered.html` as the seventeenth project file.
3. Set the project instruction to:
   ```
   You are The Autonomy Gate. Follow identity.md, rules.md, and operating-contract.md. Produce canonical Markdown, then create a separate rendered Claude Artifact for the complete Execution Artifact using artifact-rendered.html. Do not print HTML source in chat. Preserve exact semantic parity. If rendering is unavailable, state ARTIFACT_RENDERING_UNAVAILABLE and return Markdown only.
   ```
4. At the start of each session, paste your organization profile using CONFIGURE mode:
   ```
   CONFIGURE: [paste your organization-profile.md content here]
   ```
5. Submit workflow descriptions. Receive governed assessments. Record operator dispositions. Store completed artifacts externally.

**What persists across sessions:** The 16 canonical runtime files, the Claude HTML design reference where used, and any uploaded organization profile. Conversation history where supported.

**What does not persist:** Evidence supplied mid-session that was not saved to a file. Operator dispositions not recorded in an external artifact.

---

## Shared Team Workspace

For a team of operators assessing workflows together, with shared governance defaults.

**Setup:**

1. Create a shared Claude Project or ChatGPT Project with access for all operators.
2. Upload the 16 canonical runtime files. In Claude Project, also upload `artifact-rendered.html`.
3. Upload your organization profile as a 15th file (`organization-profile.md`).
4. Set the project instruction to:
   ```
   You are The Autonomy Gate. Follow identity.md, rules.md, and operating-contract.md. Apply organization-profile.md as inherited evidence requiring workflow-level applicability confirmation.
   ```
5. Establish an artifact naming convention: `[WorkflowName]-[Date]-v[N].md`
6. Establish a shared folder (Google Drive, Notion, SharePoint) for completed artifacts.

**Access rule:** All operators who use the workspace may submit assessments. Only the named approval authorities (from the organization profile) may record `APPROVE_FOR_BUILD` dispositions.

---

## Artifact Naming and Archival

**Naming convention:**
```
[WorkflowName]-[YYYY-MM-DD]-v[N].md
```

Examples:
- `WeeklyKPIReport-2026-06-11-v1.md`
- `VendorBankChange-2026-06-11-v1.md`
- `VendorBankChange-2026-06-11-v2.md` (after REVISE disposition)

**Versioning:** Increment `v[N]` when a new packet is issued (evidence update, revision request, recertification). The version in the filename must match the `Packet version` field in the OPERATOR DISPOSITION section.

**Archival:** Retain completed artifacts according to the organization's stated records policy. If no policy is supplied, mark retention `UNKNOWN`; do not invent a duration. An expired artifact remains historical record only and cannot authorize operation.

**Access:** Completed artifacts with `APPROVE_FOR_BUILD` dispositions should be accessible to: the operator who approved, the builder who received the handoff, and any auditor who reviews the governance trail.

---

## File Upload Limits

**Claude Project:** Upload the 16 canonical runtime files plus `artifact-rendered.html`, for 17 uploaded files total. Check current plan limits before installation.

**ChatGPT Project:** Maximum 10 files per upload batch. Upload in two batches:
- Batch 1 (10 files): `identity.md`, `rules.md`, `examples.md`, `operating-contract.md`, `autonomy-criteria.md`, `risk-classification.md`, `surface-capability-matrix.md`, `precedents.md`, `template-project-setup.md`, `template-control-plan.md`
- Batch 2 (6 files): `template-automation-architecture.md`, `template-project-setup.md`, `template-control-plan.md`, `template-cowork-config.md`, `template-governance-memo.md`, `template-stabilization-plan.md`

All 16 files must be present before use. Verify by asking the Gate to list accessible runtime files and confirm `operating-contract.md` is included.

---

## Memory and Durability

Claude and ChatGPT Projects may offer conversational memory features. These can assist with convenience (remembering your name, recent workflow names) but may not be used as a substitute for durable records.

**Rely on project memory for:** Operator name, frequently used CONFIGURE profile values, preferred output format.

**Do not rely on project memory for:** Operator disposition records, packet versions, completed artifacts, or any governance-relevant decision. These must be recorded in external files.

If memory is unavailable or cleared, the Gate workspace continues to function using the uploaded files. No governance decision is lost because memory was cleared — all governance decisions live in the external artifacts.
