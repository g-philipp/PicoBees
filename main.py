import machine
import src.BME280.bme280_float as bme280
from src.hx711endail.src.hx711 import *

i2c = machine.I2C(0, sda=machine.Pin(8), scl=machine.Pin(9))
bme = bme280.BME280(i2c=i2c)

# driver = HX711(d_out=5, pd_sck=4)
hx = hx711(Pin(4), Pin(5))
hx.set_power(hx711.power.pwr_up)

while True:
    # 4. wait for readings to settle
    hx711.wait_settle(hx711.rate.rate_10)

    # 5. read values

    # wait (block) until a value is read
    val = hx.get_value()
    print(val)

print(bme.values[0])
print(bme.values[1])
print(bme.values[2])