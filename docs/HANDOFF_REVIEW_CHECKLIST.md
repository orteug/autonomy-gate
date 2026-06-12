# Handoff Review Checklist

- Packet version and workflow ID match every artifact.
- Autonomy and terminal action match the assessment.
- Assessment surface, execution architecture, and builder surface are distinct.
- Operator selected the architecture option.
- Every named file has exact path, purpose, complete content, and source evidence.
- Deterministic controls are implemented outside prompts.
- Prohibited actions are explicit and enforceable.
- Acceptance tests include setup, input, expected behavior, and pass criterion.
- Expiration triggers, stop conditions, rollback limits, logging, and incident routing are present.
- `BUILD_READY` contains no unresolved dependencies or placeholders.
- `APPROVE_FOR_BUILD` includes operator identity, date, packet version, and rationale.
- Builder Acknowledgement restates scope, controls, file plan, and evidence plan before implementation.
- Any tool substitution changing controls or permissions returns to the Gate.

Run `python3 testing/review_handoff.py artifact.md` before delivery.
