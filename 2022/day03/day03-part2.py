import string
target_input = open("input.txt" , "r")
data = target_input.read().split("\n")
del data[-1]

alphabet = string.ascii_lowercase+string.ascii_uppercase

answer = 0
turn = 0
rucksack = []
for each in data:
    rucksack.append(each)
    if len(rucksack) == 3:
        answer += alphabet.index(''.join(set(rucksack[0]).intersection(rucksack[1]).intersection(rucksack[2]))) + 1
        rucksack.clear()

print(answer)