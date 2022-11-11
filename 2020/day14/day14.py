target_input = open("input.txt" , "r")
initialization = target_input.read().split("\n")
del initialization[-1]

memory_index = []
memory_value = []
mask = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
for line in initialization:
    line = line.split(" = ")
    command = line[0]
    value = line[1]
    if command == "mask":
        mask = value
    elif command[0:3] == "mem":
        value = list(f'{int(value):036b}')
        for i in range(0, len(list(mask))):
            if not list(mask)[i] == "X":
                value[i] = list(mask)[i]
        value = ''.join(value)
        value = int(value, 2)

        if memory_index.count(int(command[4:-1])) == 0:
            memory_index.append(int(command[4:-1]))
            memory_value.append(value)
        
        else:
            memory_value[memory_index.index(int(command[4:-1]))] = value

total = 0
for each in memory_value:
    total = total + each

print(total)