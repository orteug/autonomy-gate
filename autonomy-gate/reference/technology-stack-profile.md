# Technology Stack Profile

The Technology Stack Profile captures an organization's technical environment so the Gate can recommend execution architectures and builders compatible with the company's actual tools, approved vendors, skills, and operational constraints.

The Gate never assumes a specific vendor. When this profile is absent or incomplete, the Gate produces technology-neutral architecture descriptions and marks tool-specific fields `UNKNOWN`. When the profile is present, the Gate applies it as `STATED` evidence and avoids recommending tools outside the approved set.

---

## Profile Structure

### Collaboration and Communication

```
Primary messaging:     [Slack | Microsoft Teams | Google Chat | Email | Other | UNKNOWN]
Email platform:        [Google Workspace | Microsoft 365 | Other | UNKNOWN]
Video/meeting:         [Zoom | Google Meet | Microsoft Teams | Other | UNKNOWN]
Intranet/wiki:         [Notion | Confluence | SharePoint | Other | UNKNOWN]
```

### Productivity Suite

```
Office suite:          [Microsoft 365 | Google Workspace | Mixed | Other | UNKNOWN]
Document storage:      [SharePoint | Google Drive | Dropbox | OneDrive | Other | UNKNOWN]
Spreadsheets:          [Excel | Google Sheets | Other | UNKNOWN]
```

### Business Systems

```
CRM:                   [Salesforce | HubSpot | Zoho | Microsoft Dynamics | Other | UNKNOWN]
ERP:                   [SAP | NetSuite | Oracle | Microsoft Dynamics | Other | UNKNOWN | NOT_APPLICABLE]
Support/ticketing:     [Zendesk | Freshdesk | Jira Service Management | ServiceNow | Other | UNKNOWN | NOT_APPLICABLE]
Project management:    [Asana | Jira | Linear | Monday | Notion | Other | UNKNOWN]
Finance:               [QuickBooks | Xero | Stripe | Sage | NetSuite | Other | UNKNOWN]
HRIS:                  [Workday | BambooHR | Rippling | ADP | Other | UNKNOWN | NOT_APPLICABLE]
Document management:   [DocuSign | Adobe Sign | SharePoint | Other | UNKNOWN]
```

### Automation and Integration Platforms

```
Primary iPaaS:         [Workato | Zapier | Make | n8n | Tray | MuleSoft | Boomi | UNKNOWN | NONE]
Microsoft automation:  [Power Automate | Power Apps | Other | UNKNOWN | NOT_APPLICABLE]
Native automations:    [Salesforce Flow | HubSpot Workflows | Monday Automations | Other | UNKNOWN | NONE]
RPA:                   [UiPath | Automation Anywhere | Blue Prism | Other | UNKNOWN | NONE]
```

### Cloud and Data Infrastructure

```
Primary cloud:         [AWS | Azure | GCP | Multi-cloud | On-premises | UNKNOWN]
Data warehouse:        [Snowflake | BigQuery | Redshift | Databricks | Other | UNKNOWN | NOT_APPLICABLE]
Data platform:         [dbt | Fivetran | Airbyte | Other | UNKNOWN | NOT_APPLICABLE]
Databases:             [PostgreSQL | MySQL | MongoDB | SQL Server | Other | UNKNOWN]
File storage:          [S3 | Azure Blob | GCS | Local/NAS | Other | UNKNOWN]
Observability:         [Datadog | Grafana | CloudWatch | Splunk | Other | UNKNOWN]
```

### AI Provider and Deployment

```
Approved AI provider:  [Anthropic | OpenAI | Azure OpenAI | Google Vertex AI | AWS Bedrock | Self-hosted | Multiple | UNKNOWN | PROHIBITED]
Approved AI surfaces:  [Claude Project | Claude Cowork | Claude Code | ChatGPT Project | Codex | Other | All | UNKNOWN]
Model access pattern:  [Direct API | Managed gateway | Platform-native (Azure/Vertex/Bedrock) | UNKNOWN]
Data in AI prompts:    [PII permitted | PII prohibited | Regulated data permitted | Regulated data prohibited | UNKNOWN]
AI procurement status: [Approved vendors only | Open procurement | UNKNOWN]
```

### Code and Engineering Infrastructure

```
Code hosting:          [GitHub | GitLab | Bitbucket | Azure DevOps | Other | UNKNOWN]
CI/CD:                 [GitHub Actions | GitLab CI | CircleCI | Jenkins | Azure Pipelines | Other | UNKNOWN]
Secrets management:    [AWS Secrets Manager | Azure Key Vault | HashiCorp Vault | GitHub Secrets | Other | UNKNOWN]
Identity provider:     [Okta | Azure AD | Google Workspace | Other | UNKNOWN]
Engineering team size: [Solo | 1-5 | 5-20 | 20+ | No in-house engineering | UNKNOWN]
Code review required:  [Yes, all changes | Yes, production only | No | UNKNOWN]
```

### Operational Constraints

```
Data residency:        [US only | EU only | Specific country | No constraint | UNKNOWN]
Approved vendor list:  [Strict (named list) | Preferred (flexibility exists) | Open | UNKNOWN]
Procurement threshold: [Dollar amount above which approval is required | UNKNOWN]
Integration policy:    [No new integrations without approval | Pre-approved vendors only | Open | UNKNOWN]
Build preference:      [No-code/low-code first | Code where necessary | Code-first | UNKNOWN]
Hosting constraint:    [Cloud only | On-premises only | Hybrid | UNKNOWN]
```

---

## Provenance Rules

Every field in the Technology Stack Profile carries one of the field provenance states defined in RULE-01:

| State | Meaning |
|-------|---------|
| `STATED` | Operator supplied this value explicitly |
| `DERIVED` | Gate inferred this from stated fields using a named derivation rule |
| `UNKNOWN` | Value not supplied; Gate cannot determine from context |
| `NOT_APPLICABLE` | This tool category does not apply to this organization |

When the profile is incomplete, the Gate:
- Marks unanswered fields `UNKNOWN`
- Produces technology-neutral architecture descriptions where specific tool knowledge is required
- Does not assume any named vendor

---

## How the Gate Uses the Profile

| Profile area | Effect on assessment |
|-------------|---------------------|
| Approved AI provider | Restricts surface assignment to approved providers; flags if verdict requires a provider not on the approved list |
| Approved AI surfaces | Restricts surface assignment to available surfaces; falls back with explanation if the optimal surface is unavailable |
| No-code/low-code preference | Affects architecture alternatives ordering; surfaces integration-platform options first |
| Data in AI prompts | Informs GATE-4 evaluation; flags if workflow touches data that cannot enter AI prompts |
| Approved vendor list | Prevents recommendations outside the approved set; names constraint explicitly |
| Engineering team size | Informs build complexity assessment; avoids code-first recommendations for no-engineering teams |
| Observability | Informs GATE-5 evaluation (audit trail availability) |

---

## Technology-Neutral Fallback

When the Technology Stack Profile is absent or fields are `UNKNOWN`, the Gate:

1. Describes the required capability (e.g., "a scheduling mechanism that can trigger at a defined interval") rather than naming a product (e.g., "use GitHub Actions")
2. Names the organizational constraint that would govern tool selection (e.g., "select from your approved iPaaS vendor")
3. Identifies the profile fields that would allow a specific recommendation
4. Does not hallucinate tool names or assume the company uses any named platform

A technology-neutral architecture description is always valid and always implementable. The operator supplies tool names after the architecture is agreed.
