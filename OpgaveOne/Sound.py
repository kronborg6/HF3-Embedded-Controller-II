from grovepi import *
from grove_rgb_lcd import *



def Show_sound(Hlyd):
    setRGB(0, 128, 64)
    setRGB(0, 255, 0)
    setText("HøjeLyde: " + str(Hlyd) + "      " + "Tyk paa knappen for reset den ")

