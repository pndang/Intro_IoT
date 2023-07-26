import time
from network import Bluetooth

SERVICE_UUID = 0x1800
DATA_CHARACTERISTIC_UUID = 0x2A00
ACK_CHARACTERISTIC_UUID = 0x2A01

SERVER_NAME = 'Grp3'  # Replace 'Server' with the actual name of the server device

bluetooth = Bluetooth()

def handle_data(chr, event_data):
    time.sleep(0.1)
    print('in handle')
    if bluetooth.isconnected():
        print('is connected')
        data = chr.value()
        print("New value: {}".format(data))

        ack_chr.value('ACK')  # Send acknowledgment message
        print('sent ack')

    else:
        print("Not connected.")

print("Scanning for servers...")
bluetooth.start_scan(-1)  # Scan indefinitely until connection is established

# Scanning and Connection Loop
while True:
    advs = bluetooth.get_advertisements()
    for adv in advs:
        name = bluetooth.resolve_adv_data(adv.data, Bluetooth.ADV_NAME_CMPL)
        if name == SERVER_NAME:
            conn = bluetooth.connect(adv.mac)
            print("Connected to Grp3")
            try:
                services = conn.services()
                for service in services:
                    characteristics = service.characteristics()
                    for characteristic in characteristics:
                        if characteristic.uuid() == DATA_CHARACTERISTIC_UUID:
                            data_chr = characteristic
                            print(data_chr.properties())
                            print(Bluetooth.PROP_NOTIFY)
                            if (data_chr.properties() & Bluetooth.PROP_NOTIFY):
                                print('in data')
                                data_chr.callback(trigger=Bluetooth.CHAR_NOTIFY_EVENT, handler=handle_data)
                        elif characteristic.uuid() == ACK_CHARACTERISTIC_UUID:
                            print('in ack')
                            ack_chr = characteristic

                print('test')

                if (data_chr.properties() & Bluetooth.PROP_NOTIFY):
                    while conn.isconnected():
                        print(data_chr.value())
                        time.sleep(2)

            except:
                continue
            

# def send_acknowledgment(chr):
#     chr.write('ACK')  # Send acknowledgment message




# *****

# import time
# from network import Bluetooth

# SERVICE_UUID = 0xAAAA
# DATA_CHARACTERISTIC_UUID = 0xBBBB
# ACK_CHARACTERISTIC_UUID = 0xCCCC

# # bt = Bluetooth()
# # bt.set_advertisement(name='Client', service_uuid=SERVICE_UUID)

# def handle_data(chr):
#     value = chr.value()
#     print("Received:", value)

# def send_acknowledgment(chr):
#     chr.value('ACK')  # Send acknowledgment message

# # bt.advertise(True)

# bt = Bluetooth()
# print('Start scanning for BLE services')
# bt.start_scan(-1)
# adv = None

# while True:
#     adv = bt.get_adv()
#     if adv and bt.resolve_adv_data(adv.data, Bluetooth.ADV_NAME_CMPL)=="Team 3: Aidan & Phu":
#         conn = bt.connect(adv.mac)
#         if conn:
#             print("Connected to Team 3: Aidan & Phu")
#             try:
#                 service = conn.services()[0]
#                 data_chr = service.characteristic(DATA_CHARACTERISTIC_UUID)
#                 ack_chr = service.characteristic(ACK_CHARACTERISTIC_UUID)

#                 conn.subscribe(data_chr, callback=handle_data)

#                 while conn.isconnected():
#                     send_acknowledgment(ack_chr)
#                     time.sleep(2)
#             except:
#                 continue

# bt.stop_scan()
# bt.disconnect_client() 
