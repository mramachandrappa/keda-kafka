from kafka import KafkaConsumer
import json
import time
import os


if __name__ == "__main__":
    consumer = KafkaConsumer(
        os.environ['TOPIC_NAME'],
        bootstrap_servers=os.environ['BOOTSTRAP_SERVER'],
        auto_offset_reset='earliest',
        group_id="consumer-group-a")
    
    print("starting the consumer")
    
    for msg in consumer:
        print("Processing msg from partition {} = {}".format(msg.partition, json.loads(msg.value)))
        time.sleep(int(os.environ['WAIT_TIME']))