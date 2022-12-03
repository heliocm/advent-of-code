target_input = open("input.txt" , "r")
data = target_input.read().split("\n")
del data[-1]

rules = {
    'A': {
        'X': 'D',
        'Y': 'W',
        'Z': 'L'
    },
    'B': {
        'X': 'L',
        'Y': 'D',
        'Z': 'W'
    },
    'C': {
        'X': 'W',
        'Y': 'L',
        'Z': 'D'
    }
}

points = {
    'W': 6,
    'D': 3,
    'L': 0,
    'X': 1,
    'Y': 2,
    'Z': 3
}

input_test = "\
A Y\n\
B X\n\
C Z".split("\n")
answer = 0
for round in input_test:
    answer += points[round[-1]] + points[rules[round[0]][round[-1]]]

print(answer)