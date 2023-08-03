from datetime import datetime

import db_functions as db
import psycopg
from fastapi import FastAPI, Response, status
from validation_models import AccountModel, WeatherModel

app = FastAPI()


@app.get("/")
async def home():
    return {"message": "Hello World"}


@app.post("/create_account/")
async def create_account(new_account: AccountModel, response: Response):
    try:
        return db.create_account(new_account)
    except psycopg.Error as e:
        treated_error = str(e).split("\n")
        response.status_code = status.HTTP_409_CONFLICT
        return treated_error


@app.get("/get_accounts_by_name/{account_name}")
async def get_accounts_by_name(account_name: str, response: Response):
    result = db.get_accounts_by_name(account_name)
    if result is None:
        response.status_code = status.HTTP_404_NOT_FOUND
    return result


@app.post("/historical_weather/")
async def historical_weather(weather_info: WeatherModel):
    return db.insert_weather_table(weather_info)
