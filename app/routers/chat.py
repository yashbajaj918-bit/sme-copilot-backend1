from fastapi import APIRouter, Depends
from ..models.schemas import ChatRequest, ChatResponse
from ..utils.security import get_current_user
from ..services.agent import run_agent

router = APIRouter()

@router.post("/chat", response_model=ChatResponse)
async def chat(req: ChatRequest, user=Depends(get_current_user)):
    result = await run_agent([m.model_dump() for m in req.messages], req.context or {})
    return ChatResponse(**result)
