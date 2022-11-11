target_input = open("input.txt" , "r")
data = target_input.read().split("\n")
del data[-1]

evidence = {
    'children': 3,
    'cats': 7,
    'samoyeds': 2,
    'pomeranians': 3,
    'akitas': 0,
    'vizslas': 0,
    'goldfish': 5,
    'trees': 3,
    'cars': 2,
    'perfumes': 1
}

# dicionario = {}
# chave = "bla"
# valor = "ble"
# dicionario.update({chave : valor})
sues = {}
for line in data:
    line = line.split(" ")
    for word in line:
        sues.update({
            line[1][:-1]: {
                line[2][:-1]: int(line[3][:-1]),
                line[4][:-1]: int(line[5][:-1]),
                line[6][:-1]: int(line[7])
            }
        })
possible_sues = []
for number, feature in sues.items():
    is_this_my_aunt = True
    for key, value in evidence.items():
        if key in feature:
            if key == 'cats' or key == 'trees':
                is_this_my_aunt = False if feature[key] <= value else is_this_my_aunt
            elif key == 'pomeranians' or key == 'goldfish':
                is_this_my_aunt = False if feature[key] >= value else is_this_my_aunt
            else:
                is_this_my_aunt = False if feature[key] != value else is_this_my_aunt
    
    if is_this_my_aunt:
        possible_sues.append(number)

print(possible_sues)
