# Adversarial Input Flags
## _guardrails/shared · Load on every invocation · Applies to all screen modes

> Detects patterns in user-provided input that suggest the information is one-sided, incomplete in a non-random way, or framed to produce a favorable verdict. Fires a visible warning in the output.
>
> **This is a shared guardrail.** Domain-specific patterns live in `_guardrails/domain/`. This file covers patterns common to any business acquisition.

---

## Why This Guardrail Exists

Broker memos and seller presentations are marketing documents. They are written to make a deal look attractive. A user who pastes a broker memo into the analyst is giving the analyst seller-optimized inputs — and the analyst will produce a screen based on what it was told.

This guardrail does not prevent that. It flags it so the user knows to verify independently before acting.

---

## Flag Patterns

When any of the following appear in the input, a `⚠️ INPUT INTEGRITY FLAG` block appears in the output before the Deal Summary.

### Financial Framing Flags

| Pattern | Flag reason |
|---------|------------|
| SDE described as "adjusted" without itemized add-backs | Adjusted SDE without detail is unverifiable. Common inflator in seller presentations. |
| Revenue described as "stabilizing" or "turning around" without 3-year figures | Directional language without data. The trend could be worsening. |
| EBITDA margin significantly higher than SDE margin with no explanation | Suggests owner compensation is being added back inconsistently. |
| "Owner takes a below-market salary" without a stated comparable market salary | Classic SDE inflator — "market salary" is doing unknown work here. |
| Revenue figures given as TTM without specifying the trailing period | TTM cherry-picking — a business with a strong Q4 can show a favorable TTM ending December. |
| "Recurring revenue" stated without specifying contract terms or renewal rates | Recurring is a spectrum. Month-to-month with no lock-in is not the same as 3-year auto-renew. |

### Operational Framing Flags

| Pattern | Flag reason |
|---------|------------|
| "Owner is ready to transition" without specifying transition length or role | "Ready to transition" is not a transition plan. |
| Customer concentration mentioned as "well-diversified" without top-client percentages | Diversification without data is a claim, not a fact. |
| "Strong team in place" without headcount or tenure detail | Who, how many, how long — all unknown. |
| Reason for sale stated as "retirement" for owner under 55 | Retirement at under 55 is possible but warrants verification. Common cover story. |
| "Growth opportunity" language without specifying what has prevented that growth | If growth was easy, the current owner would have captured it. |

### Deal Structure Flags

| Pattern | Flag reason |
|---------|------------|
| Seller note offered upfront (in listing) as a feature | Sellers who lead with seller note may be signaling that SBA financing will be difficult. |
| Asking price stated as "negotiable" without any anchor | Either the price is meaningless or the seller has already received low offers. |
| "Priced to sell quickly" or urgency language | Urgency in a seller is a signal, not a feature. Find out why. |
| Multiple based on "projected" or "forward" revenue | Acquisitions are priced on trailing performance, not projections. |

---

## Flag Block Format

When one or more patterns are detected, prepend this block before the Deal Summary:

```
─────────────────────────────────────────────────────────────────
⚠️ INPUT INTEGRITY FLAG

The information provided contains patterns commonly found in seller-optimized
or broker-prepared presentations. This does not mean the deal is bad — it means
some inputs should be independently verified before this screen is relied upon.

Flagged patterns:
• [Pattern 1]: [Plain-language explanation of what to verify and how. 1–2 sentences.]
• [Pattern 2]: [Same format.]

This screen proceeds with the inputs as provided. Where flagged data points are
the basis for the verdict, treat the verdict as provisional until verified.
─────────────────────────────────────────────────────────────────
```

---

## What This Guardrail Is NOT

It is not an accusation that the seller is dishonest. These patterns appear in legitimate deals too — a seller who truly has stable revenue still needs to prove it with 3-year P&Ls, not a description. The flag is about verification, not suspicion.
