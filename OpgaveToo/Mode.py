from grove_rgb_lcd import *
from grovepi import *



def pick_mode():

    potentiometer = 2
    button = 4
    setRGB(0, 128, 64)
    setRGB(0, 255, 0)

    pinMode(button, "INPUT")
    print("Inset Room")

    while True:
        button_status = digitalRead(button)
        i = analogRead(potentiometer)
        if i < 333:
            setText_norefresh("Normal Mode" + "       " + "Press button to pick")
            if button_status:
                return 1, "Normal Mode"
        elif i < 666:
            setText_norefresh("Test Mode 10 time faster" + "       " + "Press button to pick")
            if button_status:
                return 0.1, "Test Mode 10 time faster"
        elif i < 1100:
            setText_norefresh("Test Mode 100 time faster" + "       " + "Press button to pick")
            if button_status:
                return 0.01, "Test Mode 100 time faster"


# def normal_mode(speed):
#     print("")

# def test_mode_10_time_faster(speed):
#     print("")

# def test_mode_100_time_faster(speed):
#     print("")