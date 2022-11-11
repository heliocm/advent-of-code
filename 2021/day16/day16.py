target_input = open("input.txt" , "r")
data = target_input.read().split("\n")
del data[-1]

package = data[0]

converter = {
    '0' : '0000',
    '1' : '0001',
    '2' : '0010',
    '3' : '0011',
    '4' : '0100',
    '5' : '0101',
    '6' : '0110',
    '7' : '0111',
    '8' : '1000',
    '9' : '1001',
    'A' : '1010',
    'B' : '1011',
    'C' : '1100',
    'D' : '1101',
    'E' : '1110',
    'F' : '1111'
}

def hex2bin (hexa):
    binary = ''
    for char in hexa:
        binary += converter[char]
    return binary

def bin2int (binary):
    return int(binary, 2)

def getVersion(binary):
    return bin2int(binary[:3])

def getType(binary):
    if bin2int(binary[3:6]) == 4:
        return 'literal'
    return 'operator'

def parsePackage(binary):
    header = binary[:6]
    content = binary[6:]
    return header, content


def getLiteral(content):
    literal = ''
    if content[:5][0] == '1':
        literal += content[1:5] + getLiteral(content[5:])[0]
        position = 5 + getLiteral(content[5:])[1]
    else:
        literal += content[1:5]
        position = 6 + 5
    return literal, position

def getOperator(content):
    position = 6
    type_ID = 15 if int(content[0]) == 0 else 11
    position += 1
    if type_ID == 15:
        length = bin2int(content[1:16])
        position += 15 + length
        packages = content[16:16+length]
        return packages, position, 1
    else:
        number_of_packets = bin2int(content[1:12])
        packages = content[12:]
        position += 11 + len(content[12:])
        return packages, position, number_of_packets

print(hex2bin(package))
print(len(hex2bin(package)))
header, content = parsePackage(hex2bin(package))
print(getOperator(content))

def unpack(binary):
    answer = 0
    header, content = parsePackage(binary)
    answer += getVersion(header)
    print(getVersion(header))
    if getType(header) == 'operator':
        print(getOperator(content))
        packages, position, number_of_packets = getOperator(content)
        if position < len(binary) and '1' in binary[position:]:
            answer += unpack(packages)
            answer += unpack(binary[position:])
        else:
            answer += unpack(packages)
    else:
        print(getLiteral(content))
        literal, position = getLiteral(content)
        if position < len(binary) and '1' in binary[position:]:
            answer += unpack(binary[position:])
    return answer

print(unpack(hex2bin(package)))
    
    
