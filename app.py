import requests
from decouple import config
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = config('POSTGRES')

db = SQLAlchemy(app)

# entity needs to be placed after app and db is created
from entity.coin_tracker import Coin_tracker

# can be used to creade tables from the entity classes
db.create_all()

@app.route('/price/', methods=['GET'])
def get_price():
    if 'coin' in request.args:
        coin = str(request.args.get('coin'))
        r =requests.get('https://api.coingecko.com/api/v3/simple/price?ids=' + coin + '&vs_currencies=usd')
        price = float(r.json()[coin]['usd'])
    if price:
        coin_tracker = Coin_tracker(coin=coin, price=price)
        db.session.add(coin_tracker)
        db.session.commit()
        return jsonify(price)
    else:
        return 'Internal Server Error'

if __name__ == '__main__':
    app.run()
