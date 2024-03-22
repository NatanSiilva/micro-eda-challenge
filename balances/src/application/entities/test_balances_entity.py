import unittest
from uuid import uuid4
from datetime import datetime

from src.application.entities import BalancesEntity
from src.application.shared.exception import ValidationException


class TestBalancesEntity(unittest.TestCase):
    def test_init(self):
        account_id = str(uuid4())
        balance = 1000
        entity = BalancesEntity(account_id, balance)

        self.assertEqual(entity.get_account_id, account_id)
        self.assertEqual(entity.get_balance, balance)

    def test_invalid_init(self):
        account_id = 111
        balance = 10

        with self.assertRaises(ValidationException) as assert_error:
            BalancesEntity(account_id, balance)

        self.assertEqual(
            "The account_id must be a string", 
            assert_error.exception.args[0]   
        )

        account_id = str(uuid4())
        balance = 10.1

        with self.assertRaises(ValidationException) as assert_error:
            BalancesEntity(account_id, balance)

    def test_set_balance(self):
        account_id = str(uuid4())
        balance = 1000
        created_at = "2024-03-15 12:00:00"
        updated_at = "2024-03-15 12:00:00"
        entity = BalancesEntity(account_id, balance, created_at, updated_at)
    
        new_balance = 2000
        entity.add_new_balance(new_balance)
        self.assertEqual(entity.get_balance, new_balance)
