# import os
from decouple import config

import pika
class Consumer:
    def __init__(self, host, port, username, password):
        self.host = host
        self.port = port
        self.username = username
        self.password = password

    def _init_channel(self):
        # connection = pika.BlockingConnection(
        # pika.URLParameters(f'amqps://b-293e9d26-e935-4fd4-89ac-4fbcc36767de.mq.af-south-1.amazonaws.com:5671'))
        # pika.URLParameters(f'amqp://guest:guest@rabbitmq:5672/vhost'))
        # pika.URLParameters(f'amqp://{self.username}:{ self.password}@{self.host}:5672'))
        self.credentials = pika.PlainCredentials(username=self.username, password=self.password)
        self.parameters = pika.ConnectionParameters(host=self.host, port=self.port, credentials=self.credentials)
        self.connection = pika.BlockingConnection(self.parameters)
        self.channel = self.connection.channel()
        return self.connection.channel()
    
    def _init_queue(self, channel, exchange, queue_name, routing_key):
        queue = channel.queue_declare(queue=queue_name)
        channel.queue_bind(
            exchange=exchange,
            queue=queue_name, 
            routing_key=routing_key
        )
        return queue
    
    def consume(self, exchange, queue_name, routing_key, callback):
        channel = self._init_channel()
        queue_name = self._init_queue(channel, exchange, queue_name, routing_key)
        channel.basic_consume( 
            queue=queue_name, 
            on_message_callback=callback, 
        )

        print("Started consuming")

        channel.start_consuming()

consumer = Consumer(
    host=config('RABBITMQ_HOST'),
    port=config('RABBITMQ_PORT'),
    username=config('RABBITMQ_USERNAME'),
    password=config('RABBITMQ_PASSWORD'),
)
def on_call_back(channel, method, x, body):
    print(body)

consumer.consume(
    queue_name="letterbox", 
    exchange='direct',  
    routing_key="home.cureate_view:0.0.1", 
    callback=on_call_back
    )