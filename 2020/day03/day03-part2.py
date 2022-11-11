target_input = open("input.txt" , "r")
grid = target_input.read().split("\n")
del grid[-1]

tree = "#"
square = "."
number_of_trees = 0
position_x = 0
position_y = 0
width_of_geology = len(grid[0])
height_of_geology = len(grid)

magic_number = 1


steps = [[1, 1], [3, 1], [5, 1], [7, 1], [1, 2]]

for step in steps:
    while position_y != height_of_geology - 1:
        position_x = position_x + step[0]
        position_y = position_y + step[1]
        #print(list(grid[position_y])[position_x % width_of_geology])
        if list(grid[position_y])[position_x % width_of_geology] == tree:
            number_of_trees = number_of_trees + 1

    print(number_of_trees)

    position_x = 0
    position_y = 0
    magic_number = magic_number * number_of_trees
    number_of_trees = 0

print (magic_number)