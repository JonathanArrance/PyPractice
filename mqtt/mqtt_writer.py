import paho.mqtt.client as mqtt

def on_publish(client, userdata, result):
    print("Message published successfully!")

def publish_message(broker_address, topic, message):
    client = mqtt.Client()
    client.on_publish = on_publish

    # Connect to the broker
    client.connect(broker_address, 1883, 60)

    # Publish the message to the specified topic
    result = client.publish(topic, message)

    # Wait for the message to be published (optional)
    result.wait_for_publish()

    # Disconnect from the broker
    client.disconnect()

if __name__ == "__main__":
    # Replace these with your MQTT broker address, topic, and message
    broker_address = "192.168.1.66"
    topic = "example_topic"
    message = "Hello, MQTT!"

    publish_message(broker_address, topic, message)
