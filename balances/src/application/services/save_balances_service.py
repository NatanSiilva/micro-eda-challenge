from src.application.shared.observer import Observer
from src.pkg.kafka.kafka_consumer import KafkaConsumer
from src.adapters.database.repository import BalancesRepository
import json

from src.application.entities import BalancesEntity


class SaveBalancesServiceObserver(Observer):
    def __init__(self, kafka_consumer: KafkaConsumer, repository: BalancesRepository):
        self._kafka_consumer = kafka_consumer
        self._kafka_consumer.register(self)
        self._repository = repository

    def update(self, *args, **kwargs):
        message = args[0]

        entity = BalancesEntity(
            account_id=message["Payload"]["account_id_from"],
            balance=message["Payload"]["balance_account_id_from"],
        )

        exist_balance = self._repository.get_by_account_id(entity.get_account_id)

        if exist_balance:
            self._repository.update(entity)
        else:
            self._repository.create(entity)
        

        entity = BalancesEntity(
            account_id=message["Payload"]["account_id_to"],
            balance=message["Payload"]["balance_account_id_to"],
        )

        exist_balance = self._repository.get_by_account_id(entity.get_account_id)

        if exist_balance:
            self._repository.update(entity)
        else:
            self._repository.create(entity)



