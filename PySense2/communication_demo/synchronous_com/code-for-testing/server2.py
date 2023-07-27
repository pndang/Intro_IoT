from network import Bluetooth
from machine import Timer
import time

SERVICE_UUID = 0xec00
DATA_CHARACTERISTIC_UUID = 0xec0e

battery = 100
update = False

def conn_cb(chr):
    events = chr.events()
    if events & Bluetooth.CLIENT_CONNECTED:
        print('client connected')
    elif events & Bluetooth.CLIENT_DISCONNECTED:
        print('client disconnected')
        update = False

def chr1_handler(chr, data):
    global battery
    global update
    events = chr.events()
    print("events: ",events)
    if events & (Bluetooth.CHAR_READ_EVENT | Bluetooth.CHAR_SUBSCRIBE_EVENT):
        chr.value(battery)
        print("transmitted :", battery)
        if (events & Bluetooth.CHAR_SUBSCRIBE_EVENT):
            update = True
    elif events & Bluetooth.CHAR_WRITE_EVENT:
        ack_msg = data.decode()
        if ack_msg.startswith('ACK:'):
            print('ACK Received:', ack_msg[4:])

bluetooth = Bluetooth()
bluetooth.set_advertisement(name='Grp3', manufacturer_data="Pycom", service_uuid=SERVICE_UUID)

bluetooth.callback(trigger=Bluetooth.CLIENT_CONNECTED | Bluetooth.CLIENT_DISCONNECTED, handler=conn_cb)
bluetooth.advertise(True)

srv1 = bluetooth.service(uuid=SERVICE_UUID, isprimary=True,nbr_chars=1)

chr1 = srv1.characteristic(uuid=DATA_CHARACTERISTIC_UUID, value='read_from_here', properties=Bluetooth.PROP_READ | Bluetooth.PROP_WRITE | Bluetooth.PROP_NOTIFY)

chr1.callback(trigger=(Bluetooth.CHAR_READ_EVENT | Bluetooth.CHAR_SUBSCRIBE_EVENT), handler=chr1_handler)

print('Start BLE service')
def update_handler(update_alarm):
    global battery
    global update
    battery-=1
    if battery == 1:
        battery = 100
    if update:
        chr1.value(str(battery))

update_alarm = Timer.Alarm(update_handler, 1, periodic=True)