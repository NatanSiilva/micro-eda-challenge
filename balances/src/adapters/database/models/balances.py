from typing import Optional
from datetime import datetime

from sqlmodel import Field, SQLModel, create_engine


class Balances(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    account_id: str
    balance: int
    created_at: datetime
    updated_at: datetime
    