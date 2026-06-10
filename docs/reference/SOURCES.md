# Sources And Platform Assumptions

The Autonomy Gate documentation references the following sources for platform capability claims.

**Important:** Platform capabilities vary by account, plan, region, and organization configuration. This file documents what was verified and when. Verify capabilities for your specific environment before operational use.

---

## Claude Projects

Source: Claude Help Center, "What are projects?", March 16, 2026.
URL: https://support.claude.com/en/articles/9517075-what-are-projects

Verified assumptions:

- Claude Projects are self-contained workspaces with their own chat histories and knowledge bases.
- Users can upload documents and define project instructions.
- Paid plans may enable expanded project knowledge.
- Team and Enterprise plans may support sharing and permissions.

Documentation boundary:

- The Gate runs in Claude Project as a human-initiated decision layer.
- The documentation does not assume Claude Project can schedule or execute unattended workflows.

---

## Claude Code

Source: Claude Code documentation, "How Claude remembers your project."
URL: verify at docs.anthropic.com/en/docs/claude-code before publication — exact section path not confirmed.

Verified assumptions:

- `CLAUDE.md` files provide persistent project instructions.
- Claude Code treats `CLAUDE.md` as context, not enforced configuration.
- Blocking actions requires hooks or other enforcement mechanisms.

Documentation boundary:

- `CLAUDE.md` is recommended for carrying the Gate packet into Claude Code.
- High-consequence controls must be implemented technically, not only written as instructions.

---

## ChatGPT Projects

Source: OpenAI Help Center, "Projects in ChatGPT."
URL: https://help.openai.com/en/articles/10169521-using-projects-in-chatgpt

Verified assumptions:

- ChatGPT Projects support project files and project instructions.
- Project instructions apply inside the respective project.
- Projects may support memory, tools, app links, connected apps, and web search depending on plan and settings.

Documentation boundary:

- The Gate can run in ChatGPT Project as a decision layer.
- Optional tools and connected apps are treated as optional, not required Gate behavior.

---

## Codex

Source: OpenAI Codex documentation, fetched 2026-06-10.
URLs:
- AGENTS guidance: https://developers.openai.com/codex/concepts/customization#agents-guidance
- Hooks reference: https://developers.openai.com/codex/config-advanced#hooks
- Configuration reference: https://developers.openai.com/codex/config-reference

Verified assumptions:

- Codex reads `AGENTS.md` before doing work.
- Codex layers global and project guidance.
- Codex uses sandbox and approval policies to control capability and approval points.
- Codex supports hooks around tool and lifecycle events.

Documentation boundary:

- `AGENTS.md` is recommended for carrying the Gate packet into Codex.
- Sandbox, approval policy, hooks, and code-level tests are required for high-consequence enforcement.

---

## Cowork

Assumption status: **verify before operational use.**

The documentation treats Cowork as an available scheduled/local-work surface only when the user confirms required capabilities in their environment. Cowork guides are written conditionally. If Cowork is unavailable, use the artifact's fallback path.

---

## AI Governance Concepts

The documentation uses the following governance concepts as grounding principles, not as claims of official framework compliance:

- proportional oversight
- graded autonomy
- automation stopping when abnormality appears
- terminal action risk
- runtime guardrails

These are elaborated in `autonomy-gate/reference/precedents.md`.

---

*Platform claims verified through: 2026-06-10. Verify against current documentation before operational deployment.*
