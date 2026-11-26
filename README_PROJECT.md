# Executive Intelligence AI

Phase 0 starter foundation for the responsive enterprise workspace described in `PROJECT_SPEC.md` and the supplied design references.

## Current scope

This is a **starter UI**, not a production business platform. It provides responsive module navigation, an honest empty-state dashboard, an assistant preview that does not call an AI, and a minimal FastAPI health endpoint. It does not yet include a database, authentication, business records, persistent files, real analytics, or connected AI. No demo metrics are presented as actual data.

## Run the web interface

Requirements: Node.js 20.9+ and npm.

```bash
cd frontend
npm install
npm run dev
```

Open <http://localhost:3000>.

## Run the API

Requirements: Python 3.12+ and pip.

```bash
cd backend
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
uvicorn app.main:app --reload
```

Check <http://127.0.0.1:8000/health>.

See `TESTING.md` and `PROGRESS.md`. Do not enter real business data or commit secrets in this foundation milestone.
