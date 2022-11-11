def orientation(facing, rotation):
    if facing == 'N':
        if rotation == 'L':
            return 'O'
        else:
            return 'L'
    elif facing == 'S':
        if rotation == 'L':
            return 'L'
        else:
            return 'O'
    elif facing == 'L':
        if rotation == 'L':
            return 'N'
        else:
            return 'S'
    else:
        if rotation == 'L':
            return 'S'
        else:
            return 'N'

def takeSteps(facing, stepsize, vertical, horizontal):
    if facing == 'N':
        vertical += stepsize
    elif facing == 'S':
        vertical -= stepsize
    elif facing == 'L':
        horizontal += stepsize
    else:
        horizontal -= stepsize

    return(vertical, horizontal)

target_input = open("input.txt" , "r")
data = target_input.read().split("\n")
del data[-1]

instructions = data[0].split(", ")

facing = 'N'
horizontal = 0
vertical = 0
for instruction in instructions:
    rotation = instruction[0]
    stepsize = int(instruction[1:])
    facing = orientation(facing, rotation)
    vertical, horizontal = takeSteps(facing, stepsize, vertical, horizontal)
    print(vertical,horizontal)

away = abs(horizontal) + abs(vertical)
print(away)

