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

## Required Output

Every applicable artifact contains an `ARCHITECTURE OPTIONS` block before `BUILD HANDOFF PACK`. The canonical option classes are `PRIMARY`, `NATIVE_SUITE`, `LOW_CODE`, `CODE_FIRST`, and `VENDOR_NEUTRAL`. An option class may be absent only when `Omitted option classes` records an evidence-based reason.

```
ARCHITECTURE OPTIONS
### OPT-1 — PRIMARY
**Execution architecture:** Capability-first production design
**Builder surface:** Implementation owner or builder
**Control fit:** Deterministic control enforcement
**Implementation effort:** Relative effort and dependencies
**Operating cost:** Grounded cost information or named evidence gap
**Maintenance burden:** Ownership and recurring operational work
**Security fit:** Identity, permissions, data, and compliance fit
**Portability:** Switching constraints and export path
**Skill requirements:** Build and operating skills
**Source evidence:** Official source plus verification date, or technology-neutral basis

Omitted option classes:
- NATIVE_SUITE — Evidence-based reason when omitted
- LOW_CODE — Evidence-based reason when omitted
- CODE_FIRST — Evidence-based reason when omitted
- VENDOR_NEUTRAL — Evidence-based reason when omitted

Selected option: NOT_SELECTED
Selection by: NOT_RECORDED
Selection date: NOT_RECORDED
```

`PRIMARY` is the Gate's recommendation, not the operator's decision. The operator records `Selected option`, `Selection by`, and `Selection date`. The pack remains `BLOCKED_FOR_EVIDENCE` until a generated option is selected. Substituting a tool is permitted only when it preserves controls, permissions, data flow, audit behavior, rollback, security posture, and operating burden; otherwise reassessment is required.
