import time
from multiprocessing import Process

from grove_rgb_lcd import *
from grovepi import *
from set_local import *

from OpgaveToo.Mode import *
from OpgaveToo.Set_local import *
from OpgaveToo.Showtemp import *
from OpgaveToo.Vinduer import *
from OpgaveToo.vandes import *



rooms_name = ["DriveHus 1", "DriveHus 2", "DriveHus 3", "DriveHus 4", "DriveHus 5", "DriveHus 6", "DriveHus 7", "DriveHus 8", "DriveHus 9", "DriveHus 10"]

dht_sensor_port = 7
potentiometer = 2
light_sensor = 1

def main():

    STemp = 20
    state = False
    max_delay = 0.60
    last_time = time.time()
    pulse_count = 0

    # button = 4

    sound_senor = 0
    led = 3

    setRGB(0, 128, 64)
    setRGB(0, 255, 0)


    while True:

        [ temp,hum ] = dht(dht_sensor_port, 0)
        light_intensity = analogRead(light_sensor)
        i = analogRead(potentiometer)

        


        if i < 220: #Show hvad drivehus den er sat op i

            setText_norefresh(room + "")
        elif i < 440: # Daglig eller Nat rutine
            if light_intensity < 10:
                setText_norefresh("Daglig rutine")
            else:
                setText_norefresh("natlige rutine")
        elif i < 660: #Temp i c
            display_temp_c(temp, hum)
        elif i < 880: #Temp i f
            display_temp_fan(temp, hum)
        elif i < 1100: #Show Mode
            setText_norefresh("Aktiv Mode" + mode[1])
        # elif i < 600:
        #     print("")
        # elif i < 700:
        #     print("")
if __name__ == '__main__':

    room = GetRoom(rooms_name)
    mode = pick_mode()
    # main()
    p1 = Process(target=Open_Vinduer, args=(mode[0]))
    p1.start()
    p2 = Process(target=main,  args=(room, mode))
    p2.start()
    p3 = Process(target=run_vandes,  args=(room, mode))
    p3.start()
    p1.join()
    p2.join()