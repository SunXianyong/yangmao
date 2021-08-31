from fastapi import APIRouter
from starlette.requests import Request
from starlette.responses import HTMLResponse
from wechatpy import parse_message
from wechatpy.replies import TextReply


router = APIRouter()


@router.post("/weixin")
async def mssg(request: Request):
    msg = parse_message(await request.body())
    print(msg)

    reply = TextReply(message=msg)
    reply.content = '小主，您的外卖红包来了~\n' \
                    '今日的外卖红包已更新！\n' \
                    '-----------------------\n\n' \
                    '🔜&lt;a href=&quot;weixin://bizmsgmenu?msgmenucontent=%E3%80%90%E7%82%B9%E6%88%91%E3%80%91%E9%A5%BF%E4%BA%86%E4%B9%88%E7%BA%A2%E5%8C%85&amp;msgmenuid=0&quot;&gt;【点我】饿了么红包&lt;/a &gt;\n\n' \
                    '🔜&lt;a href=&quot;weixin://bizmsgmenu?msgmenucontent=%E3%80%90%E7%82%B9%E6%88%91%E3%80%91%E7%BE%8E%E5%9B%A2%E7%BA%A2%E5%8C%85&amp;msgmenuid=0&quot;&gt;【点我】美团外卖红包&lt;/a &gt;\n\n' \
                    '❗❗❗提示：如领取红包时显示暂无福利请再领一次~\n' \
                    '---------------------\n' \
                    '【点击菜单栏，每天领最新红包】'

    # 转换成 XML
    xml = reply.render()
    print(xml)
    return HTMLResponse(xml)
