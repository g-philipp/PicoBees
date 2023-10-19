from machine import Pin, I2C, SoftI2C, SPI, RTC, deepsleep, lightsleep
import src.sd.sdcard
import uos
import os
import src.ds1307.ds1307 as ds1307
import src.BME280.bme280_float as bme280
import src.PicoUPSA.picoUPSa as picoUps
from src.hx711endail.hx711 import *


################################
            #Vars              
################################

# 5000 ms = 5 Sekunden
sleepTime = 60000


################################
            #Init              
################################

# BME280 1
bmeI2c = I2C(1, sda=Pin(26), scl=Pin(27))
bmeInt = bme280.BME280(i2c=bmeI2c)
# BME280 2
bmeI2c2 = I2C(1, sda=Pin(6), scl=Pin(7))
bmeExt = bme280.BME280(i2c=bmeI2c2)
# RTC
# uses SoftI2C class and pins for Raspberry Pi pico 
i2c0 = SoftI2C(scl=Pin(27), sda=Pin(26), freq=100000)
ds1307rtc = ds1307.DS1307(i2c0, 0x68)
# UPS
ups = picoUps.INA219(addr=0x43)
# SD
# Assign chip select (CS) pin (and start it high)
sdcs = Pin(9, Pin.OUT)

# Intialize SPI peripheral (start with 1 MHz)
sdSpi = SPI(1,
            baudrate=1000000,
            polarity=0,
            phase=0,
            bits=8,
            firstbit=SPI.MSB,
            sck=Pin(10),
            mosi=Pin(11),  #TX
            miso=Pin(12))  #RX
# Initialize SD card
sd = src.sd.sdcard.SDCard(sdSpi, sdcs)

# internal RealTimeClock
# rtc = RTC()



################################
          #Functions              
################################

# def goToSleep():
#     # deepsleep(sleepTime)
#     lightsleep(sleepTime)

def getTime():
#     # internal RealTimeClock
#     print(rtc.datetime())
#     return rtc.datetime()
      return ds1307rtc.datetime

def setTime():
    # internal RTC
    # rtc.datetime((2023, 10, 14, 6, 15, 56, 0, 0))
    # set time (year, month, day, hours. minutes, seconds, weekday: integer: 0-6 )
    ds1307rtc.datetime = (2023, 10, 19, 19, 24, 0, 3)

def mountSD():
    try:
        # Mount filesystem
        vfs = uos.VfsFat(sd)
        uos.mount(vfs, "/sd", readonly=False)

        # Check if the mount was successful
        if "/sd" in uos.listdir():
            print("Mount operation successful.")
        # else:
        #     print("/sd not found, mount may have failed.")
    except OSError as e:
        print("Error:", e)

def unmountSD():
    uos.umount("/sd")

def writeSD(text):
    # if "/sd" in uos.listdir():
    with open("/sd/sensors.txt", "a") as file:
        file.write(text+"\r\n")
        file.close()
    print("Write operation successful.")
    # else:
    #     print("/sd not found, mount may have failed.")

def getWeight():
    with hx711(Pin(5), Pin(4)) as hx:
        hx.set_power(hx711.power.pwr_up)
        hx.set_gain(hx711.gain.gain_128)
        hx711.wait_settle(hx711.rate.rate_10)
        print(hx.get_value())
        return hx.get_value()

# def getWeather():
#     ## BME280 ##
#     print(bmeInt.values[0])
#     print(bmeInt.values[1])
#     print(bmeInt.values[2])
#     print(bmeExt.values[0])
#     print(bmeExt.values[1])
#     print(bmeExt.values[2])
#     return bmeInt.values, bmeExt.values

def getUPS():
    # UPS ##
    bus_voltage = ups.getBusVoltage_V()             # voltage on V- (load side)
    current = ups.getCurrent_mA()                   # current in mA
    P = (bus_voltage -3)/1.2*100
    if(P<0):P=0
    elif(P>100):P=100
    # print("Voltage:  {:6.3f} V".format(bus_voltage))
    # print("Current:  {:6.3f} A".format(current/1000))
    # print("Percent:  {:6.1f} %".format(P))
    return bus_voltage,current,P



################################
            #main              
################################

try:
    mountSD()
    time = getTime()
    weight = getWeight()
    bmeIntDeg = bmeInt.values[0]
    bmeIntPress = bmeInt.values[1]
    bmeIntHumid = bmeInt.values[2]
    bmeExtDeg = bmeExt.values[0]
    bmeExtPress = bmeExt.values[1]
    bmeExtHumid = bmeExt.values[2]
    power = getUPS()

    timestamp = str(time[0])+"-"+str(time[1])+"-"+str(time[2])+"_"+str(time[3])+"-"+str(time[4])+"-"+str(time[5])
    weatherInt = str(bmeIntDeg)+ ";" + str(bmeIntPress)+ ";" + str(bmeIntHumid)
    weatherExt = str(bmeExtDeg)+ ";" + str(bmeExtPress)+ ";" + str(bmeExtHumid)
    parsedPower = str(power[0])+ "V;" + str(power[1])+ "mA;" + str(power[2])+"%"

    text = str(timestamp) + ";" + str(weight) + ";" + str(weatherInt) + ";" + weatherExt+ ";" + parsedPower

    print(text)
    writeSD(text=text)
    unmountSD()
    # goToSleep()
except Exception as e:
    print(e)