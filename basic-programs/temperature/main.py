from machine import Pin, ADC
from time import sleep

sensor = ADC(Pin(4))
sensor.atten(ADC.ATTN_11DB)

while True:
    touch = sensor.read()
    #realTemp = (330 * temp)/4096
    print(touch)
    sleep(0.1)