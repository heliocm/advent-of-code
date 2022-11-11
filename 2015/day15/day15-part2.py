target_input = open("input.txt" , "r")
data = target_input.read().split("\n")
del data[-1]

ingredients = []
for line in data:
    line = line.split(" ")
    ingredients.append([int(line[2][:-1]),int(line[4][:-1]),int(line[6][:-1]),int(line[8][:-1]),int(line[-1])])
possible_comb = []

print(ingredients)

for a in range(0,101):
    for b in range(0,101):
        for c in range(0,101):
            for d in range(0,101):
                if a + b + c + d == 100:
                    possible_comb.append((a,b,c,d))

result = 0 

for (a, b, c, d) in possible_comb:
    cap = a * ingredients[0][0] + b * ingredients[1][0] + c * ingredients[2][0] + d * ingredients[3][0]
    dur = a * ingredients[0][1] + b * ingredients[1][1] + c * ingredients[2][1] + d * ingredients[3][1]
    flav = a * ingredients[0][2] + b * ingredients[1][2] + c * ingredients[2][2] + d * ingredients[3][2]
    text = a * ingredients[0][3] + b * ingredients[1][3] + c * ingredients[2][3] + d * ingredients[3][3]
    cal = a * ingredients[0][4] + b * ingredients[1][4] + c * ingredients[2][4] + d * ingredients[3][4]


    cap = 0 if cap <= 0 else cap
    dur = 0 if dur <= 0 else dur
    flav = 0 if flav <= 0 else flav
    text = 0 if text <= 0 else text

    if cal == 500:
        result = cap * dur * flav * text if cap * dur * flav * text >= result else result

print(result)

