import time
import pika
from variables import my_queue

def do_what_on_message(ac, method, properties, body):
    print(body)
    time.sleep(3)


# parameters = pika.ConnectionParameters("localhost")
credentials = pika.PlainCredentials(username='guest', password='guest')
parameters = pika.ConnectionParameters(host='localhost', port=5672, credentials=credentials)
# connection = pika.BlockingConnection(parameters)

connection = pika.BlockingConnection(parameters)

channel = connection.channel()


channel.queue_declare(queue=my_queue)
channel.basic_qos(prefetch_count=1)

channel.basic_consume(queue=my_queue, auto_ack=True, on_message_callback=do_what_on_message)


print("Consuming")

channel.start_consuming()