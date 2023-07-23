from typing import Annotated, Optional

from fastapi import Query
from pydantic import BaseModel


class AccountModel(BaseModel):
    id: Optional[str] = None
    username: str
    password: str


class ExchangeModel(BaseModel):
    symbol: Annotated[str, Query(pattern=r"\b(?:BRL|USD)\b")]
    start_date: Optional[str] = None
    end_date: Optional[str] = None
