# Execution Adapters

Use this folder only after the Gate issues a verdict. The artifact's `BUILD HANDOFF PACK` contains the completed configuration; these files explain how each surface consumes and enforces it.

| Verdict surface | Adapter |
|---|---|
| Claude Project | `claude/claude-project-setup.md` |
| Claude Cowork | `claude/cowork-handoff.md` |
| Claude Code | `claude/claude-code-CLAUDE.md` |
| ChatGPT Project | `openai/chatgpt-project-setup.md` |
| Codex | `openai/codex-AGENTS.md` |

`decision-packet-contract.md` defines the platform-independent handoff fields. The `CLAUDE.md` and `AGENTS.md` files are reference schemas used by the Gate when generating complete configuration; operators should not fill them manually.
