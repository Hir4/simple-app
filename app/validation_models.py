from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class AccountModel(BaseModel):
    id: Optional[str] = None
    username: str
    password: str
    inserted_at: Optional[datetime] = None


class WeatherModel(BaseModel):
    id: Optional[str] = None
    latitude: float
    longitude: float
    start_date: str
    end_date: str
    inserted_at: Optional[datetime] = None

class HttpResult(BaseModel):
    detail: dict
