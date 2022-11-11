target_input = open("input.txt" , "r")
data = target_input.read().split("\n")
del data[-1]

def binaryToDecimal(binary):
    binary1 = binary
    decimal, i, n = 0, 0, 0
    while(binary != 0):
        dec = binary % 10
        decimal = decimal + dec * pow(2, i)
        binary = binary//10
        i += 1
    return decimal

def compareResults(zeros, ones):
    if zeros > ones:
        return 0
    return 1

def invert(result):
    if result == 0:
        return 1
    return 0

oxygenBinary = data

position = 0
while len(oxygenBinary) != 1:
    zeros = 0
    ones = 0
    for each in oxygenBinary:
        if each[position] == '0':
            zeros += 1
        elif each[position] == '1':
            ones += 1
    newArray = []
    result = compareResults(zeros, ones)
    for each in oxygenBinary:
        if int(each[position]) == result:
            newArray.append(each)
    oxygenBinary = newArray
    position += 1

co2Binary = data

position = 0
while len(co2Binary) != 1:
    zeros = 0
    ones = 0
    for each in co2Binary:
        if each[position] == '0':
            zeros += 1
        elif each[position] == '1':
            ones += 1
    newArray = []
    result = invert(compareResults(zeros, ones))
    for each in co2Binary:
        if int(each[position]) == result:
            newArray.append(each)
    co2Binary = newArray
    position += 1

print(binaryToDecimal(int(oxygenBinary[0]))*binaryToDecimal(int(co2Binary[0])))