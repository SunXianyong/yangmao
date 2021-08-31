from fastapi import FastAPI, APIRouter
from pydantic import BaseModel
from typing import Optional
from starlette.responses import JSONResponse
from wechatpy.utils import check_signature
from wechatpy.exceptions import InvalidSignatureException

from services import button, mssg

app = FastAPI()
router = APIRouter()


class Item(BaseModel):
    name: str
    price: float
    is_offer: Optional[bool] = None


@app.get("/weixin")
async def main(signature, timestamp, nonce, echostr):
    try:
        check_signature('sxy122333', str(signature), str(timestamp), str(nonce))
    except InvalidSignatureException:
        print("微信验证失败")
        return "微信验证失败"
    return int(echostr)


app.include_router(mssg.router, default_response_class='application/xml')

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=80)
