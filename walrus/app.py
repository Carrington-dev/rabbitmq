while (do := input("Message: ").strip()) != 'q':
    # time.sleep(random.randint(1, 10))
    # channel.basic_publish(exchange="",  routing_key='letter', body= (do if do else "This is my message body"))
    print("Sent a message")