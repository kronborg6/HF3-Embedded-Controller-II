import time
from grovepi import *
from grove_rgb_lcd import *




def set_temp(STemp):
# def set_temp(STemp, state, max_delay, pulse_count, last_time):
    button = 4
    state = False
    max_delay = 0.60
    last_time = time.time()
    pulse_count = 0
    pinMode(button, "INPUT")
    setRGB(0, 128, 64)
    setRGB(0, 255, 0)
    while True:
        tempstr = str(STemp)
        # time.sleep(4)
        setRGB(0, 128, 64)
        setRGB(0, 255, 0)
        setText("Tryk En gnag for + Et tryk - tre tryk SET")
        new_state = digitalRead(button)
        if new_state:
            while True:
                setRGB(0, 128, 64)
                setRGB(0, 255, 0)
                setText("Set temperature: " + tempstr + "C ")
                new_state = digitalRead(button)
                if new_state and not state:
                    pulse_count += 1
                    state = True
                    last_time = time.time()
                elif not new_state:
                    state = False
                if time.time() > (last_time + max_delay) and pulse_count > 0:
                    if pulse_count == 1:
                        STemp += 1
                    if pulse_count == 2:
                        STemp -= 1
                    if pulse_count == 3:
                        return STemp
