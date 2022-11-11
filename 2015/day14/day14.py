target_input = open("input.txt" , "r")
data = target_input.read().split("\n")
del data[-1]

runtime = 2503

reindeers = []
for line in data:
    line = line.split(" ")
    reindeers.append([int(line[3]), int(line[6]), int(line[-2])])

#print(reindeers)

results = []
for (vel, stamina, rest) in reindeers:
    sprint = runtime % (stamina+rest)
    runs = runtime // (stamina+rest)
    if sprint >= stamina:
        results.append((runs+1)*vel*stamina)
    else:
        results.append(runs*vel*stamina + sprint*vel)

print(max(results))