import time
start_time = time.time()
target_input = open("input.txt" , "r")
data = target_input.read().split("\n")
del data[-1]

molecule = data[-1]
del data[-1]
del data[-1]
#Ar, Rn, Y

def minimize(formula, data, steps):
    different_molecules = []
    mudou = True
    while mudou:
        mudou = False
        for each in data:
            each = each.split(" ")
            if each[-1] in formula:
                formula = formula.replace(each[-1], each[0], 1)
                steps += 1
                mudou = True
    return formula , steps
# print(minimize('CaSiThCaPBCaSi', data, 0))
def crop(formula):
    new = formula[:find_next(formula)]
    return new

def find_next(formula):
    search = ['Rn', 'Y', 'Ar']
    position = []
    for each in search:
        if formula.find(each) > 0:
            position.append(formula.find(each))
        else:
            position.append(1000)
    return formula.find(search[position.index(min(position))]) + len(search[position.index(min(position))])
index = 0
steps = 0
minimized = ''
# print(crop(molecule[index:]))
# print(minimize(crop(molecule[index:]), data, steps))
# index = find_next(molecule[index:])
# print(index)
# print(molecule[index:])
gone = 0
while index + gone < len(molecule):
    stage, steps = minimize(crop(molecule[index+gone:]), data, steps)
    minimized += stage
    gone += index
    index = find_next(molecule[gone:])

print(steps)
print(minimized)
print(len(minimized))

# final_stage = ''
# countRN = 0
# countAR = 0
# while minimized.find('Rn') > 0:
#     index = 0
#     while countRN != countAR or countRN == 0:
#         if minimized[index:].find('Rn') < minimized[index:].find('Ar'):
#             countRN += 1
#             index += minimized[index:].find('Rn') + 2
#         else:
#             countAR += 1
#             index += minimized[index:].find('Ar') + 2
#             if countRN == countAR and countRN != 0:
#                 stage, steps = minimize(minimized[:minimized[index:].find('Ar')+2], data, steps)
#                 final_stage += stage
#                 minimized = minimized[minimized[index:].find('Ar')+2:]
#                 print(minimized)
# print(final_stage)
while minimized != 'e':
    mudou = False
    for each in data:
        each = each.split(" ")
        if each[-1] in minimized and 'Rn' in each[-1]:
            minimized = minimized.replace(each[-1],each[0],1)
            steps += 1
            mudou = True
    if mudou == False:
        print(minimized)
        print(steps)
        index = 0
        final_stage = ''
        gone = 0
        while index + gone < len(minimized):
            stage, steps = minimize(crop(minimized[index+gone:]), data, steps)
            final_stage += stage
            gone += index
            index = find_next(minimized[gone:])
        minimized = (final_stage + '.')[:-1]

print(minimized)
print(steps)
CRnSiRnFYCaRnFArArFArAl - 190
CRnSiRnFYSiThRnFArArFArAl - 189
CRnSiRnFYSiAlArFArAl - 190
CRnSiRnFYFArFArAl - 191
CRnCaFArAl - 192
CRnFArAl - 193
NAl - 194
e - 195

