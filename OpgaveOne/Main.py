from alram import Set_Alram
from Showtemp import display_temp
import time
import math
from grovepi import *
from grove_rgb_lcd import *
from Set_local import *
from Showtemp import *
from Temp import *

rooms_name = ["Lærerværelse", "Kantian", "Kontor", "klasselokale 1", "klasselokale 2", "klasselokale 3", "Mødelokale", "klasselokale 4", "klasselokale 5", "klasselokale 6"]


room = GetRoom()

STemp = 20
state = False
max_delay = 0.60
last_time = time.time()
pulse_count = 0

dht_sensor_port = 7
potentiometer = 2
light_sensor = 1

pinMode(button, "INPUT")

while True:
    light_intensity = analogRead(light_sensor)
    i = analogRead(potentiometer)
    [ temp,hum ] = dht(dht_sensor_port, 0)
    if light_intensity < 50:
        Set_Alram()

    if i < 50:
        display_temp_c(temp, hum)
    elif i < 100:
        display_temp_fan(temp, hum)
    elif i < 150:
        set_temp(STemp, state, max_delay, pulse_count)
    else:
        if light_intensity < 50:
            Set_Alram()

