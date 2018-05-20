import network
import time

SSID = "SSID"
PASSWORD = "PASSWORD"


def do_connect():
    sta_if = network.WLAN(network.STA_IF)
    if not sta_if.isconnected():
        print('Connecting...')
        sta_if.active(True)
        sta_if.connect(SSID, PASSWORD)
    while not sta_if.isconnected():
        time.sleep(1)
    print('network_config:', sta_if.ifconfig())
    # now turn off access point mode
    ap_if = network.WLAN(network.AP_IF)
    if ap_if.active():
        ap_if.active(False)


def main():
    do_connect()

if __name__ == "__main__":
    main()
