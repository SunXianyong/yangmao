from fastapi import APIRouter
from starlette.requests import Request
from starlette.responses import HTMLResponse
from wechatpy import parse_message
from wechatpy.replies import TextReply


router = APIRouter()


@router.post("/weixin")
async def mssg(request: Request):
    msg = parse_message(await request.body())

    reply = TextReply(message=msg)
    reply.content = '测试'
    # 转换成 XML
    xml = reply.render()

    return HTMLResponse(xml)
