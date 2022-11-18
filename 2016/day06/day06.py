
#### INPUT TEST ####
# data = ['eedadn',
# 'drvtee',
# 'eandsr',
# 'raavrd',
# 'atevrs',
# 'tsrnev',
# 'sdttsa',
# 'rasrtv',
# 'nssdts',
# 'ntnada',
# 'svetve',
# 'tesnvt',
# 'vntsnd',
# 'vrdear',
# 'dvrsen',
# 'enarar']

target_input = open("input.txt" , "r")
data = target_input.read().split("\n")
del data[-1]
answer = ''
def get_most_common(letter_list):
    dict = {}
    for letter in letter_list:
        dict.update({letter: letter_list.count(letter)})
    sorted_list = sorted(dict.items(), key=lambda x:(-x[1],x[0]), reverse=False)
    return sorted_list[0]
turn = 0
while turn < len(data[0]):
    letter_bag = ''
    for each in data:
        letter_bag += each[turn]
    answer += get_most_common(letter_bag)[0]
    turn += 1
print(answer)

