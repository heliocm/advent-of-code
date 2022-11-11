target_input = open("input.txt" , "r")
data = target_input.read().split("\n")
del data[-1]

def findLowPoint(data):
    points = []
    for x in range(len(data)):
        for y in range(len(data[0])):
            if x-1 >= 0 and x+1 < len(data):
                if y-1 >= 0 and y+1 < len(data[0]):
                    if data[x][y] < data[x-1][y] and data[x][y] < data[x+1][y] and data[x][y] < data[x][y-1] and data[x][y] < data[x][y+1]:
                        points.append((x,y))
                elif y-1 <0:
                    if data[x][y] < data[x-1][y] and data[x][y] < data[x+1][y] and data[x][y] < data[x][y+1]:
                        points.append((x,y))
                else:
                    if data[x][y] < data[x-1][y] and data[x][y] < data[x+1][y] and data[x][y] < data[x][y-1]:
                        points.append((x,y))
            elif x-1 < 0:
                if y-1 >= 0 and y+1 < len(data[0]):
                    if data[x][y] < data[x+1][y] and data[x][y] < data[x][y-1] and data[x][y] < data[x][y+1]:
                        points.append((x,y))
                elif y-1 <0:
                    if data[x][y] < data[x+1][y] and data[x][y] < data[x][y+1]:
                        points.append((x,y))
                else:
                    if data[x][y] < data[x+1][y] and data[x][y] < data[x][y-1]:
                        points.append((x,y))
            else:
                if y-1 >= 0 and y+1 < len(data[0]):
                    if data[x][y] < data[x-1][y] and data[x][y] < data[x][y-1] and data[x][y] < data[x][y+1]:
                        points.append((x,y))
                elif y-1 <0:
                    if data[x][y] < data[x-1][y] and data[x][y] < data[x][y+1]:
                        points.append((x,y))
                else:
                    if data[x][y] < data[x-1][y] and data[x][y] < data[x][y-1]:
                        points.append((x,y))
    return points

def sizeBasin (lowpoint, data):
    tocheck = [lowpoint]
    checked = []
    i = 0
    while len(tocheck) != 0:
        (x, y) = tocheck[0]
        if x-1 >= 0 and data[x-1][y] != '9':
            if (x-1,y) not in checked:
                tocheck.append((x-1,y)) 
        if x+1 < len(data) and data[x+1][y] != '9':
            if (x+1,y) not in checked:
                tocheck.append((x+1,y))
        if y-1 >= 0 and data[x][y-1] != '9':
            if (x,y-1) not in checked:
                tocheck.append((x,y-1))
        if y+1 < len(data[0]) and data[x][y+1] != '9':
            if (x,y+1) not in checked:
                tocheck.append((x,y+1))
        if tocheck[0] not in checked:
            checked.append(tocheck[0])
        tocheck.pop(0)
        i += 1
    return len(checked)

sizes = []
for (x,y) in findLowPoint(data):
    sizes.append(sizeBasin((x,y), data))
sizes.sort(reverse=True)
highest = sizes[:3]
answer = 1
for number in highest:
    answer *= number

print(answer)
