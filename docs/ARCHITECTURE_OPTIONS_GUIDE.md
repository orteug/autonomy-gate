# Architecture Options Guide

The Gate compares capability architectures before products.

| Option class | Purpose |
|---|---|
| Primary | Best fit using confirmed organization constraints and capabilities. |
| Native suite | Minimizes procurement by using the organization's existing platform suite. |
| Low-code | Supports teams with limited engineering capacity where required controls are enforceable. |
| Code-first | Supports durable state, custom controls, testing, scale, and operational ownership. |
| Vendor-neutral | Preserves portability or remains valid while the company stack is unknown. |

Each option compares control fit, implementation effort, operating cost, maintenance burden, security/compliance fit, portability, and skill requirements. Named tools require an official source URL and verification date. The operator selects an option before the handoff can be `BUILD_READY`.

Example: the same supervised approval workflow may use a company's native suite, an approved integration platform, or a code-first durable workflow engine. The autonomy verdict and terminal-action boundary remain unchanged; only implementation changes.
