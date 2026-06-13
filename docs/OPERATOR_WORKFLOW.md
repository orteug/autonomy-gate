# Operator Workflow

1. Configure the persistent Gate workspace with the 16 runtime files. Add organization and technology-stack profiles only when their values are real and attributable.
2. Submit a free-form workflow description. The Gate issues the snapshot and decision packet before architecture design.
3. Review autonomy, terminal action, controls, confidence, and evidence gaps. Use `REVISE` when the decision is wrong; use evidence resolution when a named fact is missing.
4. Compare architecture options. Confirm company-stack constraints and select one option explicitly.
5. Review the Build Handoff Pack. `BUILD_READY` requires complete manifest content, source evidence, controls, tests, expiration triggers, and stop behavior.
6. Record disposition. Approval requires name and role, date, packet version, and rationale. The Gate cannot approve for you.
7. Send the approved pack and Builder Acknowledgement to the implementer. The builder must stop on unenforceable controls or scope changes.
8. Validate implementation against every acceptance criterion before moving to `ACTIVE`.
9. Monitor incidents and expiration triggers. Pause immediately when authorization expires and submit for recertification.

The durable workflow record, not project memory, is the source of truth.
