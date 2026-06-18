# Escalation Triggers
## _guardrails/shared · Load on every invocation · Applies to all screen modes

> Hard gates that require professional involvement before specific actions. These appear in the output as visible blocks — they are not suggestions buried in prose.
>
> **This is a shared guardrail.** Domain-specific triggers live in `_guardrails/domain/`. When both fire, both blocks appear.

---

## How Escalation Triggers Work

When a trigger condition is met, a `🔴 PROFESSIONAL REQUIRED` block appears in the output immediately before the Next Step Recommendation. The user cannot miss it.

Escalation triggers do NOT change the verdict. A PURSUE remains PURSUE. The trigger tells the user what professional action must precede any next step.

---

## Trigger Table

| Condition | Trigger fires | Required professional |
|-----------|--------------|----------------------|
| Any PURSUE verdict | Always | QoE firm or business broker review before LOI |
| Asking price >$500K | Always | SBA lender pre-qualification before approaching seller |
| Any LOI discussion or recommendation | Always | M&A attorney review before signing |
| DSCR <1.5× at asking price | Always | CPA or lender review of debt service model |
| SDE is self-reported with no P&L reference | Always | CPA to verify SDE before advancing |
| Any mention of earnout, seller note, or performance clause | Always | M&A attorney to review structure |
| Customer concentration >25% in top account | Always | Seller must introduce buyer to that client before LOI |
| Owner is the sole license holder | Always | Licensing attorney in the relevant state before LOI |

---

## Escalation Block Format

```
─────────────────────────────────────────────────────────────────
🔴 PROFESSIONAL REQUIRED — Before Your Next Step

[One or more of the following apply to this deal:]

• [Trigger 1]: [Plain-language explanation of why a professional is needed here
  and what specifically they should review. 2–3 sentences max. No jargon.]

• [Trigger 2]: [Same format.]

These are not optional. Taking action on this deal without the relevant
professional review increases your risk significantly.
─────────────────────────────────────────────────────────────────
```

---

## Example Escalation Block

```
─────────────────────────────────────────────────────────────────
🔴 PROFESSIONAL REQUIRED — Before Your Next Step

• QoE Review (PURSUE verdict): This screen says the deal is worth
  pursuing. That means it's time to verify the numbers — not act on them.
  A Quality of Earnings review confirms whether the SDE is real, sustainable,
  and transferable. Budget $8K–$20K for this step before you commit capital.

• SBA Lender Pre-Qualification (asking price >$500K): You cannot approach
  this seller credibly without knowing what you can borrow. Get pre-qualified
  first. It also tells you if this deal can be financed at the asking price —
  if the DSCR doesn't work, the price needs to change before you proceed.

• M&A Attorney (LOI recommended): An LOI is a legal document even when
  it says "non-binding." The exclusivity clause, deposit terms, and carve-outs
  matter. A one-hour review with an M&A attorney before signing costs less
  than one clause going wrong.

These are not optional. Taking action on this deal without the relevant
professional review increases your risk significantly.
─────────────────────────────────────────────────────────────────
```

---

## What Escalation Triggers Are NOT

They are not a liability shield for the tool. They are there because the tool is designed to help users make better decisions — and better decisions at this stage of an acquisition require professional input. A user who gets a PURSUE and immediately approaches a seller without QoE or lender pre-qualification is making a predictably worse outcome more likely. The trigger exists to interrupt that path.
