target_input = open("input.txt" , "r")
data = target_input.read().split("\n")
del data[-1]

fishes = [int(number) for number in data[0].split(",")]
print(fishes)

day = 0
while day < 80:
    nextday = []
    born = 0
    for fish in fishes:
        if fish == 0:
            nextday.append(6)
            born += 1
        else:
            nextday.append(fish-1)
    for i in range(born):
        nextday.append(8)
    day += 1
    fishes = nextday

print(len(fishes))