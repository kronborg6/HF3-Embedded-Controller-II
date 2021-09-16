import time


state = False
max_delay = 0.60
last_time = time.time()
pulse_count = 0

pinMode(button, "INPUT")



def Set_Alram():
    state = False
    max_delay = 0.60
    last_time = time.time()
    pulse_count = 0
    button = 4
    while True:
        new_state = digitalRead(button)

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
                break