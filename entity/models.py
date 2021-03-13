from sqlalchemy import Column, Integer, String, Float, DateTime, func

from db.database import Base


class Coin(Base):
    __tablename__ = 'coin_tracker'

    id = Column('id', Integer, primary_key=True)
    name = Column('coin', String(255), nullable=False)
    price = Column('price', Float(), nullable=False)
    time_created = Column('time_created', DateTime, default=func.current_timestamp())
