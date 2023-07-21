from fastapi import FastAPI
from validation_models import AccountModel, ExchangeModel
import uuid
from datetime import datetime


app = FastAPI()

@app.get("/")
async def home():
  return {"message": "Hello World"}

@app.post("/create_account/")
async def create_account(created_account: AccountModel):
  created_account.id = uuid.uuid4().hex
  return created_account

@app.post("/exchange_rate/")
async def exchange_rate(exchange_symbol: ExchangeModel):
  exchange_symbol.start_date = datetime.strptime(exchange_symbol.start_date, "%Y-%m-%d")
  exchange_symbol.end_date = datetime.strptime(exchange_symbol.end_date, "%Y-%m-%d")
  return exchange_symbol

# curl -d '{"id":"1", "name":"fael", "password": "123"}' -H "Content-Type: application/json" -X POST http://localhost:8000/create_account/
# curl -d '{"symbol":"BRL", "start_date": "2023-01-01", "end_date": "2023-02-02"}' -H "Content-Type: application/json" -X POST http://localhost:8000/exchange_rate/
# curl -d '{"symbol":"USD", "start_date": "2023-01-01", "end_date": "2023-02-02"}' -H "Content-Type: application/json" -X POST http://localhost:8000/exchange_rate/