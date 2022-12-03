target_input = open("input.txt" , "r")
data = target_input.read().split("\n")
del data[-1]

elfs = []
elf = []
for each in data:
    if each != '':
        elf.append(int(each))
    else:
        elfs.append(elf)
        elf = []

top_calories = []
for elf in elfs:
    if len(top_calories) < 3:
        top_calories.append(sum(elf))
    else:
        top_calories.sort(reverse=True)
        if sum(elf) > top_calories[-1]:
            top_calories.pop(-1)
            top_calories.append(sum(elf))

answer = sum(top_calories)
print(answer)