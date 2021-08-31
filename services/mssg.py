from fastapi import APIRouter
from pydantic import BaseModel
from starlette.requests import Request
from starlette.responses import HTMLResponse, Response

router = APIRouter()


@router.post("/weixin")
async def mssg(request: Request):
    print(await request.body())
    return HTMLResponse('success')
