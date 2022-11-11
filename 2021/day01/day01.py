target_input = open("input.txt" , "r")
data = target_input.read().split("\n")
del data[-1]

result = 0
for each in data:
    if int(each) == int(data[0]):
        previous = int(each)
    else:
        if int(each) > previous:
            result += 1
        previous = int(each)
    print(result)

print(result)