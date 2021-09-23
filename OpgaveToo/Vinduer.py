import time
from grove_rgb_lcd import *
from grovepi import *

def Open_Vinduer(mode, dht_sensor_port):
    dht_sensor_port = 7
    start_time = time.time()
    while True:
        [ temp,hum ] = dht(dht_sensor_port, 0)
        if temp > 28:
            print("Oppen Vindue")
            while True:
                [ temp,hum ] = dht(dht_sensor_port, 0)
                if temp < 25:
                    if time.time() - start_time > 299 * mode:
                        start_time = time.time()
                        print("Luk Vindue")
                        break
                