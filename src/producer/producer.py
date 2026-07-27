import json
import time

from kafka import KafkaProducer

from src.services.retail_order_generator import RetailOrderGenerator
from src.config.settings import KAFKA_BOOTSTRAP_SERVERS
from src.config.settings import KAFKA_TOPIC


producer = KafkaProducer(
    bootstrap_servers=KAFKA_BOOTSTRAP_SERVERS,
    value_serializer=lambda value: json.dumps(value).encode("utf-8")
)

generator = RetailOrderGenerator()

print("Kafka Producer Started...")

while True:

    order = generator.generate_order()

    producer.send(KAFKA_TOPIC, order)

    print(order)

    time.sleep(2)