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
        check_signature('sxy122333', signature, timestamp, nonce)
    except InvalidSignatureException:
        return {"微信验证失败"}
    return echostr


app.include_router(button.router, prefix='/button', default_response_class=JSONResponse)
app.include_router(mssg.router, prefix='/wexin', default_response_class=JSONResponse)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=80)
