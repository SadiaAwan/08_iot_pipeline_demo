import time
from wifi import connect_wifi
from machine import Pin
from dht import DHT11
from umqtt.simple import MQTTClient
import json

time.sleep(.1)

# byte representation -> MSQUITTO NEEDS THIS 
TOPIC = b"home/pico/dht11"
MQTT_BROKER = "172.20.10.3"

led = Pin(15,1)
dht_sensor = DHT11(Pin(16))

if connect_wifi():
    led.value(1)

def connect_mqtt():
    client = MQTTClient(client_id="pico", server= MQTT_BROKER, port=1883)
    client.connect()
    print("Connected to MQTT")
    return client

client = connect_mqtt()

while True:
    dht_sensor.measure()
    temp = dht_sensor.temperature()
    humidity = dht_sensor.humidity()

   
    data = {"temperature": temp, "humidity": humidity}
    print(data)

    payload = json.dumps(data)    
    client.publish(TOPIC, payload)
    time.sleep(3)

    
   
   
