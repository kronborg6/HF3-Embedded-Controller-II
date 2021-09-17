from grovepi import *
from grove_rgb_lcd import *
import time



def display_temp_c(temp, hum):
    if str(temp) != "nan" and str(hum) != "nan":
        setRGB(0, 128, 64)
        setRGB(0, 255, 0)
        setText_norefresh("Temp: " + str(temp) + "C       " + "Humidity: " + str(hum) + "%")

def display_temp_fan(temp, hum):
    if str(temp) != "nan" and str(hum) != "nan":
        f = temp * 1.8 + 32
        setRGB(0, 128, 64)
        setRGB(0, 255, 0)
        setText_norefresh("Temp: " + str(f) + "C       " + "Humidity: " + str(hum) + "%")
