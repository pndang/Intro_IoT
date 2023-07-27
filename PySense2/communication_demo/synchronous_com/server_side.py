import time
from network import Bluetooth

SERVICE_UUID = 0xec00
DATA_CHARACTERISTIC_UUID = 0xec0e
ACK_CHARACTERISTIC_UUID = 0x2A01

bluetooth = Bluetooth()
bluetooth.set_advertisement(name='Grp3', service_uuid=SERVICE_UUID)

srv = bluetooth.service(uuid=SERVICE_UUID, isprimary=True, nbr_chars=2)
data_chr = srv.characteristic(uuid=DATA_CHARACTERISTIC_UUID, value='Hello, Client!', properties=Bluetooth.PROP_READ | Bluetooth.PROP_NOTIFY | Bluetooth.PROP_WRITE)
ack_chr = srv.characteristic(uuid=ACK_CHARACTERISTIC_UUID, value='Waiting for ACK', properties=Bluetooth.PROP_WRITE)

# Flag to indicate acknowledgment status
acknowledgment_received = False

# Flag to indicate client connection status
client_connected = False
first_packet = True

def send_data():
    global acknowledgment_received, client_connected
    if acknowledgment_received and client_connected:
        # Send data to the client using notifications
        data_chr.value('Hello, Client!')
        acknowledgment_received = False  # Set flag to False, waiting for acknowledgment
        time.sleep(2)

def first_send():
    global first_packet, client_connected
    print('in first send')
    if client_connected:
        print('in send')
        data_chr.value('Hello!!')
        first_packet = False
        print('first sent')
        print(data_chr.value())
        time.sleep(2)

def handle_ack(chr, data):
    global acknowledgment_received
    print("ACK Received:", data)
    acknowledgment_received = True  # Set flag to True, acknowledgment received

# ack_chr.callback(trigger=Bluetooth.CHAR_WRITE_EVENT, handler=handle_ack)

def conn_cb(chr):
    global client_connected
    events = chr.events()
    if events & Bluetooth.CLIENT_CONNECTED:
        print('client connected')
        client_connected = True
    elif events & Bluetooth.CLIENT_DISCONNECTED:
        print('client disconnected')
        client_connected = False

bluetooth.callback(trigger=Bluetooth.CLIENT_CONNECTED | Bluetooth.CLIENT_DISCONNECTED, handler=conn_cb)

data_chr.callback(trigger=Bluetooth.CHAR_NOTIFY_EVENT, handler=handle_ack)

print("BLE Started!")
bluetooth.advertise(True)

while True:

    print('test')

    print(first_packet)

    print("ACK: {}".format(acknowledgment_received))
    
    if client_connected:
        while not acknowledgment_received:
            data_chr.value('hello!!! from loop')
            print(data_chr.value())
            time.sleep(2)

    # if first_packet:
    #     first_send()

    send_data()
    time.sleep(2)
