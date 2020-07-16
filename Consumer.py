from kafka import KafkaConsumer
consumer = KafkaConsumer('hello1', bootstrap_servers=['localhost:9092'])
print("starting processing messages")
for message in consumer:
    print("topic=%s partition=%d offset=%d key=%s value=%s" % (message.topic, message.partition,
                                               message.offset, message.key, message.value))

