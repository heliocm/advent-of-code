target_input = open("input.txt" , "r")
boot_code = target_input.read().split("\n")
del boot_code[-1]

accumulator = 0
index = 0
visited = []
visited.append(index)

while len(visited) == len(set(visited)):
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
        if operation == '+':
            index = index + int(value)
        elif operation == '-':
            index = index - int(value)
    elif instruction == 'nop':
        index = index + 1
    visited.append(index)
    print(index)

print(accumulator)
