
import unittest
from datetime import datetime
from uuid import uuid4

from src.application.shared.entities import BaseEntity


class TestBaseEntity(unittest.TestCase):
    def test_init_with_default_values(self):
        entity = BaseEntity()
        self.assertIsInstance(entity.id, str)
        self.assertIsInstance(entity.created_at, datetime)
        self.assertIsInstance(entity.updated_at, datetime)

    def test_init_with_given_values(self):
        id_ = uuid4()
        created_at = "2024-03-15 12:00:00"
        updated_at = "2024-03-15 12:00:00"
        entity = BaseEntity(id=id_, created_at=created_at, updated_at=updated_at)
        self.assertEqual(entity.id, str(id_))
        self.assertEqual(entity.created_at, created_at)
        self.assertEqual(entity.updated_at, updated_at)
