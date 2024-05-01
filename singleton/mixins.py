import random
import time
import pika
import requests

class RabbitMQ:
    def __init__(self, username, password, host, port):
        self.credentials = pika.PlainCredentials(username=username, password=password)
        self.parameters = pika.ConnectionParameters(host=host, port=port, credentials=self.credentials)
        self.connection = pika.BlockingConnection(self.parameters)
        self.channel = self.connection.channel()
        self.queue_name = 'letterhead'
        self.declare_queue(self.queue_name)
    
    def declare_queue(self, queue):
        self.channel.queue_declare(queue=queue)
    
    def recieve_message(self, ):
        self.channel.basic_qos(prefetch_count=1)
        self.channel.basic_consume(queue=self.queue_name,  on_message_callback=self.do_what_on_message)
        print("Consuming")
        self.channel.start_consuming()

    def send_message(self, exchange,  routing_key, data):
        print(data)
        self.channel.basic_publish(exchange=exchange,  routing_key=routing_key, body= data)

    def do_what_on_message(self, channel, method, properties, body):
        t =  random.randint(1, 3)
        print(f"This will run for {t} seconds, recieved id { body }")
        time.sleep((t))
        response = requests.post(data=body)
        channel.basic_ack(delivery_tag=method.delivery_tag)

sender = RabbitMQ('guest', 'guest', 'localhost', 5672)
# sender.recieve_message()