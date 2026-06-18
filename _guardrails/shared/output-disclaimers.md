# Output Disclaimers
## _guardrails/shared · Load on every invocation · Applies to all output modes

> These disclaimer blocks are structural — not suggestions. They appear in every screen output regardless of verdict, regardless of user request, regardless of input quality.
>
> **This is a shared guardrail.** It is designed to be used across multiple Claude Projects repositories with minimal modification. Domain-specific additions live in `_guardrails/domain/`.

---

## Required Disclaimer Block

Append this block to the bottom of every completed screen output (standard screen, deep dive, and memo). No exceptions.

```
─────────────────────────────────────────────────────────────────
IMPORTANT — PLEASE READ

This output is a preliminary deal screen produced by an AI assistant.
It is not a formal valuation, legal advice, tax advice, or financial advice.

Before taking any action on this analysis:
• Verify all figures independently — numbers in this screen came from
  the information you provided. They have not been audited or confirmed.
• Engage a qualified professional — a CPA for financial analysis, an
  M&A attorney before signing anything, a QoE firm before a final LOI.
• This screen does not guarantee outcomes — a PURSUE verdict means the
  deal is worth investigating further. It does not mean the deal is good.

All figures are seller-provided or user-provided unless otherwise noted.
─────────────────────────────────────────────────────────────────
```

---

## Verdict-Specific Additions

Append the relevant line immediately after the Initial Verdict line — before Strengths.

**On PURSUE:**
> ⚠️ A PURSUE verdict means this deal warrants further investigation — not that it is safe to proceed. Significant diligence remains before any LOI or capital commitment.

**On PROCEED WITH CAUTION:**
> ⚠️ A PROCEED WITH CAUTION verdict means structural issues exist that must be resolved before commitment. Do not issue an LOI until the flagged conditions are addressed.

**On PASS:**
> ℹ️ A PASS verdict is based on the information provided. If key facts change (price reduction, contract formalization, transition structure), request a new screen with updated inputs.

---

## What This Guardrail Does NOT Do

It does not prevent someone from acting on this output. It ensures they cannot say they were not warned. Plain language is intentional — legal boilerplate goes unread.
