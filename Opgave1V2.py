import time
import math
from grovepi import *
from grove_rgb_lcd import *

rooms = [1, 2, 3, 4, 5, 6, 7, 8, 9]
rooms_name = ["Lærerværelse", "Kantian", "Kontor", "klasselokale 1", "klasselokale 2", "klasselokale 3", "Mødelokale", "klasselokale 4", "", ""]
indstilling = ["Daglig rutine", "Nat indstilling"]

led = 3
potentiometer = 2
dht_sensor_port = 7
button = 4
light_sensor = 1
sound_senor = 0

state = False
max_delay = 0.60
last_time = time.time()
pulse_count = 0

pinMode(led, "OUTPUT")
pinMode(button, "INPUT")


def GetRoom():
    on_start = True 

    while on_start:

        button_status = digitalRead(button)
        i = analogRead(potentiometer)
        sound_level = analogRead(sound_senor)

        if i > 1 and i < 100:
            #print("Room 1")
            time.sleep(1)
            setText(rooms_name[0] + "       " + "Pick Room ")
            if button_status:
                return rooms_name[0]
        elif i > 100 and i < 200:
            time.sleep(1)
            print("Room 2")
            setText(rooms_name[1] + "       " + "Pick Room ")
            if button_status:
                return rooms_name[1]
        elif  i > 200 and i < 300:
            time.sleep(1)
            print("Room 3")
            setText(rooms_name[2] + "       " + "Pick Room ")
            if button_status:
                return rooms_name[2]
        elif i > 300 and i < 400:
            time.sleep(1)
            print("Room 4")
            setText(rooms_name[3] + "       " + "Pick Room ")
            if button_status:
                return rooms_name[3]
        elif i > 400 and i < 500:
            time.sleep(1)
            print("Room 5")
            setText(rooms_name[4] + "       " + "Pick Room ")
            if button_status:
                return rooms_name[4]
        elif i > 500 and i < 600:
            time.sleep(1)
            print("Room 6")
            setText(rooms_name[5] + "       " + "Pick Room ")
            if button_status:
                return rooms_name[5]
        elif i > 600 and i < 700:
            time.sleep(1)
            print("Room 7")
            setText(rooms_name[6] + "       " + "Pick Room ")
            if button_status:
                return rooms_name[6]
        elif i > 700 and i < 800:
            time.sleep(1)
            print("Room 8")
            setText(rooms_name[7] + "       " + "Pick Room ")
            if button_status:
                return rooms_name[7]
        elif i > 800 and i < 900:
            time.sleep(1)
            print("Room 9")
            setText(rooms_name[8] + "       " + "Pick Room ")
            if button_status:
                return rooms_name[8]
        elif i > 900 and i < 1000:
            time.sleep(1)
            setText(rooms_name[9] + "       " + "Pick Room ")
            if button_status:
                return rooms_name[9]




time.sleep(1)
analogWrite(led, 1)
i = 0
x = 0
Pickt_name = GetRoom()
HLyd = 0


on_off = False

#while True:

def til_fahrenheit():
    print("gg")
def til_c(temp):
    c = (temp - 32) * 0.5556
    return str(c)

while True:
#    i = analogRead(potentiometer)
    on = True

    light_intensity = analogRead(light_sensor)
    sound_level = analogRead(sound_senor)
    new_state = digitalRead(button)
    i = analogRead(potentiometer)
    [ temp,hum ] = dht(dht_sensor_port, 0)

    # t = str(temp)

    h = str(hum)

    if sound_level > 500:
        HLyd += 1

    if light_intensity > 50:
        x = 1

        if sound_level < 500:
            while on:
                print("Allam")
                if new_state and not state:
                    pulse_count += 1
                    state = True
                    last_time = time.time()
                elif not new_state:
                    state = False
                if time.time() > (last_time + max_delay) and pulse_count > 0:
                    if pulse_count == 2:
                        print("Slå alem fra")
                        on = False

        if new_state:
            on_off = not on_off
        
        if on_off:
            t = str(temp)

        else:
            t = til_c(temp)


        setRGB(0, 128, 64)
        setRGB(0, 255, 0)
        setText("Place: " + Pickt_name + "      " + indstilling[x])
        time.sleep(3)
        setRGB(0, 128, 64)
        setRGB(0, 255, 0)
        setText("Temp: " + t + "C       " + "Humidity: " + h + "%")

    else:

        if i < 500:

            setRGB(0, 128, 64)
            setRGB(0, 255, 0)
            setText("HøjeLyde: " + HLyd + "      " + "Tryk på knapen for reset den")

            if new_state:
                HLyd = 0
        else:

            if new_state:
                on_off = not on_off
            
            if on_off:
                t = str(temp)

            else:
                t = til_c(temp)


            setRGB(0, 128, 64)
            setRGB(0, 255, 0)
            setText("Place: " + Pickt_name + "      " + indstilling[x])
            time.sleep(3)
            setRGB(0, 128, 64)
            setRGB(0, 255, 0)
            setText("Temp: " + t + "C       " + "Humidity: " + h + "%")


