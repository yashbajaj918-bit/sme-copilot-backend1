import os, time
from jose import jwt, JWTError
from fastapi import HTTPException, status, Depends
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials

JWT_SECRET = os.getenv("JWT_SECRET", "dev-secret")
ALGO = "HS256"
auth_scheme = HTTPBearer()

def create_token(sub: str, role: str = "member", exp_seconds: int = 86400):
    payload = {"sub": sub, "role": role, "exp": int(time.time()) + exp_seconds}
    return jwt.encode(payload, JWT_SECRET, algorithm=ALGO)

def get_current_user(token: HTTPAuthorizationCredentials = Depends(auth_scheme)):
    try:
        payload = jwt.decode(token.credentials, JWT_SECRET, algorithms=[ALGO])
        return payload
    except JWTError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid token")
