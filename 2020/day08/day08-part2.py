target_input = open("input.txt" , "r")
boot_code = target_input.read().split("\n")
del boot_code[-1]

accumulator = 0
index = 0
visited = []
visited.append(index)
tried = []
changed = False
while index <= len(boot_code) - 1:
    instruction = boot_code[index].split(' ')[0]
    operation = boot_code[index].split(' ')[1][:1]
    value = boot_code[index].split(' ')[1][1:]
    if instruction == 'acc':
        if operation == '+':
            accumulator = accumulator + int(value)
        elif operation == '-':
            accumulator = accumulator - int(value)
        index = index + 1
    elif instruction == 'jmp':
        if tried.count(index) == 0 and not changed:
            tried.append(index)
            changed = True
            index = index + 1
        else:
            if operation == '+':
                index = index + int(value)
            elif operation == '-':
                index = index - int(value)

    elif instruction == 'nop':
        if tried.count(index) == 0 and not changed:
            tried.append(index)
            changed = True
            if operation == '+':
                index = index + int(value)
            elif operation == '-':
                index = index - int(value)
        else:
            index = index + 1
    
    if visited.count(index) != 0:
        accumulator = 0
        index = 0
        visited = []
        visited.append(index)
        changed = False
    else:
        visited.append(index)

print(accumulator)
