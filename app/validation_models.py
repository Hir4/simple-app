from datetime import datetime
from typing import Optional, Union

from pydantic import BaseModel
from typing_extensions import TypedDict


class AccountModelRequest(BaseModel):
    id: Optional[str] = None
    username: str
    password: str
    inserted_at: Optional[datetime] = None


class ApiWeatherModelRequest(BaseModel):
    id: Optional[str] = None
    latitude: float
    longitude: float
    start_date: str
    end_date: str
    inserted_at: Optional[datetime] = None


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
    inserted_at: Union[str, datetime]
