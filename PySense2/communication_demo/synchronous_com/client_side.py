import time
from network import Bluetooth

SERVICE_UUID = 0xAAAA
DATA_CHARACTERISTIC_UUID = 0xBBBB
ACK_CHARACTERISTIC_UUID = 0xCCCC

# bt = Bluetooth()
# bt.set_advertisement(name='Client', service_uuid=SERVICE_UUID)

def handle_data(chr):
    value = chr.value()
    print("Received:", value)

def send_acknowledgment(chr):
    chr.value('ACK')  # Send acknowledgment message

# bt.advertise(True)

bt = Bluetooth()
print('Start scanning for BLE services')
bt.start_scan(-1)
adv = None

while True:
    adv = bt.get_adv()
    if adv and bt.resolve_adv_data(adv.data, Bluetooth.ADV_NAME_CMPL)=="Team 3: Aidan & Phu":
        conn = bt.connect(adv.mac)
        if conn:
            print("Connected to Team 3: Aidan & Phu")
            try:
                service = conn.services()[0]
                data_chr = service.characteristic(DATA_CHARACTERISTIC_UUID)
                ack_chr = service.characteristic(ACK_CHARACTERISTIC_UUID)

                conn.subscribe(data_chr, callback=handle_data)

                while conn.isconnected():
                    send_acknowledgment(ack_chr)
                    time.sleep(2)
            except:
                continue

bt.stop_scan()
bt.disconnect_client() 
