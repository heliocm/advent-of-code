target_input = open("input.txt" , "r")
data = target_input.read().split("\n")
del data[-1]
print(data)
inputs = []
outputs = []
for each in data:
    each = each.split(" ")
    inp = [each[i] for i in range(0, each.index("|"))]
    out = [each[i] for i in range(each.index("|") + 1, len(each))]
    inputs.append(inp)
    outputs.append(out)
count = 0
for each in outputs:
    for number in each:
        if len(number) in [2, 3, 4, 7]:
            count += 1
print(count)