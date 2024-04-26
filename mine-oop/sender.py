import json
from initial import producer

while len(message := input().strip()) >= 1:
    producer.send_message(
        exchange = "",  
        routing_key = 'user.deleted.1.2.3',
        data = json.dumps({
            "message": message
        })
    )