from sqlalchemy.orm import Session

from models import schemas
from entity import models


def create_coin(db: Session, coin: str, price: float):
    db_coin = models.Coin(name=coin, price=price)
    db.add(db_coin)
    db.commit()
    db.refresh(db_coin)
    return db_coin
