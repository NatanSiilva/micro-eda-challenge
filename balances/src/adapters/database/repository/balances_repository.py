from typing import List, Optional

from sqlmodel import select
from src.adapters.database import DatabaseManager
from src.adapters.database.models import Balances
from src.application.entities import BalancesEntity


class BalancesRepository:
    def __init__(self, database_manager: DatabaseManager) -> None:
        self.db = database_manager

    def create_balance(self, entity: BalancesEntity) -> BalancesEntity:
        with self.db.get_session() as session:
            
            balance_obj = Balances(
                id=entity.id,
                account_id=entity.get_account_id, 
                balance=entity.get_balance, 
                created_at=entity.created_at, 
                updated_at=entity.updated_at
            )
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
        

    def delete_balance(self, balance_id: str) -> None:
        with self.db.get_session() as session:
            balance_obj = session.get(Balances, balance_id)

            if balance_obj:
                session.delete(balance_obj)
                session.commit()
                return True
            else:
                raise ValueError(f"Balance with ID {balance_id} does not exist.")    
        
