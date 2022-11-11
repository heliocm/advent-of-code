from itertools import combinations

target_input = open("input.txt" , "r")
data = target_input.read().split("\n")
del data[-1]

numbers = []
for number in data:
    numbers.append(int(number))
subsets = []
for i in range(1, len(numbers)+1):
    for each in list(combinations(numbers, i)):
        subsets.append(each)
result = 0
count_containers = len(numbers)
for each in subsets:
    if sum(each) == 150:
        if len(each) < count_containers:
            count_containers = len(each)
            result = 1
        elif len(each) == count_containers:
            result += 1

print(result)