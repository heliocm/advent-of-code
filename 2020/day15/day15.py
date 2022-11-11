input = [20,9,11,0,1,2]
turn = 0
already_said = []
last_appearence = []
last_is_new = False
next_number = 0
for each in input:
    turn = turn + 1
    if already_said.count(each) == 0:
        last_is_new = True
    already_said.append(each)
    last_appearence.append(turn)

while turn != 2020:
    turn = turn + 1
    if turn == 2020:
        print("Turno: ", turn)
        print("Numero falado", next_number)
    if last_is_new:
        if already_said.count(0) != 0:
            next_number = turn - last_appearence[already_said.index(0)]
            last_appearence[already_said.index(0)] = turn
            last_is_new = False
        else:
            already_said.append(next_number)
            last_appearence.append(turn)
            next_number = 0
    else:
        if already_said.count(next_number) == 0:
            already_said.append(next_number)
            last_appearence.append(turn)
            next_number = 0
            last_is_new = True
        else:
            auxiliar = turn - last_appearence[already_said.index(next_number)]
            last_appearence[already_said.index(next_number)] = turn
            next_number = auxiliar
