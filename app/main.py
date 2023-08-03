import db_functions as db
import psycopg
from fastapi import FastAPI, Response, status
from fastapi.encoders import jsonable_encoder
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from validation_models import AccountModel, WeatherModel

app = FastAPI()


@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request, exc):
    return JSONResponse(
        content=jsonable_encoder({"message": exc.errors(), "body": exc.body}),
        status_code=status.HTTP_400_BAD_REQUEST,
    )


@app.get("/")
async def home():
    return {"message": "Hello World"}


@app.post("/create_account/", status_code=status.HTTP_201_CREATED)
async def create_account(new_account: AccountModel, response: Response):
    try:
        result = db.create_account(new_account)
        return {"message": result}
    except psycopg.Error as e:
        return JSONResponse(
            status_code=status.HTTP_409_CONFLICT,
            content=jsonable_encoder({"message": f"{e}"}),
        )


@app.get("/get_accounts_by_name/{account_name}")
async def get_accounts_by_name(account_name: str):
    result = db.get_accounts_by_name(account_name)
    if result is None:
        return JSONResponse(
            status_code=status.HTTP_404_NOT_FOUND,
            content={"message": "Account not found"},
        )
    return {"message": result}


@app.post("/historical_weather/")
async def historical_weather(weather_info: WeatherModel):
    result = db.insert_weather_table(weather_info)
    return {"message": result}

# curl -d '{"latitude": -23.5475, "longitude": -46.6361, "start_date": "2023-07-28", "end_date": "2023-08-02"}' -H "Content-Type: application/json" -X POST  http://localhost:8080/historical_weather/
# curl -d '{"username":"fael", "password": "123"}' -H "Content-Type: application/json" -X POST http://localhost:8080/create_account/
# curl http://localhost:8080/get_accounts_by_name/Fael
# curl http://localhost:8080/