target_input = open("input-test.txt" , "r")
data = target_input.read().split("\n")
del data[-1]

def itsNotOver(game):
    for state in game:
        for score in game[state]:
            if game[state][score] != 0:
                return True
    return False

def movePawn(starting_point, steps):
    space = (starting_point + steps) % 10
    if space == 0:
        return 10
    return space

possible_scores = { (x,y): 0 for x in range(0, 21) for y in range(0, 21) }
possible_states = { (x,y): possible_scores.copy() for x in range(1, 11) for y in range(1, 11) }

game = {key: value.copy() for key, value in possible_states.items()}

starting_point_player_1 = int(data[0][-1])
starting_point_player_2 = int(data[1][-1])
game[(starting_point_player_1,starting_point_player_2)][(0,0)] = 1
player_1_won = 0
player_2_won = 0

notDone = True
turn = 0
while notDone:
    turn += 1
    next_turn = {key: value.copy() for key, value in possible_states.items()}
    #Player1 Turn
    for state in game:
        for score in game[state]:
            for i in range(1, 4):
                for j in range(1, 4):
                    for k in range(1, 4):
                        next_step = movePawn(state[0], i+j+k)
                        if score[0] + next_step >= 21:
                            player_1_won += game[state][score]
                        else:
                            next_turn[(next_step, state[1])][(score[0]+next_step, score[1])] += game[state][score]
    game = {key: value.copy() for key, value in next_turn.items()}
    next_turn = {key: value.copy() for key, value in possible_states.items()}
    for state in game:
        for score in game[state]:
            for i in range(1, 4):
                for j in range(1, 4):
                    for k in range(1, 4):
                        next_step = movePawn(state[1], i+j+k)
                        if score[1] + next_step >= 21:
                            player_2_won += game[state][score]
                        else:
                            next_turn[(state[0],next_step)][(score[0], score[1]+next_step)] += game[state][score]
    game = {key: value.copy() for key, value in next_turn.items()}
    notDone = itsNotOver(game)
print(turn)
print(max(player_1_won, player_2_won))
