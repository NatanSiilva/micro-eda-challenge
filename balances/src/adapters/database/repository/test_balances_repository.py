from uuid import uuid4
import unittest
from datetime import datetime
from typing import List, Optional

from src.adapters.database import DatabaseManager
from src.adapters.database.models import Balances
from src.application.entities import BalancesEntity
from src.adapters.database.repository import BalancesRepository


class TestBalancesRepository(unittest.TestCase):
    def setUp(self):
        self.database_manager = DatabaseManager()
        self.repository = BalancesRepository(self.database_manager)

        self.account_id = str(uuid4())
        self.balance = 25000
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

        self.balances_entity = BalancesEntity(
            account_id=self.account_id,
            balance=self.balance,
            created_at=self.created_at,
            updated_at=self.updated_at
        )

    def test_create_balance(self):
        balance_obj = self.repository.create_balance(
            self.account_id,
            self.balance,
            self.created_at,
            self.updated_at
        )

        self.assertIsInstance(balance_obj, Balances)

    def test_get_balance_by_id(self):
        balance_obj = self.repository.create_balance(
            self.account_id,
            self.balance,
            self.created_at,
            self.updated_at
        )

        retrieved_balance = self.repository.get_balance_by_id(balance_obj.id)

        self.assertEqual(balance_obj, retrieved_balance)

    def test_get_all_balances(self):
        self.repository.create_balance(
            self.account_id,
            self.balance,
            self.created_at,
            self.updated_at
        )

        balances = self.repository.get_all_balances()

        self.assertIsInstance(balances, List)
        self.assertTrue(all(isinstance(balance, Balances) for balance in balances))

