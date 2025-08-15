# SME Copilot Backend (FastAPI)

[![Deploy to Render](https://render.com/images/deploy-to-render-button.svg)](https://render.com/deploy)

This is the backend service for SME Copilot.

## Local Development
```bash
pip install -r requirements.txt
uvicorn app.main:app --reload
```

## Environment Variables
- `LLM_API_KEY` - Your LLM API key (optional for dev)
- `JWT_SECRET` - Random string for token signing
- `ALLOWED_ORIGINS` - Frontend URL (for CORS)
