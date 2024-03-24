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

        self.balances_entity = BalancesEntity(
            account_id=self.account_id,
            balance=self.balance,
        )

    def test_create_balance(self):
        balance_obj = self.repository.create(entity=self.balances_entity)
        self.assertIsInstance(balance_obj, Balances)

        deleted = self.repository.delete(balance_obj.id)
        self.assertTrue(deleted)

    def test_get_balance_by_id(self):
        balance_obj = self.repository.create(entity=self.balances_entity)
        retrieved_balance = self.repository.get_by_id(balance_obj.id)

        self.assertEqual(balance_obj, retrieved_balance)

        deleted = self.repository.delete(balance_obj.id)
        self.assertTrue(deleted)

    def test_get_balance_by_account_id(self):
        balance_obj = self.repository.create(entity=self.balances_entity)
        retrieved_balance = self.repository.get_by_account_id(balance_obj.account_id)

        self.assertEqual(balance_obj, retrieved_balance)

        deleted = self.repository.delete(balance_obj.id)
        self.assertTrue(deleted)

    def test_get_or_create(self):
        balance_obj = self.repository.create(entity=self.balances_entity)
        created, retrieved_balance = self.repository.get_or_create(
            entity=self.balances_entity
        )

        self.assertFalse(created)
        self.assertEqual(balance_obj, retrieved_balance)

        deleted = self.repository.delete(balance_obj.id)
        self.assertTrue(deleted)

        created, retrieved_balance = self.repository.get_or_create(
            entity=self.balances_entity
        )
        self.assertTrue(created)
        self.assertIsInstance(retrieved_balance, Balances)

        deleted = self.repository.delete(retrieved_balance.id)
        self.assertTrue(deleted)

    def test_get_all_balances(self):
        self.repository.create(entity=self.balances_entity)
        balances = self.repository.get_all()

        self.assertIsInstance(balances, List)
        self.assertTrue(all(isinstance(balance, Balances) for balance in balances))

        for b in balances:
            deleted = self.repository.delete(b.id)
            self.assertTrue(deleted)

    def test_update_balance(self):
        balance_obj = self.repository.create(entity=self.balances_entity)

        new_balance = 30000

        updated_balance = BalancesEntity(
            account_id=balance_obj.account_id,
            balance=new_balance,
        )

        updated_balance_obj = self.repository.update(entity=updated_balance)

        self.assertEqual(updated_balance_obj.balance, new_balance)

        deleted = self.repository.delete(balance_obj.id)
        self.assertTrue(deleted)
        
    def test_delete(self):
        entity = self.repository.create(entity=self.balances_entity)

        result = self.repository.delete(entity.id)

        self.assertTrue(result)
