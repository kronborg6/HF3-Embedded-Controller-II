import time
from grovepi import *
from grove_rgb_lcd import *
rooms = [1, 2, 3, 4, 5, 6, 7, 8, 9]
rooms_name = ["Lærerværelse", "Kantian", "Kontor", "klasselokale 1", "klasselokale 2", "klasselokale 3", "Mødelokale", "klasselokale 4", "", ""]

led = 3
potentiometer = 2
dht_sensor_port = 7
button = 4

pinMode(led, "OUTPUT")
pinMode(button, "INPUT")


def GetRoom():
    on_start = True

    while on_start:

        button_status = digitalRead(button)
        i = analogRead(potentiometer)

        if i > 1 and i < 100:
            #print("Room 1")
            setText(rooms_name[0] + "       " + "Pick Room ")
            button_status = digitalRead(button)
            if button_status:
                print("Jeg virker")
                analogWrite(led, 1)
        elif i > 100 and i < 200:
            print("Room 2")
            setText(rooms_name[1] + "       " + "Pick Room ")
            if button_status:
                analogWrite(led, 0)
        elif  i > 200 and i < 300:
            print("Room 3")
            setText(rooms_name[2] + "       " + "Pick Room ")
            if button_status:
                print("")
        elif i > 300 and i < 400:
            print("Room 4")
            setText(rooms_name[3] + "       " + "Pick Room ")
            if button_status:
                print("")
        elif i > 400 and i < 500:
            print("Room 5")
            setText(rooms_name[4] + "       " + "Pick Room ")
            if button_status:
                print("")
        elif i > 500 and i < 600:
            print("Room 6")
            setText(rooms_name[5] + "       " + "Pick Room ")
            if button_status:
                print("")
        elif i > 600 and i < 700:
            print("Room 7")
            setText(rooms_name[6] + "       " + "Pick Room ")
            if button_status:
                print("")
        elif i > 700 and i < 800:
            print("Room 8")
            setText(rooms_name[7] + "       " + "Pick Room ")
            if button_status:
                print("")
        elif i > 800 and i < 900:
            print("Room 9")
            setText(rooms_name[8] + "       " + "Pick Room ")
            if button_status:
                print("")
        elif i > 900 and i < 1000:
            setText(rooms_name[9] + "       " + "Pick Room ")
            if button_status:
                print("")




time.sleep(1)
analogWrite(led, 1)
i = 0
GetRoom()

#while True:


# while True:
# #    i = analogRead(potentiometer)

#     [ temp,hum ] = dht(dht_sensor_port, 0)
#     t = str(temp)
#     h = str(hum)


# #    setRGB(0, 128, 64)
# #    setRGB(0, 255, 0)
# #    setText("Temp: " + t + "C       " + "Humidity: " + h + "%")



# #    if True:
# #        while True:
# #            print("G")
