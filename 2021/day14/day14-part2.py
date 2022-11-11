import string
target_input = open("input-test.txt" , "r")
data = target_input.read().split("\n")
del data[-1]

def getRules(data):
    rules = {}
    for each in data[2:]:
        each = each.split(' -> ')
        rules[each[0]] = each[1]
    return rules

def addElement(element, position, polymer):
    return polymer[:position+1] + element + polymer[position+1:]

def polymerization(polymer, rules):
    added = 0
    new_polymer = polymer
    for i in range(len(polymer)-1):
        if polymer[i:i+2] in rules:
            new_polymer = addElement(rules[polymer[i:i+2]], i+added, new_polymer)
            added += 1
    return new_polymer

template = data[0]
rules = getRules(data)
steps = 0
polymer = template
while steps != 40:
    polymer = polymerization(polymer, rules)
    steps += 1

max_ = 0
min_ = 10000
for each in string.ascii_uppercase:
    if each in polymer:
        if polymer.count(each) > max_:
            max_ = polymer.count(each)
        if polymer.count(each) < min_:
            min_ = polymer.count(each)
        
print(max_ - min_)