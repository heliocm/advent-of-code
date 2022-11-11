target_input = open("input.txt" , "r")
data = target_input.read().split("\n")
del data[-1]

def decode_instructions(starting_point, instruction):
    for each in instruction:
        if each == 'L':
            if starting_point not in [1, 4, 7]:
                starting_point = starting_point - 1
            else: pass
        elif each == 'R':
            if starting_point not in [3, 6, 9]:
                starting_point = starting_point + 1
            else: pass
        elif each == 'U':
            if starting_point not in [1, 2, 3]:
                starting_point = starting_point - 3
            else: pass
        else:
            if starting_point not in [7, 8, 9]:
                starting_point = starting_point + 3
            else: pass
    return starting_point

code = ""
starting_point = 5
for each in data:
    code += str(decode_instructions(starting_point, each))

print(code)


