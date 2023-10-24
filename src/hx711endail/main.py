from machine import Pin
from src.hx711endail.hx711 import *

tare_val = 110181
known_weight_raw  = 57136 # Rohwert bei 2.5kg
empty_raw = 0 # Rohwert ohne Gewicht
known_weight_kg = 2.5

SCALE = known_weight_kg / (known_weight_raw - empty_raw)
OFFSET = known_weight_raw - (SCALE * known_weight_kg)


# SCALE = (Bekanntes Gewicht in Kilogramm) / (Referenz-Rohwert - Leer-Rohwert)
# OFFSET = Referenz-Rohwert - (Skalierungsfaktor * Bekanntes Gewicht in Kilogramm)

# 1. initalise the hx711 with pin 14 as clock pin, pin
# 15 as data pin
hx = hx711(Pin(5), Pin(4))

# 2. power up
hx.set_power(hx711.power.pwr_up)

# 3. [OPTIONAL] set gain and save it to the hx711
# chip by powering down then back up
hx.set_gain(hx711.gain.gain_64)

# 4. wait for readings to settle
# hx711.wait_settle(hx711.rate.rate_10)

# 5. read values

# wait (block) until a value is read
val = hx.get_value_timeout()
if (val == None):
    print("lol")
    val = 0
else:
    val = val - 110181

weight_kg = (val - OFFSET) / SCALE

print("Skalierungsfaktor (SCALE):", SCALE)
print("Offset (OFFSET):", OFFSET)

print("Gewicht roh:", val)
print("Gewicht (in Kilogramm):", weight_kg)