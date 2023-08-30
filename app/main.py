# TODO: usar o injetor de dependencias do fastapi para injetar conexão com o banco de dados
from fastapi import FastAPI, Response, status
from fastapi.encoders import jsonable_encoder
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse

import app.db_functions as db
from app.validation_models import (
    AccountModel,
    ApiWeatherModel,
    ResponseGetAccountNotFound,
    ResponseGetOrCreateAccount,
    ResponseHistoricalWeather,
    ResponseHttpResult,
)

app = FastAPI()


@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request, exc):
    return JSONResponse(
        content=jsonable_encoder(
            ResponseHttpResult(detail={"message": exc.errors(), "body": exc.body})
        ),
        status_code=status.HTTP_400_BAD_REQUEST,
    )


@app.get("/")
async def home() -> ResponseHttpResult:
    return ResponseHttpResult(detail={"message": "Hello World"})


@app.post("/create_account/", status_code=status.HTTP_201_CREATED)
async def create_account(
    new_account: AccountModel, response: Response
) -> (ResponseGetOrCreateAccount | ResponseHttpResult):
    result = db.create_account(new_account)
    if "duplicate" in result:
        response.status_code = status.HTTP_409_CONFLICT
        return ResponseHttpResult(detail={"message": result})
    return ResponseGetOrCreateAccount(
        {
            "id": result["id"],
            "username": result["username"],
            "password": result["password"],
            "inserted_at": result["inserted_at"],
        }
    )


@app.get("/get_account_by_name/{account_name}")
async def get_account_by_name(
    account_name: str, response: Response
) -> (ResponseGetOrCreateAccount | ResponseGetAccountNotFound):
    result = db.get_account_by_name(account_name)
    if result is None:
        response.status_code = status.HTTP_404_NOT_FOUND
        return ResponseGetAccountNotFound({"message": "Account not found"})
    print("OLHE AQUI", result)
    return ResponseGetOrCreateAccount(
        {
            "id": result[0],
            "username": result[1],
            "password": result[2],
            "inserted_at": result[3],
        }
    )


@app.post("/historical_weather/")
async def historical_weather(
    coordinates_date: ApiWeatherModel,
) -> ResponseHistoricalWeather:
    result = db.insert_weather_table(coordinates_date)
    return ResponseHistoricalWeather(
        {
            "id": result["id"],
            "latitude": result["latitude"],
            "longitude": result["longitude"],
            "start_date": result["start_date"],
            "end_date": result["end_date"],
            "inserted_at": result["inserted_at"],
        }
    )


# curl -d '{"latitude": -23.5475, "longitude": -46.6361, "start_date": "2023-07-28", "end_date": "2023-08-02"}' -H "Content-Type: application/json" -X POST  http://localhost:8080/historical_weather/

# curl -d '{"username":"fael", "password": "123"}' -H "Content-Type: application/json" -X POST http://localhost:8080/create_account/

# curl http://localhost:8080/get_account_by_name/Fael

# curl http://localhost:8080/
