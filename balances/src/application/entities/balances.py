from src.application.shared import BaseEntity



class BalancesEntity(BaseEntity):
    def __init__(self, account_id: str, balance: int, created_at: str, updated_at: str):
        super().__init__(id, created_at, updated_at)
        
        self._account_id = account_id
        self._balance = balance

    @property
    def get_account_id(self):
        return self._account_id
    
    @property
    def get_balance(self):
        return self._balance
    
    def add_new_balance(self, new_balance):
        self._balance = new_balance