import time
start_time = time.time()
target_input = open("input.txt" , "r")
seats = target_input.read().split("\n")
del seats[-1]

def check_adjacents(array, x, y):
    adjacents = []
    for i in range(x - 1,x + 2):
        for j in range(y - 1,y + 2):
            if not (i == x and j == y) and ( i >= 0 and j >= 0):
                try:
                    adjacents.append(array[i][j])
                except:
                    pass
    
    return adjacents

actual_layout = []
for seat in seats:
    actual_layout.append(list(seat))

previous_layout = []

while previous_layout != actual_layout:
    previous_layout = []
    for line in actual_layout:
        previous_layout.append(line.copy())
    for i in range(0, len(actual_layout)):
        for j in range(0, len(actual_layout[0])):
            if actual_layout[i][j] == "L":
                adjacents = check_adjacents(previous_layout, i, j)
                if adjacents.count("#") == 0:
                    actual_layout[i][j] = "#"
            elif actual_layout[i][j] == "#":
                adjacents = check_adjacents(previous_layout, i, j)
                if not adjacents.count("#") < 4:
                    actual_layout[i][j] = "L"

count = 0
for line in actual_layout:
    count = count + line.count("#")

print(count)

print("--- %s seconds ---" % (time.time() - start_time))


