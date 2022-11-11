import time
start_time = time.time()
target_input = open("input.txt" , "r")
seats = target_input.read().split("\n")
del seats[-1]

def check_adjacents(array, x, y):
    adjacents = []
    for i in reversed(range(0, x)):
        j = y
        try:
            if not array[i][j] == ".":
                adjacents.append(array[i][j])
                break
        except:
            pass
    for i in range(x+1, len(array)):
        j = y
        try:
            if not array[i][j] == ".":
                adjacents.append(array[i][j])
                break
        except:
            pass
    for j in reversed(range(0,y)):
        i = x
        try:
            if not array[i][j] == ".":
                adjacents.append(array[i][j])
                break
        except:
            pass
    for j in range(y+1, len(array[0])):
        i = x
        try:
            if not array[i][j] == ".":
                adjacents.append(array[i][j])
                break
        except:
            pass

    for i,j in zip(reversed(range(0, x)), reversed(range(0,y))):
        try:
            if not array[i][j] == ".":
                adjacents.append(array[i][j])
                break
        except:
            pass
    for i,j in zip(range(x+1, len(array)), range(y+1, len(array[0]))):
        try:
            if not array[i][j] == ".":
                adjacents.append(array[i][j])
                break
        except:
            pass
    for i,j in zip(reversed(range(0, x)), range(y+1, len(array[0]))):
        try:
            if not array[i][j] == ".":
                adjacents.append(array[i][j])
                break
        except:
            pass
    for i,j in zip(range(x+1, len(array)), reversed(range(0,y))):
        try:
            if not array[i][j] == ".":
                adjacents.append(array[i][j])
                break
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
            try:
                if actual_layout[i][j] == "L":
                    adjacents = check_adjacents(previous_layout, i, j)
                    if adjacents.count("#") == 0:
                        actual_layout[i][j] = "#"
                elif actual_layout[i][j] == "#":
                    adjacents = check_adjacents(previous_layout, i, j)
                    if not adjacents.count("#") < 5:
                        actual_layout[i][j] = "L"
            except:
                pass

# for line in actual_layout:
#     str1 = ""
#     print(str1.join(line))

count = 0
for line in actual_layout:
    count = count + line.count("#")

print(count)

print("--- %s seconds ---" % (time.time() - start_time))


