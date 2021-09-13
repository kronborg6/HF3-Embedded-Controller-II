import time
#from grovepi import *
#from grove_rgb_lcd import *
rooms = [1, 2, 3, 4, 5, 6, 7, 8, 9]
rooms_name = ["", "", "", "", "", "", "", "", "", ""]

led = 4
potentiometer = 2
dht_sensor_port = 7
button = 3


def GetRoom():
    # i = analogRead(potentiometer)
    on_start = True

    while on_start:

        if i > 1 and i < 100:
            print("Test")
        elif i > 100 and i < 200:
            return 0
        elif  i > 200 and i < 300:
            return 0
        elif i > 300 and i < 400:
            return 0
        elif i > 400 and i < 500:
            return 0
        elif i > 500 and i < 600:
            return 0
        elif i > 600 and i < 700:
            return 0
        elif i > 700 and i < 800:
            return 0
        elif i > 800 and i < 900:
            return 0
        elif i > 900 and i < 1000:
            return 0
        return 0



pinMode(led, "OUTPUT")
time.sleep(1)

i = 0

while True:
    i = analogRead(potentiometer)

    [ temp,hum ] = dht(dht_sensor_port, 0)
    t = str(temp)
    h = str(hum)


    if True:
        while True:
            print("G")

