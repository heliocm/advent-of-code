target_input = open("input.txt" , "r")
data = target_input.read().split("\n")
del data[-1]

molecule = data[-1]
del data[-1]
del data[-1]

different_molecules = []
for each in data:
    each = each.split(" ")
    if each[0] in molecule:
        for i in range(0, molecule.count(each[0])):
            if i == 0 :
                last_seen = molecule.find(each[0])
                aux = molecule.replace(each[0], each[-1], 1)
            else:
                sufix = molecule[last_seen + len(each[0]):].replace(each[0], each[-1], 1)
                aux = molecule[:last_seen + len(each[0])] + sufix
                last_seen = last_seen + len(each[0]) + molecule[last_seen+len(each[0]):].find(each[0])
            if aux not in different_molecules:
                different_molecules.append(aux)

print(len(different_molecules))