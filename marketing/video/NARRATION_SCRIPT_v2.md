# Narration Script — The Autonomy Gate Demo Video
**Version:** v2 — reviewed against live system (2026-06-13)
**Previous version:** v1 (2026-06-09) — archived in `_archive/pre-git-working-copy/production-assets/`
**Changes from v1:** Surface axis removed (not a second verdict axis in the current system); verdict format corrected; file count updated; platform mention expanded.

---

## Script Notes

- `[PAUSE]` = 0.5–0.8 second silence in synthesis. Insert at every key concept landing.
- `[LONG PAUSE]` = 1.0–1.5 second silence. Used before and after GATE-2 naming in Act 4.
- `[BEAT]` = 0.3 second silence. Separates clauses within a sentence.
- All emphasis is through pacing, not pitch. Chatterbox synthesis parameters should hold flat delivery — the pauses do the work.
- Total narrated runtime target: ~3:30–3:45. With on-screen action time in Acts 3–4, full video lands at 4:30–4:40.

---

## Act 1 — The Problem
*Screen: Title card — "This was built by a system — the same framework it's designed to run."*
*Then: Flowchart building — three branches from "Can we automate this?"*

---

During a job application, [PAUSE] I was handed a stack of workflows [PAUSE] and asked to decide what to automate.

The real work was not building the automations. [PAUSE] It was deciding which ones should exist at all. [PAUSE] How much authority each one deserved. [PAUSE] And what would happen if they were wrong.

I didn't have a framework to do that. [PAUSE] I couldn't finish the task.

[PAUSE]

The Autonomy Gate is the tool I would have needed.

[PAUSE]

Every automation decision collapses to the same three paths. [BEAT] Over-automate — [BEAT] the system runs something it shouldn't. [PAUSE] Under-automate — [BEAT] the tool exists but nothing changes. [PAUSE] Or minimum justified autonomy — [BEAT] the right level, with the right controls, for what the workflow actually is.

[PAUSE]

The Gate decides which path. [PAUSE] Not by asking what you want. [PAUSE] By running the evidence.

---

## Act 2 — What the Gate Decides
*Screen: Four verdict labels building. Gates appearing. Six artifact types branching.*

---

The Gate issues one verdict on every workflow. [PAUSE] Four possible outcomes.

Autonomous. [PAUSE] Supervised. [PAUSE] SOP First. [PAUSE] Or Human Only.

[PAUSE]

The verdict is not a label — [BEAT] it is a decision about the terminal action. [PAUSE] What the workflow actually executes last. [PAUSE] Not what it's called.

[PAUSE]

Above the scoring: five hard gates. [PAUSE] GATE-1 through GATE-5. [PAUSE] Structural conditions that override any scoring. [PAUSE] If the terminal action triggers a gate — [BEAT] the verdict changes. [PAUSE] Regardless of what the base scoring produced.

[PAUSE]

The verdict maps to one of six execution artifacts. [PAUSE] An Automation Architecture. A Project Setup Brief. A Cowork Config. A Control Plan. A Stabilization Plan. Or a Governance Memo. [PAUSE] Each one is a complete execution document — [BEAT] readable in a meeting, [BEAT] without additional context.

[LONG PAUSE]

Not every workflow that AI can do should be autonomous. [PAUSE] The Gate decides the minimum autonomy level justified by the evidence.

---

## Act 3 — Live Demo: Workflow 1
*Screen: OBS — Claude Project. Weekly KPI report workflow paste. Output generating.*
*Reference artifact: `examples/artifacts/project-setup-brief.html`*

---

First workflow. [PAUSE] Weekly KPI report. [PAUSE] Pipeline, revenue, and support volume. [PAUSE] A team member exports the data, pastes it in, and receives a formatted Slack-ready summary — ready to post. [PAUSE] Monday morning. Every week.

[PAUSE]

Three outputs. Always in this order.

*[Screen: Scroll to WORKFLOW INTAKE SNAPSHOT header]*

The Workflow Intake Snapshot. [PAUSE] Every assessment begins here. [PAUSE] The Gate normalizes the input, populates every field it can, and names the fields it cannot. [PAUSE] This is the audit trail that makes the verdict trustworthy.

*[Screen: Scroll to AUTONOMY DECISION PACKET header]*

The Autonomy Decision Packet. [PAUSE] Verdict: Autonomous. [PAUSE] Confidence: High. [PAUSE] Every required snapshot field populated. [PAUSE] Adversarial check passed. [PAUSE] No gate conditions triggered.

*[Screen: Scroll to PROJECT SETUP BRIEF header — artifact]*

The execution artifact. [PAUSE] Project Setup Brief. [PAUSE] Complete. [PAUSE] Ready to configure a Claude Project.

[PAUSE]

This is the clean case. [PAUSE] All four autonomy criteria pass. [PAUSE] Reversible. Observable. Low exception rate. Low failure consequence. [PAUSE] No gates triggered. [PAUSE] Autonomous is the correct verdict.

---

## Act 4 — Live Demo: Workflow 2 — The Hard Case
*Screen: OBS — Claude Project. Vendor bank account change workflow paste.*
*Reference artifact: `examples/artifacts/governance-memo.html`*

