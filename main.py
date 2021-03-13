import requests
import uvicorn
from decouple import config
from fastapi import FastAPI
from fastapi_utils.tasks import repeat_every

from repository import crud
from entity import models
from models import schemas
from db.database import SessionLocal, engine

port = int(config("PORT"))
scheduler_coin = config("SCHEDULERCOIN")

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.get("/api")
def hello():
    return {"Hello": "World"}


@app.get("/api/new", response_model=schemas.Coin)
def insert_manually():
    return insert_db()


@app.on_event("startup")
@repeat_every(seconds=60)
def scheduler():
    insert_db()

def insert_db():
    r = requests.get('https://api.coingecko.com/api/v3/simple/price?ids=' + scheduler_coin + '&vs_currencies=usd')
    if r.status_code == 200:
        db = SessionLocal()
        price = float(r.json()[scheduler_coin]['usd'])
        create_coin = crud.create_coin(db=db, coin=scheduler_coin, price=price)
        db.close()
        return create_coin

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=port)






