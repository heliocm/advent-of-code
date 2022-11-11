target_input = open("input.txt" , "r")
data = target_input.read().split("\n")
del data[-1]

fishes = [int(number) for number in data[0].split(",")]

tracking = {}
for i in range(9):
    tracking[i] = 0

for fish in fishes:
    tracking[fish] += 1

day = 0
nextday = {}
while day < 256:
    for i in range(9):
        nextday[i] = 0
    for fish in tracking:
        if fish == 0:
            nextday[6] += tracking[fish]
            nextday[8] += tracking[fish]
            tracking[fish] = 0
        else:
            nextday[fish-1] += tracking[fish]
            tracking[fish] = 0
    day += 1
    for i in range(9):
        tracking[i] = nextday[i]
answer = 0
for fish in tracking:
    answer += tracking[fish]

print(answer)