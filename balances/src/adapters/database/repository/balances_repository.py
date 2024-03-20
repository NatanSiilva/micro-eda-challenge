from typing import List, Optional

from sqlmodel import Session, select
from src.adapters.database import DatabaseManager
from src.adapters.database.models import Balances


class BalancesRepository:
    def __init__(self, database_manager: DatabaseManager) -> None:
        self.db = database_manager

    def create_balance(self, account_id: str, balance: int, created_at: str, updated_at: str) -> Balances:
        with self.db.get_session() as session:
            balance_obj = Balances(account_id=account_id, balance=balance, created_at=created_at, updated_at=updated_at)
            session.add(balance_obj)
            session.commit()
            session.refresh(balance_obj)
            return balance_obj

    def get_balance_by_id(self, balance_id: int) -> Optional[Balances]:
        with self.db.get_session() as session:
            return session.get(Balances, balance_id)

    def get_all_balances(self) -> List[Balances]:
        with self.db.get_session() as session:
            statement = select(Balances)
            return session.exec(statement).all()
