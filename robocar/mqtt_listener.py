import time
import umqtt

import car_control

SERVER = '192.168.0.31'
PORT = 1883
CLIENT_ID = 'esp8266'
TOPIC = "car_controls"
CONTROLS = car_control.CarControl()


def car_control(topic, msg):
    print('Topic and message: %s, %s' % (topic, msg))
    msg_map = {b'left': CONTROLS.left,
               b'right': CONTROLS.right,
               b'backward': CONTROLS.backward,
               b'forward': CONTROLS.forward,
               b'stop': CONTROLS.stop}
    if msg in msg_map:
        print('Executing command: %s' % msg)
        msg_map[msg]()


def main(server=SERVER, port=PORT):
    client = umqtt.MQTTClient(CLIENT_ID, server=server, port=port)
    client.set_callback(car_control)
    print('Connecting...')
    client.connect()
    print('Connected')
    client.subscribe(TOPIC)
    while True:
        if True:
            client.wait_msg()
        else:
            client.check_msg()
            time.sleep(1)

    client.disconnect()


if __name__ == "__main__":
    main()
