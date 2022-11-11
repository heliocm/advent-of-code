target_input = open("input.txt" , "r")
rules = target_input.read().split("\n")
del rules[-1]

next_bags = [['shiny gold',1]]
result = 0
while len(next_bags) > 0:
    for color in next_bags:
        for rule in rules:
            rule = rule.split(" bags contain ")
            if rule[0].find(color[0]) != -1:
                containers = rule[1].split(", ")
                for container in containers:
                    container = container.split(" ")
                    if container[0].isnumeric():
                        result = result + int(container[0]) * int(color[1])
                        next_bags.append([container[1] + ' ' + container[2], int(container[0]) * int(color[1])])

        next_bags.remove(color)

print(result)


