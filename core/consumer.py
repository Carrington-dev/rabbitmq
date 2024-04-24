import time
import pika

def do_what_on_message(ac, method, properties, body):
    print(body)
    time.sleep(int(body))

parameters = pika.ConnectionParameters("localhost")

connection = pika.BlockingConnection(parameters)

channel = connection.channel()


channel.queue_declare(queue="letter")
channel.basic_qos(prefetch_count=1)

channel.basic_consume(queue="letter", auto_ack=True, on_message_callback=do_what_on_message)


print("Consuming")

channel.start_consuming()