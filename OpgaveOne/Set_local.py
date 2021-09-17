from grovepi import *
from grove_rgb_lcd import *


potentiometer = 2
button = 4

def GetRoom(rooms_name):
    on_start = True 
    pinMode(button, "INPUT")
    print("Inset Room")

    while on_start:

        button_status = digitalRead(button)
        i = analogRead(potentiometer)

        if i > 1 and i < 100:
            #print("Room 1")
            time.sleep(1)
            setText_norefresh(rooms_name[0] + "       " + "Pick Room ")
            if button_status:
                return rooms_name[0]
        elif i > 100 and i < 200:
            time.sleep(1)
            print("Room 2")
            setText_norefresh(rooms_name[1] + "       " + "Pick Room ")
            if button_status:
                return rooms_name[1]
        elif  i > 200 and i < 300:
            time.sleep(1)
            print("Room 3")
            setText_norefresh(rooms_name[2] + "       " + "Pick Room ")
            if button_status:
                return rooms_name[2]
        elif i > 300 and i < 400:
            time.sleep(1)
            print("Room 4")
            setText_norefresh(rooms_name[3] + "       " + "Pick Room ")
            if button_status:
                return rooms_name[3]
        elif i > 400 and i < 500:
            time.sleep(1)
            print("Room 5")
            setText_norefresh(rooms_name[4] + "       " + "Pick Room ")
            if button_status:
                return rooms_name[4]
        elif i > 500 and i < 600:
            time.sleep(1)
            print("Room 6")
            setText_norefresh(rooms_name[5] + "       " + "Pick Room ")
            if button_status:
                return rooms_name[5]
        elif i > 600 and i < 700:
            time.sleep(1)
            print("Room 7")
            setText_norefresh(rooms_name[6] + "       " + "Pick Room ")
            if button_status:
                return rooms_name[6]
        elif i > 700 and i < 800:
            time.sleep(1)
            print("Room 8")
            setText_norefresh(rooms_name[7] + "       " + "Pick Room ")
            if button_status:
                return rooms_name[7]
        elif i > 800 and i < 900:
            time.sleep(1)
            print("Room 9")
            setText_norefresh(rooms_name[8] + "       " + "Pick Room ")
            if button_status:
                return rooms_name[8]
        elif i > 900 and i < 1000:
            time.sleep(1)
            setText_norefresh(rooms_name[9] + "       " + "Pick Room ")
            if button_status:
                return rooms_name[9]