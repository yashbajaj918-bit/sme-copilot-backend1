from typing import List, Dict
from .llm import chat as llm_chat

SYSTEM_PROMPT = {
    "role": "system",
    "content": "You are an SME Copilot specializing in finance, sales, and operations. Be concise, cite data sources when available."
}

async def run_agent(messages: List[Dict], context: Dict):
    # Insert tools, routing, and retrieval here. For MVP we just call the LLM.
    full_messages = [SYSTEM_PROMPT] + messages
    answer = await llm_chat(full_messages)
    return {"answer": answer, "sources": context.get("sources", [])}
