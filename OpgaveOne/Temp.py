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
        setRGB(0, 128, 64)
        setRGB(0, 255, 0)
        setText_norefresh("Tryk En gnag for + Et tryk - tre tryk SET")
        new_state = digitalRead(button)
        if new_state:
            while True:
                # time.sleep(0.5)
                tempstr = str(STemp)
                setRGB(0, 128, 64)
                setRGB(0, 255, 0)
                setText_norefresh("Set temperature: " + tempstr + "C ")
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
                        STemp = STemp
                        # pulse_count = 0
                    if pulse_count == 2:
                        STemp -= 1
                        STemp = STemp
                    if pulse_count == 3:
                        pulse_count = 0
                        return STemp
                        # STemp = STemp
                        # pulse_count = 0
                    # if pulse_count == 5:
                    else:
                        pulse_count = 0
