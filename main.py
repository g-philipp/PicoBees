import machine
import src.BME280.bme280_float as bme280
import src.PicoUPSA.picoUPSa as picoUps
from src.hx711endail.src.hx711 import *

# BME280
# bmeI2c = machine.I2C(0, sda=machine.Pin(8), scl=machine.Pin(9))
# bme = bme280.BME280(i2c=bmeI2c)

# UPS
ups = picoUps.INA219(addr=0x43)

# # driver = HX711(d_out=5, pd_sck=4)
# hx = hx711(Pin(4), Pin(5))
# hx.set_power(hx711.power.pwr_up)

# while True:
#     # 4. wait for readings to settle
#     hx711.wait_settle(hx711.rate.rate_10)

#     # 5. read values

#     # wait (block) until a value is read
#     val = hx.get_value()
#     print(val)


## BME280 ##
# print(bme.values[0])
# print(bme.values[1])
# print(bme.values[2])

## UPS ##
bus_voltage = ups.getBusVoltage_V()             # voltage on V- (load side)
current = ups.getCurrent_mA()                   # current in mA
P = (bus_voltage -3)/1.2*100
if(P<0):P=0
elif(P>100):P=100

print("Voltage:  {:6.3f} V".format(bus_voltage))
print("Current:  {:6.3f} A".format(current/1000))
print("Percent:  {:6.1f} %".format(P))