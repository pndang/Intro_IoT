from network import Bluetooth
import ubinascii
import time

bluetooth = Bluetooth()
bluetooth.start_scan(-1)    # start scanning with no timeout

while True:
    adv = bluetooth.get_adv()

    if adv:
        # try to get the complete name
        print(bluetooth.resolve_adv_data(adv.data, Bluetooth.ADV_NAME_CMPL))

        mfg_data = bluetooth.resolve_adv_data(adv.data, Bluetooth.ADV_MANUFACTURER_DATA)

        if mfg_data:
            # try to get the manufacturer data (Apple's iBeacon data is sent here)
            print(ubinascii.hexlify(mfg_data))

    time.sleep(2)