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
    result = ""
    for i in range(0, len(zeros)):
        if zeros[i] > ones[i]:
            result += '0'
        else:
            result += '1'
    return int(result)

countZeros = []
countOnes = []

for each in data:
    if countZeros == [] and countOnes == []:
        for i in range(0,len(each)):
            countZeros.append(0)
            countOnes.append(0)
    position = 0
    for number in each:
        if number == '0':
            countZeros[position] += 1
        elif number == '1':
            countOnes[position] += 1
        position += 1

gamma = compareResults(countZeros, countOnes)
epsilon = compareResults(countOnes, countZeros)
print(binaryToDecimal(gamma)*binaryToDecimal(epsilon))