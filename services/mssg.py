from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()


class WeiXinData(BaseModel):
    pass


@router.post("/weixin")
async def mssg(itme: WeiXinData):
    print(itme)
