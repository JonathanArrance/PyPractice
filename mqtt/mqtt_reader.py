import paho.mqtt.client as mqtt

def on_connect(client, userdata, flags, rc):
    print(f"Connected with result code {rc}")
    # Subscribe to the desired topic on connection
    client.subscribe("example_topic")

def on_message(client, userdata, msg):
    print(f"Received message on topic {msg.topic}: {msg.payload.decode()}")

if __name__ == "__main__":
    # Replace this with your MQTT broker address
    broker_address = "192.168.1.66"

    client = mqtt.Client()
    client.on_connect = on_connect
    client.on_message = on_message

    # Connect to the broker
    client.connect(broker_address, 1883, 60)

    # Continue the network loop to receive messages
    client.loop_forever()
