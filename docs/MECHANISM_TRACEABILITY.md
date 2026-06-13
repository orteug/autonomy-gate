# Mechanism Traceability

This index maps each release-critical mechanism to its authority, enforcement, deterministic test, and public evidence. A mechanism is incomplete if any column is empty.

| Mechanism | Defined in | Enforced by | Tested by | Demonstrated by |
|---|---|---|---|---|
| Canonical autonomy verdict | `rules.md` RULE-03 through RULE-06 | `validate_gate_output.py`, decision-packet schema | packet and release-contract unit tests | all three receipts |
| Terminal-action hard gates | `rules.md` RULE-04 and RULE-06 | packet validator and fixture bank | Claude/OpenAI calibration and fixture consistency | supervised refund and HUMAN_ONLY bank-change receipts |
| Separate assessment, architecture, and builder fields | `operating-contract.md` | decision-packet schema and packet validator | `test_decision_packet_schema_uses_three_surface_fields` | autonomous and supervised receipts |
| Architecture alternatives | `rules.md` RULE-10 and `workflow-architecture-contract.md` | architecture validator and Markdown validator | architecture-option and release-contract tests | autonomous and supervised receipts |
| Operator architecture selection | `operating-contract.md` | architecture and handoff validators | selection contradiction tests | autonomous receipt |
| Build Handoff Pack completeness | `build-handoff-contract.md` and RULE-14 | JSON schema, structured validator, Markdown validator | full-contract and manifest-content tests | all three receipts |
| Confidence versus handoff status | `operating-contract.md` and RULE-06 | packet and handoff validators | high-confidence contradiction and blocked-pack tests | supervised receipt |
| Operator disposition authority | RULE-15 and `operator-disposition.md` | Markdown validator and registry schema | approval metadata and preselection tests | all three receipts |
| Builder acknowledgement | `builder-acknowledgement.md` | handoff contract and lifecycle boundary | acknowledgement metadata release test | BUILD_READY autonomous receipt |
| Material-change invalidation | `operating-contract.md`, RULE-14, and user journey | lifecycle contract and version fields | material-change invalidation release test | supervised receipt version triggers |
| HUMAN_ONLY safe decomposition | `build-handoff-contract.md` and governance template | JSON and Markdown validators | NOT_APPLICABLE safe-decomposition tests | bank-change receipt |
| Canonical lifecycle | `operating-contract.md` | governance registry schema | exact transition-state parity test | registry guide |
| Exact public release scope | `PUBLIC_RELEASE_MANIFEST.txt` | competition-package validator | release suite manifest check | public repository tree |

Historical acceptance records are evidence of prior behavior, not normative definitions. Current contracts, validators, fixtures, and receipts govern release readiness.
