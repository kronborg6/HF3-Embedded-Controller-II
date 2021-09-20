import time
from grove_rgb_lcd import *
from grovepi import *



# Test varbiles to use for setup not 

temp = 0


def Open_Vinduer():

    sleep_time = 300

    if temp < 30:
        # Make a tread
        print("Oppen Vindue")
        while True:
           time.sleep(sleep_time) 

           if temp < 25:
               break



    print("test")