import ast
target_input = open("input.txt" , "r")
representation = target_input.read().split("\n")
del representation[-1]

state = {}
cycle = 0
for i in range(0, len(representation)):
    for j in range(0, len(representation[0])):
        if representation[i][j] == "#":
            state[str([i,j,0])] = []
            for x in range(i-1, i+2):
                for y in range(j-1, j+2):
                    for z in range(-1, 2):
                        state[str([i,j,0])].append([x,y,z])
            state[str([i,j,0])].remove([i,j,0])

while cycle < 6:
    cycle = cycle + 1
    possible_changes = {}
    to_delete = []
    for each in state:
        active_neighbors = 0
        for neighbor in state[each]:
            if str(neighbor) in state:
                active_neighbors = active_neighbors + 1
            if str(neighbor) in possible_changes:
                possible_changes[str(neighbor)] = possible_changes[str(neighbor)] + 1
            else:
                possible_changes[str(neighbor)] = 1
        if not (active_neighbors == 2 or active_neighbors == 3):
            to_delete.append(each)
    for each in to_delete:
        state.pop(each)

    for each in possible_changes:
        if possible_changes[each] == 3 and not each in state:
            state[each] = []
            neighborX = ast.literal_eval(each)[0]
            neighborY = ast.literal_eval(each)[1]
            neighborZ = ast.literal_eval(each)[2]
            for x in range(neighborX-1, neighborX+2):
                for y in range(neighborY-1, neighborY+2):
                    for z in range(neighborZ-1,neighborZ+2):
                        state[each].append([x,y,z])
            state[each].remove([neighborX,neighborY,neighborZ])

print(len(state))

