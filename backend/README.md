# API foundation

Run in this directory:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
pytest
uvicorn app.main:app --reload
```

The current API only has a health endpoint. No authentication or database persistence is implemented yet.
