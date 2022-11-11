target_input = open("input.txt" , "r")
data = target_input.read().split("\n\n")
del data[-1]


def get_borders(tile):
    tile_id = each[each.index("Tile ") + len("Tile "):each.index(":")]
    pattern = each[each.index("\n") + 1:].split("\n")
    borders = { 
        "up": set(),
        "down": set(),
        "left": set(),
        "right": set()
    }
    for i, line in list(enumerate(pattern)):
        for k, element in list(enumerate(line)):
            if element == "#":
                if i == 0:
                    borders["up"].add(k)
                elif i == len(pattern) - 1:
                    borders["down"].add(k)
                if k == 0:
                    borders["left"].add(i)
                elif k == len(line) - 1:
                    borders["right"].add(i)

    return(tile_id, borders)

def adjacents(tiles):
    tile_adjacents = {}
    for tile_id, tile_borders in tiles.items():
        tile_adjacents[tile_id] = {
            "up": set(),
            "down": set(),
            "left": set(),
            "right": set()
        }
        for comparison_id, comparison_borders in tiles.items():
            if tile_id != comparison_id:
                if tile_borders["up"] == comparison_borders["down"]:
                    tile_adjacents[tile_id]["up"].add(comparison_id)
                if tile_borders["down"] == comparison_borders["up"]:
                    tile_adjacents[tile_id]["down"].add(comparison_id)
                if tile_borders["left"] == comparison_borders["right"]:
                    tile_adjacents[tile_id]["left"].add(comparison_id)
                if tile_borders["right"] == comparison_borders["left"]:
                    tile_adjacents[tile_id]["right"].add(comparison_id)

    return(tile_adjacents)

count = 0
tiles = {}
for each in data:
    tile_id, tile_border = get_borders(each)
    tiles[tile_id] = tile_border
    count = count + 1