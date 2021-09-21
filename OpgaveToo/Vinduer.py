import time
from grove_rgb_lcd import *
from grovepi import *

temp = 0

def Open_Vinduer():

    start_time = time.time()
    print("Oppen Vindue")
    while True:
        if temp < 30:
            while True:
                if temp < 25:
                    if time.time() - start_time > 299:
                        start_time = time.time()
                        print("Luk Vindue")
                        # break
                