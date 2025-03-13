import paho.mqtt.client as mqtt

# Callback when a message is received
def on_message(client, userdata, message):
    msg = message.payload.decode("utf-8")
    if msg == "ON":
        print("status: bulb is TURNED ON")
    elif msg == "OFF":
        print("status: bulb is TURNED OFF")

# Setup MQTT client
broker = "broker.hivemq.com"  
port = 1883  
topic = "/student_group/light_control"

# Create an MQTT client instance
client = mqtt.Client()

# Assign the callback for receiving messages
client.on_message = on_message

# Connect to the broker and subscribe to the topic
client.connect(broker, port, 60)
client.subscribe(topic)

# Loop forever to keep the script running and listening for messages
print("Waiting for messages...")
client.loop_forever()
