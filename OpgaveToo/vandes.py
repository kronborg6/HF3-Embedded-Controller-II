import time
import schedule
from grove_rgb_lcd import *
from grovepi import *

# check
# if time.time() - oldtime > 59:

def vandes_start(faster):
    led = 3
    pinMode(led, "OUTPUT")
    oldtime = time.time()
    print("Vandes")
    analogWrite(led, 1)
    while True:
        if time.time() - oldtime > 599 * faster:
            print("Det er blivet vandet")
            analogWrite(led, 0)

            break

def run_vandes(mode):
    val = mode[0]
    if val == 0.1:
        schedule.every(10).seconds.do(vandes_start, faster=val)
    elif val == 0.01:
        schedule.every(2).seconds.do(vandes_start, faster=val)
    else:
        schedule.every().day.at("10:30").do(vandes_start, faster=val)
        schedule.every().day.at("18:30").do(vandes_start, faster=val)

    while True:
        schedule.run_pending()
        time.sleep(1)

def vandes_stop():
    print("Stop med at vande")
