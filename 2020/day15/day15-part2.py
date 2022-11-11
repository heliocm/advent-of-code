input = [20,9,11,0,1,2]
turn = 0
already_said = {}
next_number = 0
for each in input:
    turn = turn + 1
    already_said[each] = { "last_seen": turn }

while turn != 30000000:
    turn = turn + 1
    if turn == 30000000:
        print("Turno: ", turn)
        print("Numero falado", next_number)

    try:
        last_seen = already_said[next_number]["last_seen"]
        already_said[next_number]["last_seen"] = turn
        next_number = turn - last_seen
    except:
        already_said[next_number] = {"last_seen": turn}
        next_number = 0