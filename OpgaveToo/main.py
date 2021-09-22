import time

from grove_rgb_lcd import *
from grovepi import *
from set_local import *

from OpgaveToo.Set_local import *

rooms_name = ["DriveHus 1", "DriveHus 2", "DriveHus 3", "DriveHus 4", "DriveHus 5", "DriveHus 6", "DriveHus 7", "DriveHus 8", "DriveHus 9", "DriveHus 10"]

speed = [1, 50, 100]

room = GetRoom(rooms_name)

STemp = 20
state = False
max_delay = 0.60
last_time = time.time()
pulse_count = 0

button = 4
dht_sensor_port = 7
potentiometer = 2
light_sensor = 1
sound_senor = 0
led = 3


while True:

    light_intensity = analogRead(light_sensor)
    i = analogRead(potentiometer)

    if i < 100:
        print("")
    elif i < 200:
        print("")
    elif i < 300:
        print("")
    elif i < 400:
        print("")
    elif i < 500:
        print("")
    elif i < 600:
        print("")
    elif i < 700:
        print("")






    print("TEST")
