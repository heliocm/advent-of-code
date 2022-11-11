target_input = open("input.txt" , "r")
data = target_input.read().split("\n")
del data[-1]

area_instruction = data[0]
range_x = ''
for i in range(area_instruction.index('=')+1, area_instruction.index(',')):
    if area_instruction[i] == '.':
        range_x += ' '
    else:
        range_x += area_instruction[i]
range_x = range_x.split('  ')
range_x = [int(each) for each in range_x]
range_y = ''
for i in range(area_instruction.index('y=')+2, len(area_instruction)):
    if area_instruction[i] == '.':
        range_y += ' '
    else:
        range_y += area_instruction[i]
range_y = range_y.split('  ')
range_y = [int(each) for each in range_y]
range_y.reverse()

def takeStepsX(vx, steps):
    position = 0
    for i in range(steps):
        position += vx
        if vx > 0:
            vx -= 1
        elif vx < 0:
            vx += 1
        else:
            vx = 0
    return position
    
def getStepsY(vy):
    min_lim = range_y[0]
    max_lim = range_y[1]
    position = 0
    step = 0
    steps = []
    while position + vy >= max_lim:
        position += vy
        vy -= 1
        step += 1
        if max_lim <= position <= min_lim:
            steps.append(step)
    return steps

def getValidInitials():
    initials = []
    y_max_lim = range_y[1]
    x_min_lim = range_x[0]
    x_max_lim = range_x[1]
    for vy in range(y_max_lim, abs(y_max_lim)):
        steps = getStepsY(vy)
        for vx in range(x_max_lim+1):
            for each in steps:
                if x_min_lim <= takeStepsX(vx, each) <= x_max_lim:
                    initials.append((vx, vy))
    return set(initials)
print(len(getValidInitials()))
