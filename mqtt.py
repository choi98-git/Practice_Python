import paho.mqtt.client as mqtt

def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("채팅 서버에 연결됨 ")
    client.subscribe("shingu/#")

def on_message(client, userdata, msg):
    print(msg.topic + ": " + msg.payload.decode("utf-8"))


client = mqtt.Client()

client.on_connect = on_connect
client.on_message = on_message

client.connect("mqtt.eclipseprojects.io", 1883, 60)

client.loop_start()

# 1.
while True:
    message = input(" : ")
    client.publish("shingu/2017132067", message, 1 , True)

client.loop_stop()
