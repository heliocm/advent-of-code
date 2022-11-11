target_input = open("input.txt" , "r")
data = target_input.read().split("\n")
del data[-1]

runtime = 2503

reindeers = []
points = []
distance = []
for line in data:
    line = line.split(" ")
    reindeers.append([int(line[3]), int(line[6]), int(line[-2])])
    points.append(0)
    distance.append(0)

seconds = 0
while seconds < runtime:
    seconds += 1
    for i in range(len(distance)):
        (vel, stamina, rest) = reindeers[i]
        sprint = seconds % (stamina+rest)
        if sprint <= stamina and sprint > 0:
            distance[i] += vel
    if seconds <= 7:
        print(distance)
    lead_distance = max(distance)
    for i in range(len(distance)):
        if distance[i] == lead_distance:
            points[i] += 1
    if seconds <= 7:
        print(points)
print(max(points))