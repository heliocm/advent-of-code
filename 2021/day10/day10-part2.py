target_input = open("input.txt" , "r")
data = target_input.read().split("\n")
del data[-1]

def findError(word):
    checking = []
    for char in word:
        if char in left:
            checking.append(char)
        elif char in right:
            if left[right.index(char)] == checking[-1]:
                checking.pop()
            else:
                return 0
    return checking
left = ['(', '[', '{', '<']
right = [')', ']', '}', '>']
errors = []
answer = []
for each in data:
    incomplete = [right[left.index(i)] for i in reversed(findError(each))] if findError(each) != 0 else 0
    if incomplete != 0:
        valour = 0
        for char in incomplete:
            valour *= 5
            if right.index(char) == 0:
                valour += 1
            elif right.index(char) == 1:
                valour += 2
            elif right.index(char) == 2:
                valour += 3
            elif right.index(char) == 3:
                valour += 4
        answer.append(valour)
answer.sort()
print(answer[len(answer) // 2])