import json
import random
import pika
import time

parameters = pika.ConnectionParameters("localhost")

connection = pika.BlockingConnection(parameters)

channel = connection.channel()

channel.queue_declare(queue="letter")

# while (do := input("Message: ").strip()) != 'q':
#     time.sleep(random.randint(1, 10))
#     channel.basic_publish(exchange="",  routing_key='letter', body= (do if do else "This is my message body"))
#     print("Sent a message")
count = 1
while True:
    do =  "Message"
    t =  random.randint(1, 10)
    body =  { "message": do, "time_to": t}
    time.sleep(t)
    channel.basic_publish(exchange="",  routing_key='letter', body= str(count))
    print("Sent a message ", t)
    count += 1



channel.close()