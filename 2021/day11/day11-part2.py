target_input = open("input.txt" , "r")
data = target_input.read().split("\n")
del data[-1]

def findZeroes(octopuses):
    zeroes = []
    for x in range(len(octopuses)):
        for y in range(len(octopuses[0])):
            if octopuses[x][y] == '0': zeroes.append((x,y))
    return zeroes

def findAdjacents(nine, octopuses):
    adjacents = []
    (x,y) = nine
    if 1<=x<len(octopuses)-1:
        if 1<=y<len(octopuses[0])-1:
            for i in range(x-1,x+2):
                for j in range(y-1, y+2):
                    if (i,j) != (x,y):
                        adjacents.append((i,j))
        elif y == 0:
            for i in range(x-1,x+2):
                for j in range(y, y+2):
                    if (i,j) != (x,y):
                        adjacents.append((i,j))
        else:
            for i in range(x-1,x+2):
                for j in range(y-1, y+1):
                    if (i,j) != (x,y):
                        adjacents.append((i,j))
    elif x == 0:
        if 1<=y<len(octopuses[0])-1:
            for i in range(x,x+2):
                for j in range(y-1, y+2):
                    if (i,j) != (x,y):
                        adjacents.append((i,j))
        elif y == 0:
            for i in range(x,x+2):
                for j in range(y, y+2):
                    if (i,j) != (x,y):
                        adjacents.append((i,j))
        else:
            for i in range(x,x+2):
                for j in range(y-1, y+1):
                    if (i,j) != (x,y):
                        adjacents.append((i,j))
    else:
        if 1<=y<len(octopuses[0])-1:
            for i in range(x-1,x+1):
                for j in range(y-1, y+2):
                    if (i,j) != (x,y):
                        adjacents.append((i,j))
        elif y == 0:
            for i in range(x-1,x+1):
                for j in range(y, y+2):
                    if (i,j) != (x,y):
                        adjacents.append((i,j))
        else:
            for i in range(x-1,x+1):
                for j in range(y-1, y+1):
                    if (i,j) != (x,y):
                        adjacents.append((i,j))
    return adjacents

def countZeroes(octopuses):
    return len(findZeroes(octopuses))

answer = 0
steps = 0
total = len(data) * len(data[0])
while countZeroes(data) != total:
    board = []
    for each in data:
        line = ""
        for char in each:
            if int(char) != 9:
                line += str(int(char)+1)
            else:
                line += str(0)
        board.append(line)
    data = board
    adjacents = []
    for each in findZeroes(data):
        for adjacent in findAdjacents(each, data):
            adjacents.append(adjacent)
    final_board = [list(each) for each in data]
    while len(adjacents) > 0:
        (x,y) = adjacents[0]
        char = final_board[x][y]
        if int(char) != 9 and int(char) != 0:
            final_board[x][y] = str(int(char)+1)
        elif int(char) == 9:
            final_board[x][y] = str(0)
            for adjacent in findAdjacents((x,y), final_board):
                adjacents.append(adjacent)
        adjacents.pop(0)
    steps += 1

    data = [''.join(each) for each in final_board]

print(steps)