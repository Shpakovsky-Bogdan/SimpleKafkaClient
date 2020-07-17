from kafka import KafkaConsumer
from kafka.errors import NoBrokersAvailable
import time


def connect():
    attempts = 0
    while attempts < 3:
        try:
            print("Connecting to kafka, attempt %d" % attempts)
            cs = KafkaConsumer('hello1', bootstrap_servers=['kafka-server:9092'])
            return cs
        except NoBrokersAvailable:
            attempts += 1
            print("No brokers available")
            time.sleep(10)
    exit(2)


print("Consumer start")
consumer = connect()
# logFile = open("Log.txt", 'w')
try:
    print("starting processing messages")
    # logFile.write("starting processing messages")
    for message in consumer:
        print("topic=%s partition=%d offset=%d key=%s value=%s"
              % (message.topic, message.partition, message.offset, message.key, message.value))
        # logFile.write("topic=%s partition=%d offset=%d key=%s value=%s\n"
        #             % (message.topic, message.partition, message.offset, message.key, message.value))
finally:
    # logFile.close()
    consumer.close()