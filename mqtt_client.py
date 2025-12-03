import paho.mqtt.client as mqtt
import json 
from database import save_sensor_data
broker = "localhost"
port = 1883
topic = ["home/temperature", "home/gaz"]
def on_connect(client, userdata, flags, rc):
    print("connecte to MQTT BROKER")
    for t in topic:
        client.subscribe(t)
        print(f"subscribed to topic: {t}")
def on_message(client, userdata, msg):
  payload = json.loads(msg.payload.decode())
  print(f"message received from topic {msg.topic}: {payload}")
  save_sensor_data(msg.topic, payload["value"])

def start_mqtt():
    client = mqtt.Client()
    client.on_connect = on_connect
    client.on_message = on_message
    client.connect(broker, port)
    client.loop_forever()

if __name__ == "__main__":
    start_mqtt() 
