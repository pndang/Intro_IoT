from network import Bluetooth
from machine import Timer
import time

SERVICE_UUID = 0xec00
DATA_CHARACTERISTIC_UUID = 0xec0e

def char_notify_callback(char, arg):
    char_value = (char.value())
    print("New value: {}".format(char_value))

# def send_acknowledgment():
#     global chr1
#     ack_msg = "ACK: Received 90!"
#     chr1.write(ack_msg)
#     print('ACK sent')

bt = Bluetooth()
print('Start scanning for BLE services')
bt.start_scan(-1)
adv = None
conn = None
while(True):
    adv = bt.get_adv()
    if adv:
        try:
            if bt.resolve_adv_data(adv.data, Bluetooth.ADV_NAME_CMPL)=="Grp3":
                conn = bt.connect(adv.mac)
                print("Connected to Grp3")
                try:
                    services = conn.services()
                    for service in services:
                        chars = service.characteristics()
                        for char in chars:
                            if char.uuid() == DATA_CHARACTERISTIC_UUID:
                                if (char.properties() & Bluetooth.PROP_NOTIFY):
                                    char.callback(trigger=Bluetooth.CHAR_NOTIFY_EVENT, handler=char_notify_callback)      
                
                except:                 
                    continue
        except:
            continue
    
    if conn and conn.isconnected():
        try:
            chr1 = conn.characteristic(DATA_CHARACTERISTIC_UUID)
            data = chr1.read()
            print('read: ', chr1.read())
            print('value: ', chr1.value())
            if data == b'90':
                chr1.write('ACK: Received 90!')
                print('sent ACK')
        except:
            print('error')
    
    time.sleep(2)

bt.stop_scan()
bt.disconnect_client() 