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


while position_y != height_of_geology - 1:
        position_x = position_x + 3
        position_y = position_y + 1
        #print(list(grid[position_y])[position_x % width_of_geology])
        if list(grid[position_y])[position_x % width_of_geology] == tree:
            number_of_trees = number_of_trees + 1

print(number_of_trees)
