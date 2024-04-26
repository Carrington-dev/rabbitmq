# pizza/utils/producer.py
import json
from decouple import config
import pika
import sys
from django.conf import settings


class Producer:
    def __init__(self, host, port, username, password):
        # self.connection = pika.BlockingConnection(
            # pika.ConnectionParameters(host=f"amqps://b-293e9d26-e935-4fd4-89ac-4fbcc36767de.mq.af-south-1.amazonaws.com:5671")
            # pika.URLParameters(f'amqps://b-293e9d26-e935-4fd4-89ac-4fbcc36767de.mq.af-south-1.amazonaws.com:5671')
            # pika.URLParameters(f'amqp://{username}:{password}@{host}:5672')
            # )
        self.credentials = pika.PlainCredentials(username=username, password=password)
        self.parameters = pika.ConnectionParameters(host=host, port=port, credentials=self.credentials)
        self.connection = pika.BlockingConnection(self.parameters)
        self.channel = self.connection.channel()
        self.exchanges = []

    def produce(self, exchange, body, routing_key, queue):
        if exchange not in self.exchanges:
            # self.channel.declare_exchange(exchange=exchange)
            self.exchanges.append(exchange)
            self.channel.queue_declare(queue=queue)
            self.channel.basic_publish(
                exchange=exchange,
                routing_key=routing_key,
                body=json.dumps(body)
                )
        print('sent a message: ', body)
            
producer = Producer(
    host=config('RABBITMQ_HOST'),
    port=config('RABBITMQ_PORT'),
    username=config('RABBITMQ_USERNAME'),
    password=config('RABBITMQ_PASSWORD'),
)