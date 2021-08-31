from fastapi import APIRouter
from starlette.requests import Request
from starlette.responses import HTMLResponse
from wechatpy import parse_message
from wechatpy.replies import TextReply, to_text
from wechatpy.fields import BaseField

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
    msg = parse_message(await request.body())
    print(msg)

    reply = NewTextReply(message=msg)
    reply.content = '&lt;a href=&quot;weixin://bizmsgmenu?msgmenucontent=美团红包&amp;msgmenuid=0&quot;&gt;美团红包&lt;/a&gt;' \
                    '&lt;a href=&quot;weixin://bizmsgmenu?msgmenucontent=饿了吗红包&amp;msgmenuid=0&quot;&gt;饿了吗红包&lt;/a&gt;'

    # 转换成 XML
    xml = reply.render()
    print(xml)
    return HTMLResponse(xml)
