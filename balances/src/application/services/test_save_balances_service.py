
from src.pkg.kafka.kafka_consumer import KafkaConsumer
from src.application.services import SaveBalancesServiceObserver

import asyncio
import json
import pytest


@pytest.mark.asyncio
async def test_save_balances_service_observer():
    consumer = KafkaConsumer("balances")
    SaveBalancesServiceObserver(consumer)
    await consumer.start()
    