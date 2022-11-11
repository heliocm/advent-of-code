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

def game(playe1, player2):
    while len(player1)!=0 and len(player2)!=0:
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

game(player1,player2)
total = 0
if len(player1) != 0:
    i = 1
    for each in reversed(player1):
        total += each * i
        i += 1
else:
    i = 1
    for each in reversed(player2):
        total += each * i
        i += 1

print(total)