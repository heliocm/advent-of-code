target_input = open("input.txt" , "r")
data = target_input.read().split("\n")
del data[-1]

def getInstructions(line):
    limits = []
    partial = line.split(' ')
    instruction = partial[0]
    content = partial[1]
    limits.append([int(each) for each in content[content.index('x')+2:content.index('y')-1].split('..')])
    limits.append([int(each) for each in content[content.index('y')+2:content.index('z')-1].split('..')])
    limits.append([int(each) for each in content[content.index('z')+2:].split('..')])

    return instruction, limits

on = set()
for each in data:
    outOfLimit = False
    instruction, limits = getInstructions(each)
    for limit in limits:
        for number in limit:
            if -50 <= number <= 50:
                pass
            else:
                outOfLimit = True
    if outOfLimit:
        pass
    else:
        print(limits)
        for x in range(limits[0][0], limits[0][1]+1):
            for y in range(limits[1][0], limits[1][1]+1):
                for z in range(limits[2][0], limits[2][1]+1):
                    if instruction == 'on':
                        if (x,y,z) not in on:
                            on.add((x,y,z))
                    else:
                        if (x,y,z) in on:
                            on.remove((x,y,z))

print(len(on))