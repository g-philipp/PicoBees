from machine import SPI, Pin
from src.hx711Lopy.hx711_gpio import HX711

pin_OUT = Pin(5, Pin.IN, pull=Pin.PULL_DOWN)
pin_SCK = Pin(4, Pin.OUT)

hx711 = HX711(pin_SCK, pin_OUT)

hx711.set_scale(48.36)
hx711.tare()
val = hx711.get_units()
print(val)
