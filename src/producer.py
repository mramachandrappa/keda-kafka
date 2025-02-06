from kafka import KafkaProducer
import json
from data import get_registered_user
import time
import os

def json_serializer(data):
    return json.dumps(data).encode("utf-8")


producer = KafkaProducer(bootstrap_servers=[os.environ['BOOTSTRAP_SERVER']],
                         value_serializer=json_serializer)

if __name__ == "__main__":
    while 1 == 1:
        user_event = get_registered_user()
        print(user_event)
        producer.send(os.environ['TOPIC_NAME'], user_event)
        time.sleep(int(os.environ['WAIT_TIME']))