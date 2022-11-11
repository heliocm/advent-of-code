target_input = open("input.txt" , "r")
data = target_input.read().split("\n")
del data[-1]

subject = 7
magic = 20201227
private_keys = []
for goal in data:
    value = 1
    goal = int(goal)
    counter = 0
    while value != goal:
        value = value * subject
        value = value % magic
        counter += 1
    private_keys.append(counter)

encryption = []
for i in range(len(data)):
    value = 1
    subject = int(data[i])
    counter = 0
    while counter != private_keys[1-i]:
        value = value * subject
        value = value % magic
        counter += 1
    encryption.append(value)

if encryption[0] == encryption[1]:
    print(encryption)