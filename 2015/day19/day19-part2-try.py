import time
start_time = time.time()
target_input = open("input-test.txt" , "r")
data = target_input.read().split("\n")
del data[-1]

molecule = data[-1]
del data[-1]
del data[-1]

fabrication = ['e']
steps = 0
while molecule not in fabrication:
    steps += 1
    print(steps)
    print("--- %s seconds ---" % (time.time() - start_time))
    different_formulas = []
    for formula in fabrication:
        for each in data:
            each = each.split(" ")
            if each[0] in formula:
                for i in range(0, formula.count(each[0])):
                    if i == 0 :
                        last_seen = formula.find(each[0])
                        aux = formula.replace(each[0], each[-1], 1)
                    else:
                        sufix = formula[last_seen + len(each[0]):].replace(each[0], each[-1], 1)
                        aux = formula[:last_seen + len(each[0])] + sufix
                        last_seen = last_seen + len(each[0]) + formula[last_seen+len(each[0]):].find(each[0])
                    if aux not in different_formulas:
                        different_formulas.append(aux)
    fabrication.clear()
    for each in different_formulas:
        fabrication.append(each)

print(steps)