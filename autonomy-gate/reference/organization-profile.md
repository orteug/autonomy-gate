# Organization Profile

The Organization Profile is an optional persistent context document that an operator loads into the Gate workspace once and reuses across assessments. When present, the Gate applies the profile as background evidence — reducing evidence gaps and enabling faster, more accurate assessments.

The profile does not override hard gate conditions (GATE-2, GATE-3). It supplies organizational context that the Gate would otherwise have to request or leave as UNKNOWN.

---

## What the Profile Contains

An organization profile covers seven areas. Each area is optional — populate what you know. More complete profiles produce fewer evidence gaps.

### 1. Business Context

```
Organization name:      [your organization or team name]
Industry:               [sector — e.g., SaaS, financial services, healthcare, logistics]
Size:                   [headcount or revenue band — helps calibrate cost-of-failure scoring]
Regulatory exposure:    [regulations that apply — e.g., SOC 2, HIPAA, GDPR, PCI-DSS, none]
Primary value chain:    [what the organization does — one or two sentences]
```

### 2. Risk Tolerance

```
Default risk posture:   [CONSERVATIVE | BALANCED | PERMISSIVE]
Financial threshold:    [dollar amount above which human approval is required]
Reputational threshold: [type of content or action that requires human review before external publication]
Escalation authority:   [name or role of the person who approves exceptions]
```

**Risk posture definitions:**
- `CONSERVATIVE` — when uncertain, route to SUPERVISED. Prefer false negatives (denying automation) over false positives (over-automating).
- `BALANCED` — apply rules as written. Accept AUTONOMOUS when the evidence supports it.
- `PERMISSIVE` — require only GATE-2 and GATE-3 to force HUMAN_ONLY. Accept AUTONOMOUS for any workflow with low exception rate.

The Gate always applies hard gate conditions regardless of posture. Posture affects scoring at the MEDIUM boundary only.

### 3. Approval Authorities

```
Workflow approver:      [name or role — who records APPROVE_FOR_BUILD]
Finance approver:       [name or role — required for GATE-1 workflows]
Security approver:      [name or role — required for GATE-3 workflows]
Legal approver:         [name or role — required for GATE-4 regulatory content]
```

### 4. Regulated Domains

```
Off-limits domains:     [workflow types the organization has decided not to automate, regardless of verdict]
Restricted domains:     [workflow types that require additional approval beyond the Gate's standard controls]
```

Examples:
- Off-limits: "No AI involvement in hiring decisions"
- Restricted: "All workflows touching customer PII require security approver sign-off"

### 5. Technology Stack

```
Primary stack:          [languages, frameworks, platforms the organization builds on]
Approved AI surfaces:   [which Gate surfaces are available — Claude Project, Cowork, Claude Code, Codex]
Approved AI providers:  [Anthropic, OpenAI, both, other]
Prohibited tools:       [specific tools the organization has ruled out]
Data handling policy:   [how data must be handled — e.g., no PII in AI prompts, approved vendors only]
```

### 6. Build Preferences

```
Default builder:        [who implements artifacts — internal, contractor, specific team]
Deployment environment: [where built workflows run — cloud, local, hybrid]
Code review required:   [yes | no | required for production only]
Builder acknowledgement:[yes | no — whether builders must sign BUILDER_ACKNOWLEDGEMENT]
```

### 7. Governance Defaults

```
Default recertification interval: [e.g., 6 months, 12 months, or "when material change occurs"]
Default error-rate threshold:     [acceptable error rate before escalation — e.g., under 2% per week]
Audit trail requirement:          [what logs must be retained and for how long]
Incident escalation path:         [who to notify if a workflow produces an unexpected outcome]
```

---

## How the Gate Uses the Profile

When a profile is loaded, the Gate applies it as follows:

| Profile field | Effect on assessment |
|--------------|---------------------|
| Regulatory exposure | Pre-populates `Data sensitivity` in the snapshot; informs GATE-4 evaluation |
| Risk posture | Adjusts MEDIUM-boundary scoring; does not override hard gates |
| Financial threshold | Informs GATE-1 evaluation when the workflow description mentions money movement |
| Off-limits domains | Triggers RULE-04 terminal action check; may produce HUMAN_ONLY regardless of scoring |
| Approved AI surfaces | Restricts surface assignment to approved options; flags if verdict requires an unavailable surface |
| Governance defaults | Pre-fills recertification interval and error-rate threshold; removes these from BLOCKED list |

Profile fields carried into a snapshot are annotated with provenance `STATED` (operator-supplied via profile). They are treated identically to values stated in the workflow description.

---

## Using the Profile

Load the profile at the beginning of a Gate session by pasting it as a CONFIGURE input (see user-journey-contract.md, CONFIGURE mode). The Gate confirms which fields were received.

Profile fields apply to all subsequent assessments in the session. They do not carry across sessions unless the operator reloads the profile.

For a persistent workspace where the profile is always available, see `docs/PROJECT_WORKSPACE_SETUP.md`.
