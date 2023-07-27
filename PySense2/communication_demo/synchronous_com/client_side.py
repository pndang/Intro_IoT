import time
from network import Bluetooth

SERVICE_UUID = 0xec00
DATA_CHARACTERISTIC_UUID = 0xec0e
ACK_CHARACTERISTIC_UUID = 0x2A01

SERVER_NAME = 'Grp3'

bluetooth = Bluetooth()

def handle_data(chr, event_data):
    global connected
    time.sleep(0.1)
    print('in handle')
    if connected:
        print('is connected')
        data = chr.value()
        print("New value: {}".format(data))

        # print('ACK:', ack_chr.value())
        if data == b'Hello, Client!':
            send_acknowledgment()
        

    else:
        print("Not connected.")

# def send_acknowledgment():
#     global ack_chr
#     ack_chr.write('ACK')  # Send acknowledgment message
#     print('sent ack')

def send_acknowledgment():
    print('in send ack')
    global chr1
    chr1.write('ACK') 
    print('Sent ACK')

print("Scanning for servers...")
bluetooth.start_scan(-1)  # Scan indefinitely until connection is established

connected = False

# Scanning and Connection Loop
while True:
    advs = bluetooth.get_advertisements()
    for adv in advs:
        if adv:
            try:
                name = bluetooth.resolve_adv_data(adv.data, Bluetooth.ADV_NAME_CMPL)
                if name == SERVER_NAME:
                    conn = bluetooth.connect(adv.mac)
                    print("Connected to Grp3")
                    connected = True
                    try:
                        services = conn.services()
                        for service in services:
                            characteristics = service.characteristics()
                            for characteristic in characteristics:
                                if characteristic.uuid() == DATA_CHARACTERISTIC_UUID:
                                    data_chr = characteristic
                                    # print(data_chr.properties())
                                    # print(Bluetooth.PROP_NOTIFY)
                                    if (data_chr.properties() & Bluetooth.PROP_NOTIFY):
                                        print('in data')
                                        data_chr.callback(trigger=Bluetooth.CHAR_NOTIFY_EVENT, handler=handle_data)
                                    chr1 = characteristic
                                # elif characteristic.uuid() == ACK_CHARACTERISTIC_UUID:
                                #     print('in ack')
                                #     ack_chr = characteristic

                        print('test')

                        # if (data_chr.properties() & Bluetooth.PROP_NOTIFY):
                        #     while conn.isconnected():
                        #         print(data_chr.value())
                        #         time.sleep(2)

                    except:
                        continue
            except:
                continue
