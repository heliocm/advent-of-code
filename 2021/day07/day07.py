target_input = open("input.txt" , "r")
data = target_input.read().split("\n")
del data[-1]
crabs = [int(number) for number in data[0].split(",")]

result = 100000000000000
possible = [i for i in range(min(crabs), max(crabs))]

for each in possible:
    turn = 0
    for crab in crabs:
        turn += abs(crab - each)
    if turn < result:
        result = turn

print(result)

