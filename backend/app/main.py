from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="Executive Intelligence AI API", version="0.1.0")

# Local development origin only. Protected business APIs are not implemented yet.
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["GET"],
    allow_headers=["*"],
)


@app.get("/health", tags=["system"])
def health() -> dict[str, str]:
    """Indicate the API process responds; this is not database readiness."""
    return {"status": "ok", "service": "executive-intelligence-api"}
