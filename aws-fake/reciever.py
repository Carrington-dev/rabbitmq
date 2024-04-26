import pika
from time import sleep

def do_what_on_message(channel, method, properties, body):
    print(body)
    print('Message recieved')
    sleep(1)
    # method.

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
connection = pika.BlockingConnection(parameters=parameters)
channel = connection.channel()

channel.queue_declare(queue="letter")
channel.basic_qos(prefetch_count=1)

channel.basic_consume(queue="letter", auto_ack=True, on_message_callback=do_what_on_message)


print("Consuming")

channel.start_consuming()