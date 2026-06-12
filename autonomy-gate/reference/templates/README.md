# Artifact Templates

These six files are internal production structures used by the Gate during Phase 2. Users do not fill them.

The Gate selects one template from the verdict, fills it as a standalone document, removes all placeholders, and adds a complete `BUILD HANDOFF PACK`. If required deployment values are missing, the artifact names them under `REQUIRED BEFORE BUILD` and marks deployment `BLOCKED` rather than asking the user to translate or complete the template.

The templates remain separate because each verdict produces a materially different operational document. Their separation improves retrieval precision and keeps the decision-to-artifact mapping auditable.
