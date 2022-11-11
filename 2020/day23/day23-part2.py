target_input = open("input.txt" , "r")
data = target_input.read()
list_cups = list(data)

cups = {}
def pick_up(cups, current):
    picked = []
    pick_next = current
    for i in range(0, 3):
        picked.append(cups[pick_next]['next'])
        pick_next = cups[pick_next]['next']
    return picked

def destination(cups, pick_up_list, current):
    dest = current - 1
    if dest < 1:
        dest = 1000000
    while dest in pick_up_list:
        dest -= 1
        if dest < 1:
            dest = 1000000
    return dest

def next_current(cups, current):
    return cups[current]['next']

for i in range(1,1000000+1):
    if i == 1:
        cups[int(list_cups[i-1])] = { 'next': int(list_cups[i]),
                                    'previous': 1000000
                                    }
    elif i == len(list_cups):
        cups[int(list_cups[i-1])] = { 'next': 10,
                                    'previous': int(list_cups[i-2])
                                    }
    elif i>1 and i < len(list_cups):
        cups[int(list_cups[i-1])] = { 'next': int(list_cups[i]),
                                    'previous': int(list_cups[i-2])
                                    }
    elif i == 10:
        cups[i] = { 'next': 11,
                    'previous': int(list_cups[8])
                    }
    elif i == 1000000:
        cups[i] = { 'next': int(list_cups[0]),
                    'previous': 999999
                    }
    else:
        cups[i] = { 'next': i+1,
                    'previous': i-1
                    }

current = 3
for i in range(0, 10000000):
    picked = pick_up(cups, current)
    dest = destination(cups, picked, current)
    cups[current]['next'] = cups[picked[2]]['next']
    auxiliar = cups[dest]['next']
    cups[dest]['next'] = picked[0]
    cups[picked[0]]['previous'] = dest
    cups[picked[2]]['next'] = auxiliar
    cups[auxiliar]['previous'] = picked[2]
    current = next_current(cups, current)

first_next = cups[1]['next']
second_next = cups[first_next]['next']
total = first_next * second_next
print(total)