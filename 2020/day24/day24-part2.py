target_input = open("input.txt" , "r")
data = target_input.read().split("\n")
del data[-1]

def find_tile(instructions):
    instructions = list(instructions)
    x = 0
    y = 0
    change_line = 0
    for direction in instructions:
        if direction == 'e':
            if change_line == 1:
                x += 1
                y += 1
                change_line = 0
            elif change_line == -1:
                x -= 1
                y += 1
                change_line = 0
            else:
                y += 2
                change_line = 0
        elif direction == 'n':
            change_line = 1
        elif direction == 's':
            change_line = -1
        else:
            if change_line == 1:
                x += 1
                y -= 1
                change_line = 0
            elif change_line == -1:
                x -= 1
                y -= 1
                change_line = 0
            else:
                y -= 2
                change_line = 0
    return(x, y)

def paint(painted, tile):
    if tile not in painted:
        painted[tile] = "black"
    else:
        if painted[tile] == "white":
            painted[tile] = "black"
        else:
            painted[tile] = "white"

def adjacents(tile):
    adjacents = set()
    for x in range(tile[0]-1, tile[0]+2):
        if x != tile[0]:
            adjacents.add((x, tile[1]-1))
            adjacents.add((x, tile[1]+1))
        else:
            adjacents.add((x, tile[1]-2))
            adjacents.add((x, tile[1]+2))
    return adjacents
painted = {}
for instructions in data:
    tile = find_tile(instructions)
    paint(painted, tile)


black_tiles = set()
for key, value in painted.items():
    if value == "black":
        black_tiles.add(key)

number_of_days = 100

for i in range(number_of_days):
    whites_with_black_adjacents = {}
    to_remove = set()
    for black_tile in black_tiles:
        black_adjacent = 0
        for adjacent in adjacents(black_tile):
            if adjacent in black_tiles:
                black_adjacent += 1
            else:
                if adjacent in whites_with_black_adjacents:
                    whites_with_black_adjacents[adjacent] += 1
                else:
                    whites_with_black_adjacents[adjacent] = 1
        if black_adjacent == 0 or black_adjacent > 2:
            to_remove.add(black_tile)
    for each in to_remove:
        black_tiles.discard(each)
    for each in whites_with_black_adjacents:
        if whites_with_black_adjacents[each] == 2:
            black_tiles.add(each)

print(len(black_tiles))