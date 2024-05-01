import json
from mixins import sender


while len(message := input().strip()) >= 1:
    sender.send_message(
        exchange = "",  
        # routing_key = 'user.deleted.1.2.3',
        routing_key = 'letterhead',
        data = json.dumps({
            "message": message
        })
    )