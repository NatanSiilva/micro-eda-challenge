from src.application.shared.entities import BaseEntity
from src.application.entities.validator_balances_entity import ValidatorBalances


class BalancesEntity(BaseEntity, ValidatorBalances):
    def __init__(self, 
            account_id: str, 
            balance: int,
            id: str = None, 
            created_at: str = None, 
            updated_at: str = None
        ):

        super().__init__(id, created_at, updated_at)
        
        self._account_id = account_id
        self._balance = balance

        self.validator(self)

    @property
    def get_account_id(self):
        return self._account_id
    
    @property
    def get_balance(self):
        return self._balance
    
    def add_new_balance(self, new_balance):
        self._balance = new_balance