from fastapi import APIRouter
from starlette.requests import Request
from starlette.responses import HTMLResponse
from wechatpy import parse_message
from wechatpy.replies import TextReply, to_text
from wechatpy.fields import BaseField
from wechatpy.messages import TextMessage

router = APIRouter()


class MyStringField(BaseField):

    def __to_text(self, value):
        return to_text(value)

    converter = __to_text

    def to_xml(self, value):
        value = self.converter(value)
        tpl = '<{name}>{value}</{name}>'
        return tpl.format(name=self.name, value=value)

    @classmethod
    def from_xml(cls, value):
        return value


# 原框架不支持超链接 重写
class NewTextReply(TextReply):
    """
    文本回复
    详情请参阅 http://mp.weixin.qq.com/wiki/9/2c15b20a16019ae613d413e30cac8ea1.html
    """
    type = 'text'
    content = MyStringField('Content')


@router.post("/weixin")
async def mssg(request: Request):
    msg: TextMessage = parse_message(await request.body())
    print(msg)
    content = msg.content

    if content == 'test':
        return await test(msg)
    elif content == '帮助':
        return

    reply = NewTextReply(message=msg)
    reply.content = """Hi，每天红包已供上，请先收下！
    🧧&lt;a href=&quot;http://dpurl.cn/7DnghG2z&quot;&gt;美团外卖-每日红包①&lt;/a&gt;
    🧧&lt;a href=&quot;http://dpurl.cn/9joHoGaz&quot;&gt;美团外卖-每日红包②&lt;/a&gt;
    🧧&lt;a href=&quot;http://y6.pub/uH8CWP&quot;&gt;美团生鲜超市-每日红包&lt;/a&gt;
    小技巧：
    红包金额随机，多领一个用大的。
    """
    # '--&lt;a href=&quot;weixin://bizmsgmenu?msgmenucontent=帮助&amp;msgmenuid=0&quot;&gt;【有什么不懂可以点我】&lt;/a&gt;--'
    # reply.content = '🧧&lt;a href=&quot;weixin://bizmsgmenu?msgmenucontent=美团红包&amp;msgmenuid=0&quot;&gt;美团红包&lt;/a&gt;\n' \
    #                 '🧧&lt;a href=&quot;weixin://bizmsgmenu?msgmenucontent=饿了吗红包&amp;msgmenuid=0&quot;&gt;饿了吗红包&lt;/a&gt;'

    # 转换成 XML
    xml = reply.render()
    return HTMLResponse(xml)


async def test(msg: TextMessage) -> HTMLResponse:
    reply = NewTextReply(message=msg)
    reply.content = """Hi，每天红包已供上，请先收下！
    🧧&lt;a href=&quot;http://dpurl.cn/7DnghG2z&quot;&gt;美团外卖-每日红包①&lt;/a&gt;
    🧧&lt;a href=&quot;http://dpurl.cn/9joHoGaz&quot;&gt;美团外卖-每日红包②&lt;/a&gt;
    🧧&lt;a href=&quot;http://y6.pub/uH8CWP&quot;&gt;美团生鲜超市-每日红包&lt;/a&gt;
    小技巧：
    红包金额随机，多领一个用大的。
    """
    # --&lt;a href=&quot;weixin://bizmsgmenu?msgmenucontent=帮助&amp;msgmenuid=0&quot;&gt;【有什么不懂可以点我】&lt;/a&gt;--
    # """
    return HTMLResponse(reply.render())
