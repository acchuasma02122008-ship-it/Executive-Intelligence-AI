# Testing and local verification

## Frontend
Requirements: Node.js 20.9+ and npm.

```bash
cd frontend
npm install
npm run lint
npm run build
npm run dev
```

Open <http://localhost:3000>. Check module navigation, search filtering, sidebar collapse, mobile navigation, and the assistant's disconnected status.

## Backend
Requirements: Python 3.12+ and pip.

```bash
cd backend
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
pytest
uvicorn app.main:app --reload
```

Expected `GET http://127.0.0.1:8000/health` response:

```json
{"status":"ok","service":"executive-intelligence-api"}
```

Only the health endpoint has a test. Frontend build/lint and all business, security, database, and AI tests remain pending. If a command fails, share the full command and output before changing dependencies.
