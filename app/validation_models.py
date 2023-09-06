from datetime import datetime

from pydantic import BaseModel
from typing_extensions import TypedDict


class AccountModel(BaseModel):
    id: str
    username: str
    password: str
    inserted_at: datetime


class AccountModelRequest(BaseModel):
    username: str
    password: str


class ApiWeatherModel(BaseModel):
    id: str
    latitude: float
    longitude: float
    start_date: str
    end_date: str
    inserted_at: datetime


class ApiWeatherModelRequest(BaseModel):
    latitude: float
    longitude: float
    start_date: str
    end_date: str


class HttpResultResponse(BaseModel):
    detail: dict


class GetOrCreateAccountResponse(TypedDict):
    id: str
    username: str
    password: str
    inserted_at: datetime


class GetAccountNotFoundResponse(TypedDict):
    message: str


class HistoricalWeatherResponse(TypedDict):
    id: str
    latitude: float
    longitude: float
    start_date: str
    end_date: str
    inserted_at: datetime
