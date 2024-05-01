import json
import random
import pika
import time
from variables import my_queue


parameters = pika.ConnectionParameters("localhost")
connection = pika.BlockingConnection(parameters)
channel = connection.channel()
channel.queue_declare(queue=my_queue)

# while (do := input("Message: ").strip()) != 'q':
#     time.sleep(random.randint(1, 10))
#     channel.basic_publish(exchange="",  routing_key='letter', body= (do if do else "This is my message body"))
#     print("Sent a message")

count = 1
while True:
    do =  "Message"
    t =  random.randint(1, 3)
    body =  { "message": do, "time_to": t}
    time.sleep(t)
    channel.basic_publish(exchange="",  routing_key='letter', body= f"count: {count},  time: {t} seconds")
    print("Sent a message ", t)
    count += 1



channel.close()