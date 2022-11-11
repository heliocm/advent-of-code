target_input = open("input.txt" , "r")
data = target_input.read().split("\n\n")
#del data[-1]
valid = 0
required_fields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
for entry in data:
    number_of_fields = 0
    entry = entry.replace("\n", " ")
    for field in required_fields:
        if entry.count(field) == 1:
            number_of_fields = number_of_fields + 1
    if number_of_fields == 7:
        valid = valid + 1

print(valid)


#print(data)