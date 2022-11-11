target_input = open("input.txt" , "r")
initialization = target_input.read().split("\n")
del initialization[-1]

memory_index = []
memory_value = []
mask = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
for line in initialization:
    possible_addresses = []
    line = line.split(" = ")
    command = line[0]
    value = line[1]
    if command == "mask":
        mask = value
    elif command[0:3] == "mem":
        value = int(value)
        address = int(command[4:-1])
        address = list(f'{int(address):036b}')
        for i in range(0, len(list(mask))):
            if not list(mask)[i] == "0":
                address[i] = list(mask)[i]
        address = ''.join(address)
        constructor = []
        constructor.append(address)
        for each in constructor:
            if  each.find("X") != -1 :
                constructor.append(each.replace("X", "0", 1))
                constructor.append(each.replace("X", "1", 1))

        for each in constructor:
            if each.find("X") == -1:
                possible_addresses.append(int(each, 2))

        for each in possible_addresses:
            if memory_index.count(each) == 0:
                memory_index.append(each)
                memory_value.append(value)
            else:
                memory_value[memory_index.index(each)] = value

total = 0
for each in memory_value:
    total = total + each

print(total)