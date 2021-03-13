from datetime import datetime

from pydantic import BaseModel


class CoinBase(BaseModel):
    name: str
    price: float


class Coin(CoinBase):
    id: int
    time_created: datetime

    class Config:
        orm_mode = True
