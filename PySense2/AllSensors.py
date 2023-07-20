from network import Bluetooth
import time
import ubinascii
import struct
import math
import pycom
from pycoproc_2 import Pycoproc
import machine

from LIS2HH12 import LIS2HH12
from SI7006A20 import SI7006A20
from LTR329ALS01 import LTR329ALS01
from MPL3115A2 import MPL3115A2,ALTITUDE,PRESSURE

pycom.heartbeat(False)
pycom.rgbled(0x0A0A08) # white

bt = Bluetooth()
bt.start_scan(-1)

def twoscmp(value):
    if value > 128:
        value = value - 256
    return value

def byte_to_info(uuid):
    gas_res_d = 0
    name = uuid[0:3]
    name_text = ''.join(chr(t) for t in name)
    if name_text == "PyN":
        sensor_id = uuid[7]
        mac = ubinascii.hexlify(uuid[10:16])
        press = ubinascii.hexlify(uuid[8:10])
        press_d = int(press, 16)
        gas_res = ubinascii.hexlify(uuid[3:7])
        gas_res_d = int(gas_res, 16)
        print("{} {} BLE_MAC: {}, Pressure: {} hPa, Gas resistance: {} ohm".format(name_text, sensor_id, mac, press_d, gas_res_d), end=", ")
    return (name_text,gas_res_d)

def air_quality_score(hum, gas_res):
    gas_reference = 250000
    hum_reference = 40
    gas_lower_limit = 5000
    gas_upper_limit = 50000
    if (hum >= 38 and hum <= 42):
        hum_score = 0.25*100
    else:
        if (hum < 38):
            hum_score = 0.25/hum_reference*hum*100
        else:
            hum_score = ((-0.25/(100-hum_reference)*hum)+0.416666)*100
    if (gas_reference > gas_upper_limit):
        gas_reference = gas_upper_limit
    if (gas_reference < gas_lower_limit):
        gas_reference = gas_lower_limit
    gas_score = (0.75/(gas_upper_limit-gas_lower_limit)*gas_reference -(gas_lower_limit*(0.75/(gas_upper_limit-gas_lower_limit))))*100
    air_quality_score = hum_score + gas_score

    print("IAQ score:", air_quality_score)

    print("Air quality is", end=" ")
    air_quality_score = (100-air_quality_score)*5
    if (air_quality_score >= 301):
        print("Hazardous")
    elif (air_quality_score >= 201 and air_quality_score <= 300 ):
        print("Very Unhealthy")
    elif (air_quality_score >= 176 and air_quality_score <= 200 ):
        print("Unhealthy")
    elif (air_quality_score >= 151 and air_quality_score <= 175 ):
        print("Unhealthy for Sensitive Groups")
    elif (air_quality_score >=  51 and air_quality_score <= 150 ):
        print("Moderate")
    elif (air_quality_score >=  00 and air_quality_score <=  50 ):
        print("Good")

while True:
    # print('Air Sensor External:\n')
    adv = bt.get_adv()
    while adv: # and adv.rssi>-80:# and ubinascii.hexlify(adv.mac)==b'cd9e13c0f24a':
        read_adv = bt.resolve_adv_data(adv.data, Bluetooth.ADV_MANUFACTURER_DATA)
        if read_adv==None:
            pass
        else:
            manuf = ubinascii.hexlify(read_adv)
            manuf_data = ubinascii.hexlify(read_adv[0:4])
            # print(manuf_data)
            print(manuf_data)
            if (manuf_data == b'4c000215') :#or (manuf_data == b'd2000215')):# company id=d2 is Dialog, b'4c000215' is Apple's id and it implies ibeacon
                # print("mac:", ubinascii.hexlify(adv.mac))
                uuid_raw = read_adv[4:20]
                uuid = ubinascii.hexlify(uuid_raw)
                name, air=byte_to_info(uuid_raw)
                if name == "PyN":
                    print("rssi:",adv.rssi)
                    major = ubinascii.hexlify(read_adv[20:22])
                    minor = ubinascii.hexlify(read_adv[22:24])
                    tx_power = ubinascii.hexlify(read_adv[24:25])
                    tx_power_real = twoscmp(int(tx_power, 16))
                    major_int = int(major, 16)
                    major_f = major_int/100 # bme688
                    minor_int = int(minor,16)
                    minor_f = minor_int/100 # bme688, it is divided by 10 initially in the dialog's firmware.
                    print("Temperature: {} C, Humidity: {} %r.H.".format(major_f, minor_f), time.time())
                    air_quality_score(minor_f, air)
                    print("")
                    break
        adv = bt.get_adv()
    else:
        time.sleep(0.050)

    # print("Internal sensors:\n")

    py = Pycoproc()
    if py.read_product_id() != Pycoproc.USB_PID_PYSENSE:
        raise Exception('Not a Pysense')

    pybytes_enabled = False
    if 'pybytes' in globals():
        if(pybytes.isconnected()):
            print('Pybytes is connected, sending signals to Pybytes')
            pybytes_enabled = True

    mp = MPL3115A2(py,mode=ALTITUDE) # Returns height in meters. Mode may also be set to PRESSURE, returning a value in Pascals
    print("MPL3115A2 temperature: " + str(mp.temperature()))
    print("Altitude: " + str(mp.altitude()))

    mpp = MPL3115A2(py,mode=PRESSURE) # Returns pressure in Pa. Mode may also be set to ALTITUDE, returning a value in meters
    print("Pressure: " + str(mpp.pressure()))

    si = SI7006A20(py)
    print("Temperature: " + str(si.temperature())+ " deg C")
    print("Relative Humidity: " + str(si.humidity()) + " %RH")
    print("Dew point: "+ str(si.dew_point()) + " deg C")

    t_ambient = 24.4
    print("Humidity Ambient for " + str(t_ambient) + " deg C: " + str(si.humid_ambient(t_ambient)) + " %RH")

    lt = LTR329ALS01(py)
    print("Light (channel Blue, channel Red): " + str(lt.light()))
    print("Lux: ", str(lt.lux()), "lx")

    li = LIS2HH12(py)
    print("Acceleration: " + str(li.acceleration()))
    print("Roll: " + str(li.roll()))
    print("Pitch: " + str(li.pitch()))

    print("Battery voltage: " + str(py.read_battery_voltage()))

    # set your battery voltage limits here
    vmax = 4.2
    vmin = 3.3
    battery_voltage = py.read_battery_voltage()
    battery_percentage = (battery_voltage - vmin / (vmax - vmin))*100
    print("Battery voltage: " + str(py.read_battery_voltage()),", percentage: ", battery_percentage)
    if(pybytes_enabled):
        pybytes.send_signal(1, mpp.pressure())
        pybytes.send_signal(2, si.temperature())
        pybytes.send_signal(3, lt.light())
        pybytes.send_signal(4, li.acceleration())
        pybytes.send_battery_level(int(battery_percentage))
        print("Sent data to pybytes")

    time.sleep(3)