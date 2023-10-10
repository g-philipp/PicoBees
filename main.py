from machine import Pin, I2C
import src.BME280.bme280_float as bme280
import src.PicoUPSA.picoUPSa as picoUps
from src.hx711endail.hx711 import *

# BME280 1
bmeI2c = I2C(0, sda=Pin(8), scl=Pin(9))
bme1 = bme280.BME280(i2c=bmeI2c)
# BME280 2
# bmeI2c2 = I2C(1, sda=Pin(6), scl=Pin(7))
# bme2 = bme280.BME280(i2c=bmeI2c2)

# UPS
# ups = picoUps.INA219(addr=0x43)


with hx711(Pin(4), Pin(5)) as hx:
    hx.set_power(hx711.power.pwr_up)
    hx.set_gain(hx711.gain.gain_128)
    hx711.wait_settle(hx711.rate.rate_10)
    print(hx.get_value())


## BME280 ##
print(bme1.values[0])
print(bme1.values[1])
print(bme1.values[2])
# print(bme2.values[0])
# print(bme2.values[1])
# print(bme2.values[2])

## UPS ##
# bus_voltage = ups.getBusVoltage_V()             # voltage on V- (load side)
# current = ups.getCurrent_mA()                   # current in mA
# P = (bus_voltage -3)/1.2*100
# if(P<0):P=0
# elif(P>100):P=100

# print("Voltage:  {:6.3f} V".format(bus_voltage))
# print("Current:  {:6.3f} A".format(current/1000))
# print("Percent:  {:6.1f} %".format(P))
