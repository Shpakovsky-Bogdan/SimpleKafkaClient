from kafka import KafkaProducer
from kafka.errors import NoBrokersAvailable
import time


def connect():
    attempts = 0
    while attempts < 3:
        try:
            print("Connecting to kafka, attempt %d" % attempts)
            pr = KafkaProducer(bootstrap_servers='kafka-server:9092')
            return pr
        except NoBrokersAvailable:
            attempts += 1
            print("No brokers available")
            time.sleep(10)
    exit(2)


print("Producer start")
producer = connect()
# logFile = open("Log.txt", 'w')
n = 1
try:
    while True:
        msgKey = "message %f" % time.time()
        msgValue = "Hello, World %d! time: %s" % (n, time.strftime("%Y.%m.%d %H:%M:%S", time.localtime()))
        print("Sending message %d to topic hello1" % n)
        # logFile.write("Sending message %d to topic hello1\n" % n)
        producer.send('hello1', key=msgKey.encode('utf-8'), value=msgValue.encode('utf-8'))
        time.sleep(5)
        n += 1
finally:
    # logFile.close()
    producer.close()