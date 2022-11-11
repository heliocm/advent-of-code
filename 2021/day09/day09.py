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

answer = 0
for (x,y) in findLowPoint(data):
    answer += int(data[x][y]) + 1

print(answer)

