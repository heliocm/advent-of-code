def getUniques (combination):
    uniques = {}
    for each in combination:
        if len(each) == 2:
            uniques['1'] = each
        elif len(each) == 3:
            uniques['7'] = each
        elif len(each) == 4:
            uniques['4'] = each
        elif len(each) == 7:
            uniques['8'] = each
    return uniques
# 1, 7, 4 e 8 são unicos. Tem 2, 3, 4 e 7 respectivamente
# 9 tem comprimento 6 e contem o 4 e ou contem o 1
# 0 tem comprimento 6 mas nao contem o 4 e contem o 1
# 6 tem comprimento 6 mas nao contem o 4 e nao contem o 1
# 3 tem comprimento 5 e contem o 1
# 5 tem comprimento 5 e tem intersecao de 3 com o 4
# 2 tem comprimento 5 e tem intersecao de 2 com o 4
def identifyNumbers(numberset, uniques):
    for each in uniques:
        if numberset == uniques[each]:
            return each
    if len(numberset) == 6:
        if len(numberset.intersection(uniques['1'])) == 2 and len(numberset.intersection(uniques['4'])) == 3 and len(numberset.intersection(uniques['7'])) == 3:
            return '0'
        if len(numberset.intersection(uniques['1'])) == 1 and len(numberset.intersection(uniques['4'])) == 3 and len(numberset.intersection(uniques['7'])) == 2:
            return '6'
        if len(numberset.intersection(uniques['1'])) == 2 and len(numberset.intersection(uniques['4'])) == 4 and len(numberset.intersection(uniques['7'])) == 3:
            return '9'
    elif len(numberset) == 5:
        if len(numberset.intersection(uniques['1'])) == 1 and len(numberset.intersection(uniques['4'])) == 2 and len(numberset.intersection(uniques['7'])) == 2:
            return '2'
        if len(numberset.intersection(uniques['1'])) == 2 and len(numberset.intersection(uniques['4'])) == 3 and len(numberset.intersection(uniques['7'])) == 3:
            return '3'
        if len(numberset.intersection(uniques['1'])) == 1 and len(numberset.intersection(uniques['4'])) == 3 and len(numberset.intersection(uniques['7'])) == 2:
            return '5'
        
        


target_input = open("input.txt" , "r")
data = target_input.read().split("\n")
del data[-1]

inputs = []
outputs = []
for each in data:
    each = each.split(" ")
    inp = [set(each[i]) for i in range(0, each.index("|"))]
    out = [set(each[i]) for i in range(each.index("|") + 1, len(each))]
    inputs.append(inp)
    outputs.append(out)

answer = 0
for i in range(len(inputs)):
    uniques = getUniques(inputs[i])
    for numberset in inputs[i]:
        number = identifyNumbers(numberset, uniques)
        if number not in uniques:
            uniques[number] = numberset
    number = ''
    for numberset in outputs[i]:
        number += identifyNumbers(numberset, uniques)
    answer += int(number)

print(answer)

# for each in outputs:

