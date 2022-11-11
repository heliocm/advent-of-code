target_input = open("input-test.txt" , "r")
data = target_input.read().split("\n\n")
rules = data[0].split("\n")
messages = data[1].split("\n")
del messages[-1]
messages = set(messages)

rules_book = {}
for rule in rules:
    rules_book[rule[:rule.index(":")]] = set()
    if not rule[rule.index(":")+2:].find(" | ") == -1:
        rules_book[rule[:rule.index(":")]].add(rule[rule.index(":")+2:][:rule[rule.index(":")+2:].index("|")-1])
        rules_book[rule[:rule.index(":")]].add(rule[rule.index(":")+2:][rule[rule.index(":")+2:].index("|")+2:])
    else:
        if rule[rule.index(":")+2:] == '"a"' or rule[rule.index(":")+2:] == '"b"':
            rules_book[rule[:rule.index(":")]].add(rule[rule.index(":")+2:][1:-1])
        else:
            rules_book[rule[:rule.index(":")]].add(rule[rule.index(":")+2:])
finished = False
print(rules_book)
print(messages)

