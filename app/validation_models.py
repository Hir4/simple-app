from pydantic import BaseModel
from typing import Optional, Annotated
from fastapi import Query

class AccountModel(BaseModel):
  id: Optional[str] = None
  name: str
  password: str

class ExchangeModel(BaseModel):
  symbol: Annotated[Optional[str], Query(pattern=r"\b(?:BRL|USD)\b")]
  start_date: Optional[str] = None
  end_date: Optional[str] = None