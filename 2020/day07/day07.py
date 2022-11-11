target_input = open("input.txt" , "r")
rules = target_input.read().split("\n")
del rules[-1]

wanted_bag = ['shiny gold']
all_possible_containers = []
while len(wanted_bag) > 0:
    for color in wanted_bag:
        for rule in rules:
            rule = rule.split(" bags contain ")
            if rule[1].find(color) != -1:
                wanted_bag.append(rule[0])
                all_possible_containers.append(rule[0])
        wanted_bag.remove(color)

print(len(set(all_possible_containers)))


