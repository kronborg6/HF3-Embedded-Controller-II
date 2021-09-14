List = ["Mikkel", "Kronborg"]

def name(id):
    if id == 1:
        return List[0]
    else:
        return List[1]

new_name = name(0)

print(new_name)