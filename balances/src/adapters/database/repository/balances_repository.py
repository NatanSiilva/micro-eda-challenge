from typing import List, Optional

from sqlmodel import select
from src.adapters.database import DatabaseManager
from src.adapters.database.models import Balances
from src.application.entities import BalancesEntity


class BalancesRepository:
    def __init__(self, database_manager: DatabaseManager) -> None:
        self.db = database_manager

    def create(self, entity: Balances) -> Balances:
        with self.db.get_session() as session:

            balance_obj = Balances(
                id=entity.id,
                account_id=entity.get_account_id,
                balance=entity.get_balance,
                created_at=entity.created_at,
                updated_at=entity.updated_at,
            )
            session.add(balance_obj)
            session.commit()
            session.refresh(balance_obj)

            return balance_obj

    def get_by_id(self, balance_id: int) -> Optional[Balances]:
        with self.db.get_session() as session:
            return session.get(Balances, balance_id)

    def get_by_account_id(self, account_id: str) -> Optional[Balances]:
        with self.db.get_session() as session:
            statement = select(Balances).where(Balances.account_id == account_id)
            return session.exec(statement).first()

    def get_all(self) -> List[Balances]:
        with self.db.get_session() as session:
            statement = select(Balances)
            return session.exec(statement).all()

    def get_or_create(self, entity: BalancesEntity) -> Balances:
        balance_obj = self.get_by_account_id(entity.get_account_id)
        if balance_obj:
            return False, balance_obj
        else:
            return True, self.create(entity)

    def update(self, entity: BalancesEntity) -> Balances:
        with self.db.get_session() as session:
            balance_obj = select(Balances).where(
                Balances.account_id == entity.get_account_id
            )
            result = session.exec(balance_obj)
            balance = result.one()

            balance.balance = entity.get_balance
            session.commit()
            session.refresh(balance)

            return balance
    

    def delete(self, balance_id: str) -> None:
        with self.db.get_session() as session:
            balance_obj = session.get(Balances, balance_id)

            if balance_obj:
                session.delete(balance_obj)
                session.commit()
                return True
            else:
                raise ValueError(f"Balance with ID {balance_id} does not exist.")
