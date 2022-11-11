target_input = open("input.txt" , "r")
document = target_input.read().split("\n\n")
# del document[-1]

rules = document[0].split("\n")
my_ticket = document[1]
nearby_tickets = document[2].split(":\n")
# nearby_tickets = nearby_tickets[1].split["\n"]
ticket_numbers = nearby_tickets[1].split("\n")
del ticket_numbers[-1]
total = 0

for line in ticket_numbers:
    line = line.split(",")
    for each in line:
        valid_ticket = False
        for rule in rules:    
            rule = rule.split(": ")
            values = rule[1].split(" or ")
            min_range = values[0]
            max_range = values[1]
            min_range = min_range.split("-")
            max_range = max_range.split("-")
            if int(each) >= int(min_range[0]) and int(each) <= int(min_range[1]):
                valid_ticket = True
            if int(each) >= int(max_range[0]) and int(each) <= int(max_range[1]):
                valid_ticket = True
        if not valid_ticket:
            total = total + int(each)

print(total)
