target_input = open("input.txt" , "r")
data = target_input.read().split("\n")
del data[-1]

def get_most_commons(encrypted_name):
    dict = {}
    for letter in encrypted_name:
        dict.update({letter: encrypted_name.count(letter)})
    sorted_list = sorted(dict.items(), key=lambda x:(-x[1],x[0]), reverse=False)
    most_commons = ''
    for i in range(5):
        most_commons += sorted_list[i][0]
    return most_commons

answer = 0
for each in data:
    encrypted_name = each.split('-')
    sector_id = int(encrypted_name[-1].split('[')[0])
    check_sum = encrypted_name[-1].split('[')[1][:-1]
    del encrypted_name[-1]
    possible = get_most_commons(''.join(encrypted_name))
    if possible == check_sum:
        answer += sector_id

print(answer)