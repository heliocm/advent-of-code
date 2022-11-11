target_input = open("input.txt" , "r")
instructions = target_input.read().split("\n")
del instructions[-1]

def multiply_arrays(first, second):
    result = [0, 0]

    for i in range(len(first)):
        for j in range(len(second)):
            result[i] += first[j] * second[i][j]
    return result

vertical_position = 0
horizontal_position = 0
waypoint = [10, 1]
for each in instructions:
    direction = each[0]
    angle = int(each[1:])
    distance = int(each[1:])
    if direction == "N":
        waypoint[1] = waypoint[1] + distance
    elif direction == "S":
        waypoint[1] = waypoint[1] - distance
    elif direction == "E":
        waypoint[0] = waypoint[0] + distance
    elif direction == "W":
        waypoint[0] = waypoint[0] - distance
    elif direction == "L":
        if int(angle/90) == 1:
            rotation = [[0, -1], [1, 0]]
            waypoint = multiply_arrays(waypoint,rotation)
        elif int(angle/90) == 2:
            rotation = [[-1, 0], [0, -1]]
            waypoint = multiply_arrays(waypoint,rotation)
        elif int(angle/90) == 3:
            rotation = [[0, 1], [-1, 0]]
            waypoint = multiply_arrays(waypoint,rotation)
    elif direction == "R":
        if int(angle/90) == 1:
            rotation = [[0, 1], [-1, 0]]
            waypoint = multiply_arrays(waypoint,rotation)
        elif int(angle/90) == 2:
            rotation = [[-1, 0], [0, -1]]
            waypoint = multiply_arrays(waypoint,rotation)
        elif int(angle/90) == 3:
            rotation = [[0, -1], [1, 0]]
            waypoint = multiply_arrays(waypoint,rotation)
    elif direction == "F":
        horizontal_position = horizontal_position + waypoint[0] * distance
        vertical_position = vertical_position + waypoint[1] * distance

result = abs(vertical_position) + abs(horizontal_position)
print(result)