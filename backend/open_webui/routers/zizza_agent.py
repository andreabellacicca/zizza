import logging
from typing import List, Optional, Annotated
from datetime import datetime
import time
import math
import json

from pydantic import BaseModel
from fastapi import APIRouter, Depends, HTTPException, Request, status
from fastapi.responses import StreamingResponse

from open_webui.env import SRC_LOG_LEVELS
from open_webui.utils.auth import get_admin_user, get_password_hash, get_verified_user


log = logging.getLogger(__name__)
log.setLevel(SRC_LOG_LEVELS["MODELS"])

router = APIRouter()


@router.get("/models")
async def models():
    agents = []
    agents.append({
        'id': 'ZizZA',
        'object': "model",
        "created": math.floor(datetime.utcnow().timestamp()),
        "owned_by": "Andre&WhooW"
    })

    resp = {
        "object": "list",
        "data": agents
    }
    return resp


class ChatCompletionRequest(BaseModel):
    model: str
    messages: List
    max_tokens: Optional[int] = 512
    temperature: Optional[float] = 0.1
    stream: Optional[bool] = False
    seed: Optional[int] = None
    top_p: Optional[int] = 1
    user: Optional[dict] = None

def _create_packet(id_i: int | str,
                   text: str,
                   model: str,
                   finish_reason: str | None = None):
    chunk = {
        "id": str(id_i),
        "object": "chat.completion.chunk",
        "created": int(time.time()),
        "model": model,
        "choices": [{
            "index": 0,
            "delta":
                {
                    "content": text,
                },
            'logprobs': None,
            'finish_reason': finish_reason,

        }],
    }
    return chunk

def answer():
    i = 0
    chunk = _create_packet(f"##{i}_nodename\n", "ROBE DA FARE", "ZizZA")
    yield f"data: {json.dumps(chunk)}\n\n"
    yield "data: [DONE]\n\n"

def answer_no():
    i = 0
    chunk = _create_packet(i, f"##WHY BRO???", "No ZizZA")
    yield f"data: {json.dumps(chunk)}\n\n"
    yield "data: [DONE]\n\n"

class ChatMessage(BaseModel):
    role: str
    content: str

@router.post("/chat/completions")
async def chat_completions(request: ChatCompletionRequest):
    print("INIT REQUEST")
    print(f"->{request}")
    print(f"request: \n{request.messages[-2:]}")
    print(f"Stream: {request.stream}\n\n**************")
    if request.stream:
        if request.model == "ZizZA":
            return StreamingResponse(answer(),
                                     media_type="text/event-stream")
        else:
            return StreamingResponse(answer_no(),
                                     media_type="text/event-stream",
                                     )
    else:
        response = {
            "id": "5000",
            "object": "chat.completion",
            "created": int(time.time()),
            "model": request.model,
            "choices": [{
                "message": ChatMessage(role="assistant", content='Nuova Chat')}]
        }
        return response



