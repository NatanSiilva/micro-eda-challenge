import unittest
from datetime import datetime
from uuid import uuid4
from src.application.entities import BalancesEntity

class TestBalancesEntity(unittest.TestCase):
    def test_init(self):
        account_id = str(uuid4())
        balance = 1000
        created_at = "2024-03-15 12:00:00"
        updated_at = "2024-03-15 12:00:00"
        entity = BalancesEntity(account_id, balance, created_at, updated_at)
        self.assertEqual(entity.get_account_id, account_id)
        self.assertEqual(entity.get_balance, balance)
        self.assertEqual(entity.created_at, created_at)
        self.assertEqual(entity.updated_at, updated_at)

    def test_set_balance(self):
        account_id = str(uuid4())
        balance = 1000
        created_at = "2024-03-15 12:00:00"
        updated_at = "2024-03-15 12:00:00"
        entity = BalancesEntity(account_id, balance, created_at, updated_at)
    
        new_balance = 2000
        entity.add_new_balance(new_balance)
        self.assertEqual(entity.get_balance, new_balance)


