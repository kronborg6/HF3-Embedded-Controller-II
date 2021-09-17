from grovepi import *
from grove_rgb_lcd import *
import time



def display_temp_c(temp, hum):
    c = (temp - 32) * 0.5556
    time.sleep(1)
    setRGB(0, 128, 64)
    setRGB(0, 255, 0)
    setText("Temp: " + str(c) + "C       " + "Humidity: " + str(hum) + "%")

def display_temp_fan(temp, hum):
    time.sleep(1)
    setRGB(0, 128, 64)
    setRGB(0, 255, 0)
    setText("Temp: " + str(temp) + "C       " + "Humidity: " + str(hum) + "%")
