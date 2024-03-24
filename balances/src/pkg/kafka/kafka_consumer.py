import asyncio
import json

from aiokafka import AIOKafkaConsumer

from src.config.settings import settings
from src.application.shared.observer import Subject


class KafkaConsumer(Subject):
    def __init__(self, topic: str):
        self._topic = topic
        self.consumer = AIOKafkaConsumer(
            self._topic,
            bootstrap_servers=settings.KAFKA_BOOTSTRAP_SERVERS,
            auto_offset_reset="earliest",
        )
        self._observers = []

    async def start(self):
        await self.consumer.start()
        asyncio.create_task(self._consume())

    async def stop(self):
        await self.consumer.stop()

    async def _consume(self):
        try:
            async for msg in self.consumer:
                data = json.loads(msg.value.decode("utf-8"))
                self.notifyObservers(data)
        finally:
            await self.stop()

    def register(self, observer):
        self._observers.append(observer)

    def unregister(self, observer):
        self._observers.remove(observer)

    def get_observers(self):
        return self._observers

    def notifyObservers(self, *args, **kwargs):
        for  observer in self._observers:
            observer.update(*args, **kwargs)

