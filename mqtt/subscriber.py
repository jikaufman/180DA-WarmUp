import paho.mqtt.client as mqtt

def on_connect(client, userdata, flags, rc):
    print("Connection returned result: " + str(rc))
    client.subscribe("wordoftheday", qos=1)

def on_disconnect(client, userdata, rc):
    print("Disconnected with result: " + str(rc))

def on_message(client, userdata, message):
    print("The word of the day is: " + str(message.payload)[2:-1] + "!")

if __name__ == "__main__":
    client = mqtt.Client()
    client.on_connect = on_connect
    client.on_disconnect = on_disconnect
    client.on_message = on_message

    client.connect_async("mqtt.eclipse.org")

    client.loop_start()

    while True:
        pass

    client.loop_stop()
    client.disconnect()
    
