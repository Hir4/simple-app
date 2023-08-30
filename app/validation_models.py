from datetime import datetime
from typing import Optional, Union

from pydantic import BaseModel
from typing_extensions import TypedDict


class AccountModel(BaseModel):
    id: Optional[str] = None
    username: str
    password: str
    inserted_at: Optional[datetime] = None


class ApiWeatherModel(BaseModel):
    id: Optional[str] = None
    latitude: float
    longitude: float
    start_date: str
    end_date: str
    inserted_at: Optional[datetime] = None


class ResponseHttpResult(BaseModel):
    detail: dict


class ResponseGetOrCreateAccount(TypedDict):
    id: str
    username: str
    password: str
    inserted_at: datetime


class ResponseGetAccountNotFound(TypedDict):
    message: str


class ResponseHistoricalWeather(TypedDict):
    id: str
    latitude: float
    longitude: float
    start_date: str
    end_date: str
    inserted_at: Union[str, datetime]