---

Second workflow. [PAUSE] A vendor has emailed asking to update their bank account details before the next invoice cycle. [PAUSE] Can we automate the verification and update?

[PAUSE]

*[Screen: WORKFLOW INTAKE SNAPSHOT visible — cursor moves to terminal action field]*

Phase 1 runs. [PAUSE] The Gate identifies the terminal action — [BEAT] not the label on the workflow, [BEAT] the last thing that actually executes.

[PAUSE]

The label is "verification and update." [PAUSE] The terminal action is: [BEAT] authorize a payment routing change.

[PAUSE]

*[Screen: AUTONOMY DECISION PACKET visible — GATE-2 cited]*

[LONG PAUSE]

This is GATE-2. [LONG PAUSE] Irreversible external commitment. [PAUSE] The Gate does not suppress this. [PAUSE] It escalates it.

[PAUSE]

Vendor bank account fraud is the second-largest category of financial crime by loss volume. [PAUSE] Funds wired to a fraudulent account are recovered in fewer than sixty percent of cases — [BEAT] even when flagged immediately. [PAUSE] The workflow sounds rule-based. [PAUSE] The terminal action is an exact attack surface.

[PAUSE]

Verdict: Human Only. [PAUSE] GATE-2 cited by name.

*[Screen: GOVERNANCE MEMO artifact visible — scroll to "Why this cannot be delegated" section]*

[PAUSE]

The execution artifact: Governance Memo. [PAUSE] Why this cannot be delegated — [BEAT] gate condition, specific risk, human review process, and what would need to change for the verdict to change. [PAUSE] A complete document. [PAUSE] Cite it in a meeting. [PAUSE] The Gate said no, [BEAT] with authority, [BEAT] citing a named mechanism.

[PAUSE]

No other system in this competition can do that.

---

## Act 5 — Why This Architecture
*Screen: Act 2 diagram returns. Pipeline stages layer in. Opinion card.*

---

The diagram from Act 2 — now with three more layers visible.

Rule Zero: [PAUSE] The Gate always issues a verdict. [PAUSE] It never asks. [PAUSE] Every input produces three sections. [PAUSE] Without exception.

Minimum Signal Threshold: [PAUSE] Four required fields. [PAUSE] If any are missing, confidence is capped at Low. [PAUSE] The verdict is still issued — [BEAT] but the gaps are named.

Adversarial Check: [PAUSE] Before issuing any verdict, the Gate challenges itself. [PAUSE] Is this the minimum justified autonomy, or is there pressure to over-automate? [PAUSE] What is the most likely failure mode if this verdict is wrong? [PAUSE] Does the terminal action trigger any gate condition the base scoring missed?

[PAUSE]

*[Screen: Opinion card building line by line]*

[LONG PAUSE]

Businesses do not just need more automations.

[PAUSE]

They need to know which automations should exist, [PAUSE] which should not, [PAUSE] and what controls make them trustworthy.

[PAUSE]

That is what the Gate answers.

[PAUSE]

*[Screen: Repo structure visible, Claude Project instruction, competition link]*

Sixteen runtime files. [PAUSE] One project instruction. [PAUSE] Runs on Claude Projects and ChatGPT Projects. [PAUSE] Paste any workflow. [PAUSE] Get a verdict, a justification, and a complete execution document — [BEAT] in one pass, without asking back.

[PAUSE]

Link below.

---

## Changes from v1

| Location | v1 (stale) | v2 (corrected) |
|----------|-----------|----------------|
| Act 2 | "The autonomy axis... The surface axis — Project, Cowork, Code Agent, or no AI at all" | Single verdict axis (AUTONOMOUS/SUPERVISED/SOP_FIRST/HUMAN_ONLY); implementation architecture is a separate selection, not a second verdict axis |
| Act 3 | "Verdict: Autonomous / Project" | "Verdict: Autonomous · Confidence: High" (format matches current Decision Packet) |
| Act 4 | "Verdict: Human Only / No AI" | "Verdict: Human Only" (NO_AI phrasing retired; verdict is HUMAN_ONLY) |
| Act 4 | "WHY THIS CANNOT BE DELEGATED section" | "Why this cannot be delegated section" (matches actual section label in governance-memo.html) |
| Act 5 | "The folder is five files. One Claude Project." | "Sixteen runtime files. Runs on Claude Projects and ChatGPT Projects." |

---

## Word Count / Runtime Estimate

| Act | Approximate word count | Estimated spoken time at deliberate pace |
|-----|----------------------|----------------------------------------|
| Act 1 | ~130 words | ~55s |
| Act 2 | ~130 words | ~55s |
| Act 3 | ~105 words | ~45s |
| Act 4 | ~175 words | ~75s |
| Act 5 | ~120 words | ~55s |
| **Total** | **~660 words** | **~5:05 narration time** |

If the final assembly runs long: Act 3 narration can trim the Snapshot explanation paragraph without losing meaning. Act 5 can trim the Adversarial Check to one sentence. Do not cut Act 4 — the GATE-2 beat must have full room.

---

## Gate Status

Script is ready for voice synthesis. Gated on Ariel's voice sample.
