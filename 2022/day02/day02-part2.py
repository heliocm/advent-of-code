target_input = open("input.txt" , "r")
data = target_input.read().split("\n")
del data[-1]

rules = {
    'A': {
        'X': 'C',
        'Y': 'A',
        'Z': 'B'
    },
    'B': {
        'X': 'A',
        'Y': 'B',
        'Z': 'C'
    },
    'C': {
        'X': 'B',
        'Y': 'C',
        'Z': 'A'
    }
}

new_rules = {
    'X': 'L',
    'Y': 'D',
    'Z': 'W'
}

points = {
    'W': 6,
    'D': 3,
    'L': 0,
    'A': 1,
    'B': 2,
    'C': 3
}

input_test = "\
A Y\n\
B X\n\
C Z".split("\n")
answer = 0
for round in data:
    answer += points[rules[round[0]][round[-1]]] + points[new_rules[round[-1]]]

print(answer)