import time
from grovepi import *
from grove_rgb_lcd import *


pinMode(button, "INPUT")

def set_temp(STemp, state, max_delay, pulse_count, last_time):
    button = 4
    time.sleep(1)
    tempstr = str(STemp)
    while True:
        setRGB(0, 128, 64)
        setRGB(0, 255, 0)
        setText("Set temperature: " + tempstr + " " + "Tryk En gnag for + Et tryk - tre tryk SET")
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
