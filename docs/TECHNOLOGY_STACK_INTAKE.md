# Technology Stack Intake

Use this form to configure your organization's technology stack profile in the Gate workspace. Paste the completed form as a CONFIGURE input, or upload it as part of your organization profile.

You do not need to complete every field. The Gate marks incomplete fields `UNKNOWN` and produces technology-neutral output for those areas. The more fields you complete, the more specific the Gate's architecture recommendations can be.

---

## Instructions

1. Copy the form below.
2. Replace each `UNKNOWN` with the correct value for your organization, or with `NOT_APPLICABLE` if the category doesn't apply.
3. Submit using the CONFIGURE mode:

```
CONFIGURE:
[paste your completed form here]
```

The Gate will confirm which fields were received and how they affect your assessments.

---

## Stack Profile Form

```
TECHNOLOGY STACK PROFILE

## Collaboration
Primary messaging:     UNKNOWN
Email platform:        UNKNOWN
Video/meeting:         UNKNOWN
Intranet/wiki:         UNKNOWN

## Productivity
Office suite:          UNKNOWN
Document storage:      UNKNOWN

## Business Systems
CRM:                   UNKNOWN
ERP:                   UNKNOWN
Support/ticketing:     UNKNOWN
Project management:    UNKNOWN
Finance:               UNKNOWN
HRIS:                  UNKNOWN
Document management:   UNKNOWN

## Automation
Primary iPaaS:         UNKNOWN
Microsoft automation:  UNKNOWN
Native automations:    UNKNOWN
RPA:                   UNKNOWN

## Cloud and Data
Primary cloud:         UNKNOWN
Data warehouse:        UNKNOWN
Databases:             UNKNOWN
File storage:          UNKNOWN
Observability:         UNKNOWN

## AI
Approved AI provider:  UNKNOWN
Approved AI surfaces:  UNKNOWN
Model access pattern:  UNKNOWN
Data in AI prompts:    UNKNOWN
AI procurement status: UNKNOWN

## Engineering
Code hosting:          UNKNOWN
CI/CD:                 UNKNOWN
Secrets management:    UNKNOWN
Identity provider:     UNKNOWN
Engineering team size: UNKNOWN
Code review required:  UNKNOWN

## Constraints
Data residency:        UNKNOWN
Approved vendor list:  UNKNOWN
Procurement threshold: UNKNOWN
Integration policy:    UNKNOWN
Build preference:      UNKNOWN
Hosting constraint:    UNKNOWN
```

---

## Minimal Starter — Fill These Six First

If you only complete one section, complete these six fields. They have the largest impact on surface assignment and architecture recommendations:

```
Approved AI provider:  [Anthropic | OpenAI | Azure OpenAI | Google Vertex AI | AWS Bedrock | Multiple | PROHIBITED]
Approved AI surfaces:  [Claude Project | Claude Code | ChatGPT Project | Codex | Cowork | All]
Build preference:      [No-code/low-code first | Code where necessary | Code-first]
Engineering team size: [Solo | 1-5 | 5-20 | 20+ | No in-house engineering]
Data in AI prompts:    [PII permitted | PII prohibited | Regulated data prohibited]
Primary iPaaS:         [Workato | Zapier | Make | n8n | NONE | UNKNOWN]
```

---

## What the Gate Does With Your Stack Profile

- **Approved AI provider / surfaces:** The Gate restricts surface assignments to your approved providers and surfaces. If the optimal verdict surface is unavailable in your environment, the Gate names the constraint and provides the best available alternative.

- **Build preference:** Affects ordering of architecture alternatives. A no-code/low-code preference surfaces integration-platform options first.

- **Engineering team size:** Avoids code-first recommendations when no engineering team is available to maintain them.

- **Data in AI prompts:** The Gate flags workflows that would pass prohibited data types into AI prompts and adjusts the verdict accordingly.

- **Primary iPaaS:** When present, the Gate includes your integration platform as a named option in architecture alternatives.

---

## Updating the Profile

To update individual fields mid-session:

```
CONFIGURE update:
- [field name]: [new value]
- [field name]: [new value]
```

Updates take effect immediately for subsequent assessments in the session.
