import paho.mqtt.publish as publish
import time, random, json

BROKER = "localhost"
TOPIC = "home/gas"

while True:
    value = round(random.uniform(0, 200), 2)
    payload = json.dumps({"value": value})
    publish.single(TOPIC, payload, hostname=BROKER)
    print(f" Gas level sent: {value}")
    time.sleep(5)
