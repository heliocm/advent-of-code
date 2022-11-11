target_input = open("input.txt" , "r")
data = target_input.read().split("\n")
del data[-1]

print(data)
area_instruction = data[0]
range_x = ''
for i in range(area_instruction.index('=')+1, area_instruction.index(',')):
    if area_instruction[i] == '.':
        range_x += ' '
    else:
        range_x += area_instruction[i]
range_x = range_x.split('  ')
range_x = [int(each) for each in range_x]
print(range_x)
range_y = ''
for i in range(area_instruction.index('y=')+2, len(area_instruction)):
    if area_instruction[i] == '.':
        range_y += ' '
    else:
        range_y += area_instruction[i]
range_y = range_y.split('  ')
range_y = [int(each) for each in range_y]
range_y.reverse()
print(range_y)

def getMaxY(start, limits):
    min_lim = limits[0]
    max_lim = limits[1]
    max_vy = start - max_lim - 1
    return int(max_vy * (max_vy+1)/2)

print(getMaxY(0, range_y))