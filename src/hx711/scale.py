from machine import SPI, Pin
from src.hx711.hx711_pio import HX711


hx = HX711(clk=Pin(5), data=Pin(4))
hx.power_up()
# hx.set_scale(48.36)
hx.tare()
# val = hx.get_units()
val = hx.get_value()
print(val)
