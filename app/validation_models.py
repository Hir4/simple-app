from typing import Optional

from pydantic import BaseModel


class AccountModel(BaseModel):
    id: Optional[str] = None
    username: str
    password: str


class ExchangeModel(BaseModel):
    symbol: str
    timestamp: Optional[str] = None
    # symbol: Annotated[str, Query(pattern=r"\b(?:BRL|USD|ethbtc)\b")]
    # start_date: Optional[str] = None
    # end_date: Optional[str] = None
