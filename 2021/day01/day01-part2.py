target_input = open("input.txt" , "r")
data = target_input.read().split("\n")
del data[-1]

result = 0
last_three = []
for each in data:
    last_three.append(int(each))
    if len(last_three) == 3:
        previous = sum(last_three)
    if len(last_three) == 4:
        del(last_three[0])
        actual = sum(last_three)
        if actual > previous:
            result += 1
        previous = actual

print(result)