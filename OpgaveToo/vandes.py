import time
import schedule
from grove_rgb_lcd import *
from grovepi import *

# check
# if time.time() - oldtime > 59:

def vandes_start(mode):

    oldtime = time.time()
    print("Vandes")
    while True:
        if time.time() - oldtime > 599 * mode:
            print("Det er blivet vandet i 10 min")
            break

def run_vandes():
    if True:
        print("")
    else:
        schedule.every().day.at("10:30").do(vandes_start)
        schedule.every().day.at("18:30").do(vandes_start)

    while True:
        schedule.run_pending()
        time.sleep(1)

def vandes_stop():
    print("Stop med at vande")
