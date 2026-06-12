# Tool Selection Rules

Tool choice follows architecture and controls. It never follows brand familiarity or the platform running the Gate.

1. Define the required capability and deterministic controls before naming a product.
2. Prefer an already approved organizational tool when verified capabilities satisfy the requirement.
3. Verify every named capability against an official vendor or project source. Record the source URL and verification date in the architecture option.
4. Reject a recommendation that violates approved-vendor, residency, security, procurement, identity, credential, or data-handling constraints.
5. Require a blocking and audited approval mechanism for SUPERVISED terminal actions. Notifications alone do not qualify.
6. Require durable state, retry, idempotency, timeout, and compensation capabilities when the workflow architecture needs them.
7. Require hosting, secrets, observability, ownership, incident response, and operating procedures for code-first architectures.
8. Require a viable alternative when the preferred tool is unavailable or unapproved.
9. When claims cannot be verified, describe the capability neutrally and set tool selection to `UNKNOWN`.
10. Reassess when a builder substitutes a tool in a way that changes permissions, data flow, controls, audit behavior, rollback, or operating burden.

The maintained catalog is discovery data, not authority. Official documentation and the organization's own contract, configuration, and security review determine actual capability.
