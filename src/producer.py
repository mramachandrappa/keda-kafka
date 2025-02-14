from kafka import KafkaProducer
import json
from faker_data import generate_user_data
import time
import os

BOOTSTRAP_SERVER = "192.168.31.125:9092" #os.environ['BOOTSTRAP_SERVER']
TOPIC_NAME = "keda-test" #os.environ['TOPIC_NAME']
SLEEP_TIME = 1 #int(os.environ['WAIT_TIME'])

def json_serializer(data):
    return json.dumps(data).encode("utf-8")


producer = KafkaProducer(bootstrap_servers=[BOOTSTRAP_SERVER],
                         value_serializer=json_serializer)

if __name__ == "__main__":
    while True:
        user_event = generate_user_data()
        print(user_event)
        producer.send(TOPIC_NAME, user_event)
        time.sleep(SLEEP_TIME)