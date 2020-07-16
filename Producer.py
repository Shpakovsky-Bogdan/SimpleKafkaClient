from kafka import KafkaProducer
import time

n = 1
producer = KafkaProducer(bootstrap_servers='localhost:9092')
while True:
    msgKey = "message "+time.time().__str__()
    msgValue = "Hello, World " + n.__str__() + "!" + time.strftime("%Y.%m.%d %H:%M:%S", time.localtime())
    print("Sending message " + n.__str__() + " to topic hello1")
    producer.send('hello1', key=msgKey.encode('utf-8'), value=msgValue.encode('utf-8'))
    time.sleep(5)
    n += 1

