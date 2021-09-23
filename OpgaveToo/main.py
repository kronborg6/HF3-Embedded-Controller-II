import time
from multiprocessing import Process

from grove_rgb_lcd import *
from grovepi import *


from Mode import *
from Set_local import *
from OpgaveToo.Showtemp import *
from OpgaveToo.Vinduer import *
from OpgaveToo.vandes import *



rooms_name = ["DriveHus 1", "DriveHus 2", "DriveHus 3", "DriveHus 4", "DriveHus 5", "DriveHus 6", "DriveHus 7", "DriveHus 8", "DriveHus 9", "DriveHus 10"]

dht_sensor_port = 7
potentiometer = 2
light_sensor = 1

global room

def main():

    # STemp = 20
    # state = False
    # max_delay = 0.60
    # last_time = time.time()
    # pulse_count = 0

    # button = 4

    # sound_senor = 0
    # led = 3

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

if __name__ == '__main__':

    try:
        room = GetRoom(rooms_name)
        mode = pick_mode()
        global name
        name = mode[1]
        speed = mode[0]
        # main()
        p1 = Process(target=Open_Vinduer, args=(speed,))
        p2 = Process(target=run_vandes,  args=(speed,))
        p3 = Process(target=main)
        p1.start()
        time.sleep(0.1)
        p2.start()
        time.sleep(0.1)
        p3.start()
        time.sleep(0.1)
        p1.join()
        p2.join()
        p3.join()

    except KeyboardInterrupt:
        p1.terminate()
        time.sleep(0.1)
        p2.terminate()
        time.sleep(0.1)
        p3.terminate()
        time.sleep(0.1)
    except (IOError, TypeError) as e:
        p1.terminate()
        time.sleep(0.1)
        p2.terminate()
        time.sleep(0.1)
        p3.terminate()
        time.sleep(0.1)
        print(e)