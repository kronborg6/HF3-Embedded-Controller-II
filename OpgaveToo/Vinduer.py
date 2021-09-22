import time
from grove_rgb_lcd import *
from grovepi import *

# temp = 0

def Open_Vinduer():
    dht_sensor_port = 7
    start_time = time.time()
    while True:
        [ temp,hum ] = dht(dht_sensor_port, 0)
        if temp > 28:
            print("Oppen Vindue")
            while True:
                [ temp,hum ] = dht(dht_sensor_port, 0)
                if temp < 25:
                    if time.time() - start_time > 299:
                        start_time = time.time()
                        print("Luk Vindue")
                        break
                