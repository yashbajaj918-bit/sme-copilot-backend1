import os, httpx

API_KEY = os.getenv("LLM_API_KEY")
API_BASE = os.getenv("LLM_API_BASE", "https://api.openai.com/v1")
MODEL = os.getenv("LLM_MODEL", "gpt-4o-mini")

HEADERS = {"Authorization": f"Bearer {API_KEY}", "Content-Type": "application/json"}

async def chat(messages):
    if not API_KEY:
        # Dev fallback without network call
        last = next((m["content"] for m in reversed(messages) if m["role"]=="user"), "")
        return f"(DEV MODE) You asked: {last}\nHere's a placeholder answer. Plug your LLM in services/llm.py"
    body = {
        "model": MODEL,
        "messages": messages,
        "temperature": 0.2
    }
    async with httpx.AsyncClient(base_url=API_BASE, headers=HEADERS, timeout=60) as client:
        r = await client.post("/chat/completions", json=body)
        r.raise_for_status()
        data = r.json()
        return data["choices"][0]["message"]["content"]
