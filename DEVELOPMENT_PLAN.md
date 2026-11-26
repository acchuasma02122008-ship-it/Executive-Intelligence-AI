# Development plan

Deliver and verify one milestone before starting the next.

| Phase | Scope | Exit criteria |
|---|---|---|
| 0 — Foundation | Docs, responsive shell, API health endpoint | Both applications start locally; configured checks pass |
| 1 — Platform | PostgreSQL, migrations, organizations, users, memberships, authentication and authorization | Tests demonstrate tenant isolation and Executive/EA permissions |
| 2 — CRM | Hospitals/branches, doctor affiliations, products/assets, sales, payments, installation/service | Validated organization-scoped CRUD tests pass |
| 3 — Files and Excel | Private storage, folders, workbook parsing, mapping/quality preview, approved import, history and exports | Upload, preview, conflicts, import and recovery tested |
| 4 — AI assistant | Provider integration, scoped tools, authorized retrieval, citations, history and action confirmation | Permissions, sources, numerical answers and error behavior tested |
| 5 — Overview and BI | Real KPIs, chart filters/drill-down, comparisons and briefing | Every value traces to records; empty states are accurate |
| 6 — Operations | Tasks, projects, meetings, calendar, deadlines, follow-ups and time | Shared records remain consistent across modules |
| 7 — Event intelligence | Source adapters, verification, changes, deduplication and monitoring | Failures visible; no invented events; notification rules tested |
| 8 — Reporting | PDF/XLSX/CSV, reminders and scheduled summaries | Export calculations match source records |
| 9 — Passkeys/PWA | WebAuthn and installable mobile experience | Registration, authentication, recovery and permissions tested |
| 10 — Deployment | Monitoring, backup/restore, security and performance | Restore exercise and release checklist pass |

Keep `main` untouched during development. Add new files first; ask before modifying/deleting existing files. Explain beginner commands and expected results. Do not advance past failing or unverified criteria.
