import time

target_input = open("input.txt" , "r")
data = target_input.read().split("\n")
del data[-1]

#Execution time
#--- 364.8067989349365 seconds ---
def decompress(compressed):
    answer = 0
    if compressed.find('(') != -1:
        answer += len(compressed[:compressed.find('(')])
    size, repetition = get_compression(compressed)
    if size != -1:
        part = compressed[compressed.find(')')+1:compressed.find(')')+1+size] * repetition
        if part.find('(') != -1:
            answer += decompress(part)
        else:
            answer += len(part)
        new_compressed = compressed[compressed.find(')')+1+size:]
        answer += decompress(new_compressed)
    else:
        answer += len(compressed)
    return answer

#Execution time
#--- 0.004220008850097656 seconds ---
def good_decompress(compressed):
    answer = 0
    if compressed.find('(') != -1:
        answer += len(compressed[:compressed.find('(')])
    size, repetition = get_compression(compressed)
    if size != -1:
        answer += repetition * good_decompress(compressed[compressed.find(')')+1:compressed.find(')')+1+size])
        answer += good_decompress(compressed[compressed.find(')')+1+size:])
    else:
        answer += len(compressed)
    return answer

def get_compression(compressed):
    if compressed.find('(') != -1:
        size = int(compressed[compressed.find('(')+1:compressed.find(')')].split('x')[0])
        repetition = int(compressed[compressed.find('(')+1:compressed.find(')')].split('x')[1])
    else:
        size = -1
        repetition = -1
    return size, repetition

data = ''.join(data)
data_test = '(25x3)(3x3)ABC(2x3)XY(5x2)PQRSTX(18x9)(3x2)TWO(5x7)SEVEN'
start_time = time.time()
print('Good Algorithm')
print(good_decompress(data))
print("--- %s seconds ---" % (time.time() - start_time))
start_time = time.time()
print('Bad Algorithm')
print(decompress(data))
print("--- %s seconds ---" % (time.time() - start_time))