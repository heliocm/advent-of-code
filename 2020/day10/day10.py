target_input = open("input.txt" , "r")
list_of_numbers = target_input.read().split("\n")
del list_of_numbers[-1]
adapters = [0]
for each in list_of_numbers:
    adapters.append(int(each))

adapters.sort()
adapters.append(adapters[-1] + 3)
print(adapters)
distance_by_one = 0
distance_by_three = 0
for index in range(len(adapters)):
    if index != 0:
        difference = adapters[index] - adapters[index - 1]
        if difference == 1:
            distance_by_one = distance_by_one + 1
        #elif difference == 2:
            
        elif difference == 3:
            distance_by_three = distance_by_three + 1

print((distance_by_one) * (distance_by_three))  
