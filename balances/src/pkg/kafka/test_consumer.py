import asyncio
import json
import pytest

from aiokafka import AIOKafkaConsumer


# KAFKA_INSTANCE = "kafka:29092"


# @pytest.mark.asyncio
# async def test_kafka_consumer():
#     consumer = AIOKafkaConsumer(
#                         "balances", 
#                         bootstrap_servers=KAFKA_INSTANCE, 
#                         enable_auto_commit=True,       # Is True by default anyway
#                         auto_commit_interval_ms=1000,  # Autocommit every second
#                         auto_offset_reset="earliest",
#                     )
#     await consumer.start()
#     try:
#         async for msg in consumer:
#             assert isinstance(msg.value, bytes)
#             data = json.loads(msg.value.decode())
    
#             print("Received message:", data)
#             assert "campo_esperado" in data
#     finally:
#         await consumer.stop()






import json
import unittest

from aiokafka import AIOKafkaConsumer, AIOKafkaProducer

from src.config.settings import settings


KAFKA_INSTANCE = settings.KAFKA_INSTANCE


class TestKafkaConsumer(unittest.TestCase):
    async def consume_messages(self):
        consumer = AIOKafkaConsumer(
                        "balances", 
                        bootstrap_servers=KAFKA_INSTANCE, 
                        enable_auto_commit=True,       
                        auto_commit_interval_ms=1000,
                        auto_offset_reset="earliest",
                    )
        
        await consumer.start()

        try:
            async for msg in consumer:
                assert isinstance(msg.value, bytes)
                data = json.loads(msg.value.decode())
                print("Received message ========:", data)
                return data
        
        finally:
            await consumer.stop()


    async def produce_messages(self):
        producer =  AIOKafkaProducer(bootstrap_servers=KAFKA_INSTANCE)

        await producer.start()

        try:
            
            messages = [
                {
                    "Name": "BalanceUpdated", 
                    "Payload": {
                        "account_id_from": "9a9d550f-c475-4bad-a034-cfd3dbdb6813",
                        "account_id_to": "092ce768-68e5-448f-8747-b0b149b01131",
                        "balance_account_id_from": 24950,
                        "balance_account_id_to": 550
                        }
                },
                {
                    "Name": "BalanceUpdated", 
                    "Payload": {
                        "account_id_from": "9a9d550f-c475-4bad-a034-cfd3dbdb6813",
                        "account_id_to": "092ce768-68e5-448f-8747-b0b149b01131",
                        "balance_account_id_from": 24900,
                        "balance_account_id_to": 600
                    }
                }
            ]

            for message in messages:
                await producer.send_and_wait("balances", json.dumps(message).encode())
                return message
            
            
        finally:
            await producer.stop()

    
    def test_consumer(self):
        loop = asyncio.get_event_loop()
        message = loop.run_until_complete(self.consume_messages())
        self.assertIsNotNone(message)

    def test_producer(self):
        self.assertIsNotNone(self.produce_messages())
