from kafka import KafkaConsumer
import json
import time
import os

BOOTSTRAP_SERVER = os.environ['BOOTSTRAP_SERVER']
CONSUMER_GROUP_ID = os.environ['CONSUMER_GROUP_ID']
TOPIC_NAME = os.environ['TOPIC_NAME']
SLEEP_TIME = int(os.environ['WAIT_TIME'])

if __name__ == "__main__":
    consumer = KafkaConsumer(
        TOPIC_NAME,
        bootstrap_servers=BOOTSTRAP_SERVER,
        auto_offset_reset='earliest',
        group_id=CONSUMER_GROUP_ID)
    
    print("starting the consumer")
    
    for msg in consumer:
        print("Processing msg from partition {} = {}".format(msg.partition, json.loads(msg.value)))
        time.sleep(SLEEP_TIME)