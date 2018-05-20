import paho.mqtt.publish as publish

# FIXME move to config
SERVER = '192.168.0.31'
PORT = 1883
TOPIC = "car_controls"


def publish_msg(msg, topic=TOPIC, hostname=SERVER, port=PORT):
    publish.single(topic, payload=msg, hostname=hostname, port=port)
