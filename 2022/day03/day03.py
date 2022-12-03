import string
target_input = open("input.txt" , "r")
data = target_input.read().split("\n")
del data[-1]

alphabet = string.ascii_lowercase+string.ascii_uppercase

answer = 0
for each in data:
    first = each[:len(each)//2]
    second = each[len(each)//2:]
    answer += alphabet.index(''.join(set(first).intersection(second))) + 1

print(answer)