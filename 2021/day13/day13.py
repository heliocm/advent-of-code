target_input = open("input.txt" , "r")
data = target_input.read().split("\n")
del data[-1]

dots = {tuple(int(number) for number in each.split(',')) for each in data[:data.index('')]}
instructions = [tuple(each.replace('fold along ', '').split('=')) for each in data[data.index('')+1:]]
def transformDot(dot, instruction):
    if instruction[0] == 'x':
        if dot[0] < int(instruction[1]):
            return (int(instruction[1])*2 - dot[0], dot[1])
        else:
            return(dot[0], dot[1])
    else:
        if dot[1] > int(instruction[1]):
            return (dot[0], int(instruction[1])*2 - dot[1])
        else:
            return(dot[0], dot[1])

new_dots = set()
for each in dots:
    new_dots.add(transformDot(each, instructions[0]))
print(len(new_dots))