target_input = open("input.txt" , "r")
instructions = target_input.read().split("\n")
del instructions[-1]

vertical_position = 0
horizontal_position = 0
possible_directions = list("NWSE")
facing_direction = "E"
for each in instructions:
    direction = each[0]
    angle = int(each[1:])
    distance = int(each[1:])
    if direction == "N":
        vertical_position = vertical_position + distance
    elif direction == "S":
        vertical_position = vertical_position - distance
    elif direction == "E":
        horizontal_position = horizontal_position + distance
    elif direction == "W":
        horizontal_position = horizontal_position - distance
    elif direction == "L":
        facing_direction = possible_directions[(possible_directions.index(facing_direction) + int(angle / 90)) % 4]
    elif direction == "R":
        facing_direction = possible_directions[(possible_directions.index(facing_direction) - int(angle / 90)) % 4]
    elif direction == "F":
        if facing_direction == "N":
            vertical_position = vertical_position + distance
        elif facing_direction == "S":
            vertical_position = vertical_position - distance
        elif facing_direction == "E":
            horizontal_position = horizontal_position + distance
        elif facing_direction == "W":
            horizontal_position = horizontal_position - distance

result = abs(vertical_position) + abs(horizontal_position)
print(result)