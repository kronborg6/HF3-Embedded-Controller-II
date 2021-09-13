import time
#from grovepi import *

rooms = [1, 2, 3, 4, 5, 6, 7, 8, 9]
rooms_name = ["", "", "", "", "", "", "", "", "", ""]

led = 4
potentiometer = 2


def GetRoom():
    i = analogRead(potentiometer)

    if i < 100:
        print("Test")
    elif i > 100 and i < 200:
        return 0
    elif  i < 300:
        return 0

    return 0



pinMode(led, "OUTPUT")
time.sleep(1)

i = 0

while True:
    i = analogRead(potentiometer)

    if i < 100:
        print("Test")
    elif i > 100 and i < 200:
        break
    elif  i < 300:
        break