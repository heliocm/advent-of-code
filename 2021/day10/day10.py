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
                return char
    return 0
left = ['{', '[', '(', '<']
right = ['}', ']', ')', '>']
errors = []
for each in data:
    error = findError(each)
    if error != 0:
        errors.append(error)
answer = 0
for error in errors:
    if error == ')':
        answer += 3
    elif error == ']':
        answer += 57
    elif error == '}':
        answer += 1197
    else:
        answer += 25137
print(answer)
