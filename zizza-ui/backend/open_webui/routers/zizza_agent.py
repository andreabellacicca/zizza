import logging
from typing import List, Optional, Annotated
from datetime import datetime
import time
import math
import json
import requests as r
import os
from pydantic import BaseModel
from fastapi import APIRouter, Depends, HTTPException, Request, status
from fastapi.responses import StreamingResponse
from fastapi.security import OAuth2PasswordBearer

from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder


from open_webui.env import SRC_LOG_LEVELS
from open_webui.utils.auth import get_admin_user, get_password_hash, get_verified_user

ZIZZA_BLOCKCHAIN_INTENTS_SERVER_HOST = os.getenv("ZIZZA_BLOCKCHAIN_INTENTS_SERVER_HOST", "localhost")


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


log = logging.getLogger(__name__)
log.setLevel(SRC_LOG_LEVELS["MODELS"])

router = APIRouter()


@router.get("/models")
async def models(token: Annotated[str, Depends(oauth2_scheme)]):
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

def answer(message, history, token: str):
    print(f"Message: {message}")
    print(f"History: {history}")
    total_message = ""
    # CUT THE HISTORY TO THE LAST MESSAGES
    for hist in history[-4:]:
        total_message += f"{hist['content']}\n"
    total_message += message['content']
    llm = ChatOpenAI(model="ZizZA",
                     base_url="https://www.compai.team/api/v1/owui",
                     api_key=token,
                     streaming=True)
    prompt = ChatPromptTemplate.from_messages(
        [
            ("user", "{message}"),
        ]
    )
    agent = prompt | llm
    i = 0
    response = ""
    for msg in agent.stream({'message': total_message}):
        print(f"Msg: {msg}")
        if i == 0:
            i+=1
            continue
        if hasattr(msg, 'content'):
            print(f"Msg content: {msg.content}")
            response += msg.content
            chunk = _create_packet(i, msg.content, "ZizZA")
            yield f"data: {json.dumps(chunk)}\n\n"
            i += 1
    chunk = _create_packet(i, "Answer execute to confirm\n", "ZizZA")
    yield f"data: {json.dumps(chunk)}\n\n"
    print(f"Resp: {response}")
    # cmds = json.loads(split[1].replace("'", '"'))
    yield "data: [DONE]\n\n"

def execute(cmd, token):
    llm = ChatOpenAI(model="ZizZA Exe",
                     base_url="https://www.compai.team/api/v1/owui",
                     api_key=token,
                     streaming=True)
    prompt = ChatPromptTemplate.from_messages(
        [
            ("user", "{message}"),
        ]
    )
    agent = prompt | llm
    response = agent.invoke({'message': cmd})
    print(response)
    cmds = response.content
    cmds = cmds.split("\n",1)
    cmds = cmds[1]
    print(f"Cmds: {cmds}")
    i = 0
    try:
        cmds_dict = json.loads(cmds)
    except Exception:
        chunk = _create_packet(i, "There was an error while analyzing the command\n", "ZizZA")
        yield f"data: {json.dumps(chunk)}\n\n"
        chunk = _create_packet(i+1, cmds, "ZizZA")
        yield f"data: {json.dumps(chunk)}\n\n"
        yield "data: [DONE]\n\n"
        return
    try:
        response = r.post(f"http://{ZIZZA_BLOCKCHAIN_INTENTS_SERVER_HOST}:5001/execute", json=cmds_dict)
    except Exception:
        chunk = _create_packet(i+1, "I'm not able to contact the intent server. Please, verify the connection", "ZizZA")
        yield f"data: {json.dumps(chunk)}\n\n"
        yield "data: [DONE]\n\n"
        return
    resp = response.json()
    done = False
    chunk = _create_packet(i, "Executing operations\n", "ZizZA")
    yield f"data: {json.dumps(chunk)}\n\n"
    while not done:
        time.sleep(1)
        check_response = r.get(f"http://{ZIZZA_BLOCKCHAIN_INTENTS_SERVER_HOST}:5001/status/{resp['task_id']}")
        check_json = check_response.json()
        print(f"Response: {check_json}")
        if not 'Processing' in check_json['status']:
            done = True
    print(f"Done: {check_json}")
    llm_care = ChatOpenAI(model="ZizZA Care",
                          base_url="https://www.compai.team/api/v1/owui",
                          api_key=token,
                          streaming=True)
    for result in check_json['results']:
        agent_care = prompt | llm_care
        if 'error' in result:
            text = f"## {result['command']} - FAILED\n"
            explanation = agent_care.invoke({'message': f"ERROR: {result['error']}"}).content
            text += explanation.split("\n",1)[1]
            text +="\n\n"
        else:
            text = f"## {result['command']}\n"
            explanation = agent_care.invoke({'message': f"params{result['params']}\nresults: {result['result']}"}).content
            text += explanation.split("\n",1)[1]
            text +="\n\n"
            if result['command'] == "swap":
                text += f"https://nearblocks.io/it/txns/{result['result']['tx_hash']}\n\n"
        chunk = _create_packet(i, text, "ZizZA")
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
async def chat_completions(request: ChatCompletionRequest, token: Annotated[str, Depends(oauth2_scheme)]):
    print("INIT REQUEST")
    print(f"->{request}")
    print(f"request: \n{request.messages[-3:]}")
    print(f"Stream: {request.stream}\n\n**************")
    if request.stream:
        if request.model == "ZizZA":
            if request.messages[-1]['content'] == "execute":
                return StreamingResponse(execute(request.messages[-2]['content'], token),
                                         media_type="text/event-stream")
            return StreamingResponse(answer(request.messages[-1], request.messages[:-1], token),
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



