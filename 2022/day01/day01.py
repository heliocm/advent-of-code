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
answer = 0
for elf in elfs:
    if sum(elf) > answer:
        answer = sum(elf)

print(answer)