import json
import random
import pika
import time

# parameters = pika.ConnectionParameters("localhost")

host = 'localhost'
# host = 'amqps://b-293e9d26-e935-4fd4-89ac-4fbcc36767de.mq.af-south-1.amazonaws.com'
port = 5672
credentials = pika.PlainCredentials('guest', 'guest')
# credentials = pika.PlainCredentials('carrington96', '#Mulalo960809')
# {
#     'username': 'carrington96',
#     'password': '#Mulalo960809'
# }


parameters = pika.ConnectionParameters(host=host, port=port, credentials=credentials)

connection = pika.BlockingConnection(parameters)

channel = connection.channel()

channel.queue_declare(queue="on_house")


count = 1
while True:
    t =  random.randint(1, 10)
    do =  f"Sent a message to run for {t} seconds with id {count}"
    body =  { "message": do, "time_to": t}
    time.sleep(1)
    channel.basic_publish(exchange="",  routing_key='letter', body= str(count))
    print(f"{ do }")
    count += 1



channel.close()