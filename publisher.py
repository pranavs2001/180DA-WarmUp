import paho.mqtt.client as mqtt
import numpy as np

def on_connect(client, userdata, flags, rc):
    print("Connection resturned result: " + str(rc))

def on_disconnect(client, userdata, rc):
    if rc != 0:
        print("Unexpected disconnect")
    else:
        print("Expected disconnect")

def on_message(client, userdata, message):
    print("Received message: " + str(message.payload) + " on topic " + message.topic + " with QoS " + str(message.qos))

# 1. create a client instance. 
client = mqtt.Client()
# add additional client options (security, certifications, etc.)
# many default options should be good to start off.
# add callbacks to client. 
client.on_connect = on_connect
client.on_disconnect = on_disconnect
client.on_message = on_message

# 2. connect to a broker using one of the connect*() functions. 
client.connect_async("test.mosquitto.org")
# 3. call one of the loop*() functions to maintain network traffic flow with the broker. 
client.loop_start()
# 4. use subscribe() to subscribe to a topic and receive messages. 
# 5. use publish() to publish messages to the broker. 
# payload must be a string, bytearray, int, float or None.
for i in range(10):  
  client.publish("ece180d/test", float(np.random.random(1)), qos=1)

# 6. use disconnect() to disconnect from the broker. 
client.loop_stop()
client.disconnect()