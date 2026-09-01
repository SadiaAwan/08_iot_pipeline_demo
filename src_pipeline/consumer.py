import paho.mqtt.client as mqtt
import json

def on_message(client, userdata, message):
    #needs to decode because origional msg is encoded after publishing
    payload = message.payload.decode()

    print(payload)
    


if __name__ == "__main__":
    client = mqtt.Client()
    client.connect("mosquitto", 1883)
    client.subscribe("home/pico/dht11")
    client.on_message = on_message
    client.loop_forever()











from utils.connect_postgres import query_db




    temperature = float(data["temperature"])
    humidity = float(data["humidity"])

    query_db(
        """
        INSERT INTO sensor_readings 
            (time, temperature, humidity) 
        VALUES (NOW(), %s, %s)
""",
        (temperature, humidity),
    )

    print(temperature, humidity)


if __name__ == "__main__":
    query_db("""
        CREATE TABLE IF NOT EXISTS sensor_readings (
            time TIMESTAMPTZ NOT NULL,
            temperature DOUBLE PRECISION,
            humidity DOUBLE PRECISION
        )
    """)

    