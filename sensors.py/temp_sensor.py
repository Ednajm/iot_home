import paho.mqtt.publish as publish
import time, random, json

BROKER = "localhost"
TOPIC = "home/temperature"

while True:
    value = round(random.uniform(18.0, 30.0), 2)
    payload = json.dumps({"value": value})
    publish.single(TOPIC, payload, hostname=BROKER)
    print(f" Temp sent: {value}")
    time.sleep(5)
