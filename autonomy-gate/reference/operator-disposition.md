# Operator Disposition

The operator disposition is the human release gate. No Build Handoff Pack is authorized for implementation until an accountable operator records a disposition. The Gate may recommend a disposition but may not select `APPROVE_FOR_BUILD` on the operator's behalf.

---

## Four Dispositions

| Disposition | Meaning | When to use |
|-------------|---------|-------------|
| `APPROVE_FOR_BUILD` | The operator authorizes the Build Handoff Pack to move to the selected builder | All decision-material evidence is present, the architecture is selected, and the operator accepts accountability for the build scope |
| `REVISE` | The assessment or architecture requires changes before authorization | The verdict, controls, architecture selection, or handoff completeness has a specific identified problem |
| `HOLD_FOR_EVIDENCE` | The assessment is sound but required governance values are missing | The decision is correct but threshold, interval, owner, or other required values cannot be determined without additional input |
| `REJECT` | The workflow should not be built at this time | Risk cannot be bounded, organizational constraints prohibit it, or the terminal action is not appropriate for delegation regardless of controls |

---

## Required Fields When Approving

When recording `APPROVE_FOR_BUILD`, the operator must supply:

- **Name / role** — who is authorizing the build
- **Date** — when the disposition was recorded
- **Packet version** — which version of the Build Handoff Pack is authorized
- **Rationale** — one or more sentences explaining why the authorization is appropriate given the verdict, controls, and architecture

These fields must be filled by the operator. The Gate does not generate or pre-fill them.

---

## What Authorization Covers

An `APPROVE_FOR_BUILD` disposition authorizes:
- The selected execution architecture and builder surface named in the Build Handoff Pack
- The terminal action and its scope as described in the packet
- The controls and acceptance criteria as specified

An `APPROVE_FOR_BUILD` disposition does not authorize:
- Scope changes the builder introduces during implementation
- Tool substitutions that materially alter the controls
- Actions outside the terminal action boundary named in the packet
- Ongoing operation after expiration conditions trigger

---

## Scope-Change Rule

If the builder identifies a scope change, tool substitution with different controls, or a requirement that cannot be implemented within the stated boundaries, the builder must stop and return to the operator. A new Gate assessment is required before the changed scope can be authorized.

---

## RULE Reference

Operator disposition is governed by RULE-15. No artifact is build-authorized without it.
