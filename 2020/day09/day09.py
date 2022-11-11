target_input = open("input.txt" , "r")
list_of_numbers = target_input.read().split("\n")
del list_of_numbers[-1]

possible_values = []
result = 0
for i in range(25,len(list_of_numbers)):
    for k in range(i-25, i):
        for t in range(i-25, i):
            possible_values.append(int(list_of_numbers[k]) + int(list_of_numbers[t]))
    
    if possible_values.count(int(list_of_numbers[i])) == 0:
        result = int(list_of_numbers[i])

    possible_values = []

print(result)