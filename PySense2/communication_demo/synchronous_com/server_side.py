import time
from network import Bluetooth

SERVICE_UUID = 0xAAAA
DATA_CHARACTERISTIC_UUID = 0xBBBB
ACK_CHARACTERISTIC_UUID = 0xCCCC

bt = Bluetooth()
bt.set_advertisement(name='Team 3: Aidan & Phu', service_uuid=SERVICE_UUID)

srv = bt.service(uuid=SERVICE_UUID, isprimary=True)
data_chr = srv.characteristic(uuid=DATA_CHARACTERISTIC_UUID, value='Hello, Client!', properties=Bluetooth.PROP_NOTIFY)
ack_chr = srv.characteristic(uuid=ACK_CHARACTERISTIC_UUID, value='Waiting for ACK', properties=Bluetooth.PROP_READ)

# Flag to indicate acknowledgment status
acknowledgment_received = False

def send_data():
    data_chr.notify(True)
    data_chr.value('Hello, Client!')

def handle_ack(chr):
    global acknowledgment_received
    value = chr.value()
    print("ACK Received:", value)
    acknowledgment_received = True

ack_chr.callback(trigger=Bluetooth.CHAR_NOTIFY_EVENT, handler=handle_ack)

bt.advertise(True)

while True:
    # Wait until acknowledgment is received
    while not acknowledgment_received:
        pass  # Do nothing and keep waiting

    # Acknowledgment received, reset the flag and send data
    acknowledgment_received = False
    send_data()
    time.sleep(5)
    