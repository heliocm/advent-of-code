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

def takeSteps(facing, stepsize, visited, answer):
    if facing == 'N':
        for i in range(1, stepsize+1):
            new = [visited[-1][0]+1,visited[-1][1]]
            if new in visited and len(answer) < 1:
                print(sum(new))
                answer.append(new)
            else:
                visited.append(new)
    elif facing == 'S':
        for i in range(1, stepsize+1):
            new = [visited[-1][0]-1,visited[-1][1]]
            if new in visited and len(answer) < 1:
                print(sum(new))
                answer.append(new)
            else:
                visited.append(new)
    elif facing == 'L':
        for i in range(1, stepsize+1):
            new = [visited[-1][0],visited[-1][1]+1]
            if new in visited and len(answer) < 1:
                print(sum(new))
                answer.append(new)
            else:
                visited.append(new)
    else:
        for i in range(1, stepsize+1):
            new = [visited[-1][0],visited[-1][1]-1]
            if new in visited and len(answer) < 1:
                print(sum(new))
                answer.append(new)
            else:
                visited.append(new)

target_input = open("input.txt" , "r")
data = target_input.read().split("\n")
del data[-1]

instructions = data[0].split(", ")

facing = 'N'
visited = [[0,0]]
answer = []
for instruction in instructions:
    rotation = instruction[0]
    stepsize = int(instruction[1:])
    facing = orientation(facing, rotation)
    takeSteps(facing, stepsize, visited, answer)


