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

i = 0
x = 0
while True:
    # x += 1
    i += 1
    while True:
        x += 1
        if x > 15:
            break
        print("Kronborg")
    if i > 10:
        break
    print("Mikkel")

