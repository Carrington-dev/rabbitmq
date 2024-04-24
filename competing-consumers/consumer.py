import random
import time
import pika

def do_what_on_message(ch, method, properties, body):
    t =  random.randint(1, 10)
    print(f"This will run for {t} seconds, recieved id { body }")
    time.sleep((t))
    ch.basic_ack(delivery_tag=method.delivery_tag)


parameters = pika.ConnectionParameters("localhost")

connection = pika.BlockingConnection(parameters)

channel = connection.channel()


channel.queue_declare(queue="letterbox")

channel.basic_qos(prefetch_count=1)

channel.basic_consume(queue="letterbox",  on_message_callback=do_what_on_message)


print("Consuming")

channel.start_consuming()