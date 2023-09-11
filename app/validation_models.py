from dataclasses import dataclass
from datetime import datetime


@dataclass
class AccountModel:
    id: str
    username: str
    password: str
    inserted_at: datetime


@dataclass
class AccountModelRequest:
    username: str
    password: str


@dataclass
class ApiWeatherModel:
    id: str
    latitude: float
    longitude: float
    start_date: str
    end_date: str
    inserted_at: datetime


@dataclass
class ApiWeatherModelRequest:
    latitude: float
    longitude: float
    start_date: str
    end_date: str


@dataclass
class HttpResultResponse:
    detail: dict


@dataclass
class GetOrCreateAccountResponse:
    id: str
    username: str
    password: str
    inserted_at: datetime


@dataclass
class GetAccountNotFoundResponse:
    message: str


@dataclass
class HistoricalWeatherResponse:
    id: str
    latitude: float
    longitude: float
    start_date: str
    end_date: str
    inserted_at: datetime
