# Release Criteria

A release is eligible only when all applicable gates pass:

1. Runtime manifests agree and include all canonical files.
2. Unit, structural, schema-syntax, fixture, validator, link, and terminology checks pass.
3. Adversarial fixtures prove missing handoff content and incomplete approval are rejected.
4. Public release files exactly match the verified source manifest.
5. At least one Claude and one Codex live acceptance run use the exact public runtime package.
6. Hard-gate misses are zero. Decision agreement across repeated live fixtures is at least 95 percent; conservative disagreement is reported for operator review.
7. Supported model and CLI versions, dates, and unavailable evidence are recorded honestly.
8. The public remote SHA is verified after push and the smoke suite passes from the public clone.

Static validation never substitutes for live model acceptance. Recording, voice, or submission media are distribution gates, not software correctness evidence.

## Current Evidence

Static release evidence is produced by `python3 testing/run_release_suite.py`. Live evidence is produced by `python3 testing/run_cross_model_acceptance.py`; an unavailable CLI or network produces `NOT_RUN`, never `PASS`.

As of June 12, 2026:

- The full static public-clone release suite passes.
- Claude CLI authentication is healthy on a minimal prompt, but exact 16-file F02 generation exceeded the five-minute acceptance timeout. Status: `NOT_ACCEPTED_TIMEOUT`.
- Codex CLI is reachable, but the account reported a usage limit during the current exact-package run. Status: `NOT_RUN_USAGE_LIMIT`.
- An earlier Codex F02 attempt produced the correct `HUMAN_ONLY` / GATE-2 outcome but omitted the packet's required `Terminal action` field. It is diagnostic evidence, not an accepted receipt.

Release criterion 5 remains open until fresh exact-package Claude and Codex outputs pass `testing/validate_gate_output.py`.
