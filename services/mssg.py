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
    reply.content = '小主，您的外卖红包来了~\n今日的外卖红包已更新！\n-----------------------\n\n🔜<a href="weixin://bizmsgmenu?msgmenucontent=%E3%80%90%E7%82%B9%E6%88%91%E3%80%91%E9%A5%BF%E4%BA%86%E4%B9%88%E7%BA%A2%E5%8C%85&msgmenuid=0">【点我】饿了么红包</a >\n\n🔜<a href="weixin://bizmsgmenu?msgmenucontent=%E3%80%90%E7%82%B9%E6%88%91%E3%80%91%E7%BE%8E%E5%9B%A2%E7%BA%A2%E5%8C%85&msgmenuid=0">【点我】美团外卖红包</a >\n\n❗❗❗提示：如领取红包时显示暂无福利请再领一次~\n---------------------\n【点击菜单栏，每天领最新红包】'
    reply.content = '&lt;a href=&quot;weixin://www.2345.com/?k381740148&quot;&gt;这是个超链接&lt;/a&gt;'
    # reply.content = '&lt;a href=&quot;weixin://bizmsgmenu?msgmenucontent=test&amp;msgmenuid=0&quot;&gt;【点我】饿了么红包&lt;/a&gt;'
                    # '&lt;a href=&quot;weixin://bizmsgmenu?msgmenucontent=%E3%80%90%E7%82%B9%E6%88%91%E3%80%91%E7%BE%8E%E5%9B%A2%E7%BA%A2%E5%8C%85&amp;msgmenuid=0&quot;&gt;【点我】美团外卖红包&lt;/a &gt;'

    # 转换成 XML
    xml = reply.render()
    print(xml)
    return HTMLResponse(xml)
