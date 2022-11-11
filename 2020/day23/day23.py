target_input = open("input.txt" , "r")
data = target_input.read()
cups = list(data)
def pick_up(cups, current):
    picked = []
    for i in range(cups.index(current)+1, cups.index(current)+4):
        if i > 8:
            picked.append(cups[i-9])
        else:
            picked.append(cups[i])
    for each in picked:
        cups.remove(each)
    return picked
def destination(cups, pick_up_list, current):
    dest = int(current) - 1
    if dest < 1:
        dest = 9
    while str(dest) in pick_up_list:
        dest -= 1
        if dest < 1:
            dest = 9
    return str(dest)
def place_picked(cups, pick_up_list, destination):
    index = cups.index(destination)
    i=1
    for each in pick_up_list:
        cups.insert(index + i, each)
        i += 1
    return 0
def next_current(cups, current):
    if cups.index(current) == len(cups)-1:
        return cups[0]
    else:
        return cups[cups.index(current)+1]

current = cups[0]
for i in range(0, 100):
    picked = pick_up(cups, current)
    dest = destination(cups, picked, current)
    place_picked(cups, picked, dest)
    current = next_current(cups, current)
answer = "".join(cups[cups.index("1")+1:]+cups[:cups.index("1")])
print(answer)