import unittest
import asyncio
from src.pkg.kafka.kafka_consumer import KafkaConsumer


class TestKafkaConsumer(unittest.TestCase):
    async def test_kafka_consumer_register(self):
        async with KafkaConsumer("balances") as consumer:
            consumer.register("observer")
            self.assertEqual(consumer.get_observers(), ["observer"])

    async def test_kafka_consumer_unregister(self):
        async with KafkaConsumer("balances") as consumer:
            consumer.register("observer")
            consumer.unregister("observer")
            self.assertEqual(consumer.get_observers(), [])

    async def test_kafka_consumer_notify_observers(self):
        async with KafkaConsumer("balances") as consumer:
            consumer.register("observer")
            self.assertEqual(consumer.notifyObservers(), None)

    async def test_kafka_consumer_start(self):
        async with KafkaConsumer("balances") as consumer:
            await consumer.start()
            self.assertTrue(consumer.consumer.is_active)

    async def test_kafka_consumer_stop(self):
        async with KafkaConsumer("balances") as consumer:
            await consumer.start()
            await consumer.stop()
            self.assertFalse(consumer.consumer.is_active)

if __name__ == "__main__":
    unittest.main()
