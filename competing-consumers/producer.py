import json
import random
import pika
import time

parameters = pika.ConnectionParameters("localhost")

connection = pika.BlockingConnection(parameters)

channel = connection.channel()

channel.queue_declare(queue="letterbox")


count = 1
while True:
    t =  random.randint(1, 10)
    do =  f"Sent a message to run for {t} seconds with id {count}"
    body =  { "message": do, "time_to": t}
    time.sleep(1)
    channel.basic_publish(exchange="",  routing_key='letterbox', body= str(count))
    print(f"{ do }")
    count += 1



channel.close()