from fastapi import FastAPI, Response, status
from fastapi.encoders import jsonable_encoder
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse

import app.db_functions as db
from app.validation_models import AccountModel, ApiWeatherModel, HttpResult

app = FastAPI()


@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request, exc):
    return JSONResponse(
        content=jsonable_encoder(
            HttpResult(detail={"message": exc.errors(), "body": exc.body})
        ),
        status_code=status.HTTP_400_BAD_REQUEST,
    )


@app.get("/")
async def home() -> HttpResult:
    return HttpResult(detail={"message": "Hello World"})


@app.post("/create_account/", status_code=status.HTTP_201_CREATED)
async def create_account(new_account: AccountModel, response: Response) -> HttpResult:
    result = db.create_account(new_account)
    if "duplicate" in result:
        response.status_code = status.HTTP_409_CONFLICT
    return HttpResult(detail={"message": result})


@app.get("/get_account_by_name/{account_name}")
async def get_account_by_name(account_name: str, response: Response) -> HttpResult:
    result = db.get_account_by_name(account_name)
    if result is None:
        response.status_code = status.HTTP_404_NOT_FOUND
        return HttpResult(detail={"message": "Account not found"})

    return HttpResult(detail={"message": result})


@app.post("/historical_weather/")
async def historical_weather(coordinates_date: ApiWeatherModel) -> HttpResult:
    result = db.insert_weather_table(coordinates_date)
    return HttpResult(detail={"message": result})


# curl -d '{"latitude": -23.5475, "longitude": -46.6361, "start_date": "2023-07-28", "end_date": "2023-08-02"}' -H "Content-Type: application/json" -X POST  http://localhost:8080/historical_weather/
# curl -d '{"username":"fael", "password": "123"}' -H "Content-Type: application/json" -X POST http://localhost:8080/create_account/
# curl http://localhost:8080/get_account_by_name/Fael
# curl http://localhost:8080/
