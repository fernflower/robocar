# This file is executed on every boot (including wake-boot from deepsleep)
import gc
import webrepl

import mqtt_listener
import wlan_connect

webrepl.start()
gc.collect()
wlan_connect.do_connect()

# start listener
mqtt_listener.main()
