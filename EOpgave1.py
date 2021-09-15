import time
#from grovepi import *
#   from grove_rgb_lcd import *
rooms = [1, 2, 3, 4, 5, 6, 7, 8, 9]
rooms_name = ["Lærerværelse", "Kantian", "Kontor", "klasselokale 1", "klasselokale 2", "klasselokale 3", "Mødelokale", "klasselokale 4", "", ""]
indstilling = ["Daglig rutine", "Nat indstilling"]

led = 4
potentiometer = 2
dht_sensor_port = 7
button = 3


def GetRoom():
    # i = analogRead(potentiometer)
    on_start = True

    while on_start:

        button_status = digitalRead(button)


        if i > 1 and i < 100:
            setText(rooms_name[0] + "       " + "Pick Room ")
            if button_status:
                return rooms_name[0]
        elif i > 100 and i < 200:
            setText(rooms_name[1] + "       " + "Pick Room ")
            if button_status:
                return rooms_name[1]
        elif  i > 200 and i < 300:
            setText(rooms_name[2] + "       " + "Pick Room ")
            if button_status:
                return rooms_name[2]
        elif i > 300 and i < 400:
            setText(rooms_name[3] + "       " + "Pick Room ")
            if button_status:
                return rooms_name[3]
        elif i > 400 and i < 500:
            setText(rooms_name[4] + "       " + "Pick Room ")
            if button_status:
                return rooms_name[4]
        elif i > 500 and i < 600:
            setText(rooms_name[5] + "       " + "Pick Room ")
            if button_status:
                return rooms_name[5]
        elif i > 600 and i < 700:
            setText(rooms_name[6] + "       " + "Pick Room ")
            if button_status:
                return rooms_name[6]
        elif i > 700 and i < 800:
            setText(rooms_name[7] + "       " + "Pick Room ")
            if button_status:
                return rooms_name[7]
        elif i > 800 and i < 900:
            setText(rooms_name[8] + "       " + "Pick Room ")
            if button_status:
                return rooms_name[8]
        elif i > 900 and i < 1000:
            setText(rooms_name[9] + "       " + "Pick Room ")
            if button_status:
                return rooms_name[9]
        return 0



pinMode(led, "OUTPUT")
time.sleep(1)

i = 0

room = GetRoom()

x = 0

while True:
#    i = analogRead(potentiometer)

    [ temp,hum ] = dht(dht_sensor_port, 0)
    t = str(temp)
    h = str(hum)

    setRGB(0, 128, 64)
    setRGB(0, 255, 0)
    setText("Place: " + room + "      " + indstilling[x])
    time.sleep(3)
    setRGB(0, 128, 64)
    setRGB(0, 255, 0)
    setText("Temp: " + t + "C       " + "Humidity: " + h + "%")



    if True:
        while True:
            print("G")

