# Architecture — initial foundation

```text
Browser (Next.js / React / TypeScript)
             │ planned JSON API over HTTPS
             ▼
          FastAPI REST API
             │ planned
             ▼
        PostgreSQL database
             │
     Private object storage (planned)
```

Frontend and backend are separate. The browser must not connect directly to PostgreSQL or receive provider secrets. Future business logic belongs in backend services, not UI components.

## Current implementation
- `frontend/`: Next.js App Router UI shell; navigation is client-side only.
- `backend/app/main.py`: API health endpoint only.
- No database, authentication, persistence, or file storage is connected.

## Planned domain boundaries
Identity/organization membership; CRM/sales; private file metadata/storage; workbook processing/import review; tasks/calendar/events/notifications; analytics/reporting; AI orchestration with narrowly scoped tools; audit logging.

Every organization-owned record will carry an organization scope. Backend authorization will derive user identity and membership server-side. AI and analytics will call authorized services and return traceable source records. Phase 1 must decide migrations, session/password recovery, object storage, role matrix, retention, and backups. This is not a production security design.
