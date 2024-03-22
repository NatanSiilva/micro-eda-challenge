import asyncio
import json
import threading
import time

from aiokafka import AIOKafkaConsumer

from src.pkg.kafka.kafka_event import Event
from src.config.settings import settings


class KafkaConsumerService:
    def __init__(self):
        self.kafka_instance = settings.KAFKA_INSTANCE
        self.kafka_topic_name = settings.KAFKA_TOPIC_NAME

        self.consumer = AIOKafkaConsumer(
            self.kafka_topic_name, 
            bootstrap_servers=self.kafka_topic_name,
            auto_offset_reset="earliest"
        )

        self.on_message_received = Event()


    async def start(self):
        await self.consumer.start()


    async def stop(self):
        await self.consumer.stop()


    async def consume_messages(self):
        async for msg in self.consumer:
            value = json.loads(msg.value.decode())
            self.on_message_received.fire(value)




async def save_to_database(message):
    # Implemente a lógica para salvar a mensagem no banco de dados aqui
    print("Saving to database:", message)

async def consume_and_save_messages(consumer_service: KafkaConsumerService):
    await consumer_service.start()
    consumer_service.on_message_received.subscribe(save_to_database)
    try:
        while True:
            await asyncio.sleep(1)
    finally:
        await consumer_service.stop()

# Exemplo de uso:
async def main():
    consumer_service = KafkaConsumerService()
    await consume_and_save_messages(consumer_service)

if __name__ == "__main__":
    asyncio.run(main())
