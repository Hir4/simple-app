import uuid
from datetime import datetime

import database_functions as db
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
async def exchange_rate(exchange_symbol: ExchangeModel):
    exchange_symbol.start_date = datetime.strptime(
        exchange_symbol.start_date, "%Y-%m-%d"
    )
    exchange_symbol.end_date = datetime.strptime(exchange_symbol.end_date, "%Y-%m-%d")
    return exchange_symbol


# curl http://localhost:8080/
# curl http://localhost:8080/accounts_created/
# curl -d '{"username":"fael", "password": "123"}' -H "Content-Type: application/json" -X POST http://localhost:8080/create_account/
# curl -d '{"password": "123"}' -H "Content-Type: application/json" -X POST http://localhost:8080/create_account/
# curl -d '{"symbol":"BRL", "start_date": "2023-01-01", "end_date": "2023-02-02"}' -H "Content-Type: application/json" -X POST http://localhost:8080/exchange_rate/
# curl -d '{"symbol":"USD", "start_date": "2023-01-01", "end_date": "2023-02-02"}' -H "Content-Type: application/json" -X POST http://localhost:8080/exchange_rate/
