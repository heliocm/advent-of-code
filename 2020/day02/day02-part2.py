target_input = open("input.txt" , "r")
data = target_input.read().split("\n")
del data[-1]

#print(data)
valid_pass = 0

for line in data:
    repetitions = 0
    check = line.split()
    lower_limit = int(check[0].split('-')[0])
    higher_limit = int(check[0].split('-')[1])
    letter = check[1].replace(':','')
    password = check[-1]

    if password[lower_limit-1] == letter:
        repetitions = repetitions + 1
    if password[higher_limit-1] == letter:
        repetitions = repetitions + 1
    
    if repetitions == 1:
        valid_pass = valid_pass + 1

print(valid_pass)
