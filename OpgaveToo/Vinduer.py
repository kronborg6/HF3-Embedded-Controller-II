import time
from grove_rgb_lcd import *
from grovepi import *

def Open_Vinduer(faster):
    dht_sensor_port = 7
    led = 55
    on = True
    pinMode(led, "OUTPUT")
    start_time = time.time()
    analogWrite(led, 1)

    while True:

        if on:
            analogWrite(led, 1)
            on = not on

        [ temp,hum ] = dht(dht_sensor_port, 0)
        if temp > 28:
            print("Oppen Vindue")

            while True:
                [ temp,hum ] = dht(dht_sensor_port, 0)
                if temp < 25:
                    if time.time() - start_time > 299 * faster:
                        start_time = time.time()
                        print("Luk Vindue")
                        analogWrite(led, 0)
                        on = not on
                        break
                