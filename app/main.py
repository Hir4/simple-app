import json
import uuid
from datetime import datetime

import db_functions as db
import requests
from fastapi import FastAPI
from validation_models import AccountModel, ExchangeModel

app = FastAPI()


@app.get("/")
async def home():
    return {"message": "Hello World"}


@app.post("/create_account/")
async def create_account(new_account: AccountModel):
    new_account.id = uuid.uuid4().hex
    return db.create_account(new_account)


@app.get("/accounts_created/")
async def account_created():
    return db.get_accounts()


@app.post("/exchange_rate/")
async def exchange_rate(exchange_rate: ExchangeModel):
    # https://docs.gemini.com/rest-api/#trade-history
    payload = {"timestamp": f"{exchange_rate.timestamp}"}
    currency_trades = requests.get(
        f"https://api.gemini.com/v1/trades/{exchange_rate.symbol}", payload
    )
    # currency_ticker = requests.get(f"https://api.gemini.com/v2/ticker/{exchange_rate.symbol}")
    currency_trades_treated = json.loads(currency_trades.text)
    for index, value in enumerate(currency_trades_treated):
        currency_trades_treated[index]["id"] = uuid.uuid4().hex
        currency_trades_treated[index]["symbol"] = exchange_rate.symbol
    return db.insert_exchange_rate_table(currency_trades_treated)


## get accounts
# curl http://localhost:8080/
# curl http://localhost:8080/accounts_created/

## post account
# curl -d '{"username":"fael", "password": "123"}' -H "Content-Type: application/json" -X POST http://localhost:8080/create_account/
# curl -d '{"password": "123"}' -H "Content-Type: application/json" -X POST http://localhost:8080/create_account/

## post API exchange_rate
# curl -d '{"timestamp":"1690243200", "symbol": "ethbtc"}' -H "Content-Type: application/json" -X POST  http://localhost:8080/exchange_rate/
# curl -d '{"symbol":"BRL", "start_date": "2023-01-01", "end_date": "2023-02-02"}' -H "Content-Type: application/json" -X POST http://localhost:8080/exchange_rate/
# curl -d '{"symbol":"USD", "start_date": "2023-01-01", "end_date": "2023-02-02"}' -H "Content-Type: application/json" -X POST http://localhost:8080/exchange_rate/
