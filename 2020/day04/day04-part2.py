target_input = open("input.txt" , "r")
data = target_input.read().split("\n\n")
valid = 0
required_fields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
eye_colors = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
possible_characters = list("abcdef0123456789")
only_numbers = list("0123456789")
for entry in data:
    passport_is_ok = True
    number_of_fields = 0
    entry = entry.replace("\n", " ")
    for field in required_fields:
        if entry.count(field) == 1:
            number_of_fields = number_of_fields + 1

    entry = entry.split(" ")
    if number_of_fields == 7:
        for entry_field in entry:
            for field in required_fields:
                if entry_field.count(field) == 1:
                    if field == "byr":
                        if len(entry_field[4:]) != 4 or int(entry_field[4:]) < 1920 or int(entry_field[4:]) > 2002 :
                            passport_is_ok = False
                    elif field == "iyr":
                        if len(entry_field[4:]) != 4 or int(entry_field[4:]) < 2010 or int(entry_field[4:]) > 2020 :
                                passport_is_ok = False
                    elif field == "eyr":
                        if len(entry_field[4:]) != 4 or int(entry_field[4:]) < 2020 or int(entry_field[4:]) > 2030 :
                                    passport_is_ok = False
                    elif field == "hgt":
                        if entry_field[-2:] == "cm":
                            if int(entry_field[4:-2]) < 150 or int(entry_field[4:-2]) >193:
                                passport_is_ok = False
                        elif entry_field[-2:] == "in":
                            if int(entry_field[4:-2]) < 59 or int(entry_field[4:-2]) >76:
                                passport_is_ok = False
                        else:
                            passport_is_ok = False
                    elif field == "hcl":
                        if len(entry_field[4:]) != 7 or entry_field[4:-6] != "#" or all(item in possible_characters for item in list(entry_field[-6:])) != True:
                            passport_is_ok = False
                    elif field == "ecl":
                        if entry_field[4:] not in eye_colors:
                            passport_is_ok = False
                    elif field == "pid":
                        if len(entry_field[4:]) != 9 or all(item in only_numbers for item in list(entry_field[4:])) != True:
                            passport_is_ok = False
    
    
                
    if number_of_fields == 7 and passport_is_ok == True:
        valid = valid + 1

print(valid)


#print(data)