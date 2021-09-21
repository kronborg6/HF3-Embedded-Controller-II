import time
from grove_rgb_lcd import *
from grovepi import *

# check
# if time.time() - oldtime > 59:

def vandes_start():

    oldtime = time.time()
    while True:
        print("Vandes")
        if time.time() - oldtime > 599:
            print("Det er blivet vandet i 10 min")
            break
def vandes_stop():
    print("Stop med at vande")

            