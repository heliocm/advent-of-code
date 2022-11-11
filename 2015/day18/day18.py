target_input = open("input.txt" , "r")
data = target_input.read().split("\n")
del data[-1]

def check_neighbors(row, column, array):
    to_check = []
    for x in range(-1, 2):
        for y in range(-1, 2):
            if not (x == 0 and y == 0):
                if row + x in range(0,100):
                    if column + y in range(0,100):
                        to_check.append(array[row + x][column + y])
    return sum(to_check)


lights = []
for line in data:
    row = []
    line = list(line)
    for on_off in line:
        row.append(1) if on_off == "#" else row.append(0)  
    lights.append(row)



turn = 0
while turn < 100:
    turn += 1
    aux = []
    for x in range(0,100):
        row = []
        for y in range(0,100):
            row.append(0)
        aux.append(row)
    for x in range(0,100):
        for y in range(0,100):
            if lights[x][y] == 1:
                aux[x][y] = 1 if check_neighbors(x,y,lights) in range(2,4) else 0
            else:
                aux[x][y] = 1 if check_neighbors(x,y,lights) == 3 else 0
    lights = aux.copy()

result = 0
for each in lights:
    result += sum(each)

print(result)
            