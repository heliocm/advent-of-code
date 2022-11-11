import string
target_input = open("input.txt" , "r")
data = target_input.read().split("\n")
del data[-1]

def getRules(data):
    rules = {}
    for each in data[2:]:
        each = each.split(' -> ')
        rules[each[0]] = each[1]
    return rules

def getTemplate(data):
    template = {}
    for i in range(len(data[0])-1):
        if data[0][i:i+2] not in template:
            template[data[0][i:i+2]] = 1
        else:
            template[data[0][i:i+2]] += 1
    template['last'] = data[0][-2:]
    return template

def countElement(element, polymer):
    count = 0
    for each in polymer:
        if element == each[0]:
            count += polymer[each]
    if element == polymer['last'][1]:
        count += 1
    return count

def getNewPairs(piece, rules):
    if piece in rules:
        return [ piece[0]+rules[piece], rules[piece]+piece[-1] ]
    else:
        return None

def polymerization(polymer, rules):
    new_polymer = {}
    for each in polymer:
        if getNewPairs(each, rules) is not None:
            if each == polymer['last']:
                new_polymer['last'] = getNewPairs(each, rules)[1]
            for pair in getNewPairs(each, rules):
                if pair not in new_polymer:
                    new_polymer[pair] = polymer[each]
                else:
                    new_polymer[pair] += polymer[each]
    return new_polymer


template = getTemplate(data)
rules = getRules(data)

steps = 0
polymer = template
while steps != 40:
    polymer = polymerization(polymer, rules)
    steps += 1
print(polymer)
max_ = 0
min_ = 0
for each in string.ascii_uppercase:
    if countElement(each, polymer) != 0:
        if countElement(each, polymer) > max_:
            max_ = countElement(each, polymer)
        if min_ == 0:
            min_ = countElement(each, polymer)
        elif countElement(each, polymer) < min_:
            min_ = countElement(each, polymer)
print(max_ - min_)