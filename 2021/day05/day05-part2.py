target_input = open("input.txt" , "r")
data = target_input.read().split("\n")
del data[-1]

visited = {}
for any in data:
    getnumbers = any.split(" -> ")
    instructions = []
    for each in getnumbers:
        coordinates = each.split(",")
        point = [int(number) for number in coordinates]
        instructions.append(point)
    if instructions[0][0] == instructions[1][0]:
        if instructions[0][1] > instructions[1][1]:
            for i in range(instructions[1][1], instructions[0][1]+1):
                if (instructions[0][0],i) not in visited:
                    visited[instructions[0][0],i] = 1
                else:
                    visited[instructions[0][0],i] += 1
        else:
            for i in range(instructions[0][1], instructions[1][1]+1):
                if (instructions[0][0],i) not in visited:
                    visited[instructions[0][0],i] = 1
                else:
                    visited[instructions[0][0],i] += 1
            
    elif instructions[0][1] == instructions[1][1]:
        if instructions[0][0] > instructions[1][0]:
            for i in range(instructions[1][0], instructions[0][0]+1):
                if (i,instructions[0][1]) not in visited:
                    visited[i,instructions[0][1]] = 1
                else:
                    visited[i,instructions[0][1]] += 1
        else:
            for i in range(instructions[0][0], instructions[1][0]+1):
                if (i,instructions[0][1]) not in visited:
                    visited[i,instructions[0][1]] = 1
                else:
                    visited[i,instructions[0][1]] += 1
    elif instructions[0][0] > instructions[1][0]:
        if instructions[0][1] > instructions[1][1]:
            for i in range(0, instructions[0][0]-instructions[1][0]+1):
                if (instructions[0][0]-i,instructions[0][1]-i) not in visited:
                    visited[instructions[0][0]-i,instructions[0][1]-i] = 1
                else:
                    visited[instructions[0][0]-i,instructions[0][1]-i] += 1
        elif instructions[0][1] < instructions[1][1]:
            for i in range(0, instructions[0][0]-instructions[1][0]+1):
                if (instructions[0][0]-i,instructions[0][1]+i) not in visited:
                    visited[instructions[0][0]-i,instructions[0][1]+i] = 1
                else:
                    visited[instructions[0][0]-i,instructions[0][1]+i] += 1
    elif instructions[0][0] < instructions[1][0]:
        if instructions[0][1] > instructions[1][1]:
            for i in range(0, instructions[1][0]-instructions[0][0]+1):
                if (instructions[0][0]+i,instructions[0][1]-i) not in visited:
                    visited[instructions[0][0]+i,instructions[0][1]-i] = 1
                else:
                    visited[instructions[0][0]+i,instructions[0][1]-i] += 1
        elif instructions[0][1] < instructions[1][1]:
            for i in range(0, instructions[1][0]-instructions[0][0]+1):
                if (instructions[0][0]+i,instructions[0][1]+i) not in visited:
                    visited[instructions[0][0]+i,instructions[0][1]+i] = 1
                else:
                    visited[instructions[0][0]+i,instructions[0][1]+i] += 1

print(visited)
answer = 0
for each in visited:
    if visited[each] >= 2:
        answer += 1

print(answer)