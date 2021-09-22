# import schedule
import time

List = ["Mikkel", "Kronborg"]
def name(id):
    if id == 1:
        return List[0]
    else:
        return List[1]

new_name = name(0)

# print(new_name)

# print("+")

# check
# if time.time() - oldtime > 59:

def vandes():
    
    oldtime = time.time()
    print("Vandes")
    while True:
        if time.time() - oldtime > 59:
            print("Det er blivet vandet i 1 min")
            break
# vandes()
def while_loop_test():
    i = 0
    x = 0
    while True:
        i += 1
        while True:
            x += 1
            if x > 15:
                break
            print("Kronborg")
        if i > 10:
            x = 0
        print("Mikkel")
        if i > 50:
            break


# print(100 * 0.01)

# Den her køre 3 gang og printer hvert 10 sec
def Open_Vinduer():

    temp = 31
    start_time = time.time()
    print("Oppen Vindue")
    while True:
        if temp > 28:
            while True:
                if temp > 25:
                    if time.time() - start_time > 10:
                        print("10 seconds")
                        start_time = time.time()
                        temp -= 1
                        break
        if temp == 28:
            print(temp)
            print("Den kørt 3 gang")
            break


def job():
    print("I'm working...")

# schedule.every(1).minutes.do(job)
# # schedule.every().hour.do(job)
# schedule.every().day.at("10:30").do(job)
# schedule.every().monday.do(job)
# schedule.every().wednesday.at("13:15").do(job)
# schedule.every().minute.at(":17").do(job)
# print("Test")
# while True:
#     schedule.run_pending()
#     time.sleep(1)






def test_math():
    x = 0.01
    y = 100

    print(y * x)

test_math()
























