import unittest
from unittest.mock import MagicMock, patch

from sqlalchemy.engine.base import Engine
from sqlmodel import Session

from src.config.settings import Settings
from src.adapters.database import DatabaseManager



class TestDatabaseManager(unittest.TestCase):

    def test_get_session(self):
        with patch.object(DatabaseManager, "connect") as mock_connect:
            mock_engine = MagicMock(Engine)
            mock_connect.return_value = mock_engine
            db_manager = DatabaseManager()
            session = db_manager.get_session()
            self.assertIsInstance(session, Session)

