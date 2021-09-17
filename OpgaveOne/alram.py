import time
from grovepi import *

state = False
max_delay = 0.60
last_time = time.time()
pulse_count = 0




def Set_Alram():
    state = False
    max_delay = 0.60
    last_time = time.time()
    pulse_count = 0
    button = 4
    led = 3
    pinMode(button, "INPUT")
    pinMode(led, "OUTPUT")
    while True:
        new_state = digitalRead(button)

        # print("Allam")
        digitalWrite(led, 1)

        if new_state and not state:
            pulse_count += 1
            state = True
            last_time = time.time()
        elif not new_state:
            state = False
        if time.time() > (last_time + max_delay) and pulse_count > 0:
            if pulse_count == 1:
                print("Slå alem fra")
                digitalWrite(led, 0)
                break
            if pulse_count == 2:
                print("Slå alem fra")
                digitalWrite(led, 0)
                break
            else:
                pulse_count = 0