target_input = open("input.txt" , "r")
list_of_numbers = target_input.read().split("\n")
del list_of_numbers[-1]

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
my_sum = 0
for i in range(517, 534):
    my_sum = my_sum + int(list_of_numbers[i])


index = 0
contiguous_sum = 0
counter = 0
numbers_to_sum = []
while contiguous_sum != result:
    contiguous_sum = contiguous_sum + int(list_of_numbers[index + counter])
    if contiguous_sum == result:
        for each in range(index, index + counter):
            numbers_to_sum.append(int(list_of_numbers[each]))
        numbers_to_sum.sort()
        print(numbers_to_sum[0])
        print(numbers_to_sum[-1])
        print(numbers_to_sum[0] + numbers_to_sum[-1])
        break
    if contiguous_sum > result:
        index = index + 1
        counter = 0
        contiguous_sum = 0
    else:
        counter = counter + 1

        