from src.application.services import SaveBalancesServiceObserver
from src.adapters.database.repository import BalancesRepository
from src.adapters.database import DatabaseManager
from src.pkg.kafka import KafkaConsumer


class StartupComposer:
    @staticmethod
    async def compose():
        database_manager = DatabaseManager()
        consumer = KafkaConsumer("balances")
        await consumer.start()

        repository = BalancesRepository(database_manager)
        SaveBalancesServiceObserver(consumer, repository)


class BalancesRepositoryComposer:
    @staticmethod
    def compose():
        database_manager = DatabaseManager()
        return BalancesRepository(database_manager)