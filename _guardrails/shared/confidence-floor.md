# Confidence Floor
## _guardrails/shared · Load on every invocation · Applies to all screen modes

> Forces explicit uncertainty when inputs are thin. A PURSUE on 3 data points must not look identical to a PURSUE on 15 data points.
>
> **This is a shared guardrail.** Thresholds below apply to any deal type. Domain-specific overrides live in `_guardrails/domain/`.

---

## Confidence Level Definitions

Every screen output must include a Confidence Level immediately after the Initial Verdict line.

| Level | What it means | When it applies |
|-------|--------------|----------------|
| 🟢 HIGH | All minimum inputs present + at least 3 higher-confidence inputs | Full data set: SDE confirmed, customer concentration known, service agreement count, reason for sale, 2+ years revenue |
| 🟡 MEDIUM | All minimum inputs present, some higher-confidence inputs missing | Have SDE + revenue + headcount + owner role, but missing concentration, agreement count, or reason for sale |
| 🔴 LOW | One or more minimum inputs missing OR only revenue + asking price available | Thin broker summary, no SDE, no headcount detail, no owner role clarity |

---

## Required Output Block

After Initial Verdict and verdict-specific disclaimer, add:

**For HIGH confidence:**
```
Confidence Level: 🟢 HIGH
Input basis: [list the key data points present]
```

**For MEDIUM confidence:**
```
Confidence Level: 🟡 MEDIUM
What's missing: [list specific gaps]
How this affects the verdict: [one sentence — e.g. "Customer concentration is unknown; the PROCEED WITH CAUTION verdict could shift to PASS if top-client concentration exceeds 30%."]
```

**For LOW confidence:**
```
Confidence Level: 🔴 LOW — PRELIMINARY ONLY
⚠️ This screen is based on limited information. The verdict below should be treated as a directional indicator only — not a basis for action.

Missing inputs that would change this analysis:
• [list each missing minimum input and why it matters]

Do not use this output to approach a seller, broker, or lender. Gather the missing information first and request a new screen.
```

---

## Mandatory STOP on Critical Gap

If the following are both absent, do not produce a verdict at all:
- SDE or EBITDA
- Owner's role in operations

Without these two inputs, no screen output is possible — only a gap list.

Output when both are missing:
```
⛔ SCREEN CANNOT RUN

Two critical inputs are missing:

1. SDE or EBITDA — without this, there is no way to assess whether the
   asking price is reasonable or whether the business can support debt service.

2. Owner's role in operations — this is the single most common failure mode
   in trades acquisitions. Without knowing whether the owner is the business,
   no verdict is meaningful.

Please provide these two inputs and re-run.
```

---

## Confidence Floor Logic

The confidence level is determined before the screen runs — not after. Do not produce a PURSUE or PROCEED WITH CAUTION verdict and then note that confidence is LOW. LOW confidence screens produce directional output only and explicitly defer action until inputs improve.
