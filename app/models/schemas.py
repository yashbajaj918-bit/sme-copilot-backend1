from pydantic import BaseModel, Field
from typing import List, Optional

class LoginRequest(BaseModel):
    email: str
    password: str

class TokenResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"
    role: str = "member"

class ChatMessage(BaseModel):
    role: str  # user|assistant|system
    content: str

class ChatRequest(BaseModel):
    messages: List[ChatMessage]
    context: Optional[dict] = Field(default_factory=dict)

class ChatResponse(BaseModel):
    answer: str
    sources: Optional[list] = None

class InsightSummary(BaseModel):
    summary: str
    columns: List[str]
    num_rows: int
    forecast_column: Optional[str] = None
    forecast_preview: Optional[list] = None
