target_input = open("input.txt" , "r")
data = target_input.read().split("\n")
del data[-1]

starting_point_player_1 = int(data[0][-1])
starting_point_player_2 = int(data[1][-1])

total_player_1 = 0
total_player_2 = 0

def movePawn(starting_point, steps):
    space = (starting_point + steps) % 10
    if space == 0:
        return 10
    return space

def rollDice(last_number):
    if last_number == 0:
        return [1,2,3]
    else:
        if last_number + 3 <= 100:
            return [last_number+1, last_number+2, last_number+3]
        else:
            dice_roll = []
            for each in [last_number+1, last_number+2, last_number+3]:
                if each > 100:
                    dice_roll.append(each%100)
                else:
                    dice_roll.append(each)
            return dice_roll

last_number = 0
rolled = 0
while total_player_1 < 1000 or total_player_2 < 1000:
    dice_roll = rollDice(last_number)
    rolled += 3
    last_number = dice_roll[-1]
    starting_point_player_1 = movePawn(starting_point_player_1, sum(dice_roll))
    total_player_1 += starting_point_player_1
    if total_player_1 >= 1000:
        break
    dice_roll = rollDice(last_number)
    rolled += 3
    last_number = dice_roll[-1]
    starting_point_player_2 = movePawn(starting_point_player_2, sum(dice_roll))
    total_player_2 += starting_point_player_2

print(total_player_1, total_player_2)
print(rolled)
print(min(total_player_1, total_player_2) * rolled)