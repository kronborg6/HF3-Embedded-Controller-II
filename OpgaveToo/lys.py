from grove_rgb_lcd import *
from grovepi import *


def start_lys(lys_stryke, is_on):

    if lys_stryke < 25 and is_on == True:
        print("Tænd lys")
        return False

def sluk_lys():
    print("Slyk lys")
    return True