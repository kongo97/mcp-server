from fastapi import FastAPI, Request
from fastapi.responses import StreamingResponse
from pydantic import BaseModel
import asyncio
import json

app = FastAPI()

# ==== STRUMENTI NORMALI ====

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/gmail/inbox/count")
def get_inbox_count():
    mail_count = 1
    return {"inbox": mail_count}

@app.get("/gmail/read/id")
def read_email():
    mail_content = "Dear Client, Some text Some text Some text Some text Some text..."
    return {"content": mail_content}

# ==== MCP ENDPOINT (SSE) ====

@app.get("/mcp")
async def mcp_sse(request: Request):
    async def event_stream():
        # Simula un tool disponibile
        tool_def = {
            "name": "get_inbox_count",
            "description": "Ritorna il numero di email non lette nella casella Gmail.",
            "parameters": {},
        }
        yield f"data: {json.dumps({'tool': tool_def})}\n\n"
        await asyncio.sleep(0.5)

        # Simula una richiesta di esecuzione
        result = get_inbox_count()
        tool_output = {
            "tool_name": "get_inbox_count",
            "output": result,
        }
        yield f"data: {json.dumps(tool_output)}\n\n"

    return StreamingResponse(event_stream(), media_type="text/event-stream")
