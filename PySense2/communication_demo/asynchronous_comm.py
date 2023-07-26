
# Code for simple advertisement searching
  
        # from network import Bluetooth
        # import ubinascii
        # import time

        # bluetooth = Bluetooth()
        # bluetooth.start_scan(-1)    # start scanning with no timeout

        # while True:
        #     adv = bluetooth.get_adv()

        #     if adv:
        #         # try to get the complete name
        #         print(bluetooth.resolve_adv_data(adv.data, Bluetooth.ADV_NAME_CMPL))

        #         mfg_data = bluetooth.resolve_adv_data(adv.data, Bluetooth.ADV_MANUFACTURER_DATA)

        #         if mfg_data:
        #             # try to get the manufacturer data (Apple's iBeacon data is sent here)
        #             print(ubinascii.hexlify(mfg_data))

        #     time.sleep(2)

from network import Bluetooth
from machine import Timer
import time

def char_notify_callback(char, arg):
    char_value = (char.value())
    print("New value: {}".format(char_value))

bt = Bluetooth()
print('Start scanning for BLE services')
bt.start_scan(-1)
adv = None
while(True):
    adv = bt.get_adv()
    if adv:
        try:
            if bt.resolve_adv_data(adv.data, Bluetooth.ADV_NAME_CMPL)=="Team 3: Aidan & Phu":
                conn = bt.connect(adv.mac)
                print("Connected to Team 3: Aidan & Phu")
                try:
                    services = conn.services()
                    for service in services:
                        chars = service.characteristics()
                        for char in chars:
                            c_uuid = char.uuid()
                            if char.uuid() == 0xec0e:
                                if (char.properties() & Bluetooth.PROP_NOTIFY):
                                    char.callback(trigger=Bluetooth.CHAR_NOTIFY_EVENT, handler=char_notify_callback)
                                    time.sleep(3)  # check for asynchronous communication
                                    break
                except:                 
                    continue
        except:
            continue

bt.stop_scan()
bt.disconnect_client() 