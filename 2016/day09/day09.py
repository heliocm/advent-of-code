target_input = open("input.txt" , "r")
data = target_input.read().split("\n")
del data[-1]

def decompress(compressed):
    decompressed = ''
    if compressed.find('(') != -1:
        decompressed += compressed[:compressed.find('(')]
    size, repetition = get_compression(compressed)
    if size != -1:
        decompressed += compressed[compressed.find(')')+1:compressed.find(')')+1+size] * repetition
        new_compressed = compressed[compressed.find(')')+1+size:]
        decompressed += decompress(new_compressed)
    else:
        decompressed += compressed
    return decompressed

def get_compression(compressed):
    if compressed.find('(') != -1:
        size = int(compressed[compressed.find('(')+1:compressed.find(')')].split('x')[0])
        repetition = int(compressed[compressed.find('(')+1:compressed.find(')')].split('x')[1])
    else:
        size = -1
        repetition = -1
    return size, repetition

data = ''.join(data)
# data_test = 'X(8x2)(3x3)ABCY'

print(decompress(data))
print(len(decompress(data)))