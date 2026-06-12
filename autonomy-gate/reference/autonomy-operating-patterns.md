# Autonomy Operating Patterns

These patterns describe how authority is divided. They are independent of vendor and implementation tool.

| Pattern | AI authority | Human authority | Typical use |
|---|---|---|---|
| `ASSISTIVE` | Draft, summarize, classify, or recommend | Human performs terminal action | HUMAN_ONLY support or low-trust advisory work |
| `HUMAN_IN_THE_LOOP` | Prepare and pause | Human approval is blocking before terminal action | SUPERVISED workflows |
| `HUMAN_ON_THE_LOOP` | Execute within bounded scope | Human monitors, can pause, and handles exceptions | AUTONOMOUS workflows with strong observability and rollback |
| `FULLY_AUTONOMOUS` | Execute end-to-end inside explicit scope | Human governs policy and recertification, not individual runs | Low-consequence, reversible, observable workflows |
| `DETERMINISTIC_ORCHESTRATION_WITH_AI_STEP` | AI performs named reasoning only | Code controls routing, validation, permissions, and terminal action | Mixed workflows where model judgment must not enforce controls |
| `EXCEPTION_ESCALATION` | Execute standard path and create exception record | Human resolves named exception classes | Stable workflows with bounded exceptions |
| `HUMAN_ONLY` | No delegated terminal authority | Human performs and records the process | Hard-gated or judgment-bound work |

Every architecture names one primary pattern and describes human involvement at each step. Prompt text never substitutes for deterministic enforcement.
