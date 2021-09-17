from alram import *
from Sound import *
from Showtemp import *
import time
import math
from grovepi import *
from grove_rgb_lcd import *
from Set_local import *
from Showtemp import *
from Temp import *

rooms_name = ["Lærerværelse", "Kantian", "Kontor", "klasselokale 1", "klasselokale 2", "klasselokale 3", "Mødelokale", "klasselokale 4", "klasselokale 5", "klasselokale 6"]


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


HLyd = 0

pinMode(button, "INPUT")


print("Running")
while True:
    try:
        button_status = digitalRead(button)
        light_intensity = analogRead(light_sensor)
        i = analogRead(potentiometer)
        sound_level = analogRead(sound_senor)
        [ temp,hum ] = dht(dht_sensor_port, 0)


        if sound_level > 300:
            HLyd += 1
            if light_intensity < 50:
                Set_Alram()

        

        if i < 50:
            display_temp_c(temp, hum)
        elif i < 100:
            display_temp_fan(temp, hum)
        elif i < 150:
            time.sleep(1)
            setRGB(0, 128, 64)
            setRGB(0, 255, 0)
            setText("Skift tempurtur")
            if button_status:
                set_temp(STemp)
            # set_temp(STemp, state, max_delay, pulse_count, last_time)
        elif  i < 200:
            Show_sound(HLyd)
            if button_status:
                print("Høje lyd er blevet sat til 0")
                HLyd = 0
    except KeyboardInterrupt:
        break
    except (IOError, TypeError) as e:
        print(e)


