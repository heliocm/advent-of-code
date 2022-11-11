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
    return bin2int(binary[3:6])

def parsePackage(binary):
    header = binary[:6]
    content = binary[6:]
    return header, content

def getLiteral(content):
    literal = ''
    if content[:5][0] == '1':
        literal += content[1:5] + getLiteral(content[5:])
    else:
        literal += content[1:5]
    return literal

def getOperator(content):
    length_type_ID = 15 if content[0] == '0' else 11
    subpackets = []
    values = []
    if length_type_ID == 15:
        length = bin2int(content[1:16])
        to_search = content[16:]
        while length > 0:
            packet, content_left = findPackets(to_search)
            length -= len(packet)
            to_search = content_left
            subpackets.append(packet)
    else:
        number_of_packets = bin2int(content[1:12])
        to_search = content[12:]
        for i in range(number_of_packets):
            packet, content_left = findPackets(to_search)
            to_search = content_left
            subpackets.append(packet)
    for each in subpackets:
        values.append(solvePacket(each))
    return values

def findPackets(to_search):
    header, content = parsePackage(to_search)
    length = 6
    type_ID = getType(header)
    if type_ID == 4:
        content_left = content
        while content_left[0] == '1':
            length += 5
            content_left = content_left[5:]
        length += 5
        return to_search[:length], to_search[length:]
    else:
        length_type_ID = 15 if content[0] == '0' else 11
        length += 1
        if length_type_ID == 15:
            length += 15 + bin2int(content[1:16])
            return to_search[:length], to_search[length:]
        else:
            length += 11
            number_of_packets = bin2int(content[1:12])
            content_left = content[12:]
            for i in range(number_of_packets):
                packet, content_left = findPackets(content_left)
                length += len(packet)
            return to_search[:length], to_search[length:]

def calcType(type_ID, values):
        if type_ID == 0:
            answer = sum(value for value in values)
        elif type_ID == 1:
            answer = 1
            for value in values:
                answer *= value
        elif type_ID == 2:
            answer = min(values)
        elif type_ID == 3:
            answer = max(values)
        elif type_ID == 5:
            answer = 1 if values[0] > values[1] else 0
        elif type_ID == 6:
            answer = 1 if values[0] < values[1] else 0
        elif type_ID == 7:
            answer = 1 if values[0] == values[1] else 0
        return answer

def solvePacket(packet):
    header, content = parsePackage(packet)
    type_ID = getType(header)
    if type_ID == 4:
        answer = bin2int(getLiteral(content))
    else:
        answer = calcType(type_ID, getOperator(content))
    return answer

print(solvePacket(hex2bin(package)))