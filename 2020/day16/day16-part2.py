target_input = open("input.txt" , "r")
document = target_input.read().split("\n\n")
def intersection(lst1, lst2): 
    lst3 = [value for value in lst1 if value in lst2] 
    return lst3 

rules = document[0].split("\n")
my_ticket = document[1].split(":\n")
my_ticket = my_ticket[1].split(",")
nearby_tickets = document[2].split(":\n")
ticket_numbers = nearby_tickets[1].split("\n")
del ticket_numbers[-1]
total = 0
line_number = 0
tickets_to_remove = []
for line in ticket_numbers:
    valid_line = True
    line = line.split(",")
    for each in line:
        valid_value = False
        rule_number = 0
        for rule in rules:    
            rule = rule.split(": ")
            values = rule[1].split(" or ")
            min_range = values[0]
            max_range = values[1]
            min_range = min_range.split("-")
            max_range = max_range.split("-")
            if int(each) >= int(min_range[0]) and int(each) <= int(min_range[1]):
                valid_value = True
            if int(each) >= int(max_range[0]) and int(each) <= int(max_range[1]):
                valid_value = True
        if not valid_value:
            valid_line = False
    if not valid_line:
        tickets_to_remove.append(line_number)
    line_number = line_number + 1

tickets_to_remove.sort()
for each in reversed(tickets_to_remove):
    ticket_numbers.remove(ticket_numbers[each])

rule_order = []
for j in range(0, len(ticket_numbers[0].split(","))):
    column_rules = []
    rule_number = 0
    for rule in rules:
        column_rules.append(rule_number)
        rule_number = rule_number + 1
    for i in range(0, len(ticket_numbers)):
        possible_rules = []
        rule_number = 0
        check = ticket_numbers[i].split(",")
        rule_number = 0
        for rule in rules:    
            rule = rule.split(": ")
            values = rule[1].split(" or ")
            min_range = values[0]
            max_range = values[1]
            min_range = min_range.split("-")
            max_range = max_range.split("-")
            
            if int(check[j]) >= int(min_range[0]) and int(check[j]) <= int(min_range[1]):
                possible_rules.append(rule_number)
            if int(check[j]) >= int(max_range[0]) and int(check[j]) <= int(max_range[1]):
                possible_rules.append(rule_number)
            rule_number = rule_number + 1
        intersection_list = intersection(possible_rules,column_rules)
        if len(column_rules) > len(intersection_list): 
            column_rules = []
            column_rules = intersection_list.copy()

    rule_order.append(column_rules)
reconstruction = []
for i in range(0, len(rule_order)):
    reconstruction.append(len(rule_order[i]) - 1)
rule_order.sort()
rule_order.reverse()
definitive = []
for i in range(0, len(rule_order)):
    for each in rule_order[i]:
        if each not in definitive:
            definitive.append(each)
total = 1
final = []
for each in reconstruction:
    final.append(definitive[each])

for i in range(0,6):
    total = total * int(my_ticket[final.index(i)])

print(total)