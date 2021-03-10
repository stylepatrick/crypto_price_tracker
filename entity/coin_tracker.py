from app import db


class Coin_tracker(db.Model):
    __tablename__ = 'coin_tracker'

    id = db.Column('id', db.Integer, primary_key=True)
    coin = db.Column('coin', db.String(255))
    price = db.Column('price', db.Float())
    time_created = db.Column(db.DateTime, default=db.func.current_timestamp())


def __init__(self, coin, price):
    self.coin = coin
    self.price = price
