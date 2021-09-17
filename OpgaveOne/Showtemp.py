from grovepi import *
from grove_rgb_lcd import *
import time



def display_temp_c(temp, hum):
    time.sleep(1)
    setRGB(0, 128, 64)
    setRGB(0, 255, 0)
    setText_norefresh("Temp: " + str(temp) + "C       " + "Humidity: " + str(hum) + "%")

def display_temp_fan(temp, hum):
    f = temp * 1.8 + 32
    time.sleep(1)
    setRGB(0, 128, 64)
    setRGB(0, 255, 0)
    setText_norefresh("Temp: " + str(f) + "C       " + "Humidity: " + str(hum) + "%")
