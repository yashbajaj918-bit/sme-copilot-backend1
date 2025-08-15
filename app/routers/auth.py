from fastapi import APIRouter, HTTPException
from ..models.schemas import LoginRequest, TokenResponse
from ..utils.security import create_token

router = APIRouter()

@router.post("/login", response_model=TokenResponse)
def login(payload: LoginRequest):
    # Replace with real user lookup & password check
    if not payload.email or not payload.password:
        raise HTTPException(status_code=400, detail="Missing credentials")
    role = "admin" if payload.email.endswith("@admin.com") else "member"
    token = create_token(sub=payload.email, role=role)
    return TokenResponse(access_token=token, role=role)
