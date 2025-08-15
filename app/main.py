import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .routers import auth, chat, insights, connectors

ALLOWED_ORIGINS = os.getenv("ALLOWED_ORIGINS", "http://localhost:5173").split(",")

app = FastAPI(title="SME Copilot API", version="0.1.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=[o.strip() for o in ALLOWED_ORIGINS],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth.router, prefix="/api/auth", tags=["auth"])
app.include_router(chat.router, prefix="/api", tags=["chat"])
app.include_router(insights.router, prefix="/api", tags=["insights"])
app.include_router(connectors.router, prefix="/api/connectors", tags=["connectors"])

@app.get("/api/health")
def health():
    return {"status": "ok"}
