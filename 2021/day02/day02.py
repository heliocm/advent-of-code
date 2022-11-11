target_input = open("input.txt" , "r")
data = target_input.read().split("\n")
del data[-1]

horizontal = 0
depth = 0
for each in data:
    instructions = each.split(" ")
    if instructions[0] == 'forward':
        horizontal += int(instructions[1])
    elif instructions[0] == 'down':
        depth += int(instructions[1])
    elif instructions[0] == 'up':
        depth -= int(instructions[1])

print(horizontal*depth)
