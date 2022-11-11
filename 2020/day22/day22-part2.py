target_input = open("input.txt" , "r")
data = target_input.read().split("\n\n")
player1 = []
player2 = []
for each in data[0].split("\n"):
    if each.isnumeric():
        player1.append(int(each))
for each in data[1].split("\n"):
    if each.isnumeric():
        player2.append(int(each))

def prevent_loop(deck1, deck2, previous_rounds):
    this_round = (tuple(deck1), tuple(deck2))
    if this_round in previous_rounds:
        return 1
    else:
        previous_rounds.add(this_round)
        return 0

def subgame_time(player1, player2):
    if len(player1) - 1 >= player1[0] and len(player2) - 1 >= player2[0]:
        return True
    else:
        return False

def game(player1, player2):
    previous_rounds = set()
    winner = 0
    while winner == 0:
        winner = prevent_loop(player1, player2, previous_rounds)
        if winner != 0:
            return winner
        else:
            if subgame_time(player1, player2):
                subwinner = game(player1[1:player1[0]+1], player2[1:player2[0]+1])
                if subwinner == 1:
                    player1.append(player1[0])
                    player1.append(player2[0])
                    player1.pop(0)
                    player2.pop(0)
                elif subwinner == 2:
                    player2.append(player2[0])
                    player2.append(player1[0])
                    player2.pop(0)
                    player1.pop(0)
            else:
                if player1[0] > player2[0]:
                    player1.append(player1[0])
                    player1.append(player2[0])
                    player1.pop(0)
                    player2.pop(0)
                else:
                    player2.append(player2[0])
                    player2.append(player1[0])
                    player2.pop(0)
                    player1.pop(0)
        if len(player1) == 0:
            winner = 2
        elif len(player2) == 0:
            winner = 1
    return winner

total = 0
game_winner = game(player1, player2)
if game_winner == 1:
    i = 1
    for each in reversed(player1):
        total += each * i
        i += 1
elif game_winner == 2:
    i = 1
    for each in reversed(player2):
        total += each * i
        i += 1
print(total)