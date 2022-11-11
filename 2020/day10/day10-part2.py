import numpy as np
target_input = open("input.txt" , "r")
list_of_numbers = target_input.read().split("\n")
del list_of_numbers[-1]
adapters = [0]
for each in list_of_numbers:
    adapters.append(int(each))

adapters.sort()
adapters.append(adapters[-1] + 3)
possibilities = 1
essentials = [0]
for each in adapters:
    if (adapters.index(each) > 0) and (adapters.index(each) < len(adapters) - 1) and (adapters[adapters.index(each) + 1] - adapters[adapters.index(each) - 1] > 3):
        essentials.append(each)

essentials.append(adapters[-1])
optionals = np.setdiff1d(adapters, essentials)

for each in essentials:
    counter = 0
    if each != essentials[-1]:
        next_essential = essentials[essentials.index(each) + 1]
        for number in optionals:
            if number > each and number < next_essential:
                counter = counter + 1
            
        if next_essential - each > 3 :
            possibilities = possibilities * ((2 ** counter) - 1)
        else:
            if counter != 0:
                possibilities = possibilities * (2**counter)

print(possibilities)
