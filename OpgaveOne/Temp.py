import time
from grovepi import *


button = 4

def set_temp(STemp, state, max_delay, pulse_count):
    new_state = digitalRead(button)
    setRGB(0, 128, 64)
    setRGB(0, 255, 0)
    time.sleep(1)
    tempstr = str(STemp)
    setText("Set temperature: " + tempstr + " " + "Tryk En gnag for + Et tryk - tre tryk SET")
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
            print("Slå alem fra")
            # on = False
