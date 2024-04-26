import pika

class RabbitMQ:
    def __init__(self, username, password, host, port):
        self.credentials = pika.PlainCredentials(username=username, password=password)
        self.parameters = pika.ConnectionParameters(host=host, port=port, credentials=self.credentials)
        self.connection = pika.BlockingConnection(self.parameters)
        self.channel = self.connection.channel()
    
    def declare_queue(self, queue):
        self.channel.queue_declare(queue=queue)
    
    def send_message(self, exchange,  routing_key, data):
        self.declare_queue('on_house')
        print(data)
        self.channel.basic_publish(exchange=exchange,  routing_key=routing_key, body= data)



producer = RabbitMQ('guest', 'guest', 'localhost', 5672)
# url = f"amqps://b-293e9d26-e935-4fd4-89ac-4fbcc36767de.mq.af-south-1.amazonaws.com"
# url = f"amqps://{rabbitmq_user}:{rabbitmq_password}@{rabbitmq_broker_id}.mq.{region}.amazonaws.com:5671"
# producer = RabbitMQ('guest', 'guest', 'localhost', 5672)
# producer = RabbitMQ('carrington96', '#Mulalo960809', url, 5671)
