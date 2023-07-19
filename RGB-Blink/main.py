# main.py -- put your code here!

import pycom
import time

pycom.heartbeat(False)

while True:
    #colors in hexadecimal (0xRRGGBB)
    # pycom.rgbled(0xFF0000)  # Red
    pycom.rgbled(0x00FF00)  # Green
    time.sleep(1)
    # pycom.rgbled(0x0000FF)  # Blue
    pycom.rgbled(0xFFFF00)  # Yellow
    time.sleep(1)
    # pycom.rgbled(0x0000FF)  # Blue
    # pycom.rgbled(0xFF0000)  # Red
    pycom.rgbled(0xFFA500)  # Orange
    time.sleep(1)
    