from machine import Pin

pin = Pin(4, Pin.OUT)

while True:
    for i in range(100000):
        pin.value(not pin.value())