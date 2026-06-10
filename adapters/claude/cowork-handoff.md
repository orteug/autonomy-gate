# Cowork Handoff — Autonomy Gate Adapter

Use this after the Gate has issued an `AUTONOMOUS / COWORK` or `SUPERVISED / COWORK` verdict and produced a Cowork Project Config artifact. This file translates the artifact into a working Cowork setup.

---

## Before You Start

Read the full Cowork Project Config artifact before touching Cowork. The artifact contains:
- The governing Autonomy Decision Packet (verdict, terminal action, controls)
- The folder structure to create
- The project instructions to paste
- The run schedule
- The terminal statuses the run must emit
- The approval checkpoint (SUPERVISED only)
- The AUTONOMY EXPIRES WHEN conditions

Every field in the artifact is a requirement, not a suggestion.

---

## Setup Steps

**Step 1 — Create the folder structure**

The artifact names the required folders. Standard structure for Cowork workflows governed by the Gate:

```
/[workflow-name]/
├── /inputs          ← Source data files, exports, trigger documents
├── /outputs         ← Completed run outputs, formatted reports, processed files
├── /logs            ← Terminal status per run: timestamp, status, notes
└── /archive         ← Completed outputs moved after review (SUPERVISED) or retention window (AUTONOMOUS)
```

Create exactly the folders named in the artifact. Do not add folders not listed without re-running the Gate on the updated scope.

**Step 2 — Set the project instructions**

In your Cowork project settings, paste the CUSTOM INSTRUCTIONS block from the artifact verbatim. The instructions encode the allowed actions, prohibited actions, terminal action boundary, and audit requirements.

**Step 3 — Configure the run schedule**

Set the schedule from the artifact's RUN CADENCE field. If the artifact does not specify a schedule (human-initiated fallback), configure Cowork for manual trigger only.

**Step 4 — Implement the terminal status log**

Every Cowork run governed by the Gate must emit one of the following terminal statuses and write it to `/logs`:

```
[YYYY-MM-DD HH:MM] [WORKFLOW NAME] — COMPLETED
[YYYY-MM-DD HH:MM] [WORKFLOW NAME] — COMPLETED_WITH_WARNINGS: [description]
[YYYY-MM-DD HH:MM] [WORKFLOW NAME] — NEEDS_REVIEW: [description + escalation path]
[YYYY-MM-DD HH:MM] [WORKFLOW NAME] — BLOCKED: [what caused the block]
[YYYY-MM-DD HH:MM] [WORKFLOW NAME] — FAILED: [failure mode + recovery action taken]
```

The log entry must be written before the run is considered complete. A run with no log entry is an unobservable run — this triggers GATE-5 conditions and invalidates the AUTONOMOUS verdict.

**Step 5 — Configure the approval checkpoint (SUPERVISED only)**

If the verdict is SUPERVISED: the terminal action must not execute until the named reviewer has approved the run output. Implement this as a hold in `/outputs` — the output file is written and held; execution of the terminal action is blocked until the reviewer confirms.

The reviewer's approval must be logged in `/logs` with their name, the run date, and their decision (approved / rejected / returned for revision).

**Step 6 — Test before going live**

Run one test cycle with non-production data. Verify:
- [ ] Folder structure matches the artifact spec
- [ ] Terminal status is written to `/logs` after each run
- [ ] Output is in the format specified in the artifact
- [ ] Approval checkpoint blocks terminal action (SUPERVISED only)
- [ ] Run produces the correct terminal status for a BLOCKED or FAILED scenario

---

## Fallback if Cowork Is Unavailable

The artifact's fallback note names what to do. Standard fallback to PROJECT:

1. Human initiates each run manually on the intended schedule
2. Source data is pasted into the Claude Project session
3. Output is reviewed and delivered manually
4. Log entry is maintained manually in a shared doc

The autonomy verdict (AUTONOMOUS or SUPERVISED) does not change with the surface fallback. The controls and approval checkpoint still apply.

---

## Recertification

When any condition in the artifact's AUTONOMY EXPIRES WHEN section is met, the Cowork project must be paused. Re-run the Gate on the updated workflow. Do not resume until a new verdict is issued and the Cowork setup is updated to match.

Log the recertification trigger and outcome in `/logs`:
```
[YYYY-MM-DD] RECERTIFICATION TRIGGERED: [condition met]
[YYYY-MM-DD] RECERTIFICATION OUTCOME: [new verdict] — Cowork setup updated per new artifact
```
