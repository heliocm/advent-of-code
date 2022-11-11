target_input = open("input-test2.txt" , "r")
data = target_input.read().split("\n")
del data[-1]

dots = {tuple(int(number) for number in each.split(',')) for each in data[:data.index('')]}
instructions = [tuple(each.replace('fold along ', '').split('=')) for each in data[data.index('')+1:]]
def transformDot(dot, instruction):
    if instruction[0] == 'x':
        if dot[0] > int(instruction[1]):
            return (int(instruction[1])*2 - dot[0], dot[1])
        else:
            return(dot[0], dot[1])
    else:
        if dot[1] > int(instruction[1]):
            return (dot[0], int(instruction[1])*2 - dot[1])
        else:
            return(dot[0], dot[1])

for instruction in instructions:
    new_dots = set()
    for each in dots:
        new_dots.add(transformDot(each, instruction))
    dots = new_dots

maxX = 0
maxY = 0
for each in dots:
    maxX = each[0] if each[0] > maxX else maxX
    maxY = each[1] if each[1] > maxY else maxY

for y in range(maxY + 1):
    line = ''
    for x in range(maxX + 1):
        if (x,y) in dots:
            line += '#'
        else:
            line += '.'
    print(line)